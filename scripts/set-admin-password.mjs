import { createClient } from '@libsql/client';
import bcrypt from 'bcryptjs';

const newPassword = process.argv[2];

if (!newPassword || newPassword.length < 8) {
  console.error('Error: Please provide a password of at least 8 characters.');
  console.error('Usage: node scripts/set-admin-password.mjs "YourNewSecurePassword123!"');
  process.exit(1);
}

const db = createClient({
  url: process.env.DATABASE_URL || 'file:northstar.db',
  authToken: process.env.DATABASE_AUTH_TOKEN || undefined
});

async function updatePassword() {
  const hash = await bcrypt.hash(newPassword, 12);
  const now = new Date().toISOString();

  const res = await db.execute({
    sql: `UPDATE users SET password_hash = ?, failed_login_attempts = 0, locked_until = NULL, updated_at = ? WHERE email = 'admin@northstarhvac.com'`,
    args: [hash, now]
  });

  if (res.rowsAffected > 0) {
    // Invalidate existing sessions
    await db.execute("DELETE FROM sessions WHERE user_id = 'usr_owner_default'");
    console.log('SUCCESS: Admin password successfully updated and old sessions invalidated.');
    console.log('Account: admin@northstarhvac.com');
  } else {
    console.error('Error: Admin user admin@northstarhvac.com not found in database.');
  }
}

updatePassword().catch(console.error);

