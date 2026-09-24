import re

def update_file(path, replacements):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in replacements:
        if old not in content:
            print(f"WARNING: '{old[:40]}...' not found in {path}")
        else:
            content = content.replace(old, new)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {path}")

# 1. svgs/home/03-hero.svg
update_file('svgs/home/03-hero.svg', [
    (
'''        <text x="0" y="0" fill="#475569" font-family="'Inter', sans-serif" font-size="18" font-weight="400">
          <tspan x="0" dy="0">From emergency heating repairs to high-efficiency AC installations,</tspan>
          <tspan x="0" dy="28">NorthStar keeps your home comfortable year-round with clear,</tspan>
          <tspan x="0" dy="28">upfront pricing and certified local technicians.</tspan>
        </text>''',
'''        <text x="0" y="0" fill="#475569" font-family="'Inter', sans-serif" font-size="18" font-weight="400">
          <tspan x="0" dy="0">From emergency heating repairs to high-efficiency</tspan>
          <tspan x="0" dy="28">cooling installations, NorthStar keeps your home</tspan>
          <tspan x="0" dy="28">comfortable year-round with transparent pricing</tspan>
          <tspan x="0" dy="28">and certified, background-checked technicians.</tspan>
        </text>'''
    )
])

# 2. svgs/home/06-emergency-cta.svg
update_file('svgs/home/06-emergency-cta.svg', [
    (
'''      <text x="0" y="80" fill="#CBD5E1" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
        <tspan x="0" dy="0">Our emergency HVAC team is on call 24 hours a day when you need urgent heating or cooling service.</tspan>
        <tspan x="0" dy="26">Fully stocked service trucks arrive ready to diagnose and repair on the first visit.</tspan>
      </text>''',
'''      <text x="0" y="76" fill="#CBD5E1" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
        <tspan x="0" dy="0">Our emergency HVAC team is on standby 24 hours a day</tspan>
        <tspan x="0" dy="26">for urgent furnace failures, AC breakdowns, and leaks.</tspan>
        <tspan x="0" dy="26">Fully stocked service trucks arrive ready to diagnose</tspan>
        <tspan x="0" dy="26">and repair issues on the very first visit.</tspan>
      </text>'''
    )
])

# 3. svgs/home/07-why-choose-us.svg
update_file('svgs/home/07-why-choose-us.svg', [
    (
'''          <text x="0" y="68" fill="#475569" font-family="'Inter', sans-serif" font-size="14" font-weight="400">
            <tspan x="0" dy="0">Skilled, licensed trade professionals</tspan>
            <tspan x="0" dy="22">focused on accurate diagnosis and long-lasting</tspan>
            <tspan x="0" dy="22">equipment workmanship.</tspan>
          </text>''',
'''          <text x="0" y="68" fill="#475569" font-family="'Inter', sans-serif" font-size="14" font-weight="400">
            <tspan x="0" dy="0">Skilled, certified professionals</tspan>
            <tspan x="0" dy="22">focused on precision diagnosis</tspan>
            <tspan x="0" dy="22">and durable trade workmanship.</tspan>
          </text>'''
    ),
    (
'''          <text x="0" y="68" fill="#475569" font-family="'Inter', sans-serif" font-size="14" font-weight="400">
            <tspan x="0" dy="0">Understand your repair vs. replacement</tspan>
            <tspan x="0" dy="22">options clearly before committing to any</tspan>
            <tspan x="0" dy="22">equipment decision.</tspan>
          </text>''',
'''          <text x="0" y="68" fill="#475569" font-family="'Inter', sans-serif" font-size="14" font-weight="400">
            <tspan x="0" dy="0">Clear repair vs. replacement</tspan>
            <tspan x="0" dy="22">options explained before you</tspan>
            <tspan x="0" dy="22">commit to any work.</tspan>
          </text>'''
    ),
    (
'''          <text x="0" y="68" fill="#475569" font-family="'Inter', sans-serif" font-size="14" font-weight="400">
            <tspan x="0" dy="0">No surprises or hidden fees. We explain the</tspan>
            <tspan x="0" dy="22">exact scope of work and pricing upfront before</tspan>
            <tspan x="0" dy="22">any wrench turns.</tspan>
          </text>''',
'''          <text x="0" y="68" fill="#475569" font-family="'Inter', sans-serif" font-size="14" font-weight="400">
            <tspan x="0" dy="0">Upfront, flat-rate pricing with</tspan>
            <tspan x="0" dy="22">zero hidden fees or surprise</tspan>
            <tspan x="0" dy="22">charges before work starts.</tspan>
          </text>'''
    ),
    (
'''          <text x="0" y="68" fill="#475569" font-family="'Inter', sans-serif" font-size="14" font-weight="400">
            <tspan x="0" dy="0">High-efficiency systems designed around</tspan>
            <tspan x="0" dy="22">indoor reliability, low electrical utility bills,</tspan>
            <tspan x="0" dy="22">and maximum lifespan.</tspan>
          </text>''',
'''          <text x="0" y="68" fill="#475569" font-family="'Inter', sans-serif" font-size="14" font-weight="400">
            <tspan x="0" dy="0">High-efficiency systems sized for</tspan>
            <tspan x="0" dy="22">lower utility bills, quiet run,</tspan>
            <tspan x="0" dy="22">and season-long comfort.</tspan>
          </text>'''
    )
])

# 4. svgs/home/09-service-areas.svg
update_file('svgs/home/09-service-areas.svg', [
    (
'''      <text x="0" y="90" fill="#475569" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
        <tspan x="0" dy="0">Our fleet of fully equipped service vehicles is strategically stationed across</tspan>
        <tspan x="0" dy="26">the metropolitan area to guarantee prompt response times for both routine and emergency calls.</tspan>
      </text>''',
'''      <text x="0" y="90" fill="#475569" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
        <tspan x="0" dy="0">Our fully equipped service vans are strategically stationed</tspan>
        <tspan x="0" dy="26">across the metropolitan area to guarantee fast response</tspan>
        <tspan x="0" dy="26">times for both routine tune-ups and 24/7 emergency calls.</tspan>
      </text>'''
    )
])

# 5. svgs/home/11-financing-promo.svg
update_file('svgs/home/11-financing-promo.svg', [
    (
'''      <text x="0" y="70" fill="#475569" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
        <tspan x="0" dy="0">Explore convenient financing options for qualifying HVAC installations, replacements,</tspan>
        <tspan x="0" dy="26">and major emergency repairs. Keep your household budget predictable and secure.</tspan>
      </text>''',
'''      <text x="0" y="70" fill="#475569" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
        <tspan x="0" dy="0">Explore flexible monthly financing options for qualifying</tspan>
        <tspan x="0" dy="26">central air conditioners, heat pumps, and gas furnaces.</tspan>
        <tspan x="0" dy="26">Keep your household budget predictable and protected.</tspan>
      </text>'''
    )
])

# 6. svgs/home/12-final-cta.svg
update_file('svgs/home/12-final-cta.svg', [
    (
'''      <text x="0" y="80" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
        <tspan x="0" dy="0">Schedule professional HVAC service with NorthStar. Fast appointment windows,</tspan>
        <tspan x="0" dy="26">transparent estimates, and certified technicians ready to restore your peace of mind.</tspan>
      </text>''',
'''      <text x="0" y="80" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
        <tspan x="0" dy="0">Schedule professional HVAC service with NorthStar.</tspan>
        <tspan x="0" dy="26">Convenient arrival windows, transparent estimates, and</tspan>
        <tspan x="0" dy="26">certified technicians ready to restore your comfort.</tspan>
      </text>'''
    )
])

