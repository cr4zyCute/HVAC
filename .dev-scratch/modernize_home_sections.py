import os

# 1. Update svgs/home/05-services-grid.svg with official Lucide icons
p05 = 'svgs/home/05-services-grid.svg'
with open(p05, 'r', encoding='utf-8') as f:
    c05 = f.read()

# Replace Card 1 (AC Repair) icon with Lucide Snowflake
old_ic1 = '''      <g transform="translate(32, 28)">
        <rect width="44" height="44" rx="8" fill="#EFF6FF"/>
        <path d="M22 14V30M14 22H30M16 16L28 28M16 28L28 16" stroke="#2563EB" stroke-width="2.5" stroke-linecap="round"/>
      </g>'''
new_ic1 = '''      <g transform="translate(32, 28)">
        <rect width="48" height="48" rx="10" fill="#EFF6FF" stroke="#DBEAFE" stroke-width="1"/>
        <g transform="translate(12, 12)" stroke="#2563EB" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
          <path d="M2 12h20M12 2v20M20 16l-4-4 4-4M4 8l4 4-4 4M16 4l-4 4-4-4M8 20l4-4 4 4"/>
        </g>
      </g>'''
c05 = c05.replace(old_ic1, new_ic1)

# Replace Card 2 (AC Installation) icon with Lucide Installation
old_ic2 = '''      <g transform="translate(32, 28)">
        <rect width="44" height="44" rx="8" fill="#ECFDF5"/>
        <path d="M14 22L22 15L30 22V31H14V22Z" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M19 31V25H25V31" stroke="#059669" stroke-width="2"/>
      </g>'''
new_ic2 = '''      <g transform="translate(32, 28)">
        <rect width="48" height="48" rx="10" fill="#F0FDF4" stroke="#DCFCE7" stroke-width="1"/>
        <g transform="translate(12, 12)" stroke="#16A34A" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
          <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
        </g>
      </g>'''
c05 = c05.replace(old_ic2, new_ic2)

# Replace Card 3 (Heating Repair) icon with Lucide Flame
old_ic3 = '''      <g transform="translate(32, 28)">
        <rect width="44" height="44" rx="8" fill="#FFF7ED"/>
        <path d="M22 13C22 13 17 18 17 24C17 27 19.3 29.5 22 29.5C24.7 29.5 27 27 27 24C27 18 22 13 22 13Z" stroke="#EA580C" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </g>'''
new_ic3 = '''      <g transform="translate(32, 28)">
        <rect width="48" height="48" rx="10" fill="#FFF7ED" stroke="#FFEDD5" stroke-width="1"/>
        <g transform="translate(12, 12)" stroke="#EA580C" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
          <path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>
        </g>
      </g>'''
c05 = c05.replace(old_ic3, new_ic3)

# Replace Card 4 (HVAC Maintenance) icon with Lucide Wrench
old_ic4 = '''      <g transform="translate(32, 28)">
        <rect width="44" height="44" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <path d="M24 18L18 24L26 32L32 26L24 18Z" stroke="#0F2238" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M20 22L14 16" stroke="#0F2238" stroke-width="2" stroke-linecap="round"/>
      </g>'''
new_ic4 = '''      <g transform="translate(32, 28)">
        <rect width="48" height="48" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <g transform="translate(12, 12)" stroke="#0F2238" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
          <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>
        </g>
      </g>'''
c05 = c05.replace(old_ic4, new_ic4)

# Replace Card 5 (Indoor Air Quality) icon with Lucide Wind
old_ic5 = '''      <g transform="translate(32, 28)">
        <rect width="44" height="44" rx="8" fill="#F0FDFA"/>
        <path d="M14 20H26C28 20 30 18 30 16C30 14 28 12 26 12C25 12 24.5 12.5 24 13" stroke="#0D9488" stroke-width="2" stroke-linecap="round"/>
        <path d="M14 24H28C30 24 32 26 32 28C32 30 30 32 28 32C27 32 26 31 26 30" stroke="#0D9488" stroke-width="2" stroke-linecap="round"/>
        <path d="M14 28H22" stroke="#0D9488" stroke-width="2" stroke-linecap="round"/>
      </g>'''
new_ic5 = '''      <g transform="translate(32, 28)">
        <rect width="48" height="48" rx="10" fill="#F0FDFA" stroke="#CCFBF1" stroke-width="1"/>
        <g transform="translate(12, 12)" stroke="#0D9488" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
          <path d="M17.7 7.7A2.5 2.5 0 1 1 16 12H2M19.7 17.7A2.5 2.5 0 1 0 18 13H2M14.5 4A2.5 2.5 0 0 0 12 6.5V7H2"/>
        </g>
      </g>'''
c05 = c05.replace(old_ic5, new_ic5)

# Replace Card 6 (Emergency HVAC) icon with Lucide AlertTriangle
old_ic6 = '''      <g transform="translate(32, 28)">
        <rect width="44" height="44" rx="8" fill="#FEF2F2"/>
        <path d="M22 13L13 29H31L22 13Z" stroke="#DC2626" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        <line x1="22" y1="19" x2="22" y2="23" stroke="#DC2626" stroke-width="2" stroke-linecap="round"/>
        <circle cx="22" cy="26" r="1" fill="#DC2626"/>
      </g>'''
new_ic6 = '''      <g transform="translate(32, 28)">
        <rect width="48" height="48" rx="10" fill="#FEF2F2" stroke="#FECACA" stroke-width="1"/>
        <g transform="translate(12, 12)" stroke="#DC2626" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
          <path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/>
          <line x1="12" x2="12" y1="9" y2="13"/>
          <line x1="12" x2="12.01" y1="17" y2="17"/>
        </g>
      </g>'''
c05 = c05.replace(old_ic6, new_ic6)

with open(p05, 'w', encoding='utf-8') as f:
    f.write(c05)
print("Updated svgs/home/05-services-grid.svg with Lucide icons!")

# 2. Update svgs/home/04-trust-signals.svg with official Lucide icons
p04 = 'svgs/home/04-trust-signals.svg'
with open(p04, 'r', encoding='utf-8') as f:
    c04 = f.read()

# Replace Trust 1 ShieldCheck
old_t1 = '''      <rect width="52" height="52" rx="10" fill="#F1F5F9"/>
      <!-- Shield Check Icon -->
      <path d="M26 14L15 18V28C15 35 20 40 26 42C32 40 37 35 37 28V18L26 14Z" fill="#1E3A5F" fill-opacity="0.1" stroke="#1E3A5F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M22 28L25 31L31 24" stroke="#15803D" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>'''

new_t1 = '''      <rect width="52" height="52" rx="10" fill="#F0FDF4" stroke="#DCFCE7" stroke-width="1"/>
      <g transform="translate(14, 14)" stroke="#16A34A" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>
        <path d="m9 12 2 2 4-4"/>
      </g>'''
c04 = c04.replace(old_t1, new_t1)

# Replace Trust 2 Clock
old_t2 = '''      <rect width="52" height="52" rx="10" fill="#F1F5F9"/>
      <!-- Clock Icon -->
      <circle cx="26" cy="26" r="14" stroke="#E65100" stroke-width="2"/>
      <path d="M26 18V26L31 29" stroke="#E65100" stroke-width="2" stroke-linecap="round"/>'''

new_t2 = '''      <rect width="52" height="52" rx="10" fill="#FEF2F2" stroke="#FEE2E2" stroke-width="1"/>
      <g transform="translate(14, 14)" stroke="#DC2626" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"/>
        <polyline points="12 6 12 12 16 14"/>
      </g>'''
c04 = c04.replace(old_t2, new_t2)

# Replace Trust 3 Award
old_t3 = '''      <rect width="52" height="52" rx="10" fill="#F1F5F9"/>
      <!-- Award Medal Icon -->
      <circle cx="26" cy="23" r="9" stroke="#1E3A5F" stroke-width="2"/>
      <path d="M21 31L18 42L26 38L34 42L31 31" stroke="#1E3A5F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'''

new_t3 = '''      <rect width="52" height="52" rx="10" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <g transform="translate(14, 14)" stroke="#0F2238" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="8" r="6"/>
        <path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/>
      </g>'''
c04 = c04.replace(old_t3, new_t3)

# Replace Trust 4 ThumbsUp
old_t4 = '''      <rect width="52" height="52" rx="10" fill="#F1F5F9"/>
      <!-- Thumbs Up / Check Star Icon -->
      <path d="M26 15L29 22L36 23L31 28L32 35L26 31.5L20 35L21 28L16 23L23 22L26 15Z" fill="#F59E0B" fill-opacity="0.2" stroke="#F59E0B" stroke-width="2" stroke-linejoin="round"/>'''

new_t4 = '''      <rect width="52" height="52" rx="10" fill="#FFF7ED" stroke="#FFEDD5" stroke-width="1"/>
      <g transform="translate(14, 14)" stroke="#E65100" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <path d="M7 10v12M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2h0a3.13 3.13 0 0 1 3 3.88Z"/>
      </g>'''
c04 = c04.replace(old_t4, new_t4)

with open(p04, 'w', encoding='utf-8') as f:
    f.write(c04)
print("Updated svgs/home/04-trust-signals.svg with Lucide icons!")

# 3. Update svgs/home/06-emergency-cta.svg
p06 = 'svgs/home/06-emergency-cta.svg'
with open(p06, 'r', encoding='utf-8') as f:
    c06 = f.read()

# Replace phone path in call now button
old_phone = '<path d="M4.5 3C4.5 9.07513 9.42487 14 15.5 14L17.5 12C17.8 11.7 18.2 11.6 18.6 11.8L21.2 12.9C21.7 13.1 22 13.6 22 14.1V17C22 17.5523 21.5523 18 21 18C10.5066 18 2 9.49341 2 -1C2 -1.55228 2.44772 -2 3 -2H5.9C6.4 -2 6.9 -1.7 7.1 -1.2L8.2 1.4C8.4 1.8 8.3 2.2 8 2.5L6 4.5" transform="translate(26, 17) scale(0.9)" stroke="#F59E0B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
new_phone = '<g transform="translate(24, 14)" stroke="#F59E0B" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/><path d="M14.05 2a9 9 0 0 1 8 7.94M14.05 6A5 5 0 0 1 18 10"/></g>'
c06 = c06.replace(old_phone, new_phone)

with open(p06, 'w', encoding='utf-8') as f:
    f.write(c06)
print("Updated svgs/home/06-emergency-cta.svg with Lucide PhoneCall!")

