import { defineMiddleware } from 'astro:middleware';
import { getSessionIdFromCookies, validateSession, validateCsrfToken, logAuditEvent } from './lib/auth';

const PUBLIC_ADMIN_PATHS = [
  '/admin/login',
  '/admin/forgot-password',
  '/admin/reset-password',
  '/api/admin/auth/login',
  '/api/admin/auth/forgot-password',
  '/api/admin/auth/reset-password'
];

const OWNER_ONLY_PREFIXES = [
  '/admin/settings',
  '/api/admin/settings',
  '/admin/navigation',
  '/api/admin/navigation',
  '/admin/users',
  '/api/admin/users',
  '/admin/audit-logs',
  '/api/admin/audit-logs'
];

export const onRequest = defineMiddleware(async (context, next) => {
  const url = new URL(context.request.url);
  const pathname = url.pathname;
  const method = context.request.method;

  // Read session cookie
  const sessionId = getSessionIdFromCookies(context.cookies);
  const sessionUser = sessionId ? await validateSession(sessionId) : null;
  context.locals.user = sessionUser;

  const isAdminRoute = pathname.startsWith('/admin');
  const isAdminApiRoute = pathname.startsWith('/api/admin');

  // If not accessing an admin UI or admin API, continue normally
  if (!isAdminRoute && !isAdminApiRoute) {
    return next();
  }

  // Check if this is an exempted public admin path (like login or forgot password)
  const isPublicAdminPath = PUBLIC_ADMIN_PATHS.some(p => pathname === p || pathname.startsWith(p + '/'));
  if (isPublicAdminPath) {
    // If user is already authenticated and visits /admin/login, redirect to /admin
    if (sessionUser && pathname === '/admin/login') {
      return context.redirect('/admin');
    }
    return next();
  }

  // Enforce authentication for protected admin routes
  if (!sessionUser) {
    if (isAdminApiRoute) {
      return new Response(JSON.stringify({ error: 'Authentication required' }), {
        status: 401,
        headers: { 'Content-Type': 'application/json' }
      });
    }
    // Admin page: redirect to login with return path
    return context.redirect(`/admin/login?redirect=${encodeURIComponent(pathname)}`);
  }

  // Enforce strict Anti-CSRF Token check on all state-changing API mutations
  const isStateChangingMethod = ['POST', 'PUT', 'PATCH', 'DELETE'].includes(method);
  if (isAdminApiRoute && isStateChangingMethod) {
    const csrfToken = context.request.headers.get('x-csrf-token') || context.request.headers.get('csrf-token');
    const isCsrfValid = validateCsrfToken(sessionUser.sessionId, csrfToken);

    if (!isCsrfValid) {
      await logAuditEvent(
        sessionUser.userId,
        'CSRF_VALIDATION_FAILED',
        'security',
        undefined,
        { path: pathname, method, hasHeader: !!csrfToken },
        context.clientAddress
      );
      return new Response(JSON.stringify({ error: 'Forbidden: Invalid or missing CSRF token' }), {
        status: 403,
        headers: { 'Content-Type': 'application/json' }
      });
    }
  }

  // RBAC Role verification: Staff vs Owner
  const isOwnerOnly = OWNER_ONLY_PREFIXES.some(prefix => pathname.startsWith(prefix));
  if (isOwnerOnly && sessionUser.role !== 'owner') {
    if (isAdminApiRoute) {
      return new Response(JSON.stringify({ error: 'Forbidden: Owner role required' }), {
        status: 403,
        headers: { 'Content-Type': 'application/json' }
      });
    }
    // Admin page: show forbidden page or redirect to admin home with error
    return context.redirect('/admin?error=forbidden');
  }

  return next();
});

