import type { APIRoute } from 'astro';
import { db } from '@/lib/db';
import { logAuditEvent } from '@/lib/auth';
import { broadcastCmsUpdate } from '@/lib/realtime';

export const PUT: APIRoute = async ({ params, request, locals, clientAddress }) => {
  const user = locals.user;
  if (!user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  const { id } = params;
  if (!id) {
    return new Response(JSON.stringify({ error: 'Missing ID' }), { status: 400 });
  }

  try {
    const body = await request.json();
    const label = body.label !== undefined ? String(body.label).trim() : null;
    const href = body.href !== undefined ? String(body.href).trim() : null;
    const display_order = body.display_order !== undefined ? Number(body.display_order) : null;
    const is_enabled = body.is_enabled !== undefined ? (body.is_enabled ? 1 : 0) : null;

    const existing = await db.execute({
      sql: 'SELECT * FROM navigation_items WHERE id = ? LIMIT 1',
      args: [id]
    });

    if (existing.rows.length === 0) {
      return new Response(JSON.stringify({ error: 'Navigation item not found' }), { status: 404 });
    }

    const item = existing.rows[0];
    const newLabel = label !== null ? label : (item.label as string);
    const newHref = href !== null ? href : (item.href as string);
    const newOrder = display_order !== null ? display_order : Number(item.display_order);
    const newEnabled = is_enabled !== null ? is_enabled : Number(item.is_enabled);
    const now = new Date().toISOString();

    await db.execute({
      sql: `UPDATE navigation_items
            SET label = ?, href = ?, display_order = ?, is_enabled = ?, updated_at = ?
            WHERE id = ?`,
      args: [newLabel, newHref, newOrder, newEnabled, now, id]
    });

    await logAuditEvent(
      user.userId,
      'NAVIGATION_ITEM_UPDATED',
      'navigation_item',
      id,
      { label: newLabel, href: newHref, is_enabled: newEnabled },
      clientAddress
    );

    broadcastCmsUpdate({
      type: 'navigation',
      action: 'update',
      id
    });

    return new Response(JSON.stringify({ success: true }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ error: err.message }), { status: 500 });
  }
};

export const DELETE: APIRoute = async ({ params, locals, clientAddress }) => {
  const user = locals.user;
  if (!user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  const { id } = params;
  if (!id) {
    return new Response(JSON.stringify({ error: 'Missing ID' }), { status: 400 });
  }

  try {
    const existing = await db.execute({
      sql: 'SELECT * FROM navigation_items WHERE id = ? LIMIT 1',
      args: [id]
    });

    if (existing.rows.length === 0) {
      return new Response(JSON.stringify({ error: 'Navigation item not found' }), { status: 404 });
    }

    await db.execute({
      sql: 'DELETE FROM navigation_items WHERE id = ?',
      args: [id]
    });

    await logAuditEvent(
      user.userId,
      'NAVIGATION_ITEM_DELETED',
      'navigation_item',
      id,
      { label: existing.rows[0].label },
      clientAddress
    );

    broadcastCmsUpdate({
      type: 'navigation',
      action: 'delete',
      id
    });

    return new Response(JSON.stringify({ success: true }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ error: err.message }), { status: 500 });
  }
};
