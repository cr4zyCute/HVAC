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
    sql: 'SELECT * FROM reviews WHERE id = ?',
    args: [id as string]
  });

  if (res.rows.length === 0) {
    return new Response(JSON.stringify({ error: 'Review not found' }), { status: 404 });
  }

  return new Response(JSON.stringify({ review: res.rows[0] }), {
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
      sql: 'SELECT * FROM reviews WHERE id = ?',
      args: [id as string]
    });

    if (existing.rows.length === 0) {
      return new Response(JSON.stringify({ error: 'Review not found' }), { status: 404 });
    }

    const current = existing.rows[0];
    const author_name = body.author_name !== undefined ? body.author_name : current.author_name;
    const author_location = body.author_location !== undefined ? body.author_location : current.author_location;
    const rating = body.rating !== undefined ? Number(body.rating) : Number(current.rating);
    const service_type = body.service_type !== undefined ? body.service_type : current.service_type;
    const content = body.content !== undefined ? body.content : current.content;
    const is_approved = body.is_approved !== undefined ? (body.is_approved ? 1 : 0) : current.is_approved;
    const is_featured = body.is_featured !== undefined ? (body.is_featured ? 1 : 0) : current.is_featured;
    const source = body.source !== undefined ? body.source : current.source;
    const now = new Date().toISOString();

    await db.execute({
      sql: `UPDATE reviews
            SET author_name = ?, author_location = ?, rating = ?, service_type = ?, content = ?,
                is_approved = ?, is_featured = ?, source = ?, updated_at = ?
            WHERE id = ?`,
      args: [author_name, author_location, rating, service_type, content, is_approved, is_featured, source, now, id as string]
    });

    await logAuditEvent(locals.user.userId, 'UPDATE_REVIEW', 'review', id as string, {
      is_approved,
      is_featured,
      author_name
    }, clientAddress);

    return new Response(JSON.stringify({ success: true, message: 'Review updated successfully' }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ error: 'Failed to update review: ' + err.message }), { status: 500 });
  }
};

export const DELETE: APIRoute = async ({ params, locals, clientAddress }) => {
  if (!locals.user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  // Destruction permission: Only owner or authorized staff
  await ensureDbInitialized();
  const { id } = params;

  const existing = await db.execute({
    sql: 'SELECT author_name, rating FROM reviews WHERE id = ?',
    args: [id as string]
  });

  if (existing.rows.length === 0) {
    return new Response(JSON.stringify({ error: 'Review not found' }), { status: 404 });
  }

  const review = existing.rows[0];

  await db.execute({
    sql: 'DELETE FROM reviews WHERE id = ?',
    args: [id as string]
  });

  await logAuditEvent(locals.user.userId, 'DELETE_REVIEW', 'review', id as string, {
    author: review.author_name,
    rating: review.rating
  }, clientAddress);

  return new Response(JSON.stringify({ success: true, message: 'Review deleted successfully' }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
};

