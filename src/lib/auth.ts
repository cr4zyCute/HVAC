import crypto from 'node:crypto';
import bcrypt from 'bcryptjs';
import { db, ensureDbInitialized } from './db';
import type { AstroCookies } from 'astro';

export interface UserSession {
  sessionId: string;
  userId: string;
  email: string;
  role: 'owner' | 'staff';
  name: string;
  csrfToken: string;
}

const SESSION_COOKIE_NAME = 'northstar_admin_session';
const SESSION_DURATION_HOURS = 24 * 7; // 7 days
const MAX_FAILED_ATTEMPTS = 5;
const LOCKOUT_MINUTES = 15;
const CSRF_SECRET = process.env.CSRF_SECRET || 'northstar-hvac-csrf-secret-salt-2026';

/**
 * Derives a cryptographically strong HMAC CSRF token bound to the user's active session.
 */
export function generateCsrfToken(sessionId: string): string {
  return crypto.createHmac('sha256', CSRF_SECRET).update(sessionId).digest('hex');
}

/**
 * Validates the CSRF token against the user's session using constant-time comparison.
 */
export function validateCsrfToken(sessionId: string, token: string | null | undefined): boolean {
  if (!sessionId || !token || typeof token !== 'string') return false;
  const expected = generateCsrfToken(sessionId);
  if (token.length !== expected.length) return false;
  return crypto.timingSafeEqual(Buffer.from(token), Buffer.from(expected));
}

/**
 * Validates a session token from cookie/header.
 * Returns UserSession if valid and not expired, null otherwise.
 */
export async function validateSession(sessionId: string): Promise<UserSession | null> {
  if (!sessionId || typeof sessionId !== 'string') return null;
  await ensureDbInitialized();

  const nowIso = new Date().toISOString();

  const result = await db.execute({
    sql: `SELECT s.id as session_id, s.expires_at, u.id as user_id, u.email, u.role, u.name, u.locked_until
          FROM sessions s
          JOIN users u ON s.user_id = u.id
          WHERE s.id = ?`,
    args: [sessionId]
  });

  const row = result.rows[0];
  if (!row) return null;

  // Check session expiration
  if (new Date(row.expires_at as string) < new Date(nowIso)) {
    await destroySession(sessionId);
    return null;
  }

  // Check if user is locked
  if (row.locked_until && new Date(row.locked_until as string) > new Date(nowIso)) {
    return null;
  }

  return {
    sessionId: row.session_id as string,
    userId: row.user_id as string,
    email: row.email as string,
    role: row.role as 'owner' | 'staff',
    name: row.name as string,
    csrfToken: generateCsrfToken(row.session_id as string)
  };
}

/**
 * Creates a cryptographically random session and stores it in DB.
 */
export async function createSession(userId: string): Promise<string> {
  await ensureDbInitialized();
  const sessionId = crypto.randomBytes(32).toString('hex');
  const expiresAt = new Date(Date.now() + SESSION_DURATION_HOURS * 3600 * 1000).toISOString();
  const now = new Date().toISOString();

  await db.execute({
    sql: `INSERT INTO sessions (id, user_id, expires_at, created_at) VALUES (?, ?, ?, ?)`,
    args: [sessionId, userId, expiresAt, now]
  });

  return sessionId;
}

/**
 * Deletes a session from the DB.
 */
export async function destroySession(sessionId: string): Promise<void> {
  await ensureDbInitialized();
  await db.execute({
    sql: `DELETE FROM sessions WHERE id = ?`,
    args: [sessionId]
  });
}

/**
 * Verifies email + password with brute-force lockout protection.
 */
export async function authenticateWithPassword(email: string, password: string): Promise<{ success: boolean; user?: { id: string; email: string; role: 'owner' | 'staff'; name: string }; error?: string }> {
  await ensureDbInitialized();
  const now = new Date();
  const nowIso = now.toISOString();

  const normalizedEmail = email.trim().toLowerCase();

  const userRes = await db.execute({
    sql: `SELECT id, email, password_hash, role, name, failed_login_attempts, locked_until FROM users WHERE email = ?`,
    args: [normalizedEmail]
  });

  const user = userRes.rows[0];

  // Constant-time-like behavior: still hash check even if user not found to prevent timing attacks
  if (!user) {
    await bcrypt.compare(password, '$2a$12$e80e1yV53i1.L03W3J7iueh7jHqTqRzK3.l04o0yv4R8.wF2q.nK.');
    return { success: false, error: 'Invalid email or password' };
  }

  // Check lockout
  if (user.locked_until && new Date(user.locked_until as string) > now) {
    const unlockTime = new Date(user.locked_until as string);
    const minutesLeft = Math.ceil((unlockTime.getTime() - now.getTime()) / 60000);
    return {
      success: false,
      error: `Account is temporarily locked due to excessive failed attempts. Please try again in ${minutesLeft} minute(s).`
    };
  }

  const isValidPassword = await bcrypt.compare(password, user.password_hash as string);

  if (!isValidPassword) {
    const attempts = Number(user.failed_login_attempts || 0) + 1;
    let lockUntil: string | null = null;

    if (attempts >= MAX_FAILED_ATTEMPTS) {
      lockUntil = new Date(now.getTime() + LOCKOUT_MINUTES * 60000).toISOString();
    }

    await db.execute({
      sql: `UPDATE users SET failed_login_attempts = ?, locked_until = ?, updated_at = ? WHERE id = ?`,
      args: [attempts, lockUntil, nowIso, user.id as string]
    });

    return { success: false, error: 'Invalid email or password' };
  }

  // Reset failed attempts on success
  await db.execute({
    sql: `UPDATE users SET failed_login_attempts = 0, locked_until = NULL, updated_at = ? WHERE id = ?`,
    args: [nowIso, user.id as string]
  });

  return {
    success: true,
    user: {
      id: user.id as string,
      email: user.email as string,
      role: user.role as 'owner' | 'staff',
      name: user.name as string
    }
  };
}

/**
 * Creates a password reset token for a given user email.
 * Returns the raw token to send/display.
 */
export async function createPasswordResetToken(email: string): Promise<string | null> {
  await ensureDbInitialized();
  const normalizedEmail = email.trim().toLowerCase();

  const userRes = await db.execute({
    sql: `SELECT id FROM users WHERE email = ?`,
    args: [normalizedEmail]
  });

  const user = userRes.rows[0];
  if (!user) return null; // Silently avoid leaking email presence

  const rawToken = crypto.randomBytes(32).toString('hex');
  const tokenHash = crypto.createHash('sha256').update(rawToken).digest('hex');
  const expiresAt = new Date(Date.now() + 60 * 60 * 1000).toISOString(); // 1 hour
  const now = new Date().toISOString();
  const id = `prt_${crypto.randomBytes(8).toString('hex')}`;

  // Invalidate any existing unused reset tokens for this user
  await db.execute({
    sql: `UPDATE password_reset_tokens SET used = 1 WHERE user_id = ?`,
    args: [user.id as string]
  });

  await db.execute({
    sql: `INSERT INTO password_reset_tokens (id, user_id, token_hash, expires_at, used, created_at)
          VALUES (?, ?, ?, ?, 0, ?)`,
    args: [id, user.id as string, tokenHash, expiresAt, now]
  });

  return rawToken;
}

/**
 * Validates and consumes a reset token, updating the user's password.
 */
export async function resetPasswordWithToken(rawToken: string, newPassword: string): Promise<{ success: boolean; error?: string }> {
  await ensureDbInitialized();
  if (!rawToken || newPassword.length < 8) {
    return { success: false, error: 'Password must be at least 8 characters long.' };
  }

  const tokenHash = crypto.createHash('sha256').update(rawToken).digest('hex');
  const now = new Date();
  const nowIso = now.toISOString();

  const tokenRes = await db.execute({
    sql: `SELECT id, user_id, expires_at, used FROM password_reset_tokens WHERE token_hash = ?`,
    args: [tokenHash]
  });

  const tokenRow = tokenRes.rows[0];
  if (!tokenRow || Number(tokenRow.used) === 1 || new Date(tokenRow.expires_at as string) < now) {
    return { success: false, error: 'Reset link is invalid or has expired.' };
  }

  const newHash = await bcrypt.hash(newPassword, 12);

  // Invalidate token and update user password
  await db.batch([
    {
      sql: `UPDATE password_reset_tokens SET used = 1 WHERE id = ?`,
      args: [tokenRow.id as string]
    },
    {
      sql: `UPDATE users SET password_hash = ?, failed_login_attempts = 0, locked_until = NULL, updated_at = ? WHERE id = ?`,
      args: [newHash, nowIso, tokenRow.user_id as string]
    },
    // Invalidate all active sessions for this user for security
    {
      sql: `DELETE FROM sessions WHERE user_id = ?`,
      args: [tokenRow.user_id as string]
    }
  ], 'write');

  return { success: true };
}

/**
 * Records an audit log entry.
 */
export async function logAuditEvent(
  userId: string | null,
  action: string,
  entityType: string,
  entityId?: string,
  details?: Record<string, unknown>,
  ipAddress?: string
): Promise<void> {
  try {
    await ensureDbInitialized();
    const id = `aud_${crypto.randomBytes(8).toString('hex')}`;
    const now = new Date().toISOString();
    await db.execute({
      sql: `INSERT INTO audit_logs (id, user_id, action, entity_type, entity_id, details_json, ip_address, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)`,
      args: [id, userId, action, entityType, entityId || null, details ? JSON.stringify(details) : null, ipAddress || null, now]
    });
  } catch (err) {
    console.error('Failed to write audit log:', err);
  }
}

/**
 * Cookie Helpers for Astro
 */
export function setSessionCookie(cookies: AstroCookies, sessionId: string) {
  cookies.set(SESSION_COOKIE_NAME, sessionId, {
    path: '/',
    httpOnly: true,
    sameSite: 'lax',
    secure: process.env.NODE_ENV === 'production',
    maxAge: SESSION_DURATION_HOURS * 3600
  });
}

export function clearSessionCookie(cookies: AstroCookies) {
  cookies.delete(SESSION_COOKIE_NAME, {
    path: '/'
  });
}

export function getSessionIdFromCookies(cookies: AstroCookies): string | null {
  return cookies.get(SESSION_COOKIE_NAME)?.value || null;
}

