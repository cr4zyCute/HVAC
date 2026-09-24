import os, re

sections = [
    ('01-utility-bar.svg', 44, 'Utility-Bar'),
    ('02-header-nav.svg', 88, 'Header-Nav'),
    ('03-hero.svg', 640, 'Hero-Section'),
    ('04-trust-signals.svg', 120, 'Trust-Signals'),
    ('05-services-grid.svg', 780, 'Services-Grid'),
    ('06-emergency-cta.svg', 320, 'Emergency-CTA'),
    ('07-why-choose-us.svg', 680, 'Why-Choose-Us'),
    ('08-how-it-works.svg', 490, 'How-It-Works'),
    ('09-service-areas.svg', 600, 'Service-Areas'),
    ('10-customer-reviews.svg', 580, 'Customer-Reviews'),
    ('11-financing-promo.svg', 400, 'Financing-Promo'),
    ('12-final-cta.svg', 380, 'Final-CTA'),
    ('13-footer.svg', 440, 'Footer')
]

total_h = sum(h for _, h, _ in sections)
print(f"Total calculated height: {total_h}")

out_lines = []
out_lines.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 ' + str(total_h) + '" width="1440" height="' + str(total_h) + '">')
out_lines.append('  <defs>')
out_lines.append('    <style>')
out_lines.append("      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap');")
out_lines.append('    </style>')
out_lines.append('  </defs>')
out_lines.append('  <rect width="1440" height="' + str(total_h) + '" fill="#FFFFFF"/>')

current_y = 0
for fname, h, label in sections:
    path = os.path.join('svgs', 'home', fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Strip <svg ...> and </svg>
    # Remove xml declaration and defs if any to avoid duplication
    content_clean = re.sub(r'<\?xml[^>]*\?>', '', content)
    # Remove outer <svg ...>
    content_clean = re.sub(r'^\s*<svg[^>]*>', '', content_clean, flags=re.DOTALL)
    # Remove outer </svg>
    content_clean = re.sub(r'</svg>\s*$', '', content_clean, flags=re.DOTALL)
    # Remove any <defs> inside sections as we have top level defs
    content_clean = re.sub(r'<defs>.*?</defs>', '', content_clean, flags=re.DOTALL)
    
    out_lines.append(f'\n  <!-- ==================== SECTION: {label} (Y: {current_y}, H: {h}) ==================== -->')
    out_lines.append(f'  <g id="{label}" transform="translate(0, {current_y})">')
    out_lines.append(content_clean.strip())
    out_lines.append('  </g>')
    
    current_y += h

out_lines.append('</svg>\n')

full_svg = '\n'.join(out_lines)

target_path = 'svgs/pages/00-home-desktop-1440.svg'
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(full_svg)

print(f"Successfully assembled {target_path} (total height: {total_h})")

