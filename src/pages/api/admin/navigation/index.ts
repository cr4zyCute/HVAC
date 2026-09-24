import type { APIRoute } from 'astro';
import { db } from '@/lib/db';
import { logAuditEvent } from '@/lib/auth';
import { broadcastCmsUpdate } from '@/lib/realtime';

export const GET: APIRoute = async ({ locals }) => {
  const user = locals.user;
  if (!user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  try {
    const res = await db.execute('SELECT * FROM navigation_items ORDER BY display_order ASC');
    return new Response(JSON.stringify({ success: true, items: res.rows }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ error: err.message }), { status: 500 });
  }
};

export const POST: APIRoute = async ({ request, locals, clientAddress }) => {
  const user = locals.user;
  if (!user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  try {
    const body = await request.json();
    const label = String(body.label || '').trim();
    const href = String(body.href || '').trim();
    const position = String(body.position || 'header').trim();
    const display_order = Number(body.display_order ?? 0);
    const is_enabled = body.is_enabled !== undefined ? (body.is_enabled ? 1 : 0) : 1;

    if (!label || !href) {
      return new Response(JSON.stringify({ error: 'Label and destination link are required' }), { status: 400 });
    }

    const id = `nav_${Date.now()}_${Math.random().toString(36).substring(2, 6)}`;
    const now = new Date().toISOString();

    await db.execute({
      sql: `INSERT INTO navigation_items (id, label, href, position, display_order, is_enabled, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)`,
      args: [id, label, href, position, display_order, is_enabled, now, now]
    });

    await logAuditEvent(
      user.userId,
      'NAVIGATION_ITEM_CREATED',
      'navigation_item',
      id,
      { label, href, position },
      clientAddress
    );

    broadcastCmsUpdate({
      type: 'navigation',
      action: 'create',
      id
    });

    return new Response(JSON.stringify({ success: true, id }), {
      status: 201,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ error: err.message }), { status: 500 });
  }
};
