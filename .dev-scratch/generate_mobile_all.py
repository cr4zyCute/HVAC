import os, sys, base64

sys.stdout.reconfigure(encoding='utf-8')

img_dir = os.path.join(os.getcwd(), 'assets', 'images')
with open(os.path.join(img_dir, 'hero_opt.jpg'), 'rb') as f:
    b64_hero = base64.b64encode(f.read()).decode('ascii')
with open(os.path.join(img_dir, 'furnace_opt.jpg'), 'rb') as f:
    b64_furnace = base64.b64encode(f.read()).decode('ascii')
with open(os.path.join(img_dir, 'van_opt.jpg'), 'rb') as f:
    b64_van = base64.b64encode(f.read()).decode('ascii')

mobile_dir = os.path.join(os.getcwd(), 'svgs', 'responsive', 'mobile')

import importlib.util
spec = importlib.util.spec_from_file_location("mobile_helpers", "scratch/mobile_helpers.py")
mh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mh)

header = mh.mobile_header()
wrap = mh.wrap_mobile_svg

# -------------------------------------------------------------
# 00-home-mobile-390.svg
# -------------------------------------------------------------
m00 = f'''{header}
  <!-- Hero Section -->
  <g id="Hero" transform="translate(16, 120)">
        <!-- Modern Linear/Stripe-Style Live Status Badge -->
    <rect width="180" height="26" rx="13" fill="#ECFDF5" stroke="#A7F3D0" stroke-width="1"/>
    <circle cx="15" cy="13" r="5" fill="#10B981" fill-opacity="0.25"/>
    <circle cx="15" cy="13" r="3" fill="#059669"/>
    <text x="26" y="17" fill="#065F46" font-family="'Inter', sans-serif" font-size="11" font-weight="600" letter-spacing="0.4">24/7 DISPATCH ACTIVE</text>

    <text x="0" y="52" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="28" font-weight="800">
      <tspan x="0" dy="0">Reliable HVAC Service</tspan>
      <tspan x="0" dy="36">When You Need It.</tspan>
    </text>

    <text x="0" y="132" fill="#475569" font-family="'Inter', sans-serif" font-size="14">
      <tspan x="0" dy="0">From emergency heating repairs to AC</tspan>
      <tspan x="0" dy="20">installations, NorthStar keeps your home</tspan>
      <tspan x="0" dy="20">comfortable with upfront pricing.</tspan>
    </text>

    <!-- Hero Image (358 x 230) -->
    <g transform="translate(0, 195)">
      <defs>
        <clipPath id="m-hero-clip"><rect width="358" height="230" rx="10"/></clipPath>
      </defs>
      <rect width="358" height="230" rx="10" fill="#0F2238"/>
      <image href="data:image/jpeg;base64,{b64_hero}" width="358" height="230" preserveAspectRatio="xMidYMid slice" clip-path="url(#m-hero-clip)"/>
      <rect width="358" height="230" rx="10" fill="#0F2238" fill-opacity="0.15" clip-path="url(#m-hero-clip)"/>
    </g>

    <!-- Action Buttons -->
    <g transform="translate(0, 445)">
      <rect width="358" height="48" rx="8" fill="#E65100"/>
      <text x="179" y="29" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="15" font-weight="700" text-anchor="middle">Book a Service</text>

      <g transform="translate(0, 58)">
        <rect width="358" height="48" rx="8" fill="#FFFFFF" stroke="#0F2238" stroke-width="2"/>
        <text x="179" y="29" fill="#0F2238" font-family="'Inter', sans-serif" font-size="15" font-weight="700" text-anchor="middle">Call (555) 014-7824</text>
      </g>
    </g>
  </g>

  <!-- Trust Badges (2x2 Grid) -->
  <g id="Trust" transform="translate(16, 700)">
    <g transform="translate(0, 0)">
      <rect width="170" height="64" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <text x="12" y="26" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="700">Licensed &amp; Insured</text>
      <text x="12" y="44" fill="#15803D" font-family="'Inter', sans-serif" font-size="11">• Certified</text>
    </g>
    <g transform="translate(188, 0)">
      <rect width="170" height="64" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <text x="12" y="26" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="700">24/7 Emergency</text>
      <text x="12" y="44" fill="#DC2626" font-family="'Inter', sans-serif" font-size="11">• On-Call Dispatch</text>
    </g>
    <g transform="translate(0, 74)">
      <rect width="170" height="64" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <text x="12" y="26" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="700">10+ Yrs Experience</text>
      <text x="12" y="44" fill="#64748B" font-family="'Inter', sans-serif" font-size="11">• Master Techs</text>
    </g>
    <g transform="translate(188, 74)">
      <rect width="170" height="64" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <text x="12" y="26" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="700">100% Satisfaction</text>
      <text x="12" y="44" fill="#15803D" font-family="'Inter', sans-serif" font-size="11">• Guaranteed</text>
    </g>
  </g>

  <!-- Services (6 Cards Stacked) -->
  <g id="Services" transform="translate(16, 880)">
    <text x="0" y="16" fill="#E65100" font-family="'Inter', sans-serif" font-size="11" font-weight="700">OUR SERVICES</text>
    <text x="0" y="42" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="22" font-weight="800">HVAC for Every Season</text>

    <!-- Card 1 -->
    <g transform="translate(0, 60)">
      <rect width="358" height="135" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">AC Repair</text>
      <text x="16" y="60" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="16" dy="0">Fast diagnostics for warm air,</tspan>
        <tspan x="16" dy="18">strange noises, and coil leaks.</tspan>
      </text>
      <text x="16" y="112" fill="#0F2238" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Learn More →</text>
    </g>

    <!-- Card 2 -->
    <g transform="translate(0, 205)">
      <rect width="358" height="135" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">Heating &amp; Furnace Repair</text>
      <text x="16" y="60" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="16" dy="0">Reliable furnace ignition and</tspan>
        <tspan x="16" dy="18">blower fixes during freezing cold.</tspan>
      </text>
      <text x="16" y="112" fill="#0F2238" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Learn More →</text>
    </g>

    <!-- Card 3 -->
    <g transform="translate(0, 350)">
      <rect width="358" height="135" rx="8" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1"/>
      <text x="16" y="32" fill="#DC2626" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">24/7 Emergency Dispatch</text>
      <text x="16" y="60" fill="#991B1B" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="16" dy="0">Rapid arrival for complete</tspan>
        <tspan x="16" dy="18">system failure and freeze risk.</tspan>
      </text>
      <text x="16" y="112" fill="#DC2626" font-family="'Inter', sans-serif" font-size="12" font-weight="700">Call Emergency Line →</text>
    </g>
  </g>

  <!-- Workmanship Photo Card (358 x 200) -->
  <g transform="translate(16, 1400)">
    <defs>
      <clipPath id="m-furnace-clip"><rect width="358" height="200" rx="10"/></clipPath>
      <linearGradient id="m-furnace-grad" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#0F2238" stop-opacity="0.1"/>
        <stop offset="60%" stop-color="#0F2238" stop-opacity="0.85"/>
        <stop offset="100%" stop-color="#0F2238" stop-opacity="0.96"/>
      </linearGradient>
    </defs>
    <rect width="358" height="200" rx="10" fill="#0F2238"/>
    <image href="data:image/jpeg;base64,{b64_furnace}" width="358" height="200" preserveAspectRatio="xMidYMid slice" clip-path="url(#m-furnace-clip)"/>
    <rect width="358" height="200" rx="10" fill="url(#m-furnace-grad)" clip-path="url(#m-furnace-clip)"/>
    <g transform="translate(16, 120)">
      <text x="0" y="18" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="800">Clean Workmanship Guarantee</text>
      <text x="0" y="38" fill="#F1F5F9" font-family="'Inter', sans-serif" font-size="11">Shoe covers • Drop cloths • Digital diagnostic reports</text>
    </g>
  </g>

{mh.mobile_footer(1650)}'''
with open(os.path.join(mobile_dir, '00-home-mobile-390.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap(m00, 2030))
print("Created 00-home-mobile-390.svg")

# -------------------------------------------------------------
# 01-services-mobile-390.svg
# -------------------------------------------------------------
m01 = f'''{header}
  <g id="Hero" transform="translate(16, 120)">
    <text x="0" y="14" fill="#E65100" font-family="'Inter', sans-serif" font-size="11" font-weight="700">SERVICES DIRECTORY</text>
    <text x="0" y="44" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="800">HVAC Services for Every Season</text>
    <text x="0" y="72" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
      <tspan x="0" dy="0">Upfront flat-rate pricing with certified</tspan>
      <tspan x="0" dy="18">technicians across the metro region.</tspan>
    </text>
  </g>

  <!-- 4 Mobile Service Cards Stacked -->
  <g id="Services-Stack" transform="translate(16, 230)">
    <!-- 1. AC -->
    <g transform="translate(0, 0)">
      <rect width="358" height="150" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="30" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">Air Conditioning Services</text>
      <text x="16" y="58" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="16" dy="0">Fast repair for warm air, weird noises,</tspan>
        <tspan x="16" dy="18">refrigerant leaks, and blown capacitors.</tspan>
      </text>
      <g transform="translate(16, 98)">
        <rect width="130" height="36" rx="6" fill="#0F2238"/>
        <text x="65" y="22" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="600" text-anchor="middle">View AC Details →</text>
      </g>
    </g>

    <!-- 2. Heating -->
    <g transform="translate(0, 165)">
      <rect width="358" height="150" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="30" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">Heating &amp; Furnace Repair</text>
      <text x="16" y="58" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="16" dy="0">Gas furnaces, heat pumps, ignitors,</tspan>
        <tspan x="16" dy="18">and heat exchanger safety tests.</tspan>
      </text>
      <g transform="translate(16, 98)">
        <rect width="130" height="36" rx="6" fill="#0F2238"/>
        <text x="65" y="22" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="600" text-anchor="middle">View Heating →</text>
      </g>
    </g>

    <!-- 3. Maintenance -->
    <g transform="translate(0, 330)">
      <rect width="358" height="150" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="30" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">Preventive Maintenance</text>
      <text x="16" y="58" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="16" dy="0">Seasonal 24-point tune-up keeping</tspan>
        <tspan x="16" dy="18">power bills low and systems safe.</tspan>
      </text>
      <g transform="translate(16, 98)">
        <rect width="130" height="36" rx="6" fill="#0F2238"/>
        <text x="65" y="22" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="600" text-anchor="middle">View Tune-Ups →</text>
      </g>
    </g>

    <!-- 4. Emergency -->
    <g transform="translate(0, 495)">
      <rect width="358" height="150" rx="8" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1"/>
      <text x="16" y="30" fill="#DC2626" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="700">24/7 Emergency Dispatch</text>
      <text x="16" y="58" fill="#991B1B" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="16" dy="0">Urgent freeze or extreme heat call.</tspan>
        <tspan x="16" dy="18">Average response under 45 minutes.</tspan>
      </text>
      <g transform="translate(16, 98)">
        <rect width="150" height="36" rx="6" fill="#DC2626"/>
        <text x="75" y="22" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="12" font-weight="700" text-anchor="middle">Call Emergency Line</text>
      </g>
    </g>
  </g>

{mh.mobile_footer(920)}'''
with open(os.path.join(mobile_dir, '01-services-mobile-390.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap(m01, 1300))
print("Created 01-services-mobile-390.svg")

# -------------------------------------------------------------
# 02-service-detail-mobile-390.svg
# -------------------------------------------------------------
m02 = f'''{header}
  <g id="Hero" transform="translate(16, 120)">
    <text x="0" y="14" fill="#64748B" font-family="'Inter', sans-serif" font-size="11">Services &gt; Cooling &gt; <tspan font-weight="700" fill="#0F2238">AC Repair</tspan></text>
    <text x="0" y="44" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="800">Air Conditioning Repair</text>
    <text x="0" y="72" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
      <tspan x="0" dy="0">Fast diagnosis, flat-rate pricing, and</tspan>
      <tspan x="0" dy="18">long-lasting repairs by certified techs.</tspan>
    </text>
  </g>

  <!-- Symptoms Stack -->
  <g id="Symptoms" transform="translate(16, 230)">
    <text x="0" y="16" fill="#E65100" font-family="'Inter', sans-serif" font-size="11" font-weight="700">COMMON SIGNS</text>
    <text x="0" y="40" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="18" font-weight="800">Is Your AC Doing This?</text>

    <g transform="translate(0, 56)">
      <rect width="358" height="90" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="28" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">AC Blowing Warm Air</text>
      <text x="16" y="50" fill="#475569" font-family="'Inter', sans-serif" font-size="12">
        <tspan x="16" dy="0">Low refrigerant leak, failed compressor,</tspan>
        <tspan x="16" dy="16">or a blown run capacitor.</tspan>
      </text>
    </g>

    <g transform="translate(0, 156)">
      <rect width="358" height="90" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="28" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Strange Buzzing or Grinding</text>
      <text x="16" y="50" fill="#475569" font-family="'Inter', sans-serif" font-size="12">
        <tspan x="16" dy="0">Worn blower motor bearings or</tspan>
        <tspan x="16" dy="16">failing electrical contactor switches.</tspan>
      </text>
    </g>

    <g transform="translate(0, 256)">
      <rect width="358" height="90" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="28" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Water Leaking Around Unit</text>
      <text x="16" y="50" fill="#475569" font-family="'Inter', sans-serif" font-size="12">
        <tspan x="16" dy="0">Clogged drain line or cracked pan</tspan>
        <tspan x="16" dy="16">threatening ceiling water damage.</tspan>
      </text>
    </g>
  </g>

  <!-- Tap to Call Button (Fixed bottom style) -->
  <g transform="translate(16, 670)">
    <rect width="358" height="50" rx="8" fill="#E65100"/>
    <text x="179" y="30" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="14" font-weight="700" text-anchor="middle">Book AC Service Online →</text>
  </g>

{mh.mobile_footer(750)}'''
with open(os.path.join(mobile_dir, '02-service-detail-mobile-390.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap(m02, 1130))
print("Created 02-service-detail-mobile-390.svg")

# -------------------------------------------------------------
# 03-about-mobile-390.svg
# -------------------------------------------------------------
m03 = f'''{header}
  <g id="Hero" transform="translate(16, 120)">
    <text x="0" y="14" fill="#E65100" font-family="'Inter', sans-serif" font-size="11" font-weight="700">ABOUT NORTHSTAR</text>
    <text x="0" y="44" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="800">Doing the Job Right.</text>
    <text x="0" y="72" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
      <tspan x="0" dy="0">Founded on craftsmanship, honest flat-rate</tspan>
      <tspan x="0" dy="18">pricing, and clean trade workmanship.</tspan>
    </text>
  </g>

  <!-- Van Photo (358 x 200) -->
  <g transform="translate(16, 230)">
    <defs>
      <clipPath id="m-about-van"><rect width="358" height="200" rx="10"/></clipPath>
    </defs>
    <rect width="358" height="200" rx="10" fill="#0F2238"/>
    <image href="data:image/jpeg;base64,{b64_van}" width="358" height="200" preserveAspectRatio="xMidYMid slice" clip-path="url(#m-about-van)"/>
  </g>

  <!-- 3 Values Stacked -->
  <g id="Values" transform="translate(16, 455)">
    <text x="0" y="14" fill="#E65100" font-family="'Inter', sans-serif" font-size="11" font-weight="700">OUR STANDARDS</text>
    <text x="0" y="38" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="18" font-weight="800">Why Homeowners Trust Us</text>

    <g transform="translate(0, 54)">
      <rect width="358" height="90" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="28" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Absolute Integrity</text>
      <text x="16" y="50" fill="#475569" font-family="'Inter', sans-serif" font-size="12">
        <tspan x="16" dy="0">We only recommend what your system</tspan>
        <tspan x="16" dy="16">genuinely needs. Zero sales pressure.</tspan>
      </text>
    </g>

    <g transform="translate(0, 154)">
      <rect width="358" height="90" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="28" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Respect for Your Home</text>
      <text x="16" y="50" fill="#475569" font-family="'Inter', sans-serif" font-size="12">
        <tspan x="16" dy="0">Clean shoe boot covers and drop cloths</tspan>
        <tspan x="16" dy="16">used on every single service call.</tspan>
      </text>
    </g>

    <g transform="translate(0, 254)">
      <rect width="358" height="90" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="28" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">24/7 On-Call Dispatch</text>
      <text x="16" y="50" fill="#475569" font-family="'Inter', sans-serif" font-size="12">
        <tspan x="16" dy="0">Ready for sudden freeze warnings or</tspan>
        <tspan x="16" dy="16">dangerous summer heatwaves.</tspan>
      </text>
    </g>
  </g>

{mh.mobile_footer(840)}'''
with open(os.path.join(mobile_dir, '03-about-mobile-390.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap(m03, 1220))
print("Created 03-about-mobile-390.svg")

# -------------------------------------------------------------
# 04-service-areas-mobile-390.svg
# -------------------------------------------------------------
m04 = f'''{header}
  <g id="Hero" transform="translate(16, 120)">
    <text x="0" y="14" fill="#E65100" font-family="'Inter', sans-serif" font-size="11" font-weight="700">REGIONAL COVERAGE</text>
    <text x="0" y="44" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="800">Communities We Serve</text>
    <text x="0" y="72" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
      <tspan x="0" dy="0">Mobile service fleet stationed locally</tspan>
      <tspan x="0" dy="18">for prompt routine and emergency dispatch.</tspan>
    </text>
  </g>

  <!-- 6 Zones Mobile Chips -->
  <g id="Zones" transform="translate(16, 230)">
    <g transform="translate(0, 0)">
      <rect width="358" height="56" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Downtown District</text>
      <text x="342" y="32" fill="#15803D" font-family="'Inter', sans-serif" font-size="11" font-weight="600" text-anchor="end">• &lt; 30 Mins</text>
    </g>
    <g transform="translate(0, 66)">
      <rect width="358" height="56" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Northside Suburbs</text>
      <text x="342" y="32" fill="#15803D" font-family="'Inter', sans-serif" font-size="11" font-weight="600" text-anchor="end">• &lt; 35 Mins</text>
    </g>
    <g transform="translate(0, 132)">
      <rect width="358" height="56" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Westfield District</text>
      <text x="342" y="32" fill="#15803D" font-family="'Inter', sans-serif" font-size="11" font-weight="600" text-anchor="end">• &lt; 40 Mins</text>
    </g>
    <g transform="translate(0, 198)">
      <rect width="358" height="56" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Brookhaven Hills</text>
      <text x="342" y="32" fill="#15803D" font-family="'Inter', sans-serif" font-size="11" font-weight="600" text-anchor="end">• &lt; 40 Mins</text>
    </g>
    <g transform="translate(0, 264)">
      <rect width="358" height="56" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Riverside Corridor</text>
      <text x="342" y="32" fill="#15803D" font-family="'Inter', sans-serif" font-size="11" font-weight="600" text-anchor="end">• &lt; 35 Mins</text>
    </g>
    <g transform="translate(0, 330)">
      <rect width="358" height="56" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Eastwood Township</text>
      <text x="342" y="32" fill="#15803D" font-family="'Inter', sans-serif" font-size="11" font-weight="600" text-anchor="end">• &lt; 45 Mins</text>
    </g>
  </g>

{mh.mobile_footer(660)}'''
with open(os.path.join(mobile_dir, '04-service-areas-mobile-390.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap(m04, 1040))
print("Created 04-service-areas-mobile-390.svg")

# -------------------------------------------------------------
# 05-financing-mobile-390.svg
# -------------------------------------------------------------
m05 = f'''{header}
  <g id="Hero" transform="translate(16, 120)">
    <text x="0" y="14" fill="#E65100" font-family="'Inter', sans-serif" font-size="11" font-weight="700">FLEXIBLE FINANCING</text>
    <text x="0" y="44" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="800">Comfort Now. Pay Over Time.</text>
    <text x="0" y="72" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
      <tspan x="0" dy="0">Flexible monthly payment options for</tspan>
      <tspan x="0" dy="18">qualifying installations and replacements.</tspan>
    </text>
  </g>

  <!-- 3 Steps Mobile -->
  <g id="Steps" transform="translate(16, 230)">
    <g transform="translate(0, 0)">
      <rect width="358" height="84" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="28" cy="42" r="14" fill="#0F2238"/>
      <text x="28" y="47" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="800" text-anchor="middle">1</text>
      <text x="54" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Prequalify Online</text>
      <text x="54" y="52" fill="#475569" font-family="'Inter', sans-serif" font-size="11">Soft credit check with zero score impact.</text>
    </g>

    <g transform="translate(0, 94)">
      <rect width="358" height="84" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="28" cy="42" r="14" fill="#0F2238"/>
      <text x="28" y="47" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="800" text-anchor="middle">2</text>
      <text x="54" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Select Monthly Plan</text>
      <text x="54" y="52" fill="#475569" font-family="'Inter', sans-serif" font-size="11">Choose term fitting your monthly budget.</text>
    </g>

    <g transform="translate(0, 188)">
      <rect width="358" height="84" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
      <circle cx="28" cy="42" r="14" fill="#0F2238"/>
      <text x="28" y="47" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="800" text-anchor="middle">3</text>
      <text x="54" y="32" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Install &amp; Enjoy</text>
      <text x="54" y="52" fill="#475569" font-family="'Inter', sans-serif" font-size="11">Certified NorthStar installation proceeds.</text>
    </g>
  </g>

{mh.mobile_footer(550)}'''
with open(os.path.join(mobile_dir, '05-financing-mobile-390.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap(m05, 930))
print("Created 05-financing-mobile-390.svg")

# -------------------------------------------------------------
# 06-reviews-mobile-390.svg
# -------------------------------------------------------------
m06 = f'''{header}
  <g id="Hero" transform="translate(16, 120)">
    <text x="0" y="14" fill="#E65100" font-family="'Inter', sans-serif" font-size="11" font-weight="700">REVIEWS</text>
    <text x="0" y="44" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="800">4.9 / 5.0 Rating</text>
    <text x="0" y="72" fill="#475569" font-family="'Inter', sans-serif" font-size="13">Based on 650+ verified local homeowners.</text>
  </g>

  <!-- 3 Reviews Mobile -->
  <g id="Reviews" transform="translate(16, 220)">
    <g transform="translate(0, 0)">
      <rect width="358" height="150" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="28" fill="#F59E0B">★★★★★</text>
      <text x="16" y="52" fill="#1E293B" font-family="'Inter', sans-serif" font-size="12" font-style="italic">
        <tspan x="16" dy="0">"Technician arrived on time, diagnosed</tspan>
        <tspan x="16" dy="18">the bad capacitor in 20 minutes, and had</tspan>
        <tspan x="16" dy="18">our AC running before heat peaked."</tspan>
      </text>
      <text x="16" y="125" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="700">Sarah M. • <tspan font-weight="400" fill="#64748B">Northside</tspan></text>
    </g>

    <g transform="translate(0, 165)">
      <rect width="358" height="150" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="28" fill="#F59E0B">★★★★★</text>
      <text x="16" y="52" fill="#1E293B" font-family="'Inter', sans-serif" font-size="12" font-style="italic">
        <tspan x="16" dy="0">"Furnace stopped igniting on a freezing</tspan>
        <tspan x="16" dy="18">Sunday. Tech replaced the ignitor</tspan>
        <tspan x="16" dy="18">directly from their van. Great work."</tspan>
      </text>
      <text x="16" y="125" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="700">David R. • <tspan font-weight="400" fill="#64748B">Westfield</tspan></text>
    </g>
  </g>

{mh.mobile_footer(580)}'''
with open(os.path.join(mobile_dir, '06-reviews-mobile-390.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap(m06, 960))
print("Created 06-reviews-mobile-390.svg")

# -------------------------------------------------------------
# 07-contact-mobile-390.svg
# -------------------------------------------------------------
m07 = f'''{header}
  <g id="Hero" transform="translate(16, 120)">
    <text x="0" y="14" fill="#E65100" font-family="'Inter', sans-serif" font-size="11" font-weight="700">CONTACT US</text>
    <text x="0" y="44" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="800">Send a Service Request</text>
    <text x="0" y="72" fill="#475569" font-family="'Inter', sans-serif" font-size="13">Available 24 hours a day for emergency service.</text>
  </g>

  <!-- Mobile Form -->
  <g id="Form" transform="translate(16, 210)">
    <rect width="358" height="420" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
    <g transform="translate(16, 20)">
      <text x="0" y="14" fill="#334155" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Full Name *</text>
      <rect y="22" width="326" height="42" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
      <text x="12" y="48" fill="#0F172A" font-family="'Inter', sans-serif" font-size="13">Sarah Miller</text>

      <g transform="translate(0, 75)">
        <text x="0" y="14" fill="#334155" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Phone Number *</text>
        <rect y="22" width="326" height="42" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
        <text x="12" y="48" fill="#0F172A" font-family="'Inter', sans-serif" font-size="13">(555) 789-0123</text>
      </g>

      <g transform="translate(0, 150)">
        <text x="0" y="14" fill="#334155" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Service Needed *</text>
        <rect y="22" width="326" height="42" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
        <text x="12" y="48" fill="#0F172A" font-family="'Inter', sans-serif" font-size="13">AC Repair &amp; Diagnostics</text>
      </g>

      <g transform="translate(0, 225)">
        <text x="0" y="14" fill="#334155" font-family="'Inter', sans-serif" font-size="12" font-weight="600">Symptoms</text>
        <rect y="22" width="326" height="60" rx="6" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
        <text x="12" y="44" fill="#475569" font-family="'Inter', sans-serif" font-size="12">AC unit outdoor fan running, warm air.</text>
      </g>

      <g transform="translate(0, 320)">
        <rect width="326" height="46" rx="6" fill="#E65100"/>
        <text x="163" y="28" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="14" font-weight="700" text-anchor="middle">Send Service Request →</text>
      </g>
    </g>
  </g>

{mh.mobile_footer(660)}'''
with open(os.path.join(mobile_dir, '07-contact-mobile-390.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap(m07, 1040))
print("Created 07-contact-mobile-390.svg")

# -------------------------------------------------------------
# 08-book-a-service-mobile-390.svg
# -------------------------------------------------------------
m08 = f'''{header}
  <g id="Hero" transform="translate(16, 120)">
    <text x="0" y="14" fill="#E65100" font-family="'Inter', sans-serif" font-size="11" font-weight="700">STEP 1 OF 4</text>
    <text x="0" y="44" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="24" font-weight="800">Choose Your Service</text>
  </g>

  <!-- Mobile Service Chips -->
  <g id="Chips" transform="translate(16, 190)">
    <g transform="translate(0, 0)">
      <rect width="358" height="60" rx="8" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.5"/>
      <text x="16" y="35" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">AC Repair</text>
      <text x="342" y="35" fill="#2563EB" font-family="'Inter', sans-serif" font-size="11" font-weight="700" text-anchor="end">✓ SELECTED</text>
    </g>

    <g transform="translate(0, 70)">
      <rect width="358" height="60" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
      <text x="16" y="35" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">AC Installation</text>
    </g>

    <g transform="translate(0, 140)">
      <rect width="358" height="60" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
      <text x="16" y="35" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Heating &amp; Furnace Repair</text>
    </g>

    <g transform="translate(0, 210)">
      <rect width="358" height="60" rx="8" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1"/>
      <text x="16" y="35" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">Preventive Maintenance</text>
    </g>

    <g transform="translate(0, 280)">
      <rect width="358" height="60" rx="8" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1"/>
      <text x="16" y="35" fill="#DC2626" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="700">24/7 Emergency Dispatch</text>
    </g>

    <g transform="translate(0, 360)">
      <rect width="358" height="48" rx="8" fill="#E65100"/>
      <text x="179" y="29" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="14" font-weight="700" text-anchor="middle">Continue to Date →</text>
    </g>
  </g>

{mh.mobile_footer(640)}'''
with open(os.path.join(mobile_dir, '08-book-a-service-mobile-390.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap(m08, 1020))
print("Created 08-book-a-service-mobile-390.svg")

# -------------------------------------------------------------
# 09-emergency-hvac-mobile-390.svg
# -------------------------------------------------------------
m09 = f'''{header}
  <g id="Hero" transform="translate(16, 120)">
    <rect width="180" height="24" rx="12" fill="#DC2626"/>
    <text x="90" y="16" fill="#FFFFFF" font-family="'Inter', sans-serif" font-size="10" font-weight="700" text-anchor="middle">• PRIORITY DISPATCH</text>

    <text x="0" y="52" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="26" font-weight="800">
      <tspan x="0" dy="0">Emergency HVAC</tspan>
      <tspan x="0" dy="34">24/7 Fast Response</tspan>
    </text>

    <text x="0" y="130" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
      <tspan x="0" dy="0">No heat or cooling in extreme weather?</tspan>
      <tspan x="0" dy="18">Vans arrive in under 45 minutes.</tspan>
    </text>

    <!-- Tap to Call Big Button -->
    <g transform="translate(0, 175)">
      <rect width="358" height="52" rx="8" fill="#DC2626"/>
      <text x="179" y="32" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="16" font-weight="800" text-anchor="middle">Call (555) 014-7824 Now</text>
    </g>
  </g>

  <!-- Situations Mobile Stack -->
  <g id="Situations" transform="translate(16, 380)">
    <text x="0" y="14" fill="#DC2626" font-family="'Inter', sans-serif" font-size="11" font-weight="700">CALL IMMEDIATELY IF</text>
    <text x="0" y="38" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="18" font-weight="800">Common HVAC Emergencies</text>

    <g transform="translate(0, 52)">
      <rect width="358" height="84" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="28" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Complete Heat Outage</text>
      <text x="16" y="48" fill="#475569" font-family="'Inter', sans-serif" font-size="12">
        <tspan x="16" dy="0">Furnace fails during freezing temps,</tspan>
        <tspan x="16" dy="16">risking pipe freeze-ups.</tspan>
      </text>
    </g>

    <g transform="translate(0, 146)">
      <rect width="358" height="84" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="28" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">AC Failure in Heatwave</text>
      <text x="16" y="48" fill="#475569" font-family="'Inter', sans-serif" font-size="12">
        <tspan x="16" dy="0">Cooling quits with indoor temps &gt; 85°F,</tspan>
        <tspan x="16" dy="16">risking health of elderly &amp; infants.</tspan>
      </text>
    </g>

    <g transform="translate(0, 240)">
      <rect width="358" height="84" rx="8" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1"/>
      <text x="16" y="28" fill="#0F2238" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Electrical Burning Smell</text>
      <text x="16" y="48" fill="#475569" font-family="'Inter', sans-serif" font-size="12">
        <tspan x="16" dy="0">Smoke odor from blower motor indicates</tspan>
        <tspan x="16" dy="16">an immediate electrical fire risk.</tspan>
      </text>
    </g>
  </g>

{mh.mobile_footer(740)}'''
with open(os.path.join(mobile_dir, '09-emergency-hvac-mobile-390.svg'), 'w', encoding='utf-8') as f:
    f.write(wrap(m09, 1120))
print("Created 09-emergency-hvac-mobile-390.svg")

