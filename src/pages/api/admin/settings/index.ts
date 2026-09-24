import type { APIRoute } from 'astro';
import { db, ensureDbInitialized } from '../../../../lib/db';
import { logAuditEvent } from '../../../../lib/auth';
import { broadcastCmsUpdate } from '../../../../lib/realtime';

export const GET: APIRoute = async ({ locals }) => {
  if (!locals.user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  await ensureDbInitialized();

  const res = await db.execute('SELECT key, value, category, updated_at FROM site_settings');
  const settings: Record<string, string> = {};
  for (const row of res.rows) {
    settings[row.key as string] = (row.value as string) || '';
  }

  return new Response(JSON.stringify({ settings }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
};

async function handleUpdate(request: Request, locals: any, clientAddress: string) {
  if (!locals.user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  // RBAC: Owner only
  if (locals.user.role !== 'owner') {
    return new Response(JSON.stringify({ error: 'Forbidden: Owner role required' }), { status: 403 });
  }

  await ensureDbInitialized();

  try {
    const body = await request.json();
    const settings = body.settings && typeof body.settings === 'object' ? body.settings : body;

    if (!settings || typeof settings !== 'object' || Object.keys(settings).length === 0) {
      return new Response(JSON.stringify({ error: 'Invalid settings payload' }), { status: 400 });
    }

    const now = new Date().toISOString();
    const batchStatements = Object.entries(settings).map(([key, value]) => ({
      sql: `INSERT OR REPLACE INTO site_settings (key, value, updated_at) VALUES (?, ?, ?)`,
      args: [key, String(value ?? ''), now]
    }));

    await db.batch(batchStatements, 'write');

    await logAuditEvent(locals.user.userId, 'UPDATE_SITE_SETTINGS', 'settings', undefined, {
      updated_keys: Object.keys(settings)
    }, clientAddress);

    broadcastCmsUpdate({
      type: 'settings',
      action: 'update'
    });

    return new Response(JSON.stringify({
      success: true,
      message: 'Site settings updated successfully'
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ error: 'Failed to save settings: ' + err.message }), { status: 500 });
  }
}

export const PUT: APIRoute = async ({ request, locals, clientAddress }) => {
  return handleUpdate(request, locals, clientAddress);
};

export const POST: APIRoute = async ({ request, locals, clientAddress }) => {
  return handleUpdate(request, locals, clientAddress);
};
