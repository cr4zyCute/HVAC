import { createClient } from '@libsql/client';
import bcrypt from 'bcryptjs';

const db = createClient({ url: 'file:northstar.db' });
const res = await db.execute("SELECT email, password_hash, role, failed_login_attempts, locked_until FROM users WHERE email = 'admin@northstarhvac.com'");
const user = res.rows[0];
console.log('Account Email:', user.email);
console.log('Role:', user.role);
console.log('Failed Attempts:', user.failed_login_attempts);
console.log('Locked Until:', user.locked_until);

const candidates = [
  'NorthStarAdmin2026!',
  'AdminPassword123!',
  'admin12345',
  'Admin123!',
  'Northstar2026!'
];

let found = false;
for (const c of candidates) {
  const match = await bcrypt.compare(c, user.password_hash);
  if (match) {
    console.log('Active Password matches candidate:', c);
    found = true;
    break;
  }
}

if (!found) {
  console.log('Password does not match default list; user set a custom password.');
}

