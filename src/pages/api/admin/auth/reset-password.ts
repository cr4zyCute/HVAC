import type { APIRoute } from 'astro';
import { resetPasswordWithToken, logAuditEvent } from '../../../../lib/auth';

export const POST: APIRoute = async ({ request, clientAddress }) => {
  try {
    const { token, password } = await request.json();

    if (!token || !password) {
      return new Response(JSON.stringify({ error: 'Token and new password are required' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const result = await resetPasswordWithToken(token, password);

    if (!result.success) {
      return new Response(JSON.stringify({ error: result.error || 'Failed to reset password' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    await logAuditEvent(null, 'PASSWORD_RESET_SUCCESS', 'user', undefined, undefined, clientAddress);

    return new Response(JSON.stringify({
      success: true,
      message: 'Password successfully updated. You may now log in with your new credentials.'
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ error: 'Error resetting password: ' + err.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};

