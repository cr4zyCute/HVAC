import re

def regex_replace(path, pattern, replacement):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    if count == 0:
        print(f"FAILED to match pattern in {path}")
    else:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully matched and replaced in {path} ({count} times)")

# 06-emergency-cta.svg
regex_replace(
    'svgs/home/06-emergency-cta.svg',
    r'<text x="0" y="80"[^>]*>\s*<tspan[^>]*>Our emergency HVAC team.*?</text>',
    '''<text x="0" y="76" fill="#CBD5E1" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
        <tspan x="0" dy="0">Our emergency HVAC team is on standby 24 hours a day</tspan>
        <tspan x="0" dy="26">for urgent furnace failures, AC breakdowns, and leaks.</tspan>
        <tspan x="0" dy="26">Fully stocked service trucks arrive ready to diagnose</tspan>
        <tspan x="0" dy="26">and repair issues on the very first visit.</tspan>
      </text>'''
)

# 07-why-choose-us.svg - Benefit 1
regex_replace(
    'svgs/home/07-why-choose-us.svg',
    r'<text x="0" y="68" fill="#475569"[^>]*>\s*<tspan[^>]*>Skilled, background-checked professionals.*?</text>',
    '''<text x="0" y="68" fill="#475569" font-family="'Inter', sans-serif" font-size="14" font-weight="400">
            <tspan x="0" dy="0">Skilled, certified professionals</tspan>
            <tspan x="0" dy="22">focused on precision diagnosis</tspan>
            <tspan x="0" dy="22">and durable trade workmanship.</tspan>
          </text>'''
)

# 09-service-areas.svg
regex_replace(
    'svgs/home/09-service-areas.svg',
    r'<text x="0" y="90"[^>]*>\s*<tspan[^>]*>Our fleet of fully equipped.*?</text>',
    '''<text x="0" y="90" fill="#475569" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
        <tspan x="0" dy="0">Our fully equipped service vans are strategically stationed</tspan>
        <tspan x="0" dy="26">across the metropolitan area to guarantee fast response</tspan>
        <tspan x="0" dy="26">times for both routine tune-ups and 24/7 emergency calls.</tspan>
      </text>'''
)

# 11-financing-promo.svg
regex_replace(
    'svgs/home/11-financing-promo.svg',
    r'<text x="0" y="70"[^>]*>\s*<tspan[^>]*>Explore convenient financing.*?</text>',
    '''<text x="0" y="70" fill="#475569" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
        <tspan x="0" dy="0">Explore flexible monthly financing options for qualifying</tspan>
        <tspan x="0" dy="26">central air conditioners, heat pumps, and gas furnaces.</tspan>
        <tspan x="0" dy="26">Keep your household budget predictable and protected.</tspan>
      </text>'''
)

# 12-final-cta.svg
regex_replace(
    'svgs/home/12-final-cta.svg',
    r'<text x="0" y="80"[^>]*>\s*<tspan[^>]*>Schedule professional HVAC service.*?</text>',
    '''<text x="0" y="80" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
        <tspan x="0" dy="0">Schedule professional HVAC service with NorthStar.</tspan>
        <tspan x="0" dy="26">Convenient arrival windows, transparent estimates, and</tspan>
        <tspan x="0" dy="26">certified technicians ready to restore your comfort.</tspan>
      </text>'''
)

