import type { APIRoute } from 'astro';
import crypto from 'node:crypto';
import { db, ensureDbInitialized } from '../../../../lib/db';
import { logAuditEvent } from '../../../../lib/auth';
import { broadcastCmsUpdate } from '../../../../lib/realtime';

export const GET: APIRoute = async ({ url, locals }) => {
  if (!locals.user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  await ensureDbInitialized();

  const search = url.searchParams.get('q')?.trim() || '';
  let sql = 'SELECT * FROM services';
  const conditions: string[] = [];
  const args: any[] = [];

  if (search) {
    conditions.push('(title LIKE ? OR short_desc LIKE ? OR slug LIKE ?)');
    const term = `%${search}%`;
    args.push(term, term, term);
  }

  if (conditions.length > 0) {
    sql += ' WHERE ' + conditions.join(' AND ');
  }

  sql += ' ORDER BY display_order ASC, created_at DESC';

  const res = await db.execute({ sql, args });

  return new Response(JSON.stringify({ services: res.rows }), {
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
    const {
      title, slug, short_desc, full_desc, starting_price,
      features, is_active, display_order, image_url, cta_text, cta_url, seo_title, seo_description
    } = body;

    if (!title || !slug || !short_desc) {
      return new Response(JSON.stringify({ error: 'Title, slug, and short description are required.' }), { status: 400 });
    }

    const price = Number(starting_price) || 0;
    const order = Number(display_order) || 0;
    const cleanSlug = slug.trim().toLowerCase().replace(/[^a-z0-9-]+/g, '-');

    // Check duplicate slug
    const dupCheck = await db.execute({
      sql: 'SELECT id FROM services WHERE slug = ?',
      args: [cleanSlug]
    });

    if (dupCheck.rows.length > 0) {
      return new Response(JSON.stringify({ error: `A service with slug "${cleanSlug}" already exists.` }), { status: 400 });
    }

    const id = `srv_${crypto.randomBytes(8).toString('hex')}`;
    const now = new Date().toISOString();
    const featuresJson = Array.isArray(features) ? JSON.stringify(features) : JSON.stringify([]);

    await db.execute({
      sql: `INSERT INTO services (
              id, slug, title, short_desc, full_desc, starting_price, features_json,
              image_url, cta_text, cta_url, seo_title, seo_description,
              is_active, display_order, created_at, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
      args: [
        id,
        cleanSlug,
        title.trim(),
        short_desc.trim(),
        (full_desc || short_desc).trim(),
        price,
        featuresJson,
        image_url || '/images/hero-technician-ac.jpg',
        cta_text || 'Book Service',
        cta_url || '/book',
        seo_title || title.trim(),
        seo_description || short_desc.trim(),
        is_active ? 1 : 0,
        order,
        now,
        now
      ]
    });

    await logAuditEvent(locals.user.userId, 'CREATE_SERVICE', 'service', id, { title, slug: cleanSlug, price }, clientAddress);

    broadcastCmsUpdate({
      type: 'services',
      action: 'create',
      id
    });

    return new Response(JSON.stringify({ success: true, id }), {
      status: 201,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ error: 'Failed to create service: ' + err.message }), { status: 500 });
  }
};
