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

import importlib.util
spec = importlib.util.spec_from_file_location("tablet_helpers", "scratch/tablet_helpers.py")
th = importlib.util.module_from_spec(spec)
spec.loader.exec_module(th)

header = th.tablet_header()

def wrap_svg(content, height):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 834 {height}" width="834" height="{height}">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap');
    </style>
  </defs>
  <rect width="834" height="{height}" fill="#FFFFFF"/>
{content}
</svg>'''

# -------------------------------------------------------------
# 00-home-tablet-834.svg
# -------------------------------------------------------------
h00 = f'''{header}
  <!-- Hero Section -->
  <g id="Hero" transform="translate(32, 140)">
    <rect width="180" height="26" rx="13" fill="#EFF6FF"/>
    <text x="90" y="17" fill="#2563EB" font-family="'Inter', sans-serif" font-size="11" font-weight="700" text-anchor="middle">&bull; METRO SERVICE REGION</text>
    
    <text x="0" y="64" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="36" font-weight="800">
      <tspan x="0" dy="0">Reliable HVAC Service</tspan>
      <tspan x="0" dy="44">When You Need It Most.</tspan>
    </text>

    <text x="0" y="156" fill="#475569" font-family="'Inter', sans-serif" font-size="15">
      <tspan x="0" dy="0">From emergency heating repairs to high-efficiency AC installations,</tspan>
      <tspan x="0" dy="24">NorthStar keeps your home comfortable year-round with clear,</tspan>
      <tspan x="0" dy="24">upfront flat-rate pricing and certified local technicians.</tspan>
    </text>

    <g transform="translate(0, 240)">
      <rect width="170" height="48" rx="6" fill="#E65100"/>
      <text x="85" y="29" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="14" font-weight="700" text-anchor="middle">Book a Service</text>

      <g transform="translate(185, 0)">
        <rect width="190" height="48" rx="6" fill="#FFFFFF" stroke="#0F2238" stroke-width="2"/>
        <text x="95" y="29" fill="#0F2238" font-family="'Inter', sans-serif" font-size="14" font-weight="700" text-anchor="middle">Call (555) 014-7824</text>
      </g>
    </g>

    <!-- Hero Image (770 x 420) -->
    <g transform="translate(0, 310)">
      <defs>
        <clipPath id="tab-hero-clip"><rect width="770" height="400" rx="12"/></clipPath>
      </defs>
      <rect width="770" height="400" rx="12" fill="#0F2238"/>
      <image href="data:image/jpeg;base64,{b64_hero}" width="770" height="400" preserveAspectRatio="xMidYMid slice" clip-path="url(#tab-hero-clip)"/>
      <rect width="770" height="400" rx="12" fill="#0F2238" fill-opacity="0.15" clip-path="url(#tab-hero-clip)"/>

      <!-- Floating Badge -->
      <g transform="translate(20, 310)">
        <rect width="250" height="70" rx="8" fill="#FFFFFF"/>
        <circle cx="24" cy="35" r="16" fill="#ECFDF5"/>
        <path d="M19 35L22 38L29 31" stroke="#059669" stroke-width="2" stroke-linecap="round"/>
        <text x="48" y="30" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="700">Technicians On Call</text>
        <text x="48" y="48" fill="#15803D" font-family="'Inter', sans-serif" font-size="11" font-weight="600">Arrival Under 45 Mins</text>
      </g>
    </g>
  </g>

  <!-- Trust Bar (2x2 on Tablet) -->
  <g id="Trust" transform="translate(32, 900)">
    <g transform="translate(0, 0)">
      <rect width="370" height="70" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Licensed &amp; Insured</text>
      <text x="20" y="50" fill="#15803D" font-family="'Inter', sans-serif" font-size="11" font-weight="600">&bull; State Certified Contractor</text>
    </g>
    <g transform="translate(400, 0)">
      <rect width="370" height="70" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">24/7 Emergency Service</text>
      <text x="20" y="50" fill="#DC2626" font-family="'Inter', sans-serif" font-size="11" font-weight="600">&bull; Priority On-Call Dispatch</text>
    </g>
    <g transform="translate(0, 85)">
      <rect width="370" height="70" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">10+ Years Experience</text>
      <text x="20" y="50" fill="#64748B" font-family="'Inter', sans-serif" font-size="11">&bull; Certified Master Technicians</text>
    </g>
    <g transform="translate(400, 85)">
      <rect width="370" height="70" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">100% Satisfaction Focused</text>
      <text x="20" y="50" fill="#15803D" font-family="'Inter', sans-serif" font-size="11" font-weight="600">&bull; Fixed Right or Money Back</text>
    </g>
  </g>

  <!-- Services Grid (2 cols x 3 rows) -->
  <g id="Services" transform="translate(32, 1100)">
    <text x="0" y="16" fill="#E65100" font-family="'Inter', sans-serif" font-size="12" font-weight="700" letter-spacing="1">HVAC SERVICES</text>
    <text x="0" y="48" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="28" font-weight="800">HVAC for Every Season</text>

    <!-- Row 1 -->
    <g transform="translate(0, 80)">
      <rect width="370" height="190" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="20" y="40" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="17" font-weight="700">AC Repair</text>
      <text x="20" y="74" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="20" dy="0">Fast diagnostics for warm air,</tspan>
        <tspan x="20" dy="20">strange noises, and coil leaks.</tspan>
      </text>
      <text x="20" y="150" fill="#0F2238" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Learn More &rarr;</text>

      <g transform="translate(400, 0)">
        <rect width="370" height="190" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="40" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="17" font-weight="700">AC Installation</text>
        <text x="20" y="74" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">High-efficiency systems sized for</tspan>
          <tspan x="20" dy="20">lower utility bills and comfort.</tspan>
        </text>
        <text x="20" y="150" fill="#0F2238" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Learn More &rarr;</text>
      </g>
    </g>

    <!-- Row 2 -->
    <g transform="translate(0, 290)">
      <rect width="370" height="190" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="20" y="40" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="17" font-weight="700">Heating Repair</text>
      <text x="20" y="74" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="20" dy="0">Gas furnace ignition fixes and</tspan>
        <tspan x="20" dy="20">cold-climate heat pump service.</tspan>
      </text>
      <text x="20" y="150" fill="#0F2238" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Learn More &rarr;</text>

      <g transform="translate(400, 0)">
        <rect width="370" height="190" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="40" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="17" font-weight="700">Preventive Maintenance</text>
        <text x="20" y="74" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Seasonal 24-point tune-ups keeping</tspan>
          <tspan x="20" dy="20">power bills low and systems safe.</tspan>
        </text>
        <text x="20" y="150" fill="#0F2238" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Learn More &rarr;</text>
      </g>
    </g>

    <!-- Row 3 -->
    <g transform="translate(0, 500)">
      <rect width="370" height="190" rx="10" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="20" y="40" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="17" font-weight="700">Indoor Air Quality</text>
      <text x="20" y="74" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="20" dy="0">MERV-13 filters, dehumidifiers,</tspan>
        <tspan x="20" dy="20">and UV air purification units.</tspan>
      </text>
      <text x="20" y="150" fill="#0F2238" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Learn More &rarr;</text>

      <g transform="translate(400, 0)">
        <rect width="370" height="190" rx="10" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1"/>
        <text x="20" y="40" fill="#DC2626" font-family="'Plus Jakarta Sans', sans-serif" font-size="17" font-weight="700">24/7 Emergency HVAC</text>
        <text x="20" y="74" fill="#991B1B" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Urgent heat outages in winter or</tspan>
          <tspan x="20" dy="20">AC breakdowns in extreme heat.</tspan>
        </text>
        <text x="20" y="150" fill="#DC2626" font-family="'Inter', sans-serif" font-size="13" font-weight="700">Call Emergency Line &rarr;</text>
      </g>
    </g>
  </g>

  <!-- Emergency Banner (770px) -->
  <g id="Emergency-Banner" transform="translate(32, 1850)">
    <rect width="770" height="160" rx="12" fill="#0F2238"/>
    <rect width="6" height="160" rx="3" fill="#DC2626"/>
    <g transform="translate(32, 28)">
      <rect width="140" height="22" rx="11" fill="#DC2626" fill-opacity="0.2"/>
      <text x="70" y="15" fill="#F87171" font-family="'Inter', sans-serif" font-size="10" font-weight="700" text-anchor="middle">RAPID DISPATCH</text>
      <text x="0" y="52" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="20" font-weight="800">Your HVAC Problem Can&apos;t Always Wait.</text>
      <text x="0" y="76" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">24/7 emergency service team ready across metro communities.</text>
      <g transform="translate(540, 24)">
        <rect width="160" height="42" rx="6" fill="#DC2626"/>
        <text x="80" y="26" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="700" text-anchor="middle">Call Emergency</text>
      </g>
    </g>
  </g>

  <!-- Why Choose Us with Furnace Photo -->
  <g id="Why-Choose-Us" transform="translate(32, 2060)">
    <text x="0" y="16" fill="#E65100" font-family="'Inter', sans-serif" font-size="12" font-weight="700" letter-spacing="1">THE NORTHSTAR DIFFERENCE</text>
    <text x="0" y="48" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="28" font-weight="800">Professional Service. Straightforward Solutions.</text>

    <!-- Workmanship Photo Card (770 x 340) -->
    <g transform="translate(0, 75)">
      <defs>
        <clipPath id="tab-why-clip"><rect width="770" height="340" rx="12"/></clipPath>
        <linearGradient id="tab-why-grad" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0%" stop-color="#0F2238" stop-opacity="0.2"/>
          <stop offset="60%" stop-color="#0F2238" stop-opacity="0.85"/>
          <stop offset="100%" stop-color="#0F2238" stop-opacity="0.98"/>
        </linearGradient>
      </defs>
      <rect width="770" height="340" rx="12" fill="#0F2238"/>
      <image href="data:image/jpeg;base64,{b64_furnace}" width="770" height="340" preserveAspectRatio="xMidYMid slice" clip-path="url(#tab-why-clip)"/>
      <rect width="770" height="340" rx="12" fill="url(#tab-why-grad)" clip-path="url(#tab-why-clip)"/>

      <g transform="translate(32, 160)">
        <text x="0" y="24" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="20" font-weight="800">Clean Workmanship &amp; Trade Integrity</text>
        <g transform="translate(0, 45)">
          <circle cx="8" cy="8" r="8" fill="#15803D"/>
          <path d="M5 8L7 10L11 6" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round"/>
          <text x="24" y="12" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Shoe Covers &amp; Protective Drop Cloths on Every Call</text>

          <g transform="translate(0, 26)">
            <circle cx="8" cy="8" r="8" fill="#15803D"/>
            <path d="M5 8L7 10L11 6" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round"/>
            <text x="24" y="12" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="600">EPA-Certified Refrigerant &amp; Multimeter Diagnostics</text>
          </g>

          <g transform="translate(0, 52)">
            <circle cx="8" cy="8" r="8" fill="#15803D"/>
            <path d="M5 8L7 10L11 6" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round"/>
            <text x="24" y="12" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Digital Diagnostic Health Reports Sent to Your Email</text>
          </g>
        </g>
      </g>
    </g>

    <!-- 4 Benefits Grid -->
    <g transform="translate(0, 445)">
      <g transform="translate(0, 0)">
        <rect width="370" height="130" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Experienced Technicians</text>
        <text x="20" y="60" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Certified pros focused on accurate</tspan>
          <tspan x="20" dy="20">diagnosis and durable repairs.</tspan>
        </text>
      </g>
      <g transform="translate(400, 0)">
        <rect width="370" height="130" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Clear Recommendations</text>
        <text x="20" y="60" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Understand repair vs. replacement</tspan>
          <tspan x="20" dy="20">options before making decisions.</tspan>
        </text>
      </g>
      <g transform="translate(0, 145)">
        <rect width="370" height="130" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Upfront Communication</text>
        <text x="20" y="60" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Upfront flat-rate pricing with</tspan>
          <tspan x="20" dy="20">zero hidden surprises or fees.</tspan>
        </text>
      </g>
      <g transform="translate(400, 145)">
        <rect width="370" height="130" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Long-Term Comfort</text>
        <text x="20" y="60" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">High-efficiency systems sized for</tspan>
          <tspan x="20" dy="20">lower utility bills and comfort.</tspan>
        </text>
      </g>
    </g>
  </g>

  <!-- Service Areas with Van Photo -->
  <g id="Service-Areas" transform="translate(32, 2830)">
    <text x="0" y="16" fill="#E65100" font-family="'Inter', sans-serif" font-size="12" font-weight="700" letter-spacing="1">REGIONAL COVERAGE</text>
    <text x="0" y="48" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="28" font-weight="800">Proudly Serving Our Local Community</text>

    <!-- Van Card -->
    <g transform="translate(0, 75)">
      <defs>
        <clipPath id="tab-van-clip"><rect width="770" height="300" rx="12"/></clipPath>
      </defs>
      <rect width="770" height="300" rx="12" fill="#0F2238"/>
      <image href="data:image/jpeg;base64,{b64_van}" width="770" height="300" preserveAspectRatio="xMidYMid slice" clip-path="url(#tab-van-clip)"/>
      
      <!-- Van overlay -->
      <g transform="translate(20, 220)">
        <rect width="730" height="60" rx="8" fill="#0F2238" fill-opacity="0.9" stroke="#38BDF8" stroke-width="1"/>
        <text x="20" y="26" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Mobile Diagnostic Fleet</text>
        <text x="20" y="46" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="12">Stationed across Downtown, Northside, Westfield, Brookhaven, Riverside, Eastwood.</text>
      </g>
    </g>
  </g>

{th.tablet_footer(3270)}'''

with open(os.path.join(tablet_dir, '00-home-tablet-834.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap_svg(h00, 3610))

print("Created 00-home-tablet-834.svg")

