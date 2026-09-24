import type { APIRoute } from 'astro';
import { createPasswordResetToken, logAuditEvent } from '../../../../lib/auth';

export const POST: APIRoute = async ({ request, clientAddress }) => {
  try {
    const { email } = await request.json();
    if (!email) {
      return new Response(JSON.stringify({ error: 'Email is required' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    const token = await createPasswordResetToken(email);

    // OWASP recommendation: Always return a generic success message so attacker cannot enumerate existing emails
    // In local dev/staging, we also return the generated reset link if available for testing!
    const isDev = process.env.NODE_ENV !== 'production';

    await logAuditEvent(null, 'PASSWORD_RESET_REQUESTED', 'user', undefined, { email }, clientAddress);

    return new Response(JSON.stringify({
      success: true,
      message: 'If the email exists in our system, a password recovery link has been generated.',
      // For local testing convenience before SMTP integration:
      devResetLink: isDev && token ? `/admin/reset-password?token=${token}` : undefined
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ error: 'Error generating reset request: ' + err.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
};

