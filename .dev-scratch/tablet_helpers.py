import os, sys, base64

sys.stdout.reconfigure(encoding='utf-8')

img_dir = os.path.join(os.getcwd(), 'assets', 'images')
with open(os.path.join(img_dir, 'hero_opt.jpg'), 'rb') as f:
    b64_hero = base64.b64encode(f.read()).decode('ascii')
with open(os.path.join(img_dir, 'furnace_opt.jpg'), 'rb') as f:
    b64_furnace = base64.b64encode(f.read()).decode('ascii')
with open(os.path.join(img_dir, 'van_opt.jpg'), 'rb') as f:
    b64_van = base64.b64encode(f.read()).decode('ascii')

tablet_dir = os.path.join(os.getcwd(), 'svgs', 'responsive', 'tablet')
os.makedirs(tablet_dir, exist_ok=True)

def tablet_header():
    return '''  <!-- Tablet Header (834px) -->
  <g id="Tablet-Header">
    <rect width="834" height="40" fill="#0F2238"/>
    <text x="32" y="25" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12">Serving Metro Region &bull; 24/7 Emergency Dispatch Active</text>
    <text x="802" y="25" fill="#F59E0B" font-family="'Inter', sans-serif" font-size="12" font-weight="700" text-anchor="end">(555) 014-7824</text>
    
    <rect y="40" width="834" height="74" fill="#FFFFFF"/>
    <line x1="0" y1="114" x2="834" y2="114" stroke="#E2E8F0" stroke-width="1"/>
    
    <!-- Logo -->
    <g transform="translate(32, 54)">
      <rect width="36" height="36" rx="6" fill="#0F2238"/>
      <polygon points="18 9 20.5 14.5 26.5 15.2 22 19 23.5 25 18 22 12.5 25 14 19 9.5 15.2 15.5 14.5 18 9" fill="#FFFFFF"/>
      <text x="46" y="20" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="17" font-weight="800">NorthStar HVAC</text>
      <text x="46" y="33" fill="#E65100" font-family="'Inter', sans-serif" font-size="10" font-weight="600" letter-spacing="0.5">COMFORT YOU CAN COUNT ON</text>
    </g>

    <!-- Nav actions -->
    <g transform="translate(560, 56)">
      <rect width="140" height="40" rx="6" fill="#E65100"/>
      <text x="70" y="25" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="700" text-anchor="middle">Book Service</text>

      <g transform="translate(160, 4)">
        <rect width="32" height="32" rx="6" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1"/>
        <line x1="8" y1="11" x2="24" y2="11" stroke="#0F2238" stroke-width="2" stroke-linecap="round"/>
        <line x1="8" y1="16" x2="24" y2="16" stroke="#0F2238" stroke-width="2" stroke-linecap="round"/>
        <line x1="8" y1="21" x2="24" y2="21" stroke="#0F2238" stroke-width="2" stroke-linecap="round"/>
      </g>
    </g>
  </g>'''

def tablet_footer(y_pos):
    return f'''  <!-- Tablet Footer (Y: {y_pos}) -->
  <g id="Tablet-Footer" transform="translate(0, {y_pos})">
    <rect width="834" height="340" fill="#0A1829"/>
    <g transform="translate(32, 40)">
      <text x="0" y="22" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="18" font-weight="800">NorthStar HVAC Services</text>
      <text x="0" y="46" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="0" dy="0">Professional residential and commercial HVAC service.</tspan>
        <tspan x="0" dy="18">24/7 Emergency Dispatch: (555) 014-7824</tspan>
      </text>

      <line x1="0" y1="80" x2="770" y2="80" stroke="#1E293B" stroke-width="1"/>

      <!-- 3 Columns -->
      <g transform="translate(0, 110)">
        <text x="0" y="16" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Services</text>
        <text x="0" y="42" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12">AC Repair &bull; AC Installation</text>
        <text x="0" y="62" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12">Heating Repair &bull; Maintenance</text>
        <text x="0" y="82" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12">Indoor Air Quality &bull; Emergency</text>
      </g>

      <g transform="translate(280, 110)">
        <text x="0" y="16" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Company</text>
        <text x="0" y="42" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12">About NorthStar</text>
        <text x="0" y="62" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12">Service Areas</text>
        <text x="0" y="82" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12">Financing &bull; Reviews</text>
      </g>

      <g transform="translate(560, 110)">
        <text x="0" y="16" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Contact</text>
        <text x="0" y="42" fill="#38BDF8" font-family="'Inter', sans-serif" font-size="12" font-weight="600">(555) 014-7824</text>
        <text x="0" y="62" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12">hello@northstarhvac.example</text>
        <text x="0" y="82" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12">Mon-Sun 24/7 Dispatch</text>
      </g>

      <line x1="0" y1="220" x2="770" y2="220" stroke="#1E293B" stroke-width="1"/>
      <text x="0" y="248" fill="#64748B" font-family="'Inter', sans-serif" font-size="11">&copy; 2026 NorthStar HVAC Services. Fictional business website UI design project.</text>
    </g>
  </g>'''

print("Tablet helpers ready.")

