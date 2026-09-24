import os, re

# 1. Update scratch/mobile_helpers.py
mh_path = 'scratch/mobile_helpers.py'
with open(mh_path, 'r', encoding='utf-8') as f:
    mh_code = f.read()

# Replace the distorted phone icon and crude hamburger menu with official Lucide phone & menu
old_header = '''    <!-- Call & Menu Icons -->
    <g transform="translate(300, 48)">
      <!-- Phone Call Circle -->
      <circle cx="16" cy="16" r="16" fill="#EFF6FF"/>
      <path d="M11 11C11 14 13.5 16.5 16.5 16.5L18 15L20 16V18C20 19.5 18.5 20.5 17 20.5C9 20.5 3.5 15 3.5 7C3.5 5.5 4.5 4 6 4H8L9 6L7.5 7.5" transform="translate(4, 3) scale(0.65)" stroke="#2563EB" stroke-width="2" stroke-linecap="round"/>

      <!-- Hamburger Menu -->
      <g transform="translate(42, 0)">
        <rect width="32" height="32" rx="6" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <line x1="8" y1="10" x2="24" y2="10" stroke="#0F2238" stroke-width="2" stroke-linecap="round"/>
        <line x1="8" y1="16" x2="24" y2="16" stroke="#0F2238" stroke-width="2" stroke-linecap="round"/>
        <line x1="8" y1="22" x2="24" y2="22" stroke="#0F2238" stroke-width="2" stroke-linecap="round"/>
      </g>
    </g>'''

new_header = '''    <!-- Call & Menu Action Buttons (Official Lucide Phone & Menu from Iconify) -->
    <g transform="translate(286, 48)">
      <!-- Quick Call Button (36x36 with Lucide Phone) -->
      <rect width="36" height="36" rx="8" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>
      <svg x="8" y="8" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
      </svg>

      <!-- Hamburger Menu Button (36x36 with Lucide Menu) -->
      <g transform="translate(44, 0)">
        <rect width="36" height="36" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <svg x="8" y="8" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0F2238" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="4" x2="20" y1="12" y2="12"/>
          <line x1="4" x2="20" y1="6" y2="6"/>
          <line x1="4" x2="20" y1="18" y2="18"/>
        </svg>
      </g>
    </g>'''

if old_header in mh_code:
    mh_code = mh_code.replace(old_header, new_header)
    with open(mh_path, 'w', encoding='utf-8') as f:
        f.write(mh_code)
    print("Updated scratch/mobile_helpers.py with official Lucide phone & menu icons!")
else:
    print("WARNING: old_header not found in scratch/mobile_helpers.py")

# 2. Update scratch/generate_mobile_all.py
gen_path = 'scratch/generate_mobile_all.py'
with open(gen_path, 'r', encoding='utf-8') as f:
    gen_code = f.read()

# Replace old AI-looking badge in Home
old_m00_badge = '''    <rect width="160" height="24" rx="12" fill="#EFF6FF"/>
    <text x="80" y="16" fill="#2563EB" font-family="'Inter', sans-serif" font-size="10" font-weight="700" text-anchor="middle">• METRO REGION</text>'''

new_m00_badge = '''    <!-- Modern Linear/Stripe-Style Live Status Badge -->
    <rect width="180" height="26" rx="13" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1"/>
    <circle cx="15" cy="13" r="5" fill="#10B981" fill-opacity="0.25"/>
    <circle cx="15" cy="13" r="3" fill="#059669"/>
    <text x="26" y="17" fill="#065F46" font-family="'Inter', sans-serif" font-size="11" font-weight="600" letter-spacing="0.4">24/7 DISPATCH ACTIVE</text>'''

if old_m00_badge in gen_code:
    gen_code = gen_code.replace(old_m00_badge, new_m00_badge)
    print("Replaced old • METRO REGION badge in generate_mobile_all.py")
else:
    print("Note: old_m00_badge pattern not matched directly, checking variations...")

# Replace any lingering &bull; or • METRO REGION
gen_code = re.sub(
    r'<rect width="160" height="24" rx="12" fill="#EFF6FF"/>\s*<text[^>]*>.*?METRO REGION.*?</text>',
    new_m00_badge,
    gen_code
)

# Also update emergency badge in 09-emergency-hvac
old_em_badge = '''    <rect width="180" height="24" rx="12" fill="#DC2626"/>
    <text x="90" y="16" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="10" font-weight="700" text-anchor="middle">• PRIORITY DISPATCH</text>'''
new_em_badge = '''    <!-- Modern Urgent Status Badge -->
    <rect width="176" height="26" rx="13" fill="#FEF2F2" stroke="#FECACA" stroke-width="1"/>
    <circle cx="15" cy="13" r="5" fill="#EF4444" fill-opacity="0.25"/>
    <circle cx="15" cy="13" r="3" fill="#DC2626"/>
    <text x="26" y="17" fill="#991B1B" font-family="'Inter', sans-serif" font-size="11" font-weight="600" letter-spacing="0.4">PRIORITY DISPATCH</text>'''
gen_code = gen_code.replace(old_em_badge, new_em_badge)

with open(gen_path, 'w', encoding='utf-8') as f:
    f.write(gen_code)
print("Updated scratch/generate_mobile_all.py!")

