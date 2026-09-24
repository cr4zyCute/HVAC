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
    const res = await db.execute('SELECT * FROM homepage_sections ORDER BY display_order ASC');
    return new Response(JSON.stringify({ success: true, sections: res.rows }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ error: err.message }), { status: 500 });
  }
};

export const PUT: APIRoute = async ({ request, locals, clientAddress }) => {
  const user = locals.user;
  if (!user) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  try {
    const body = await request.json();
    const sectionsToSave: any[] = Array.isArray(body.sections) ? body.sections : (body.section_key ? [body] : []);

    if (sectionsToSave.length === 0) {
      return new Response(JSON.stringify({ error: 'Missing section_key or sections array' }), { status: 400 });
    }

    const now = new Date().toISOString();
    const updatedKeys: string[] = [];

    for (const sec of sectionsToSave) {
      const section_key = String(sec.section_key || '').trim();
      if (!section_key) continue;

      const title = String(sec.title || '').trim();
      const subtitle = String(sec.subtitle || '').trim();
      const badge = String(sec.badge || '').trim();
      const description = String(sec.description || '').trim();
      const image_url = String(sec.image_url || '').trim();
      const image_alt = String(sec.image_alt || '').trim();
      const primary_btn_text = String(sec.primary_btn_text || '').trim();
      const primary_btn_url = String(sec.primary_btn_url || '').trim();
      const secondary_btn_text = String(sec.secondary_btn_text || '').trim();
      const secondary_btn_url = String(sec.secondary_btn_url || '').trim();
      const is_enabled = sec.is_enabled !== undefined ? (sec.is_enabled ? 1 : 0) : 1;
      const display_order = Number(sec.display_order ?? 0);

      let extra_data_json = '{}';
      if (typeof sec.extra_data === 'object') {
        extra_data_json = JSON.stringify(sec.extra_data);
      } else if (typeof sec.extra_data_json === 'string') {
        extra_data_json = sec.extra_data_json;
      }

      const existing = await db.execute({
        sql: 'SELECT id FROM homepage_sections WHERE section_key = ? LIMIT 1',
        args: [section_key]
      });

      if (existing.rows.length === 0) {
        const id = `sec_${section_key}_${Date.now()}`;
        await db.execute({
          sql: `INSERT INTO homepage_sections
                (id, section_key, title, subtitle, badge, description, image_url, image_alt, primary_btn_text, primary_btn_url, secondary_btn_text, secondary_btn_url, extra_data_json, is_enabled, display_order, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
          args: [
            id, section_key, title, subtitle, badge, description,
            image_url, image_alt, primary_btn_text, primary_btn_url,
            secondary_btn_text, secondary_btn_url, extra_data_json,
            is_enabled, display_order, now
          ]
        });
      } else {
        await db.execute({
          sql: `UPDATE homepage_sections
                SET title = ?, subtitle = ?, badge = ?, description = ?,
                    image_url = ?, image_alt = ?, primary_btn_text = ?, primary_btn_url = ?,
                    secondary_btn_text = ?, secondary_btn_url = ?, extra_data_json = ?,
                    is_enabled = ?, display_order = ?, updated_at = ?
                WHERE section_key = ?`,
          args: [
            title, subtitle, badge, description,
            image_url, image_alt, primary_btn_text, primary_btn_url,
            secondary_btn_text, secondary_btn_url, extra_data_json,
            is_enabled, display_order, now, section_key
          ]
        });
      }
      updatedKeys.push(section_key);
    }

    await logAuditEvent(
      user.userId,
      'HOMEPAGE_SECTION_UPDATED',
      'homepage_section',
      updatedKeys.join(','),
      { updated_sections: updatedKeys },
      clientAddress
    );

    broadcastCmsUpdate({
      type: 'homepage',
      section_keys: updatedKeys,
      action: 'update'
    });

    return new Response(JSON.stringify({ success: true, updated_keys: updatedKeys }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ error: err.message }), { status: 500 });
  }
};
