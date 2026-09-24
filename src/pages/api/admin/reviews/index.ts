import type { APIRoute } from 'astro';
import crypto from 'node:crypto';
import { db, ensureDbInitialized } from '../../../../lib/db';
import { logAuditEvent } from '../../../../lib/auth';

export const GET: APIRoute = async ({ url, locals }) => {
  if (!locals.user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  await ensureDbInitialized();

  const filter = url.searchParams.get('filter') || 'all'; // all, pending, approved
  const search = url.searchParams.get('search')?.trim() || '';

  let sql = 'SELECT * FROM reviews';
  const conditions: string[] = [];
  const args: any[] = [];

  if (filter === 'pending') {
    conditions.push('is_approved = 0');
  } else if (filter === 'approved') {
    conditions.push('is_approved = 1');
  }

  if (search) {
    conditions.push('(author_name LIKE ? OR content LIKE ? OR service_type LIKE ?)');
    const term = `%${search}%`;
    args.push(term, term, term);
  }

  if (conditions.length > 0) {
    sql += ' WHERE ' + conditions.join(' AND ');
  }

  sql += ' ORDER BY created_at DESC';

  const res = await db.execute({ sql, args });

  return new Response(JSON.stringify({ reviews: res.rows }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
};

export const POST: APIRoute = async ({ request, locals, clientAddress }) => {
  if (!locals.user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  await ensureDbInitialized();

  try {
    const body = await request.json();
    const { author_name, author_location, rating, service_type, content, is_approved, is_featured, source } = body;

    if (!author_name || !content || !rating) {
      return new Response(JSON.stringify({ error: 'Author name, rating, and review text are required.' }), { status: 400 });
    }

    const numRating = Number(rating);
    if (isNaN(numRating) || numRating < 1 || numRating > 5) {
      return new Response(JSON.stringify({ error: 'Rating must be an integer between 1 and 5.' }), { status: 400 });
    }

    const id = `rev_${crypto.randomBytes(8).toString('hex')}`;
    const now = new Date().toISOString();

    await db.execute({
      sql: `INSERT INTO reviews (id, author_name, author_location, rating, service_type, content, is_approved, is_featured, source, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
      args: [
        id,
        author_name.trim(),
        (author_location || 'Minneapolis, MN').trim(),
        numRating,
        (service_type || 'HVAC Service').trim(),
        content.trim(),
        is_approved ? 1 : 0,
        is_featured ? 1 : 0,
        source || 'Google',
        now,
        now
      ]
    });

    await logAuditEvent(locals.user.userId, 'CREATE_REVIEW', 'review', id, { author_name, rating: numRating }, clientAddress);

    return new Response(JSON.stringify({ success: true, id }), {
      status: 201,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ error: 'Failed to create review: ' + err.message }), { status: 500 });
  }
};

