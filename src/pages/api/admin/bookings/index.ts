import type { APIRoute } from 'astro';
import { db, ensureDbInitialized } from '../../../../lib/db';

export const GET: APIRoute = async ({ url, locals }) => {
  if (!locals.user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  await ensureDbInitialized();

  const filter = url.searchParams.get('status') || 'all';
  const search = url.searchParams.get('q')?.trim() || '';

  let sql = 'SELECT * FROM booking_submissions';
  const conditions: string[] = [];
  const args: any[] = [];

  if (filter !== 'all') {
    conditions.push('status = ?');
    args.push(filter);
  }

  if (search) {
    conditions.push('(customer_name LIKE ? OR customer_email LIKE ? OR customer_phone LIKE ? OR service_requested LIKE ?)');
    const term = `%${search}%`;
    args.push(term, term, term, term);
  }

  if (conditions.length > 0) {
    sql += ' WHERE ' + conditions.join(' AND ');
  }

  sql += ' ORDER BY created_at DESC';

  const res = await db.execute({ sql, args });

  return new Response(JSON.stringify({ bookings: res.rows }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
};

