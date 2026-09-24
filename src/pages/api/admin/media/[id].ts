import type { APIRoute } from 'astro';
import { db } from '@/lib/db';
import { logAuditEvent } from '@/lib/auth';
import { broadcastCmsUpdate } from '@/lib/realtime';
import fs from 'node:fs/promises';
import path from 'node:path';

export const PUT: APIRoute = async ({ params, request, locals, clientAddress }) => {
  const user = locals.user;
  if (!user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  const { id } = params;
  if (!id) {
    return new Response(JSON.stringify({ error: 'Missing media ID' }), { status: 400 });
  }

  try {
    const body = await request.json();
    const altText = body.alt_text !== undefined ? String(body.alt_text).trim() : null;

    if (altText === null) {
      return new Response(JSON.stringify({ error: 'No fields to update' }), { status: 400 });
    }

    const now = new Date().toISOString();
    await db.execute({
      sql: 'UPDATE media SET alt_text = ?, updated_at = ? WHERE id = ?',
      args: [altText, now, id]
    });

    await logAuditEvent(
      user.userId,
      'MEDIA_UPDATED',
      'media',
      id,
      { alt_text: altText },
      clientAddress
    );

    broadcastCmsUpdate({
      type: 'media',
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
    return new Response(JSON.stringify({ error: 'Missing media ID' }), { status: 400 });
  }

  try {
    const existing = await db.execute({
      sql: 'SELECT * FROM media WHERE id = ? LIMIT 1',
      args: [id]
    });

    if (existing.rows.length === 0) {
      return new Response(JSON.stringify({ error: 'Media not found' }), { status: 404 });
    }

    const item = existing.rows[0];
    const itemUrl = item.url as string;

    // Delete file from disk if located in /uploads/
    if (itemUrl.startsWith('/uploads/')) {
      const diskPath = path.join(process.cwd(), 'public', itemUrl);
      try {
        await fs.unlink(diskPath);
      } catch (err: any) {
        // File may already have been removed, proceed with DB delete
        console.warn('Could not unlink media file:', err.message);
      }
    }

    await db.execute({
      sql: 'DELETE FROM media WHERE id = ?',
      args: [id]
    });

    await logAuditEvent(
      user.userId,
      'MEDIA_DELETED',
      'media',
      id,
      { file_name: item.file_name, url: item.url },
      clientAddress
    );

    broadcastCmsUpdate({
      type: 'media',
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
