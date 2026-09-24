import re, os, sys

def apply_replacements(filepath, rep_list):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    success_count = 0
    for old, new in rep_list:
        if old in content:
            content = content.replace(old, new)
            success_count += 1
        else:
            print(f"FAILED in {filepath}: '{old[:50]}...'")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[{os.path.basename(filepath)}] Applied {success_count}/{len(rep_list)} replacements.")

# ==============================================================================
# 02-service-detail-page.svg
# ==============================================================================
rep_02 = [
    (
'''        <text x="24" y="80" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          Unit powers on and off every few minutes without satisfying the thermostat, rapidly spiking power bills.
        </text>''',
'''        <text x="24" y="76" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="24" dy="0">Unit cycles on and off every few minutes</tspan>
          <tspan x="24" dy="20">without reaching thermostat setpoint, spiking</tspan>
          <tspan x="24" dy="20">power bills and stressing the compressor.</tspan>
        </text>'''
    ),
    (
'''        <text x="24" y="80" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          Clogged condensate drain lines or a cracked drain pan threatening ceiling and drywall water damage.
        </text>''',
'''        <text x="24" y="76" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="24" dy="0">Clogged condensate drain lines or cracked</tspan>
          <tspan x="24" dy="20">drain pans overflowing into drywall, creating</tspan>
          <tspan x="24" dy="20">structural ceiling water damage risk.</tspan>
        </text>'''
    ),
    (
'''        <text x="32" y="82" fill="#475569" font-family="'Inter', sans-serif" font-size="14">
          If your AC unit is under 10 years old and the repair cost is under 50% of a new system, repairing is usually most cost-effective. If older than 12-15 years or using phased-out R-22 refrigerant, replacement often provides superior long-term savings.
        </text>''',
'''        <text x="32" y="78" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="32" dy="0">If your AC is under 10 years old and repair costs are under 50% of replacement, repairing is usually most cost-effective.</tspan>
          <tspan x="32" dy="22">For systems older than 12-15 years using phased-out R-22 Freon, upgrading to high-efficiency SEER2 delivers greater savings.</tspan>
        </text>'''
    )
]
apply_replacements('svgs/pages/02-service-detail-page.svg', rep_02)

# ==============================================================================
# 03-about-page.svg
# ==============================================================================
rep_03 = [
    (
'''        <text x="24" y="126" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          We only recommend repairs or equipment that your home genuinely requires. No manufactured urgency.
        </text>''',
'''        <text x="24" y="124" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="24" dy="0">We only recommend repairs or equipment</tspan>
          <tspan x="24" dy="20">that your home genuinely requires.</tspan>
          <tspan x="24" dy="20">Zero manufactured sales urgency.</tspan>
        </text>'''
    ),
    (
'''        <text x="24" y="126" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          Manual J load calculations and digital diagnostic manifold testing ensure solutions meet engineering standards.
        </text>''',
'''        <text x="24" y="124" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="24" dy="0">Manual J load calculations and digital</tspan>
          <tspan x="24" dy="20">manifold testing ensure every repair</tspan>
          <tspan x="24" dy="20">meets factory manufacturer specs.</tspan>
        </text>'''
    ),
    (
'''        <text x="24" y="126" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          Clean uniforms, protective shoe covers, clean drop cloths, and thorough job-site clean up on every single call.
        </text>''',
'''        <text x="24" y="124" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="24" dy="0">Clean uniforms, shoe boot covers, floor</tspan>
          <tspan x="24" dy="20">drop cloths, and complete job-site</tspan>
          <tspan x="24" dy="20">clean up on every service call.</tspan>
        </text>'''
    ),
    (
'''        <text x="24" y="126" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          24/7 on-call dispatching for sudden extreme freeze or summer heat waves when comfort is a health necessity.
        </text>''',
'''        <text x="24" y="124" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="24" dy="0">24/7 on-call dispatch for sudden winter</tspan>
          <tspan x="24" dy="20">freeze warnings or summer heatwaves</tspan>
          <tspan x="24" dy="20">when climate is critical.</tspan>
        </text>'''
    ),
    (
'''          <text x="20" y="68" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            Peace of mind knowing trustworthy professionals are in your home.
          </text>''',
'''          <text x="20" y="66" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="20" dy="0">Peace of mind knowing trustworthy,</tspan>
            <tspan x="20" dy="20">vetted professionals are in your home.</tspan>
          </text>'''
    ),
    (
'''          <text x="20" y="68" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            Factory training on major brands: Carrier, Trane, Lennox, Mitsubishi.
          </text>''',
'''          <text x="20" y="66" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="20" dy="0">Factory trained on Carrier, Trane,</tspan>
            <tspan x="20" dy="20">Lennox, and Mitsubishi systems.</tspan>
          </text>'''
    ),
    (
'''          <text x="20" y="68" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            Trucks stocked with 200+ universal parts for immediate single-visit resolution.
          </text>''',
'''          <text x="20" y="66" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="20" dy="0">Vans stocked with 200+ universal parts</tspan>
            <tspan x="20" dy="20">for single-visit issue resolution.</tspan>
          </text>'''
    )
]
apply_replacements('svgs/pages/03-about-page.svg', rep_03)

# ==============================================================================
# 04-service-areas-page.svg
# ==============================================================================
rep_04 = [
    (
'''          <text x="0" y="96" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="0" dy="0">Serving high-rise condos, historic homes, and</tspan>
            <tspan x="0" dy="20">light commercial businesses. 24/7 priority routing.</tspan>
          </text>''',
'''          <text x="0" y="96" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="0" dy="0">High-rise condos, historic homes,</tspan>
            <tspan x="0" dy="20">and light commercial facilities.</tspan>
            <tspan x="0" dy="20">24/7 priority emergency dispatch.</tspan>
          </text>'''
    ),
    (
'''          <text x="0" y="96" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="0" dy="0">Single-family residential AC replacement, dual</tspan>
            <tspan x="0" dy="20">fuel heat pumps, and ductwork enhancements.</tspan>
          </text>''',
'''          <text x="0" y="96" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="0" dy="0">Single-family AC replacements,</tspan>
            <tspan x="0" dy="20">dual-fuel heat pump systems, and</tspan>
            <tspan x="0" dy="20">ductwork airflow enhancements.</tspan>
          </text>'''
    ),
    (
'''          <text x="0" y="96" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="0" dy="0">Comprehensive furnace tune-ups, filter club</tspan>
            <tspan x="0" dy="20">deliveries, and smart thermostat installations.</tspan>
          </text>''',
'''          <text x="0" y="96" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="0" dy="0">Comprehensive furnace tune-ups,</tspan>
            <tspan x="0" dy="20">MERV filter replacements, and</tspan>
            <tspan x="0" dy="20">smart thermostat installations.</tspan>
          </text>'''
    ),
    (
'''          <text x="0" y="96" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="0" dy="0">Multi-zone mini-splits, whole-home dehumidifiers,</tspan>
            <tspan x="0" dy="20">and seasonal maintenance checks.</tspan>
          </text>''',
'''          <text x="0" y="96" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="0" dy="0">Multi-zone mini-split systems,</tspan>
            <tspan x="0" dy="20">whole-home dehumidification, and</tspan>
            <tspan x="0" dy="20">seasonal preventive tune-ups.</tspan>
          </text>'''
    ),
    (
'''          <text x="0" y="96" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="0" dy="0">High-efficiency condensing units, refrigerant line</tspan>
            <tspan x="0" dy="20">repair, and light commercial rooftop units.</tspan>
          </text>''',
'''          <text x="0" y="96" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="0" dy="0">High-efficiency condensing units,</tspan>
            <tspan x="0" dy="20">refrigerant leak repairs, and</tspan>
            <tspan x="0" dy="20">light commercial rooftop service.</tspan>
          </text>'''
    ),
    (
'''          <text x="0" y="96" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="0" dy="0">Emergency furnace ignition replacements, boiler</tspan>
            <tspan x="0" dy="20">tune-ups, and whole-home filtration retrofits.</tspan>
          </text>''',
'''          <text x="0" y="96" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="0" dy="0">Emergency furnace ignitor fixes,</tspan>
            <tspan x="0" dy="20">boiler radiator tune-ups, and</tspan>
            <tspan x="0" dy="20">whole-home filtration retrofits.</tspan>
          </text>'''
    )
]
apply_replacements('svgs/pages/04-service-areas-page.svg', rep_04)

# ==============================================================================
# 05-financing-page.svg
# ==============================================================================
rep_05 = [
    (
'''        <text x="32" y="66" fill="#475569" font-family="'Inter', sans-serif" font-size="14">
          No. Initial prequalification utilizes a soft credit inquiry, allowing you to review potential loan options without affecting your score.
        </text>''',
'''        <text x="32" y="66" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="32" dy="0">No. Initial prequalification utilizes a soft credit inquiry, allowing you</tspan>
          <tspan x="32" dy="20">to review potential monthly loan options without affecting your credit score.</tspan>
        </text>'''
    ),
    (
'''        <text x="32" y="66" fill="#475569" font-family="'Inter', sans-serif" font-size="14">
          Yes. Financing programs provided through our lending network feature zero early prepayment penalties.
        </text>''',
'''        <text x="32" y="66" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="32" dy="0">Yes. Financing programs provided through our lending network feature</tspan>
          <tspan x="32" dy="20">zero early prepayment penalties, giving you total payment flexibility.</tspan>
        </text>'''
    )
]
apply_replacements('svgs/pages/05-financing-page.svg', rep_05)

# ==============================================================================
# 07-contact-page.svg
# ==============================================================================
rep_07 = [
    (
'''            <text x="14" y="50" fill="#475569" font-family="'Inter', sans-serif" font-size="14">
              AC unit outdoor condenser fan is running but indoor vents are only blowing room-temperature air.
            </text>''',
'''            <text x="14" y="46" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
              <tspan x="14" dy="0">Outdoor AC condenser fan is running, but indoor vents</tspan>
              <tspan x="14" dy="22">are only blowing room-temperature air.</tspan>
            </text>'''
    ),
    (
'''        <text x="0" y="80" fill="#047857" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="0" dy="0">Confirmation sent to your inbox. An on-call NorthStar service coordinator</tspan>
          <tspan x="0" dy="20">will telephone you shortly to confirm your scheduled time slot.</tspan>
        </text>''',
'''        <text x="0" y="80" fill="#047857" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="0" dy="0">Confirmation sent to your inbox. An on-call NorthStar</tspan>
          <tspan x="0" dy="20">coordinator will telephone you shortly to confirm your arrival window.</tspan>
        </text>'''
    )
]
apply_replacements('svgs/pages/07-contact-page.svg', rep_07)

# ==============================================================================
# 08-book-a-service-page.svg
# ==============================================================================
rep_08 = [
    (
'''          <text x="24" y="68" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            New high-efficiency system quotes &amp; upgrades.
          </text>''',
'''          <text x="24" y="66" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="24" dy="0">New high-efficiency SEER2</tspan>
            <tspan x="24" dy="18">system quotes and replacements.</tspan>
          </text>'''
    ),
    (
'''          <text x="24" y="68" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            Furnaces, boilers, and heat pumps not heating.
          </text>''',
'''          <text x="24" y="66" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="24" dy="0">Gas furnaces, boilers, and</tspan>
            <tspan x="24" dy="18">heat pumps not heating properly.</tspan>
          </text>'''
    ),
    (
'''          <text x="24" y="68" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            Seasonal 24-point comprehensive tune-up.
          </text>''',
'''          <text x="24" y="66" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="24" dy="0">Seasonal 24-point tune-up</tspan>
            <tspan x="24" dy="18">for safety, airflow, and efficiency.</tspan>
          </text>'''
    ),
    (
'''          <text x="24" y="68" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            Dehumidifiers, filters, and UV air purifiers.
          </text>''',
'''          <text x="24" y="66" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="24" dy="0">Whole-home dehumidifiers, MERV</tspan>
            <tspan x="24" dy="18">filters, and germicidal UV lamps.</tspan>
          </text>'''
    ),
    (
'''          <text x="24" y="68" fill="#991B1B" font-family="'Inter', sans-serif" font-size="13">
            Urgent failure during severe weather &amp; freeze.
          </text>''',
'''          <text x="24" y="66" fill="#991B1B" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="24" dy="0">Urgent heat outage during freezes</tspan>
            <tspan x="24" dy="18">or severe summer AC breakdowns.</tspan>
          </text>'''
    ),
    (
'''          <text x="14" y="48" fill="#475569" font-family="'Inter', sans-serif" font-size="14">
            Outside AC condenser making loud rattling noise when starting. Thermostat set to 72, house reading 79.
          </text>''',
'''          <text x="14" y="46" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="14" dy="0">Outside AC condenser making loud rattling noise on startup.</tspan>
            <tspan x="14" dy="20">Thermostat set to 72°F, house reading 79°F with weak airflow.</tspan>
          </text>'''
    ),
    (
'''          <text x="24" y="12" fill="#334155" font-family="'Inter', sans-serif" font-size="14">You will receive an automated SMS confirmation with a real-time technician GPS tracking link.</text>''',
'''          <text x="24" y="12" fill="#334155" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="24" dy="0">You will receive an automated SMS confirmation</tspan>
            <tspan x="24" dy="20">with a real-time technician GPS tracking link.</tspan>
          </text>'''
    )
]
apply_replacements('svgs/pages/08-book-a-service-page.svg', rep_08)

# ==============================================================================
# 09-emergency-hvac-page.svg
# ==============================================================================
rep_09 = [
    (
'''        <text x="24" y="124" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          Furnace stops igniting during freezing outdoor temperatures, risking frozen plumbing pipes.
        </text>''',
'''        <text x="24" y="122" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="24" dy="0">Furnace fails to ignite during</tspan>
          <tspan x="24" dy="20">freezing outdoor weather,</tspan>
          <tspan x="24" dy="20">risking frozen plumbing pipes.</tspan>
        </text>'''
    ),
    (
'''        <text x="24" y="124" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          Cooling system quits with indoor temperatures exceeding 85°F, threatening vulnerable residents.
        </text>''',
'''        <text x="24" y="122" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="24" dy="0">Cooling quits with indoor</tspan>
          <tspan x="24" dy="20">temperatures above 85°F,</tspan>
          <tspan x="24" dy="20">endangering family health.</tspan>
        </text>'''
    ),
    (
'''        <text x="24" y="124" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          Acrid smoke smell from blower cabinet indicating melted wiring or seized motor windings.
        </text>''',
'''        <text x="24" y="122" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="24" dy="0">Acrid smoke odor from the</tspan>
          <tspan x="24" dy="20">blower motor or wiring indicates</tspan>
          <tspan x="24" dy="20">an immediate fire hazard.</tspan>
        </text>'''
    ),
    (
'''        <text x="24" y="124" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          Condensate drain line overflowing inside attic or basement, creating ceiling structural risk.
        </text>''',
'''        <text x="24" y="122" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="24" dy="0">Clogged drain lines or cracked</tspan>
          <tspan x="24" dy="20">pan overflowing into drywall,</tspan>
          <tspan x="24" dy="20">threatening ceiling collapse.</tspan>
        </text>'''
    ),
    (
'''          <text x="44" y="38" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">
            Prevents further compressor motor burnout or electrical shorting.
          </text>''',
'''          <text x="44" y="38" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="44" dy="0">Prevents further compressor motor burnout,</tspan>
            <tspan x="44" dy="20">refrigerant flooding, or electrical shorts.</tspan>
          </text>'''
    ),
    (
'''          <text x="44" y="38" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">
            Check if the outdoor unit disconnect or indoor sub-panel tripped once.
          </text>''',
'''          <text x="44" y="38" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="44" dy="0">Check once if outdoor condenser disconnect</tspan>
            <tspan x="44" dy="20">or main furnace breaker has tripped off.</tspan>
          </text>'''
    ),
    (
'''          <text x="44" y="38" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">
            Ensure clear path to attic, closet, or crawlspace for fast technician access.
          </text>''',
'''          <text x="44" y="38" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">
            <tspan x="44" dy="0">Ensure clear path to furnace closet or</tspan>
            <tspan x="44" dy="20">attic for fast technician equipment access.</tspan>
          </text>'''
    ),
    (
'''        <text x="24" y="66" fill="#475569" font-family="'Inter', sans-serif" font-size="14">
          A local coordinator answers immediately, gathers symptom details, and locates the closest on-call truck.
        </text>''',
'''        <text x="24" y="66" fill="#475569" font-family="'Inter', sans-serif" font-size="14">
          <tspan x="24" dy="0">A local coordinator answers live,</tspan>
          <tspan x="24" dy="22">records symptoms, and alerts the</tspan>
          <tspan x="24" dy="22">nearest on-call technician van.</tspan>
        </text>'''
    ),
    (
'''        <text x="24" y="66" fill="#475569" font-family="'Inter', sans-serif" font-size="14">
          The assigned technician receives full equipment logs and GPS routing directly to your home address.
        </text>''',
'''        <text x="24" y="66" fill="#475569" font-family="'Inter', sans-serif" font-size="14">
          <tspan x="24" dy="0">Your technician gets diagnostics</tspan>
          <tspan x="24" dy="22">and routes directly to your home</tspan>
          <tspan x="24" dy="22">with real-time GPS tracking.</tspan>
        </text>'''
    ),
    (
'''        <text x="24" y="66" fill="#475569" font-family="'Inter', sans-serif" font-size="14">
          Upfront diagnosis provided. Universal replacement parts on board allow immediate same-visit repair.
        </text>''',
'''        <text x="24" y="66" fill="#475569" font-family="'Inter', sans-serif" font-size="14">
          <tspan x="24" dy="0">Upfront diagnosis explained. 200+</tspan>
          <tspan x="24" dy="22">universal parts on the truck allow</tspan>
          <tspan x="24" dy="22">same-visit emergency repairs.</tspan>
        </text>'''
    )
]
apply_replacements('svgs/pages/09-emergency-hvac-page.svg', rep_09)

# ==============================================================================
# mobile-390.svg
# ==============================================================================
rep_mobile = [
    (
'''      <text x="16" y="74" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        Fast diagnostics for warm air, weird noises, and leaks.
      </text>''',
'''      <text x="16" y="72" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="16" dy="0">Fast diagnostics for warm air,</tspan>
        <tspan x="16" dy="20">strange noises, and coil leaks.</tspan>
      </text>'''
    ),
    (
'''      <text x="16" y="74" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        Reliable ignition and blower repairs during freezing weather.
      </text>''',
'''      <text x="16" y="72" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="16" dy="0">Reliable furnace ignition and</tspan>
        <tspan x="16" dy="20">blower fixes during freezing cold.</tspan>
      </text>'''
    ),
    (
'''      <text x="16" y="74" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">
        Immediate arrival for complete system failure and safety risks.
      </text>''',
'''      <text x="16" y="72" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="16" dy="0">Rapid arrival for complete</tspan>
        <tspan x="16" dy="20">system failure and freeze risk.</tspan>
      </text>'''
    ),
    (
'''      <text x="0" y="90" fill="#CBD5E1" font-family="'Inter', sans-serif" font-size="14">
        Technicians on call across the metro area right now.
      </text>''',
'''      <text x="0" y="90" fill="#CBD5E1" font-family="'Inter', sans-serif" font-size="14">
        <tspan x="0" dy="0">Certified technicians on call</tspan>
        <tspan x="0" dy="22">across the metro area right now.</tspan>
      </text>'''
    ),
    (
'''      <text x="0" y="60" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        Accurate testing with upfront flat-rate pricing.
      </text>''',
'''      <text x="0" y="60" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="0" dy="0">Accurate testing with upfront</tspan>
        <tspan x="0" dy="18">flat-rate pricing guaranteed.</tspan>
      </text>'''
    )
]
apply_replacements('svgs/responsive/mobile-390.svg', rep_mobile)

# ==============================================================================
# tablet-834.svg
# ==============================================================================
rep_tablet = [
    (
'''      <text x="24" y="130" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        Fast diagnostics for warm air, weird noises, and refrigerant leaks.
      </text>''',
'''      <text x="24" y="130" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="24" dy="0">Fast diagnostics for warm air,</tspan>
        <tspan x="24" dy="20">strange noises, and refrigerant leaks.</tspan>
      </text>'''
    ),
    (
'''      <text x="24" y="130" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        High-efficiency central AC and heat pumps sized for peak savings.
      </text>''',
'''      <text x="24" y="130" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="24" dy="0">High-efficiency central AC and</tspan>
        <tspan x="24" dy="20">heat pumps sized for peak savings.</tspan>
      </text>'''
    ),
    (
'''      <text x="24" y="130" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        Gas furnace ignition fixes and cold-climate heat pump diagnostics.
      </text>''',
'''      <text x="24" y="130" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="24" dy="0">Gas furnace ignition fixes and</tspan>
        <tspan x="24" dy="20">cold-climate heat pump diagnostics.</tspan>
      </text>'''
    ),
    (
'''      <text x="24" y="130" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        Seasonal 24-point tune-up keeping power bills low and systems safe.
      </text>''',
'''      <text x="24" y="130" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="24" dy="0">Seasonal 24-point tune-ups keeping</tspan>
        <tspan x="24" dy="20">power bills low and systems safe.</tspan>
      </text>'''
    ),
    (
'''      <text x="0" y="80" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="15">
        Our emergency HVAC team is on call 24 hours a day with local van dispatch.
      </text>''',
'''      <text x="0" y="80" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="15">
        <tspan x="0" dy="0">Our emergency HVAC team is on call 24 hours a day</tspan>
        <tspan x="0" dy="22">with local service van radio dispatch.</tspan>
      </text>'''
    )
]
apply_replacements('svgs/responsive/tablet-834.svg', rep_tablet)

