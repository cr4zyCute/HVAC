import type { APIRoute } from 'astro';
import { clearSessionCookie, destroySession, getSessionIdFromCookies, logAuditEvent } from '../../../../lib/auth';

export const POST: APIRoute = async ({ cookies, locals, clientAddress }) => {
  const sessionId = getSessionIdFromCookies(cookies);
  if (sessionId) {
    await destroySession(sessionId);
  }
  clearSessionCookie(cookies);

  if (locals.user) {
    await logAuditEvent(locals.user.userId, 'LOGOUT', 'user', locals.user.userId, undefined, clientAddress);
  }

  return new Response(JSON.stringify({ success: true }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
};

