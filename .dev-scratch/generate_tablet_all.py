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
# 01-services-tablet-834.svg
# -------------------------------------------------------------
s01 = f'''{header}
  <g id="Hero" transform="translate(32, 140)">
    <text x="0" y="16" fill="#E65100" font-family="'Inter', sans-serif" font-size="12" font-weight="700" letter-spacing="1">FULL SERVICE DIRECTORY</text>
    <text x="0" y="52" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="34" font-weight="800">HVAC Services Built Around Your Comfort</text>
    <text x="0" y="86" fill="#475569" font-family="'Inter', sans-serif" font-size="15">
      <tspan x="0" dy="0">Certified technical expertise with upfront flat-rate pricing</tspan>
      <tspan x="0" dy="22">and zero surprise charges across all metro communities.</tspan>
    </text>
  </g>

  <!-- 5 Service Rows (770px wide) -->
  <g id="Service-Rows" transform="translate(32, 280)">
    <!-- 1. Cooling -->
    <g transform="translate(0, 0)">
      <rect width="770" height="230" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <g transform="translate(24, 24)">
        <rect width="44" height="44" rx="8" fill="#EFF6FF"/>
        <path d="M22 12V32M12 22H32M15 15L29 29M15 29L29 15" stroke="#2563EB" stroke-width="2" stroke-linecap="round"/>
        <text x="60" y="28" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="18" font-weight="800">Cooling &amp; Air Conditioning Services</text>
        <text x="60" y="48" fill="#64748B" font-family="'Inter', sans-serif" font-size="12">AC Repair &bull; System Replacements &bull; Ductless Mini-Splits</text>
        <text x="0" y="90" fill="#334155" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="0" dy="0">Beat intense summer heatwaves with precision cooling diagnostics.</tspan>
          <tspan x="0" dy="20">We repair frozen coils, failing compressors, and blown run capacitors.</tspan>
        </text>
        <g transform="translate(580, 120)">
          <rect width="140" height="40" rx="6" fill="#0F2238"/>
          <text x="70" y="25" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">View Cooling &rarr;</text>
        </g>
      </g>
    </g>

    <!-- 2. Heating -->
    <g transform="translate(0, 255)">
      <rect width="770" height="230" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <g transform="translate(24, 24)">
        <rect width="44" height="44" rx="8" fill="#FFF7ED"/>
        <path d="M22 12C22 12 16 17 16 23C16 26.3 18.7 29 22 29C25.3 29 28 26.3 28 23C28 17 22 12 22 12Z" stroke="#EA580C" stroke-width="2"/>
        <text x="60" y="28" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="18" font-weight="800">Heating &amp; Furnace Solutions</text>
        <text x="60" y="48" fill="#64748B" font-family="'Inter', sans-serif" font-size="12">Gas Furnaces &bull; Heat Pumps &bull; Heat Exchanger Safety</text>
        <text x="0" y="90" fill="#334155" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="0" dy="0">Reliable winter heating performance. We fix ignitor failures,</tspan>
          <tspan x="0" dy="20">failing blower motors, and thermocouple faults with digital testing.</tspan>
        </text>
        <g transform="translate(580, 120)">
          <rect width="140" height="40" rx="6" fill="#0F2238"/>
          <text x="70" y="25" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">View Heating &rarr;</text>
        </g>
      </g>
    </g>

    <!-- 3. Maintenance -->
    <g transform="translate(0, 510)">
      <rect width="770" height="230" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <g transform="translate(24, 24)">
        <rect width="44" height="44" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <path d="M25 15L29 19L19 29C18 30 17 30 16 29C15 28 15 27 16 26L25 15Z" stroke="#1E293B" stroke-width="2"/>
        <text x="60" y="28" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="18" font-weight="800">Preventive Maintenance &amp; Tune-Ups</text>
        <text x="60" y="48" fill="#64748B" font-family="'Inter', sans-serif" font-size="12">24-Point Comprehensive Check &bull; Filter Replacements &bull; Amp Testing</text>
        <text x="0" y="90" fill="#334155" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="0" dy="0">Prevent over 80% of unexpected breakdowns with seasonal tune-ups.</tspan>
          <tspan x="0" dy="20">We flush drains, calibrate thermostats, and protect warranties.</tspan>
        </text>
        <g transform="translate(580, 120)">
          <rect width="140" height="40" rx="6" fill="#0F2238"/>
          <text x="70" y="25" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">View Tune-Ups &rarr;</text>
        </g>
      </g>
    </g>

    <!-- 4. IAQ -->
    <g transform="translate(0, 765)">
      <rect width="770" height="230" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <g transform="translate(24, 24)">
        <rect width="44" height="44" rx="8" fill="#F0FDFA"/>
        <path d="M15 22H27C29 22 31 20 31 18C31 16 29 14 27 14C27 11 24 9 21 9C18 9 16 11 15 13C13 13 11 15 11 17C11 19 13 22 15 22Z" stroke="#0D9488" stroke-width="2"/>
        <text x="60" y="28" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="18" font-weight="800">Indoor Air Quality (IAQ)</text>
        <text x="60" y="48" fill="#64748B" font-family="'Inter', sans-serif" font-size="12">MERV-13 Filters &bull; Whole-Home Dehumidifiers &bull; UV Purifiers</text>
        <text x="0" y="90" fill="#334155" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="0" dy="0">Hospital-grade air filtration and germicidal UV-C coil lamps</tspan>
          <tspan x="0" dy="20">clearing airborne dust, allergens, mold, and humidity.</tspan>
        </text>
        <g transform="translate(580, 120)">
          <rect width="140" height="40" rx="6" fill="#0F2238"/>
          <text x="70" y="25" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="600" text-anchor="middle">View IAQ &rarr;</text>
        </g>
      </g>
    </g>

    <!-- 5. Emergency -->
    <g transform="translate(0, 1020)">
      <rect width="770" height="230" rx="12" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1"/>
      <g transform="translate(24, 24)">
        <rect width="44" height="44" rx="8" fill="#DC2626" fill-opacity="0.15"/>
        <circle cx="22" cy="22" r="10" stroke="#DC2626" stroke-width="2"/>
        <path d="M22 16V22M22 25V26" stroke="#DC2626" stroke-width="2" stroke-linecap="round"/>
        <text x="60" y="28" fill="#DC2626" font-family="'Plus Jakarta Sans', sans-serif" font-size="18" font-weight="800">24/7 Emergency HVAC Service</text>
        <text x="60" y="48" fill="#991B1B" font-family="'Inter', sans-serif" font-size="12">Rapid Priority Dispatch &bull; Under 45 Mins Average Arrival</text>
        <text x="0" y="90" fill="#7F1D1D" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="0" dy="0">Sudden no-heat emergencies or total AC breakdowns in heatwaves.</tspan>
          <tspan x="0" dy="20">Fully stocked service vans ready to fix issues on the spot.</tspan>
        </text>
        <g transform="translate(560, 120)">
          <rect width="160" height="40" rx="6" fill="#DC2626"/>
          <text x="80" y="25" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="13" font-weight="700" text-anchor="middle">Call Emergency &rarr;</text>
        </g>
      </g>
    </g>
  </g>

{th.tablet_footer(1620)}'''
with open(os.path.join(tablet_dir, '01-services-tablet-834.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap_svg(s01, 1960))
print("Created 01-services-tablet-834.svg")

# -------------------------------------------------------------
# 02-service-detail-tablet-834.svg
# -------------------------------------------------------------
s02 = f'''{header}
  <g id="Detail-Hero" transform="translate(32, 140)">
    <text x="0" y="14" fill="#64748B" font-family="'Inter', sans-serif" font-size="12">Services &gt; Cooling &gt; <tspan font-weight="700" fill="#0F2238">Air Conditioning Repair</tspan></text>
    <text x="0" y="54" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="34" font-weight="800">Air Conditioning Repair</text>
    <text x="0" y="88" fill="#475569" font-family="'Inter', sans-serif" font-size="15">
      <tspan x="0" dy="0">Fast diagnosis, upfront flat-rate pricing, and long-lasting cooling repairs</tspan>
      <tspan x="0" dy="22">by licensed HVAC specialists across your local neighborhood.</tspan>
    </text>
  </g>

  <!-- Symptoms Grid (2 cols x 3 rows) -->
  <g id="Symptoms" transform="translate(32, 280)">
    <text x="0" y="16" fill="#E65100" font-family="'Inter', sans-serif" font-size="12" font-weight="700" letter-spacing="1">COMMON WARNING SIGNS</text>
    <text x="0" y="48" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="800">Is Your AC Showing These Symptoms?</text>

    <g transform="translate(0, 75)">
      <!-- Sym 1 -->
      <g transform="translate(0, 0)">
        <rect width="370" height="130" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">AC Blowing Warm Air</text>
        <text x="20" y="60" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Low refrigerant from leak, failed</tspan>
          <tspan x="20" dy="20">compressor, or blown capacitor.</tspan>
        </text>
      </g>
      <!-- Sym 2 -->
      <g transform="translate(400, 0)">
        <rect width="370" height="130" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Grinding or Buzzing</text>
        <text x="20" y="60" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Worn blower motor bearings or</tspan>
          <tspan x="20" dy="20">failing electrical contactor coils.</tspan>
        </text>
      </g>
      <!-- Sym 3 -->
      <g transform="translate(0, 145)">
        <rect width="370" height="130" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Weak Airflow from Vents</text>
        <text x="20" y="60" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Clogged air filters, failing motor,</tspan>
          <tspan x="20" dy="20">or attic ductwork disconnection.</tspan>
        </text>
      </g>
      <!-- Sym 4 -->
      <g transform="translate(400, 145)">
        <rect width="370" height="130" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Short Cycling Rapidly</text>
        <text x="20" y="60" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Unit cycles on and off rapidly</tspan>
          <tspan x="20" dy="20">without cooling, spiking power.</tspan>
        </text>
      </g>
      <!-- Sym 5 (770px wide) -->
      <g transform="translate(0, 290)">
        <rect width="770" height="110" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Water Leaking Around Indoor Unit</text>
        <text x="20" y="60" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Clogged condensate drain lines or cracked drain pan overflowing into drywall,</tspan>
          <tspan x="20" dy="20">threatening ceiling water damage. Turn unit off and call immediately.</tspan>
        </text>
      </g>
    </g>
  </g>

  <!-- FAQ Accordion (770px) -->
  <g id="FAQ" transform="translate(32, 790)">
    <text x="0" y="16" fill="#E65100" font-family="'Inter', sans-serif" font-size="12" font-weight="700" letter-spacing="1">FREQUENTLY ASKED QUESTIONS</text>
    <text x="0" y="48" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="800">Air Conditioning Repair FAQ</text>

    <g transform="translate(0, 75)">
      <!-- Q1 Open -->
      <rect width="770" height="110" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/>
      <text x="20" y="34" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Should I repair my air conditioner or replace it entirely?</text>
      <text x="20" y="64" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="20" dy="0">If your AC is under 10 years old and repairs are under 50% of replacement, repairing is usually best.</tspan>
        <tspan x="20" dy="20">For units over 12-15 years using phased-out R-22 Freon, a new high-efficiency SEER2 unit saves more.</tspan>
      </text>

      <!-- Q2 Closed -->
      <g transform="translate(0, 125)">
        <rect width="770" height="54" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">How long does an emergency AC repair call take?</text>
      </g>
    </g>
  </g>

{th.tablet_footer(1100)}'''
with open(os.path.join(tablet_dir, '02-service-detail-tablet-834.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap_svg(s02, 1440))
print("Created 02-service-detail-tablet-834.svg")

# -------------------------------------------------------------
# 03-about-tablet-834.svg
# -------------------------------------------------------------
s03 = f'''{header}
  <g id="Hero" transform="translate(32, 140)">
    <text x="0" y="16" fill="#E65100" font-family="'Inter', sans-serif" font-size="12" font-weight="700" letter-spacing="1">ABOUT NORTHSTAR HVAC</text>
    <text x="0" y="52" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="34" font-weight="800">Local HVAC Professionals Focused on Doing the Job Right.</text>
    <text x="0" y="86" fill="#475569" font-family="'Inter', sans-serif" font-size="15">
      <tspan x="0" dy="0">Founded on craftsmanship, upfront flat-rate pricing, and respectful service,</tspan>
      <tspan x="0" dy="22">NorthStar keeps thousands of local homes and workplaces comfortable in every season.</tspan>
    </text>
  </g>

  <!-- Mission Card with Van Photo (770 x 300) -->
  <g transform="translate(32, 280)">
    <defs>
      <clipPath id="tab-about-van"><rect width="770" height="300" rx="12"/></clipPath>
      <linearGradient id="tab-about-grad" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#0F2238" stop-opacity="0.3"/>
        <stop offset="60%" stop-color="#0F2238" stop-opacity="0.85"/>
        <stop offset="100%" stop-color="#0F2238" stop-opacity="0.96"/>
      </linearGradient>
    </defs>
    <rect width="770" height="300" rx="12" fill="#0F2238"/>
    <image href="data:image/jpeg;base64,{b64_van}" width="770" height="300" preserveAspectRatio="xMidYMid slice" clip-path="url(#tab-about-van)"/>
    <rect width="770" height="300" rx="12" fill="url(#tab-about-grad)" clip-path="url(#tab-about-van)"/>

    <g transform="translate(32, 140)">
      <text x="0" y="20" fill="#38BDF8" font-family="'Inter', sans-serif" font-size="11" font-weight="700">OUR CORE COMMITMENT</text>
      <text x="0" y="52" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="20" font-weight="800">
        <tspan x="0" dy="0">"To deliver uncompromised indoor comfort through</tspan>
        <tspan x="0" dy="28">honest diagnostics and respectful, clean customer care."</tspan>
      </text>
    </g>
  </g>

  <!-- Core Values (2 cols x 2 rows) -->
  <g id="Values" transform="translate(32, 630)">
    <text x="0" y="16" fill="#E65100" font-family="'Inter', sans-serif" font-size="12" font-weight="700" letter-spacing="1">OUR VALUES</text>
    <text x="0" y="48" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="800">What Drives Every Service Call</text>

    <g transform="translate(0, 75)">
      <g transform="translate(0, 0)">
        <rect width="370" height="140" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">Absolute Integrity</text>
        <text x="20" y="60" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">We only recommend repairs or parts</tspan>
          <tspan x="20" dy="20">your home genuinely requires.</tspan>
          <tspan x="20" dy="20">Zero manufactured sales pressure.</tspan>
        </text>
      </g>

      <g transform="translate(400, 0)">
        <rect width="370" height="140" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">Technical Precision</text>
        <text x="20" y="60" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Manual J load calculations and digital</tspan>
          <tspan x="20" dy="20">manifold testing ensure every repair</tspan>
          <tspan x="20" dy="20">meets factory manufacturer specs.</tspan>
        </text>
      </g>

      <g transform="translate(0, 155)">
        <rect width="370" height="140" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">Respect for Your Home</text>
        <text x="20" y="60" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Clean uniforms, shoe boot covers, floor</tspan>
          <tspan x="20" dy="20">drop cloths, and complete job-site</tspan>
          <tspan x="20" dy="20">clean up on every service call.</tspan>
        </text>
      </g>

      <g transform="translate(400, 155)">
        <rect width="370" height="140" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">Always Ready Dispatch</text>
        <text x="20" y="60" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">24/7 on-call dispatch for sudden winter</tspan>
          <tspan x="20" dy="20">freeze warnings or summer heatwaves</tspan>
          <tspan x="20" dy="20">when climate is critical.</tspan>
        </text>
      </g>
    </g>
  </g>

{th.tablet_footer(1080)}'''
with open(os.path.join(tablet_dir, '03-about-tablet-834.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap_svg(s03, 1420))
print("Created 03-about-tablet-834.svg")

# -------------------------------------------------------------
# 04-service-areas-tablet-834.svg
# -------------------------------------------------------------
s04 = f'''{header}
  <g id="Hero" transform="translate(32, 140)">
    <text x="0" y="16" fill="#E65100" font-family="'Inter', sans-serif" font-size="12" font-weight="700" letter-spacing="1">LOCAL COVERAGE</text>
    <text x="0" y="52" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="34" font-weight="800">HVAC Service Across the Communities We Serve</text>
    <text x="0" y="86" fill="#475569" font-family="'Inter', sans-serif" font-size="15">
      <tspan x="0" dy="0">Our mobile service fleet guarantees under-45-minute average response times</tspan>
      <tspan x="0" dy="22">throughout the entire metropolitan area for routine and emergency calls.</tspan>
    </text>
  </g>

  <!-- 6 Service Zones (2 cols x 3 rows) -->
  <g id="Zones" transform="translate(32, 280)">
    <!-- Row 1 -->
    <g transform="translate(0, 0)">
      <rect width="370" height="150" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">Downtown District</text>
      <text x="20" y="50" fill="#15803D" font-family="'Inter', sans-serif" font-size="11" font-weight="600">&bull; Under 30 Min Arrival</text>
      <text x="20" y="78" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="20" dy="0">Condos, historic homes, and light</tspan>
        <tspan x="20" dy="20">commercial rooftop systems.</tspan>
      </text>
      <text x="20" y="130" fill="#0F2238" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Request Downtown Service &rarr;</text>
    </g>

    <g transform="translate(400, 0)">
      <rect width="370" height="150" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">Northside Suburbs</text>
      <text x="20" y="50" fill="#15803D" font-family="'Inter', sans-serif" font-size="11" font-weight="600">&bull; Under 35 Min Arrival</text>
      <text x="20" y="78" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="20" dy="0">Single-family AC replacements,</tspan>
        <tspan x="20" dy="20">heat pumps, and duct enhancements.</tspan>
      </text>
      <text x="20" y="130" fill="#0F2238" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Request Northside Service &rarr;</text>
    </g>

    <!-- Row 2 -->
    <g transform="translate(0, 165)">
      <rect width="370" height="150" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">Westfield District</text>
      <text x="20" y="50" fill="#15803D" font-family="'Inter', sans-serif" font-size="11" font-weight="600">&bull; Under 40 Min Arrival</text>
      <text x="20" y="78" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="20" dy="0">Gas furnace tune-ups, filter club</tspan>
        <tspan x="20" dy="20">deliveries, and smart thermostats.</tspan>
      </text>
      <text x="20" y="130" fill="#0F2238" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Request Westfield Service &rarr;</text>
    </g>

    <g transform="translate(400, 165)">
      <rect width="370" height="150" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">Brookhaven Hills</text>
      <text x="20" y="50" fill="#15803D" font-family="'Inter', sans-serif" font-size="11" font-weight="600">&bull; Under 40 Min Arrival</text>
      <text x="20" y="78" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="20" dy="0">Multi-zone mini-splits, whole-home</tspan>
        <tspan x="20" dy="20">dehumidifiers, and seasonal checks.</tspan>
      </text>
      <text x="20" y="130" fill="#0F2238" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Request Brookhaven Service &rarr;</text>
    </g>

    <!-- Row 3 -->
    <g transform="translate(0, 330)">
      <rect width="370" height="150" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">Riverside Corridor</text>
      <text x="20" y="50" fill="#15803D" font-family="'Inter', sans-serif" font-size="11" font-weight="600">&bull; Under 35 Min Arrival</text>
      <text x="20" y="78" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="20" dy="0">Condensing units, line set repair,</tspan>
        <tspan x="20" dy="20">and light commercial rooftop service.</tspan>
      </text>
      <text x="20" y="130" fill="#0F2238" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Request Riverside Service &rarr;</text>
    </g>

    <g transform="translate(400, 330)">
      <rect width="370" height="150" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">Eastwood Township</text>
      <text x="20" y="50" fill="#15803D" font-family="'Inter', sans-serif" font-size="11" font-weight="600">&bull; Under 45 Min Arrival</text>
      <text x="20" y="78" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="20" dy="0">Emergency furnace ignitor fixes,</tspan>
        <tspan x="20" dy="20">boiler tune-ups, and filtration.</tspan>
      </text>
      <text x="20" y="130" fill="#0F2238" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Request Eastwood Service &rarr;</text>
    </g>
  </g>

{th.tablet_footer(840)}'''
with open(os.path.join(tablet_dir, '04-service-areas-tablet-834.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap_svg(s04, 1180))
print("Created 04-service-areas-tablet-834.svg")

# -------------------------------------------------------------
# 05-financing-tablet-834.svg
# -------------------------------------------------------------
s05 = f'''{header}
  <g id="Hero" transform="translate(32, 140)">
    <text x="0" y="16" fill="#E65100" font-family="'Inter', sans-serif" font-size="12" font-weight="700" letter-spacing="1">PAYMENT OPTIONS</text>
    <text x="0" y="52" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="34" font-weight="800">Comfort Now. Flexible Payment Options.</text>
    <text x="0" y="86" fill="#475569" font-family="'Inter', sans-serif" font-size="15">
      <tspan x="0" dy="0">A broken air conditioner or furnace should never compromise your family's comfort.</tspan>
      <tspan x="0" dy="22">Explore monthly financing plans tailored for qualifying installations and repairs.</tspan>
    </text>
  </g>

  <!-- 3 Steps -->
  <g id="Steps" transform="translate(32, 280)">
    <text x="0" y="16" fill="#E65100" font-family="'Inter', sans-serif" font-size="12" font-weight="700" letter-spacing="1">HOW IT WORKS</text>
    <text x="0" y="48" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="800">Three Simple Steps to Financing</text>

    <g transform="translate(0, 75)">
      <rect width="770" height="90" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="40" cy="45" r="18" fill="#0F2238"/>
      <text x="40" y="51" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="800" text-anchor="middle">1</text>
      <text x="75" y="38" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Check Pre-Qualification Online</text>
      <text x="75" y="58" fill="#475569" font-family="'Inter', sans-serif" font-size="13">Soft credit check with no impact on your credit score. Takes under 2 minutes.</text>
    </g>

    <g transform="translate(0, 180)">
      <rect width="770" height="90" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="40" cy="45" r="18" fill="#0F2238"/>
      <text x="40" y="51" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="800" text-anchor="middle">2</text>
      <text x="75" y="38" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Select Monthly Payment Plan</text>
      <text x="75" y="58" fill="#475569" font-family="'Inter', sans-serif" font-size="13">Choose the loan term and monthly budget that fits your household finances best.</text>
    </g>

    <g transform="translate(0, 285)">
      <rect width="770" height="90" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="40" cy="45" r="18" fill="#0F2238"/>
      <text x="40" y="51" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="800" text-anchor="middle">3</text>
      <text x="75" y="38" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Complete HVAC Installation</text>
      <text x="75" y="58" fill="#475569" font-family="'Inter', sans-serif" font-size="13">Certified NorthStar installation proceeds immediately upon partner lender approval.</text>
    </g>
  </g>

{th.tablet_footer(720)}'''
with open(os.path.join(tablet_dir, '05-financing-tablet-834.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap_svg(s05, 1060))
print("Created 05-financing-tablet-834.svg")

# -------------------------------------------------------------
# 06-reviews-tablet-834.svg
# -------------------------------------------------------------
s06 = f'''{header}
  <g id="Hero" transform="translate(32, 140)">
    <text x="0" y="16" fill="#E65100" font-family="'Inter', sans-serif" font-size="12" font-weight="700" letter-spacing="1">CUSTOMER FEEDBACK</text>
    <text x="0" y="52" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="34" font-weight="800">Hear From Our Customers</text>
    <text x="0" y="86" fill="#475569" font-family="'Inter', sans-serif" font-size="15">Verified reviews from local homeowners who trust NorthStar for season-long climate comfort.</text>
  </g>

  <!-- 4 Reviews (2 cols x 2 rows) -->
  <g id="Reviews" transform="translate(32, 270)">
    <g transform="translate(0, 0)">
      <rect width="370" height="200" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="20" y="30" fill="#F59E0B">&starf;&starf;&starf;&starf;&starf;</text>
      <text x="20" y="60" fill="#1E293B" font-family="'Inter', sans-serif" font-size="13" font-style="italic">
        <tspan x="20" dy="0">"The technician arrived on time,</tspan>
        <tspan x="20" dy="20">diagnosed the faulty capacitor in</tspan>
        <tspan x="20" dy="20">20 minutes, and had our AC running</tspan>
        <tspan x="20" dy="20">before afternoon heat peaked."</tspan>
      </text>
      <text x="20" y="165" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Sarah M. &bull; <tspan font-weight="400" fill="#64748B">Northside</tspan></text>
    </g>

    <g transform="translate(400, 0)">
      <rect width="370" height="200" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="20" y="30" fill="#F59E0B">&starf;&starf;&starf;&starf;&starf;</text>
      <text x="20" y="60" fill="#1E293B" font-family="'Inter', sans-serif" font-size="13" font-style="italic">
        <tspan x="20" dy="0">"Our furnace stopped igniting on a</tspan>
        <tspan x="20" dy="20">freezing Sunday morning. Tech arrived</tspan>
        <tspan x="20" dy="20">in 35 minutes and replaced the hot</tspan>
        <tspan x="20" dy="20">surface ignitor from their truck."</tspan>
      </text>
      <text x="20" y="165" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">David R. &bull; <tspan font-weight="400" fill="#64748B">Westfield</tspan></text>
    </g>

    <g transform="translate(0, 220)">
      <rect width="370" height="200" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="20" y="30" fill="#F59E0B">&starf;&starf;&starf;&starf;&starf;</text>
      <text x="20" y="60" fill="#1E293B" font-family="'Inter', sans-serif" font-size="13" font-style="italic">
        <tspan x="20" dy="0">"Installed a 20 SEER heat pump.</tspan>
        <tspan x="20" dy="20">The crew was polite, wore shoe</tspan>
        <tspan x="20" dy="20">covers, and left the basement clean.</tspan>
        <tspan x="20" dy="20">Monthly power bills dropped 25%."</tspan>
      </text>
      <text x="20" y="165" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Elena T. &bull; <tspan font-weight="400" fill="#64748B">Brookhaven</tspan></text>
    </g>

    <g transform="translate(400, 220)">
      <rect width="370" height="200" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="20" y="30" fill="#F59E0B">&starf;&starf;&starf;&starf;&starf;</text>
      <text x="20" y="60" fill="#1E293B" font-family="'Inter', sans-serif" font-size="13" font-style="italic">
        <tspan x="20" dy="0">"Annual maintenance caught a bad</tspan>
        <tspan x="20" dy="20">blower bearing before it seized.</tspan>
        <tspan x="20" dy="20">Saved us hundreds in repairs.</tspan>
        <tspan x="20" dy="20">Very professional technicians."</tspan>
      </text>
      <text x="20" y="165" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Marcus K. &bull; <tspan font-weight="400" fill="#64748B">Riverside</tspan></text>
    </g>
  </g>

{th.tablet_footer(770)}'''
with open(os.path.join(tablet_dir, '06-reviews-tablet-834.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap_svg(s06, 1110))
print("Created 06-reviews-tablet-834.svg")

# -------------------------------------------------------------
# 07-contact-tablet-834.svg
# -------------------------------------------------------------
s07 = f'''{header}
  <g id="Hero" transform="translate(32, 140)">
    <text x="0" y="16" fill="#E65100" font-family="'Inter', sans-serif" font-size="12" font-weight="700" letter-spacing="1">GET IN TOUCH</text>
    <text x="0" y="52" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="34" font-weight="800">Contact NorthStar HVAC Services</text>
    <text x="0" y="86" fill="#475569" font-family="'Inter', sans-serif" font-size="15">Have an HVAC question, need maintenance, or require urgent dispatch? We are here 24 hours a day.</text>
  </g>

  <!-- Contact Form & Info (770px wide) -->
  <g id="Form" transform="translate(32, 270)">
    <rect width="770" height="520" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <g transform="translate(32, 32)">
      <text x="0" y="20" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="20" font-weight="800">Send an Online Service Request</text>

      <!-- Row 1: Name & Phone -->
      <g transform="translate(0, 50)">
        <text x="0" y="14" fill="#334155" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Full Name *</text>
        <rect y="22" width="340" height="42" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
        <text x="12" y="48" fill="#0F172A" font-family="'Inter', sans-serif" font-size="13">Sarah Miller</text>

        <g transform="translate(365, 0)">
          <text x="0" y="14" fill="#334155" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Phone Number *</text>
          <rect y="22" width="340" height="42" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
          <text x="12" y="48" fill="#0F172A" font-family="'Inter', sans-serif" font-size="13">(555) 789-0123</text>
        </g>
      </g>

      <!-- Row 2: Email & Service -->
      <g transform="translate(0, 135)">
        <text x="0" y="14" fill="#334155" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Email Address *</text>
        <rect y="22" width="340" height="42" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
        <text x="12" y="48" fill="#0F172A" font-family="'Inter', sans-serif" font-size="13">sarah.miller@example.com</text>

        <g transform="translate(365, 0)">
          <text x="0" y="14" fill="#334155" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Service Needed *</text>
          <rect y="22" width="340" height="42" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
          <text x="12" y="48" fill="#0F172A" font-family="'Inter', sans-serif" font-size="13">AC Repair &amp; Diagnostics</text>
        </g>
      </g>

      <!-- Message -->
      <g transform="translate(0, 220)">
        <text x="0" y="14" fill="#334155" font-family="'Inter', sans-serif" font-size="13" font-weight="600">Message / System Symptoms</text>
        <rect y="22" width="705" height="80" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
        <text x="12" y="46" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="12" dy="0">AC outdoor condenser fan running, but indoor vents</tspan>
          <tspan x="12" dy="20">are only blowing room-temperature air.</tspan>
        </text>
      </g>

      <g transform="translate(0, 360)">
        <rect width="200" height="46" rx="6" fill="#E65100"/>
        <text x="100" y="28" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="14" font-weight="700" text-anchor="middle">Send Request &rarr;</text>
      </g>
    </g>
  </g>

{th.tablet_footer(840)}'''
with open(os.path.join(tablet_dir, '07-contact-tablet-834.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap_svg(s07, 1180))
print("Created 07-contact-tablet-834.svg")

# -------------------------------------------------------------
# 08-book-a-service-tablet-834.svg
# -------------------------------------------------------------
s08 = f'''{header}
  <g id="Hero" transform="translate(32, 140)">
    <text x="0" y="16" fill="#E65100" font-family="'Inter', sans-serif" font-size="12" font-weight="700" letter-spacing="1">ONLINE BOOKING WIZARD</text>
    <text x="0" y="52" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="34" font-weight="800">Book an HVAC Service Appointment</text>
  </g>

  <!-- Step 1: Service Selection (2 cols x 3 rows) -->
  <g id="Step-1" transform="translate(32, 250)">
    <rect width="770" height="430" rx="12" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <g transform="translate(32, 28)">
      <text x="0" y="18" fill="#E65100" font-family="'Inter', sans-serif" font-size="12" font-weight="700">STEP 1 OF 4</text>
      <text x="0" y="48" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="20" font-weight="800">Choose Your Service Type</text>

      <g transform="translate(0, 70)">
        <!-- Opt 1 (Selected) -->
        <g transform="translate(0, 0)">
          <rect width="340" height="90" rx="8" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5"/>
          <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">AC Repair</text>
          <text x="20" y="52" fill="#475569" font-family="'Inter', sans-serif" font-size="12">Warm air, strange noises, leaks.</text>
          <text x="20" y="72" fill="#2563EB" font-family="'Inter', sans-serif" font-size="11" font-weight="700">&check; SELECTED</text>
        </g>

        <!-- Opt 2 -->
        <g transform="translate(365, 0)">
          <rect width="340" height="90" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
          <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">AC Installation</text>
          <text x="20" y="52" fill="#475569" font-family="'Inter', sans-serif" font-size="12">High-efficiency SEER2 replacements.</text>
        </g>

        <!-- Opt 3 -->
        <g transform="translate(0, 105)">
          <rect width="340" height="90" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
          <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Heating Repair</text>
          <text x="20" y="52" fill="#475569" font-family="'Inter', sans-serif" font-size="12">Furnaces, boilers, and heat pumps.</text>
        </g>

        <!-- Opt 4 -->
        <g transform="translate(365, 105)">
          <rect width="340" height="90" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
          <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Preventive Maintenance</text>
          <text x="20" y="52" fill="#475569" font-family="'Inter', sans-serif" font-size="12">24-point seasonal safety tune-up.</text>
        </g>

        <!-- Opt 5 -->
        <g transform="translate(0, 210)">
          <rect width="340" height="90" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
          <text x="20" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Indoor Air Quality</text>
          <text x="20" y="52" fill="#475569" font-family="'Inter', sans-serif" font-size="12">MERV-13 filters and UV coil lamps.</text>
        </g>

        <!-- Opt 6 -->
        <g transform="translate(365, 210)">
          <rect width="340" height="90" rx="8" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1"/>
          <text x="20" y="32" fill="#DC2626" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Emergency 24/7 HVAC</text>
          <text x="20" y="52" fill="#991B1B" font-family="'Inter', sans-serif" font-size="12">Urgent freeze or extreme heat call.</text>
        </g>
      </g>
    </g>
  </g>

{th.tablet_footer(730)}'''
with open(os.path.join(tablet_dir, '08-book-a-service-tablet-834.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap_svg(s08, 1070))
print("Created 08-book-a-service-tablet-834.svg")

# -------------------------------------------------------------
# 09-emergency-hvac-tablet-834.svg
# -------------------------------------------------------------
s09 = f'''{header}
  <g id="Hero" transform="translate(32, 140)">
    <rect width="210" height="26" rx="13" fill="#DC2626"/>
    <text x="105" y="17" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="11" font-weight="700" text-anchor="middle">&bull; PRIORITY RADIO DISPATCH</text>
    <text x="0" y="64" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="34" font-weight="800">24/7 Emergency HVAC Service</text>
    <text x="0" y="98" fill="#475569" font-family="'Inter', sans-serif" font-size="15">
      <tspan x="0" dy="0">No heat in freezing weather? Sudden AC breakdown during extreme heat?</tspan>
      <tspan x="0" dy="22">Our mobile emergency service vans arrive in under 45 minutes.</tspan>
    </text>

    <!-- Large Call Button -->
    <g transform="translate(0, 160)">
      <rect width="280" height="54" rx="8" fill="#DC2626"/>
      <text x="140" y="33" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="800" text-anchor="middle">Call (555) 014-7824 Now</text>
    </g>
  </g>

  <!-- 4 Emergency Situations (2 cols x 2 rows) -->
  <g id="Situations" transform="translate(32, 410)">
    <text x="0" y="16" fill="#DC2626" font-family="'Inter', sans-serif" font-size="12" font-weight="700" letter-spacing="1">WHEN TO CALL US IMMEDIATELY</text>
    <text x="0" y="48" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="800">Common HVAC Emergency Situations</text>

    <g transform="translate(0, 75)">
      <!-- Sit 1 -->
      <g transform="translate(0, 0)">
        <rect width="370" height="150" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="34" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">Complete Heat Outage</text>
        <text x="20" y="62" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Furnace fails to ignite during</tspan>
          <tspan x="20" dy="20">freezing outdoor weather,</tspan>
          <tspan x="20" dy="20">risking frozen plumbing pipes.</tspan>
        </text>
      </g>

      <!-- Sit 2 -->
      <g transform="translate(400, 0)">
        <rect width="370" height="150" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="34" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">AC Failure in Heatwave</text>
        <text x="20" y="62" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Cooling quits with indoor</tspan>
          <tspan x="20" dy="20">temperatures above 85&deg;F,</tspan>
          <tspan x="20" dy="20">endangering family health.</tspan>
        </text>
      </g>

      <!-- Sit 3 -->
      <g transform="translate(0, 165)">
        <rect width="370" height="150" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="34" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">Electrical Burning Smell</text>
        <text x="20" y="62" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Acrid smoke odor from the</tspan>
          <tspan x="20" dy="20">blower motor or wiring indicates</tspan>
          <tspan x="20" dy="20">an immediate fire hazard.</tspan>
        </text>
      </g>

      <!-- Sit 4 -->
      <g transform="translate(400, 165)">
        <rect width="370" height="150" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
        <text x="20" y="34" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">Major Water Flooding</text>
        <text x="20" y="62" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Clogged drain lines or cracked</tspan>
          <tspan x="20" dy="20">pan overflowing into drywall,</tspan>
          <tspan x="20" dy="20">threatening ceiling collapse.</tspan>
        </text>
      </g>
    </g>
  </g>

{th.tablet_footer(800)}'''
with open(os.path.join(tablet_dir, '09-emergency-hvac-tablet-834.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap_svg(s09, 1140))
print("Created 09-emergency-hvac-tablet-834.svg")

