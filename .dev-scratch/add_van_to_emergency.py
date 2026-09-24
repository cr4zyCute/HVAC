import os

# 1. Update tablet emergency generator
tablet_script = 'scratch/generate_tablet_all.py'
with open(tablet_script, 'r', encoding='utf-8') as f:
    t_code = f.read()

old_t09 = "{th.tablet_footer(800)}'''"
new_t09 = '''  <!-- Emergency Fleet Service Van Banner -->
  <g id="Fleet-Van-Banner" transform="translate(32, 790)">
    <defs>
      <clipPath id="t-van-clip"><rect width="770" height="220" rx="10"/></clipPath>
      <linearGradient id="t-van-grad" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#0F2238" stop-opacity="0.1"/>
        <stop offset="60%" stop-color="#0F2238" stop-opacity="0.85"/>
        <stop offset="100%" stop-color="#0F2238" stop-opacity="0.96"/>
      </linearGradient>
    </defs>
    <rect width="770" height="220" rx="10" fill="#0F2238"/>
    <image href="data:image/jpeg;base64,{b64_van}" width="770" height="220" preserveAspectRatio="xMidYMid slice" clip-path="url(#t-van-clip)"/>
    <rect width="770" height="220" rx="10" fill="url(#t-van-grad)" clip-path="url(#t-van-clip)"/>
    <g transform="translate(32, 130)">
      <text x="0" y="24" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="20" font-weight="800">Mobile Diagnostic Fleet • Dispatched Under 45 Mins</text>
      <text x="0" y="52" fill="#E2E8F0" font-family="'Inter', sans-serif" font-size="13">Every emergency van carries universal capacitors, contactors, motors, ignitors &amp; refrigerants for single-visit resolution.</text>
    </g>
  </g>

{th.tablet_footer(1050)}\'\'\''''

if old_t09 in t_code:
    t_code = t_code.replace(old_t09, new_t09).replace("wrap_svg(s09, 1140)", "wrap_svg(s09, 1390)")
    with open(tablet_script, 'w', encoding='utf-8') as f:
        f.write(t_code)
    print("Updated tablet emergency generator.")
else:
    print("old_t09 pattern not found in tablet script.")

# 2. Update mobile emergency generator
mobile_script = 'scratch/generate_mobile_all.py'
with open(mobile_script, 'r', encoding='utf-8') as f:
    m_code = f.read()

old_m09 = "{mh.mobile_footer(740)}'''"
new_m09 = '''  <!-- Fleet Mobile Dispatch Card -->
  <g id="Fleet-Van-Card" transform="translate(16, 760)">
    <defs>
      <clipPath id="m-van-clip"><rect width="358" height="190" rx="10"/></clipPath>
      <linearGradient id="m-van-grad" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0%" stop-color="#0F2238" stop-opacity="0.1"/>
        <stop offset="60%" stop-color="#0F2238" stop-opacity="0.85"/>
        <stop offset="100%" stop-color="#0F2238" stop-opacity="0.96"/>
      </linearGradient>
    </defs>
    <rect width="358" height="190" rx="10" fill="#0F2238"/>
    <image href="data:image/jpeg;base64,{b64_van}" width="358" height="190" preserveAspectRatio="xMidYMid slice" clip-path="url(#m-van-clip)"/>
    <rect width="358" height="190" rx="10" fill="url(#m-van-grad)" clip-path="url(#m-van-clip)"/>
    <g transform="translate(16, 120)">
      <text x="0" y="18" fill="#FFFFFF" font-family="'Plus Jakarta Sans', sans-serif" font-size="15" font-weight="800">Mobile Diagnostic Fleet</text>
      <text x="0" y="38" fill="#F1F5F9" font-family="'Inter', sans-serif" font-size="11">Fully stocked with OEM parts for single-visit fixes</text>
    </g>
  </g>

{mh.mobile_footer(980)}\'\'\''''

if old_m09 in m_code:
    m_code = m_code.replace(old_m09, new_m09).replace("wrap(m09, 1120)", "wrap(m09, 1360)")
    with open(mobile_script, 'w', encoding='utf-8') as f:
        f.write(m_code)
    print("Updated mobile emergency generator.")
else:
    print("old_m09 pattern not found in mobile script.")

