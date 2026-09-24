import os, sys, base64

sys.stdout.reconfigure(encoding='utf-8')

img_dir = os.path.join(os.getcwd(), 'assets', 'images')

with open(os.path.join(img_dir, 'hero_opt.jpg'), 'rb') as f:
    b64_hero = base64.b64encode(f.read()).decode('ascii')

with open(os.path.join(img_dir, 'furnace_opt.jpg'), 'rb') as f:
    b64_furnace = base64.b64encode(f.read()).decode('ascii')

with open(os.path.join(img_dir, 'van_opt.jpg'), 'rb') as f:
    b64_van = base64.b64encode(f.read()).decode('ascii')

print(f"Base64 sizes: Hero={len(b64_hero)}, Furnace={len(b64_furnace)}, Van={len(b64_van)}")

# 1. Update 03-hero.svg
hero_svg_path = 'svgs/home/03-hero.svg'
with open(hero_svg_path, 'r', encoding='utf-8') as f:
    hero_content = f.read()

# Replace the vector condenser with the real photograph and floating badges
old_visual_block = '''    <!-- Right Column: Visual Presentation Frame -->
    <g id="Hero-Visual-Container" transform="translate(740, 60)">
      <!-- Main Visual Backdrop Card -->
      <rect width="620" height="500" rx="16" fill="#0F2238"/>
      
      <!-- Visual Illustration: Modern HVAC Condenser & Diagnostics -->
      <g id="HVAC-Scene" transform="translate(40, 40)">
        <!-- Building Brick/Siding Texture -->
        <g opacity="0.15">
          <line x1="0" y1="60" x2="540" y2="60" stroke="#FFFFFF" stroke-dasharray="8 8"/>
          <line x1="0" y1="120" x2="540" y2="120" stroke="#FFFFFF" stroke-dasharray="8 8"/>
          <line x1="0" y1="180" x2="540" y2="180" stroke="#FFFFFF" stroke-dasharray="8 8"/>
          <line x1="0" y1="240" x2="540" y2="240" stroke="#FFFFFF" stroke-dasharray="8 8"/>
          <line x1="0" y1="300" x2="540" y2="300" stroke="#FFFFFF" stroke-dasharray="8 8"/>
        </g>

        <!-- Concrete Equipment Pad -->
        <rect x="60" y="320" width="360" height="30" rx="4" fill="#334155"/>

        <!-- Premium Outdoor Heat Pump / AC Unit -->
        <g id="AC-Condenser-Unit" transform="translate(100, 100)">
          <!-- Main Chassis Body -->
          <rect width="280" height="230" rx="12" fill="#1E293B" stroke="#475569" stroke-width="2"/>
          <!-- Fan Grille Ring -->
          <circle cx="140" cy="100" r="70" fill="#0F172A" stroke="#334155" stroke-width="3"/>
          <circle cx="140" cy="100" r="50" stroke="#475569" stroke-dasharray="6 4" stroke-width="1.5"/>
          <circle cx="140" cy="100" r="20" fill="#1E293B"/>
          <!-- Fan Blades -->
          <path d="M140 100L170 80M140 100L110 120M140 100L120 70M140 100L160 130" stroke="#94A3B8" stroke-width="4" stroke-linecap="round"/>
          <!-- Protective Grille Slats -->
          <line x1="20" y1="185" x2="260" y2="185" stroke="#334155" stroke-width="2"/>
          <line x1="20" y1="195" x2="260" y2="195" stroke="#334155" stroke-width="2"/>
          <line x1="20" y1="205" x2="260" y2="205" stroke="#334155" stroke-width="2"/>
          <!-- NorthStar Efficiency Badge on Unit -->
          <rect x="25" y="25" width="80" height="24" rx="4" fill="#0F2238" stroke="#38BDF8" stroke-width="1"/>
          <text x="65" y="41" fill="#38BDF8" font-family="'Inter', sans-serif" font-size="10" font-weight="700" text-anchor="middle">20+ SEER2</text>
        </g>
      </g>'''

new_visual_block = f'''    <!-- Right Column: Visual Presentation Frame with Realistic Photographic Imagery -->
    <g id="Hero-Visual-Container" transform="translate(740, 60)">
      <defs>
        <clipPath id="hero-photo-clip">
          <rect width="620" height="500" rx="16"/>
        </clipPath>
        <linearGradient id="hero-photo-overlay" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#0F2238" stop-opacity="0.05"/>
          <stop offset="65%" stop-color="#0F2238" stop-opacity="0.15"/>
          <stop offset="100%" stop-color="#0F2238" stop-opacity="0.75"/>
        </linearGradient>
      </defs>

      <!-- Main Visual Backdrop Card -->
      <rect width="620" height="500" rx="16" fill="#0F2238"/>
      
      <!-- Realistic Commercial HVAC Photography: Certified Technician with Digital Gauges -->
      <image href="data:image/jpeg;base64,{b64_hero}" width="620" height="500" preserveAspectRatio="xMidYMid slice" clip-path="url(#hero-photo-clip)"/>
      
      <!-- Protective Contrast Overlay -->
      <rect width="620" height="500" rx="16" fill="url(#hero-photo-overlay)" clip-path="url(#hero-photo-clip)"/>'''

if old_visual_block in hero_content:
    hero_content = hero_content.replace(old_visual_block, new_visual_block)
    with open(hero_svg_path, 'w', encoding='utf-8') as f:
        f.write(hero_content)
    print("Updated 03-hero.svg with photographic hero technician image!")
else:
    print("WARNING: old_visual_block not found in 03-hero.svg")

# 2. Update 07-why-choose-us.svg
why_svg_path = 'svgs/home/07-why-choose-us.svg'
with open(why_svg_path, 'r', encoding='utf-8') as f:
    why_content = f.read()

old_why_card = '''    <!-- Right Side: Technician Quality Standards Box -->
    <g id="Technician-Standards-Card" transform="translate(880, 200)">
      <rect width="480" height="390" rx="16" fill="#0F2238"/>
      <g transform="translate(40, 40)">
        <rect width="130" height="26" rx="13" fill="#1E3A5F"/>
        <text x="65" y="17" fill="#38BDF8" font-family="'Inter', sans-serif" font-size="11" font-weight="700" text-anchor="middle">SERVICE STANDARDS</text>
        
        <text x="0" y="68" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="800">
          <tspan x="0" dy="0">Clean Workmanship &amp;</tspan>
          <tspan x="0" dy="32">Guaranteed Protection.</tspan>
        </text>

        <g transform="translate(0, 130)">
          <!-- Standard 1 -->
          <circle cx="10" cy="10" r="10" fill="#1E3A5F"/>
          <path d="M7 10L9.5 12.5L13.5 7.5" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
          <text x="32" y="14" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="14" font-weight="600">Shoe Covers &amp; Drop Cloths Used on Every Job</text>

          <!-- Standard 2 -->
          <g transform="translate(0, 42)">
            <circle cx="10" cy="10" r="10" fill="#1E3A5F"/>
            <path d="M7 10L9.5 12.5L13.5 7.5" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
            <text x="32" y="14" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="14" font-weight="600">EPA-Certified Refrigerant Handlers</text>
          </g>

          <!-- Standard 3 -->
          <g transform="translate(0, 84)">
            <circle cx="10" cy="10" r="10" fill="#1E3A5F"/>
            <path d="M7 10L9.5 12.5L13.5 7.5" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
            <text x="32" y="14" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="14" font-weight="600">Full Post-Repair System Airflow Calibration</text>
          </g>

          <!-- Standard 4 -->
          <g transform="translate(0, 126)">
            <circle cx="10" cy="10" r="10" fill="#1E3A5F"/>
            <path d="M7 10L9.5 12.5L13.5 7.5" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
            <text x="32" y="14" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="14" font-weight="600">Digital Diagnostic Reports Sent to Your Email</text>
          </g>
        </g>
      </g>
    </g>'''

new_why_card = f'''    <!-- Right Side: Technician Quality Standards Box with Real Furnace Inspection Photography -->
    <g id="Technician-Standards-Card" transform="translate(860, 180)">
      <defs>
        <clipPath id="why-furnace-clip">
          <rect width="500" height="420" rx="16"/>
        </clipPath>
        <linearGradient id="why-photo-grad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#0F2238" stop-opacity="0.25"/>
          <stop offset="45%" stop-color="#0F2238" stop-opacity="0.82"/>
          <stop offset="100%" stop-color="#0F2238" stop-opacity="0.96"/>
        </linearGradient>
      </defs>
      
      <rect width="500" height="420" rx="16" fill="#0F2238"/>
      <!-- Realistic Commercial Technician Workmanship Photography -->
      <image href="data:image/jpeg;base64,{b64_furnace}" width="500" height="420" preserveAspectRatio="xMidYMid slice" clip-path="url(#why-furnace-clip)"/>
      <rect width="500" height="420" rx="16" fill="url(#why-photo-grad)" clip-path="url(#why-furnace-clip)"/>

      <g transform="translate(36, 175)">
        <rect width="130" height="26" rx="13" fill="#1E3A5F"/>
        <text x="65" y="17" fill="#38BDF8" font-family="'Inter', sans-serif" font-size="11" font-weight="700" text-anchor="middle">SERVICE STANDARDS</text>
        
        <text x="0" y="58" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="22" font-weight="800">
          Clean Workmanship &amp; Trade Integrity
        </text>

        <g transform="translate(0, 80)">
          <!-- Standard 1 -->
          <circle cx="10" cy="10" r="10" fill="#15803D"/>
          <path d="M7 10L9.5 12.5L13.5 7.5" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
          <text x="32" y="14" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Shoe Covers &amp; Protective Drop Cloths on Every Call</text>

          <!-- Standard 2 -->
          <g transform="translate(0, 34)">
            <circle cx="10" cy="10" r="10" fill="#15803D"/>
            <path d="M7 10L9.5 12.5L13.5 7.5" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
            <text x="32" y="14" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600">EPA-Certified Refrigerant &amp; Multimeter Diagnostics</text>
          </g>

          <!-- Standard 3 -->
          <g transform="translate(0, 68)">
            <circle cx="10" cy="10" r="10" fill="#15803D"/>
            <path d="M7 10L9.5 12.5L13.5 7.5" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
            <text x="32" y="14" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Post-Repair Airflow &amp; Static Pressure Verification</text>
          </g>

          <!-- Standard 4 -->
          <g transform="translate(0, 102)">
            <circle cx="10" cy="10" r="10" fill="#15803D"/>
            <path d="M7 10L9.5 12.5L13.5 7.5" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round"/>
            <text x="32" y="14" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Digital Diagnostic Health Reports Sent to Your Email</text>
          </g>
        </g>
      </g>
    </g>'''

if old_why_card in why_content:
    why_content = why_content.replace(old_why_card, new_why_card)
    with open(why_svg_path, 'w', encoding='utf-8') as f:
        f.write(why_content)
    print("Updated 07-why-choose-us.svg with furnace inspection photo!")
else:
    print("WARNING: old_why_card not found in 07-why-choose-us.svg")

