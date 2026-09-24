import os, sys, base64
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

img_dir = os.path.join(os.getcwd(), 'assets', 'images')

with open(os.path.join(img_dir, 'van_opt.jpg'), 'rb') as f:
    b64_van = base64.b64encode(f.read()).decode('ascii')

# 1. Update 03-about-page.svg
about_path = 'svgs/pages/03-about-page.svg'
with open(about_path, 'r', encoding='utf-8') as f:
    c_about = f.read()

# Fix line 117
old_craft = '''        <text x="24" y="126" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          EPA-certified and continually trained in the latest inverter, mini-split, and heat pump innovations.
        </text>'''

new_craft = '''        <text x="24" y="124" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="24" dy="0">EPA-certified and continually</tspan>
          <tspan x="24" dy="20">trained in inverter heat pumps,</tspan>
          <tspan x="24" dy="20">mini-splits, and safety codes.</tspan>
        </text>'''
c_about = c_about.replace(old_craft, new_craft)

# Replace mission card with photographic card
old_mission = '''      <!-- Right Column: Mission Card Box -->
      <g transform="translate(760, 0)">
        <rect width="520" height="250" rx="16" fill="#0F2238"/>
        <g transform="translate(40, 40)">
          <text x="0" y="18" fill="#38BDF8" font-family="'Inter', sans-serif" font-size="12" font-weight="700">OUR MISSION</text>
          <text x="0" y="54" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="22" font-weight="700">
            <tspan x="0" dy="0">"To deliver uncompromised indoor comfort</tspan>
            <tspan x="0" dy="30">through honest diagnostics, energy-efficient</tspan>
            <tspan x="0" dy="30">workmanship, and respectful customer care."</tspan>
          </text>
        </g>
      </g>'''

new_mission = f'''      <!-- Right Column: Mission Card Box with Fleet Photography -->
      <g transform="translate(760, 0)">
        <defs>
          <clipPath id="about-mission-clip">
            <rect width="520" height="270" rx="16"/>
          </clipPath>
          <linearGradient id="about-mission-grad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#0F2238" stop-opacity="0.3"/>
            <stop offset="55%" stop-color="#0F2238" stop-opacity="0.88"/>
            <stop offset="100%" stop-color="#0F2238" stop-opacity="0.98"/>
          </linearGradient>
        </defs>
        <rect width="520" height="270" rx="16" fill="#0F2238"/>
        <image href="data:image/jpeg;base64,{b64_van}" width="520" height="270" preserveAspectRatio="xMidYMid slice" clip-path="url(#about-mission-clip)"/>
        <rect width="520" height="270" rx="16" fill="url(#about-mission-grad)" clip-path="url(#about-mission-clip)"/>
        <g transform="translate(36, 120)">
          <text x="0" y="16" fill="#38BDF8" font-family="'Inter', sans-serif" font-size="11" font-weight="700" letter-spacing="1">OUR MISSION</text>
          <text x="0" y="46" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="18" font-weight="700">
            <tspan x="0" dy="0">"Uncompromised indoor comfort through</tspan>
            <tspan x="0" dy="24">honest diagnostics, high-efficiency equipment,</tspan>
            <tspan x="0" dy="24">and certified, respectful customer care."</tspan>
          </text>
        </g>
      </g>'''

if old_mission in c_about:
    c_about = c_about.replace(old_mission, new_mission)
    print("Updated 03-about-page.svg with mission fleet photo!")
else:
    print("WARNING: old_mission not found in 03-about-page.svg")

with open(about_path, 'w', encoding='utf-8') as f:
    f.write(c_about)

# 2. Update 04-service-areas-page.svg
areas_path = 'svgs/pages/04-service-areas-page.svg'
with open(areas_path, 'r', encoding='utf-8') as f:
    c_areas = f.read()

old_dispatch_banner = '''  <!-- Emergency Dispatch Notice -->
  <g transform="translate(80, 1160)">
    <rect width="1280" height="200" rx="16" fill="#0F2238"/>
    <g transform="translate(48, 48)">
      <rect width="160" height="26" rx="13" fill="#DC2626"/>
      <text x="80" y="17" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="11" font-weight="700" text-anchor="middle">24/7 RAPID DISPATCH</text>
      <text x="0" y="66" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="28" font-weight="800">Need Immediate Assistance in Any of These Areas?</text>
      <text x="0" y="96" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="15">Our emergency response team remains on standby round-the-clock with no extra overtime surcharges.</text>
      <g transform="translate(960, 25)">
        <rect width="210" height="48" rx="8" fill="#DC2626"/>
        <text x="105" y="29" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="14" font-weight="700" text-anchor="middle">Call (555) 014-7824</text>
      </g>
    </g>
  </g>'''

new_dispatch_banner = f'''  <!-- Emergency Dispatch Notice with Fleet Van Imagery -->
  <g transform="translate(80, 1160)">
    <defs>
      <clipPath id="areas-van-clip">
        <rect width="1280" height="220" rx="16"/>
      </clipPath>
      <linearGradient id="areas-van-grad" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0%" stop-color="#0F2238" stop-opacity="0.98"/>
        <stop offset="55%" stop-color="#0F2238" stop-opacity="0.88"/>
        <stop offset="100%" stop-color="#0F2238" stop-opacity="0.25"/>
      </linearGradient>
    </defs>
    <rect width="1280" height="220" rx="16" fill="#0F2238"/>
    <image href="data:image/jpeg;base64,{b64_van}" x="600" width="680" height="220" preserveAspectRatio="xMidYMid slice" clip-path="url(#areas-van-clip)"/>
    <rect width="1280" height="220" rx="16" fill="url(#areas-van-grad)" clip-path="url(#areas-van-clip)"/>
    <g transform="translate(48, 48)">
      <rect width="160" height="26" rx="13" fill="#DC2626"/>
      <text x="80" y="17" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="11" font-weight="700" text-anchor="middle">24/7 RAPID DISPATCH</text>
      <text x="0" y="66" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="28" font-weight="800">Need Immediate Assistance in Any of These Areas?</text>
      <text x="0" y="96" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="15">Our emergency response team remains on standby round-the-clock with no overtime surcharges.</text>
      <g transform="translate(0, 120)">
        <rect width="210" height="48" rx="8" fill="#DC2626"/>
        <text x="105" y="29" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="14" font-weight="700" text-anchor="middle">Call (555) 014-7824</text>
      </g>
    </g>
  </g>'''

if old_dispatch_banner in c_areas:
    c_areas = c_areas.replace(old_dispatch_banner, new_dispatch_banner)
    with open(areas_path, 'w', encoding='utf-8') as f:
        f.write(c_areas)
    print("Updated 04-service-areas-page.svg with van dispatch image!")
else:
    print("WARNING: old_dispatch_banner not found in 04-service-areas-page.svg")

# Test XML parsing
for p in [about_path, areas_path]:
    ET.parse(p)
    print(f"Validated XML: {p}")

