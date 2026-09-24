const res = await fetch('http://localhost:4321/api/admin/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'admin@northstarhvac.com',
    password: 'NorthStarAdmin2026!'
  })
});

const data = await res.json();
console.log('Login test HTTP Status:', res.status);
console.log('Login Response:', data);
console.log('Set-Cookie received:', res.headers.get('set-cookie') ? 'Yes (Session cookie generated)' : 'No');

