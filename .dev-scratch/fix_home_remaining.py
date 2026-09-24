import os, re

def replace_exact(file_path, old_str, new_str):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_str not in content:
        print(f"FAILED to find target in {file_path}")
        return False
    content = content.replace(old_str, new_str)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully updated {file_path}")
    return True

# --- 1. svgs/home/06-emergency-cta.svg ---
old_06 = '''      <text x="0" y="112" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
        <tspan x="0" dy="0">Our emergency HVAC team is on call 24 hours a day when you need urgent heating or cooling service.</tspan>
        <tspan x="0" dy="24">Fully stocked service trucks arrive ready to diagnose and repair on the first visit.</tspan>
      </text>'''

new_06 = '''      <text x="0" y="108" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
        <tspan x="0" dy="0">Our emergency HVAC team is on standby 24 hours a day</tspan>
        <tspan x="0" dy="24">for urgent furnace failures, AC breakdowns, and leaks.</tspan>
        <tspan x="0" dy="24">Fully stocked service trucks arrive ready to diagnose</tspan>
        <tspan x="0" dy="24">and restore your heating or cooling on the first visit.</tspan>
      </text>'''
replace_exact('svgs/home/06-emergency-cta.svg', old_06, new_06)

# --- 2. svgs/home/09-service-areas.svg ---
old_09 = '''      <text x="0" y="88" fill="#64748B" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
        <tspan x="0" dy="0">Our fleet of fully equipped service vehicles is strategically stationed across</tspan>
        <tspan x="0" dy="24">the metropolitan area to guarantee prompt response times for both routine and emergency calls.</tspan>
      </text>'''

new_09 = '''      <text x="0" y="88" fill="#64748B" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
        <tspan x="0" dy="0">Our fully equipped service vans are strategically stationed</tspan>
        <tspan x="0" dy="24">across the metro area to guarantee fast response times</tspan>
        <tspan x="0" dy="24">for both routine maintenance and 24/7 emergency calls.</tspan>
      </text>'''
replace_exact('svgs/home/09-service-areas.svg', old_09, new_09)

# --- 3. svgs/home/11-financing-promo.svg ---
old_11 = '''        <text x="0" y="112" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
          <tspan x="0" dy="0">Explore convenient financing options for qualifying HVAC installations, replacements,</tspan>
          <tspan x="0" dy="24">and major emergency repairs. Keep your household budget predictable and secure.</tspan>
        </text>'''

new_11 = '''        <text x="0" y="108" fill="#94A3B8" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
          <tspan x="0" dy="0">Explore flexible monthly financing options for qualifying</tspan>
          <tspan x="0" dy="24">central air conditioners, heat pumps, and gas furnaces.</tspan>
          <tspan x="0" dy="24">Keep your household budget predictable and protected.</tspan>
        </text>'''
replace_exact('svgs/home/11-financing-promo.svg', old_11, new_11)

# --- 4. svgs/home/12-final-cta.svg ---
old_12 = '''        <text x="0" y="104" fill="#475569" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
          <tspan x="0" dy="0">Schedule professional HVAC service with NorthStar. Fast appointment windows,</tspan>
          <tspan x="0" dy="24">transparent estimates, and certified technicians ready to restore your peace of mind.</tspan>
        </text>'''

new_12 = '''        <text x="0" y="100" fill="#475569" font-family="'Inter', sans-serif" font-size="16" font-weight="400">
          <tspan x="0" dy="0">Schedule professional HVAC service with NorthStar.</tspan>
          <tspan x="0" dy="24">Convenient arrival windows, transparent estimates, and</tspan>
          <tspan x="0" dy="24">certified technicians ready to restore your home comfort.</tspan>
        </text>'''
replace_exact('svgs/home/12-final-cta.svg', old_12, new_12)

