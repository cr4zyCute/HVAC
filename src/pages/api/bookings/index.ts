import type { APIRoute } from 'astro';
import crypto from 'node:crypto';
import { db, ensureDbInitialized } from '../../../lib/db';
import { logAuditEvent } from '../../../lib/auth';

// Persistent Database-backed Rate Limiter: max 5 bookings per 10 minutes per IP
// Works across Vercel serverless functions & container restarts via SQLite / LibSQL
const MAX_BOOKINGS_PER_WINDOW = 5;
const WINDOW_MS = 10 * 60 * 1000; // 10 minutes

async function checkDbRateLimit(ip: string): Promise<boolean> {
  const cutoff = new Date(Date.now() - WINDOW_MS).toISOString();
  const res = await db.execute({
    sql: `SELECT COUNT(*) as count FROM audit_logs 
          WHERE action = 'NEW_BOOKING_SUBMITTED' 
            AND ip_address = ? 
            AND created_at > ?`,
    args: [ip, cutoff]
  });
  const count = Number(res.rows[0]?.count || 0);
  return count < MAX_BOOKINGS_PER_WINDOW;
}

// Regex for email validation
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

// Function to validate phone numbers (must contain at least 10 digits)
function isValidPhone(phone: string): boolean {
  const digitsOnly = phone.replace(/\D/g, '');
  return digitsOnly.length >= 10 && digitsOnly.length <= 15;
}

export const POST: APIRoute = async ({ request, clientAddress }) => {
  await ensureDbInitialized();

  // 1. Persistent IP Rate Limiting (Serverless-Safe)
  const ip = clientAddress || request.headers.get('x-forwarded-for')?.split(',')[0].trim() || '127.0.0.1';
  const isAllowed = await checkDbRateLimit(ip);

  if (!isAllowed) {
    await logAuditEvent(null, 'BOOKING_RATE_LIMIT_EXCEEDED', 'security', undefined, { ip });
    return new Response(JSON.stringify({
      error: 'Too many booking requests from this network. Please wait 10 minutes or call our 24/7 hotline directly.'
    }), {
      status: 429,
      headers: {
        'Content-Type': 'application/json',
        'Retry-After': '600'
      }
    });
  }

  try {
    const body = await request.json();
    const {
      customer_name,
      customer_email,
      customer_phone,
      service_requested,
      preferred_date,
      preferred_time,
      urgency,
      message,
      // Honeypot fields (hidden from legitimate humans, filled by spam bots)
      hp_website_company_fax,
      hp_field
    } = body;

    // 2. Honeypot check: If bot filled this hidden field, silently reject to avoid alerting bot
    if (hp_website_company_fax || hp_field) {
      await logAuditEvent(null, 'SPAM_HONEYPOT_TRIGGERED', 'security', undefined, {
        ip,
        name: customer_name,
        email: customer_email
      });
      // Return 200 OK so bot thinks submission succeeded without writing to DB
      return new Response(JSON.stringify({
        success: true,
        message: 'Your service request has been received.'
      }), {
        status: 200,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // 3. Presence validation
    if (!customer_name || !customer_email || !customer_phone) {
      return new Response(JSON.stringify({
        error: 'Customer name, email address, and phone number are all required.'
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // 4. Server-side format validation: Email
    const cleanEmail = customer_email.trim().toLowerCase();
    if (!EMAIL_REGEX.test(cleanEmail) || cleanEmail.length > 254) {
      return new Response(JSON.stringify({
        error: 'Please provide a valid email address (e.g. name@example.com).'
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // 5. Server-side format validation: Phone
    const cleanPhone = customer_phone.trim();
    if (!isValidPhone(cleanPhone)) {
      return new Response(JSON.stringify({
        error: 'Please provide a valid 10-digit phone number (e.g. (612) 555-0198).'
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // 6. Name validation
    if (customer_name.trim().length < 2 || customer_name.trim().length > 100) {
      return new Response(JSON.stringify({
        error: 'Please provide a valid name between 2 and 100 characters.'
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const id = `bkg_${crypto.randomBytes(8).toString('hex')}`;
    const now = new Date().toISOString();

    await db.execute({
      sql: `INSERT INTO booking_submissions (
        id, customer_name, customer_email, customer_phone, service_requested,
        preferred_date, preferred_time, urgency, message, status, notes, created_at, updated_at
      ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'new', '', ?, ?)`,
      args: [
        id,
        customer_name.trim(),
        customer_email.trim().toLowerCase(),
        customer_phone.trim(),
        cleanEmail,
        cleanPhone,
        (service_requested || 'General HVAC Service').trim(),
        (preferred_date || 'Flexible').trim(),
        (preferred_time || 'Anytime').trim(),
        (urgency || 'standard').trim(),
        (message || '').trim(),
        now,
        now
      ]
    });

    await logAuditEvent(null, 'NEW_BOOKING_SUBMITTED', 'booking', id, {
      customer_name: customer_name.trim(),
      email: cleanEmail,
      service_requested,
      urgency
    }, ip);

    return new Response(JSON.stringify({
      success: true,
      id,
      message: 'Your service request has been received. Our dispatch team will confirm your appointment shortly.'
    }), {
      status: 201,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ error: 'Failed to submit booking: ' + err.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};

