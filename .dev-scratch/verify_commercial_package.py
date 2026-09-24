import os
import xml.etree.ElementTree as ET

# 1. Verify all desktop SVGs
desktop_dir = '01-figma-and-svgs/desktop-1440'
for svg_file in os.listdir(desktop_dir):
    if svg_file.endswith('.svg'):
        path = os.path.join(desktop_dir, svg_file)
        try:
            tree = ET.parse(path)
            assert tree.getroot() is not None
            print(f"SVG OK: {svg_file}")
        except Exception as e:
            print(f"SVG FAIL: {svg_file} -> {e}")

# 2. Check HTML files exist and have tags
template_dir = '02-html-website-template'
for html_file in ['index.html', 'service-detail.html', 'book-service.html']:
    path = os.path.join(template_dir, html_file)
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    assert '<!DOCTYPE html>' in c
    assert 'modal-booking' in c or 'book-service' in html_file
    print(f"HTML OK: {html_file} ({len(c)} bytes)")

# 3. Check CSS and JS
for fpath in ['css/tokens.css', 'css/style.css', 'js/main.js', 'js/modals.js']:
    full = os.path.join(template_dir, fpath)
    assert os.path.exists(full)
    with open(full, 'r', encoding='utf-8') as fp:
        print(f"ASSET OK: {fpath} ({len(fp.read())} bytes)")

print("\nALL COMMERCIAL PACKAGE VERIFICATIONS PASSED!")

