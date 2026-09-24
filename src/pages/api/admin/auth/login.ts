import type { APIRoute } from 'astro';
import { authenticateWithPassword, createSession, setSessionCookie, logAuditEvent } from '../../../../lib/auth';

export const POST: APIRoute = async ({ request, cookies, clientAddress }) => {
  try {
    const body = await request.json();
    const { email, password } = body;

    if (!email || !password) {
      return new Response(JSON.stringify({ error: 'Email and password are required' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const authResult = await authenticateWithPassword(email, password);

    if (!authResult.success || !authResult.user) {
      await logAuditEvent(null, 'LOGIN_FAILED', 'user', undefined, { email }, clientAddress);
      return new Response(JSON.stringify({ error: authResult.error || 'Invalid email or password' }), {
        status: 401,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // Authentication succeeded: create session and set HttpOnly cookie
    const sessionId = await createSession(authResult.user.id);
    setSessionCookie(cookies, sessionId);

    await logAuditEvent(authResult.user.id, 'LOGIN_SUCCESS', 'user', authResult.user.id, { email: authResult.user.email }, clientAddress);

    return new Response(JSON.stringify({
      success: true,
      user: {
        id: authResult.user.id,
        email: authResult.user.email,
        name: authResult.user.name,
        role: authResult.user.role
      }
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ error: 'An unexpected server error occurred: ' + err.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};

