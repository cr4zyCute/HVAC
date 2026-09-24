import type { APIRoute } from 'astro';
import { db } from '@/lib/db';
import { logAuditEvent } from '@/lib/auth';
import { broadcastCmsUpdate } from '@/lib/realtime';
import fs from 'node:fs/promises';
import path from 'node:path';

const ALLOWED_MIME_TYPES = new Set([
  'image/jpeg',
  'image/png',
  'image/webp',
  'image/svg+xml',
  'image/gif'
]);

const MAX_FILE_SIZE = 10 * 1024 * 1024; // 10MB limit

export const GET: APIRoute = async ({ request, locals }) => {
  const user = locals.user;
  if (!user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  const url = new URL(request.url);
  const search = url.searchParams.get('q')?.trim() || '';

  try {
    let sql = 'SELECT * FROM media';
    const args: any[] = [];

    if (search) {
      sql += ' WHERE file_name LIKE ? OR alt_text LIKE ?';
      const term = `%${search}%`;
      args.push(term, term);
    }

    sql += ' ORDER BY created_at DESC';

    const res = await db.execute({ sql, args });
    return new Response(JSON.stringify({ success: true, media: res.rows }), {
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
    const formData = await request.formData();
    const file = formData.get('file') as File | null;
    const altText = (formData.get('alt_text') as string) || '';

    if (!file || typeof file === 'string') {
      return new Response(JSON.stringify({ error: 'No valid file uploaded' }), { status: 400 });
    }

    if (!ALLOWED_MIME_TYPES.has(file.type)) {
      return new Response(
        JSON.stringify({ error: `File type ${file.type} is not allowed. Only JPG, PNG, WEBP, SVG, and GIF are supported.` }),
        { status: 400 }
      );
    }

    if (file.size > MAX_FILE_SIZE) {
      return new Response(
        JSON.stringify({ error: `File size exceeds 10MB limit (size: ${(file.size / (1024 * 1024)).toFixed(1)}MB)` }),
        { status: 400 }
      );
    }

    // Sanitize filename
    const originalName = file.name || 'uploaded-image.jpg';
    const ext = path.extname(originalName).toLowerCase() || '.jpg';
    const baseName = path.basename(originalName, ext).replace(/[^a-zA-Z0-9_-]/g, '-').toLowerCase();
    const uniqueFileName = `${baseName}-${Date.now()}${ext}`;

    const uploadsDir = path.join(process.cwd(), 'public', 'uploads');
    await fs.mkdir(uploadsDir, { recursive: true });

    const targetPath = path.join(uploadsDir, uniqueFileName);
    const buffer = Buffer.from(await file.arrayBuffer());
    await fs.writeFile(targetPath, buffer);

    const publicUrl = `/uploads/${uniqueFileName}`;
    const mediaId = `med_${Date.now()}_${Math.random().toString(36).substring(2, 7)}`;
    const now = new Date().toISOString();

    await db.execute({
      sql: `INSERT INTO media (id, file_name, url, mime_type, file_size, alt_text, width, height, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, NULL, NULL, ?, ?)`,
      args: [mediaId, originalName, publicUrl, file.type, file.size, altText || originalName, now, now]
    });

    await logAuditEvent(
      user.userId,
      'MEDIA_UPLOADED',
      'media',
      mediaId,
      { file_name: originalName, url: publicUrl, size: file.size, mime: file.type },
      clientAddress
    );

    broadcastCmsUpdate({
      type: 'media',
      action: 'create',
      id: mediaId
    });

    return new Response(
      JSON.stringify({
        success: true,
        media: {
          id: mediaId,
          file_name: originalName,
          url: publicUrl,
          mime_type: file.type,
          file_size: file.size,
          alt_text: altText || originalName,
          created_at: now
        }
      }),
      { status: 201, headers: { 'Content-Type': 'application/json' } }
    );
  } catch (err: any) {
    return new Response(JSON.stringify({ error: 'Upload failed: ' + err.message }), { status: 500 });
  }
};
