import type { APIRoute } from 'astro';
import { db, ensureDbInitialized } from '../../../../lib/db';
import { logAuditEvent } from '../../../../lib/auth';

export const GET: APIRoute = async ({ params, locals }) => {
  if (!locals.user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  await ensureDbInitialized();
  const { id } = params;

  const res = await db.execute({
    sql: 'SELECT * FROM booking_submissions WHERE id = ?',
    args: [id as string]
  });

  if (res.rows.length === 0) {
    return new Response(JSON.stringify({ error: 'Booking submission not found' }), { status: 404 });
  }

  return new Response(JSON.stringify({ booking: res.rows[0] }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
};

export const PUT: APIRoute = async ({ params, request, locals, clientAddress }) => {
  if (!locals.user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  await ensureDbInitialized();
  const { id } = params;

  try {
    const body = await request.json();
    const existing = await db.execute({
      sql: 'SELECT * FROM booking_submissions WHERE id = ?',
      args: [id as string]
    });

    if (existing.rows.length === 0) {
      return new Response(JSON.stringify({ error: 'Booking submission not found' }), { status: 404 });
    }

    const current = existing.rows[0];
    const allowedStatuses = ['new', 'contacted', 'scheduled', 'completed', 'cancelled'];
    const status = body.status !== undefined && allowedStatuses.includes(body.status) ? body.status : current.status;
    const notes = body.notes !== undefined ? body.notes : current.notes;
    const now = new Date().toISOString();

    await db.execute({
      sql: `UPDATE booking_submissions SET status = ?, notes = ?, updated_at = ? WHERE id = ?`,
      args: [status, notes, now, id as string]
    });

    await logAuditEvent(locals.user.userId, 'UPDATE_BOOKING_STATUS', 'booking', id as string, {
      customer: current.customer_name,
      previous_status: current.status,
      new_status: status
    }, clientAddress);

    return new Response(JSON.stringify({ success: true, message: 'Booking inquiry updated successfully' }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ error: 'Failed to update booking: ' + err.message }), { status: 500 });
  }
};

export const DELETE: APIRoute = async ({ params, locals, clientAddress }) => {
  if (!locals.user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  await ensureDbInitialized();
  const { id } = params;

  const existing = await db.execute({
    sql: 'SELECT customer_name, service_requested FROM booking_submissions WHERE id = ?',
    args: [id as string]
  });

  if (existing.rows.length === 0) {
    return new Response(JSON.stringify({ error: 'Booking submission not found' }), { status: 404 });
  }

  const bkg = existing.rows[0];

  await db.execute({
    sql: 'DELETE FROM booking_submissions WHERE id = ?',
    args: [id as string]
  });

  await logAuditEvent(locals.user.userId, 'DELETE_BOOKING', 'booking', id as string, {
    customer: bkg.customer_name,
    service: bkg.service_requested
  }, clientAddress);

  return new Response(JSON.stringify({ success: true, message: 'Booking permanently deleted' }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
};

