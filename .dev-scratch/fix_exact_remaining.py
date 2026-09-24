import re, sys

def replace_exact(file_path, old_str, new_str):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_str not in content:
        print(f"FAILED in {file_path}")
        return False
    content = content.replace(old_str, new_str)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"SUCCESS in {file_path}")
    return True

# 1. 07-contact-page.svg
old_07 = '''        <text x="0" y="60" fill="#047857" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="0" dy="0">Confirmation sent to your inbox. An on-call NorthStar service technician</tspan>
          <tspan x="0" dy="20">will telephone you shortly to confirm your scheduled time slot.</tspan>
        </text>'''

new_07 = '''        <text x="0" y="60" fill="#047857" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="0" dy="0">Confirmation sent to your inbox. An on-call NorthStar</tspan>
          <tspan x="0" dy="20">coordinator will call to confirm your appointment window.</tspan>
        </text>'''
replace_exact('svgs/pages/07-contact-page.svg', old_07, new_07)

# 2. mobile-390.svg
old_mob_1 = '''      <text x="0" y="48" fill="#FEE2E2" font-family="'Inter', sans-serif" font-size="13">
        Technicians on call across the metro area right now.
      </text>'''

new_mob_1 = '''      <text x="0" y="46" fill="#FEE2E2" font-family="'Inter', sans-serif" font-size="13">
        <tspan x="0" dy="0">Certified technicians on call</tspan>
        <tspan x="0" dy="20">across the metro region right now.</tspan>
      </text>'''
replace_exact('svgs/responsive/mobile-390.svg', old_mob_1, new_mob_1)

old_mob_2 = '''        <text x="14" y="62" fill="#475569" font-family="'Inter', sans-serif" font-size="12">Accurate testing with upfront flat-rate pricing.</text>'''

new_mob_2 = '''        <text x="14" y="58" fill="#475569" font-family="'Inter', sans-serif" font-size="12">
          <tspan x="14" dy="0">Accurate testing with upfront</tspan>
          <tspan x="14" dy="18">flat-rate pricing guaranteed.</tspan>
        </text>'''
replace_exact('svgs/responsive/mobile-390.svg', old_mob_2, new_mob_2)

# 3. tablet-834.svg
old_tab_1 = '''        <text x="20" y="80" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          Fast diagnostics for warm air, weird noises, and refrigerant leaks.
        </text>'''

new_tab_1 = '''        <text x="20" y="76" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Fast diagnostics for warm air,</tspan>
          <tspan x="20" dy="20">strange noises, and refrigerant leaks.</tspan>
        </text>'''
replace_exact('svgs/responsive/tablet-834.svg', old_tab_1, new_tab_1)

old_tab_2 = '''        <text x="20" y="80" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          High-efficiency central AC and heat pumps sized for peak savings.
        </text>'''

new_tab_2 = '''        <text x="20" y="76" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">High-efficiency central AC and</tspan>
          <tspan x="20" dy="20">heat pumps sized for peak savings.</tspan>
        </text>'''
replace_exact('svgs/responsive/tablet-834.svg', old_tab_2, new_tab_2)

old_tab_3 = '''        <text x="20" y="80" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          Gas furnace ignition fixes and cold-climate heat pump diagnostics.
        </text>'''

new_tab_3 = '''        <text x="20" y="76" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Gas furnace ignition fixes and</tspan>
          <tspan x="20" dy="20">cold-climate heat pump diagnostics.</tspan>
        </text>'''
replace_exact('svgs/responsive/tablet-834.svg', old_tab_3, new_tab_3)

old_tab_4 = '''        <text x="20" y="80" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          Seasonal 24-point tune-up keeping power bills low and systems safe.
        </text>'''

new_tab_4 = '''        <text x="20" y="76" fill="#475569" font-family="'Inter', sans-serif" font-size="13">
          <tspan x="20" dy="0">Seasonal 24-point tune-ups keeping</tspan>
          <tspan x="20" dy="20">power bills low and systems safe.</tspan>
        </text>'''
replace_exact('svgs/responsive/tablet-834.svg', old_tab_4, new_tab_4)

old_tab_5 = '''      <text x="0" y="54" fill="#FEE2E2" font-family="'Inter', sans-serif" font-size="14">
        Our emergency HVAC team is on call 24 hours a day with local van dispatch.
      </text>'''

new_tab_5 = '''      <text x="0" y="52" fill="#FEE2E2" font-family="'Inter', sans-serif" font-size="14">
        <tspan x="0" dy="0">Our emergency HVAC team is on call 24 hours a day</tspan>
        <tspan x="0" dy="22">with local service van radio dispatch.</tspan>
      </text>'''
replace_exact('svgs/responsive/tablet-834.svg', old_tab_5, new_tab_5)

