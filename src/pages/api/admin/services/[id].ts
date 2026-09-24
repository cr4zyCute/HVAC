import type { APIRoute } from 'astro';
import { db, ensureDbInitialized } from '../../../../lib/db';
import { logAuditEvent } from '../../../../lib/auth';
import { broadcastCmsUpdate } from '../../../../lib/realtime';

export const GET: APIRoute = async ({ params, locals }) => {
  if (!locals.user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  await ensureDbInitialized();
  const { id } = params;

  const res = await db.execute({
    sql: 'SELECT * FROM services WHERE id = ?',
    args: [id as string]
  });

  if (res.rows.length === 0) {
    return new Response(JSON.stringify({ error: 'Service not found' }), { status: 404 });
  }

  return new Response(JSON.stringify({ service: res.rows[0] }), {
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
      sql: 'SELECT * FROM services WHERE id = ?',
      args: [id as string]
    });

    if (existing.rows.length === 0) {
      return new Response(JSON.stringify({ error: 'Service not found' }), { status: 404 });
    }

    const current = existing.rows[0];
    const title = body.title !== undefined ? body.title : current.title;
    const slug = body.slug !== undefined ? body.slug.trim().toLowerCase().replace(/[^a-z0-9-]+/g, '-') : current.slug;
    const short_desc = body.short_desc !== undefined ? body.short_desc : current.short_desc;
    const full_desc = body.full_desc !== undefined ? body.full_desc : current.full_desc;
    const starting_price = body.starting_price !== undefined ? Number(body.starting_price) : Number(current.starting_price);
    const features_json = body.features !== undefined ? JSON.stringify(body.features) : current.features_json;
    const is_active = body.is_active !== undefined ? (body.is_active ? 1 : 0) : current.is_active;
    const display_order = body.display_order !== undefined ? Number(body.display_order) : Number(current.display_order);
    const image_url = body.image_url !== undefined ? body.image_url : current.image_url;
    const cta_text = body.cta_text !== undefined ? body.cta_text : current.cta_text;
    const cta_url = body.cta_url !== undefined ? body.cta_url : current.cta_url;
    const seo_title = body.seo_title !== undefined ? body.seo_title : current.seo_title;
    const seo_description = body.seo_description !== undefined ? body.seo_description : current.seo_description;
    const now = new Date().toISOString();

    // Check slug uniqueness if slug changed
    if (slug !== current.slug) {
      const dup = await db.execute({
        sql: 'SELECT id FROM services WHERE slug = ? AND id != ?',
        args: [slug, id as string]
      });
      if (dup.rows.length > 0) {
        return new Response(JSON.stringify({ error: `Slug "${slug}" is already taken by another service.` }), { status: 400 });
      }
    }

    await db.execute({
      sql: `UPDATE services
            SET slug = ?, title = ?, short_desc = ?, full_desc = ?, starting_price = ?,
                features_json = ?, is_active = ?, display_order = ?,
                image_url = ?, cta_text = ?, cta_url = ?, seo_title = ?, seo_description = ?,
                updated_at = ?
            WHERE id = ?`,
      args: [
        slug, title, short_desc, full_desc, starting_price,
        features_json, is_active, display_order,
        image_url, cta_text, cta_url, seo_title, seo_description,
        now, id as string
      ]
    });

    await logAuditEvent(locals.user.userId, 'UPDATE_SERVICE', 'service', id as string, {
      title,
      is_active,
      price: starting_price
    }, clientAddress);

    broadcastCmsUpdate({
      type: 'services',
      action: 'update',
      id: id as string
    });

    return new Response(JSON.stringify({ success: true, message: 'Service updated successfully' }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ error: 'Failed to update service: ' + err.message }), { status: 500 });
  }
};

export const DELETE: APIRoute = async ({ params, locals, clientAddress }) => {
  if (!locals.user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  await ensureDbInitialized();
  const { id } = params;

  const existing = await db.execute({
    sql: 'SELECT * FROM services WHERE id = ?',
    args: [id as string]
  });

  if (existing.rows.length === 0) {
    return new Response(JSON.stringify({ error: 'Service not found' }), { status: 404 });
  }

  await db.execute({
    sql: 'DELETE FROM services WHERE id = ?',
    args: [id as string]
  });

  await logAuditEvent(locals.user.userId, 'DELETE_SERVICE', 'service', id as string, {
    deleted_service_title: existing.rows[0].title
  }, clientAddress);

  broadcastCmsUpdate({
    type: 'services',
    action: 'delete',
    id: id as string
  });

  return new Response(JSON.stringify({ success: true, message: 'Service permanently deleted' }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
};
