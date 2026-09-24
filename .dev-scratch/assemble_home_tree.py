import os, sys
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

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

ET.register_namespace('', "http://www.w3.org/2000/svg")

total_h = sum(h for _, h, _ in sections)
print(f"Total calculated height: {total_h}")

# Do NOT pass xmlns in attribs dictionary because register_namespace('', ...) handles it
root = ET.Element('{http://www.w3.org/2000/svg}svg', {
    'viewBox': f"0 0 1440 {total_h}",
    'width': "1440",
    'height': str(total_h)
})

defs = ET.SubElement(root, '{http://www.w3.org/2000/svg}defs')
style = ET.SubElement(defs, '{http://www.w3.org/2000/svg}style')
style.text = "@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');"

bg = ET.SubElement(root, '{http://www.w3.org/2000/svg}rect', {
    'width': "1440",
    'height': str(total_h),
    'fill': "#FFFFFF"
})

current_y = 0
for fname, h, label in sections:
    path = os.path.join('svgs', 'home', fname)
    with open(path, 'r', encoding='utf-8-sig') as f:
        xml_text = f.read()
    
    sec_tree = ET.fromstring(xml_text)
    
    sec_g = ET.SubElement(root, '{http://www.w3.org/2000/svg}g', {
        'id': label,
        'transform': f"translate(0, {current_y})"
    })
    
    for child in sec_tree:
        if child.tag.endswith('defs'):
            continue
        sec_g.append(child)
    
    current_y += h

target_path = 'svgs/pages/00-home-desktop-1440.svg'
tree = ET.ElementTree(root)
ET.indent(tree, space='  ')
tree.write(target_path, encoding='utf-8', xml_declaration=True)

# Test parse
test_tree = ET.parse(target_path)
print(f"SUCCESS: {target_path} is 100% valid XML with root {test_tree.getroot().tag} and height {total_h}!")

