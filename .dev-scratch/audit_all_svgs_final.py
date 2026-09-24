import os, sys, glob, re
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

svg_files = sorted(glob.glob('svgs/**/*.svg', recursive=True))
print(f"Auditing {len(svg_files)} SVG files across workspace...\n")

total_errors = 0
ALLOWED_ENTITIES = {'&amp;', '&lt;', '&gt;', '&quot;', '&apos;'}

for path in svg_files:
    filename = os.path.basename(path)
    
    # 1. XML Parsing
    try:
        tree = ET.parse(path)
        root = tree.getroot()
    except Exception as e:
        print(f"[FAIL XML] {path}: {e}")
        total_errors += 1
        continue
    
    # 2. Raw Entities Check
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    entities = re.findall(r'&[a-zA-Z0-9#]+;', content)
    bad_ents = [e for e in entities if e not in ALLOWED_ENTITIES]
    if bad_ents:
        print(f"[FAIL ENTITY] {filename}: found illegal entities {set(bad_ents)}")
        total_errors += 1

    # 3. Check for text lines inside cards (> 40 chars)
    # Exclude wide full-width page titles/footers
    card_overflows = []
    for t_el in root.iter('{http://www.w3.org/2000/svg}text'):
        # Check if text is inside a card (indicated by font size <= 14 and not a page title/footer)
        fs = t_el.attrib.get('font-size', '14')
        try:
            fs_val = float(re.sub(r'[^\d.]', '', fs))
        except:
            fs_val = 14.0
        
        tspans = list(t_el.iter('{http://www.w3.org/2000/svg}tspan'))
        if tspans:
            for ts in tspans:
                txt = (ts.text or '').strip()
                # If small font (card body) and line > 45 chars
                if fs_val <= 14.0 and len(txt) > 42:
                    card_overflows.append((fs_val, len(txt), txt))
        else:
            txt = (t_el.text or '').strip()
            # If card text without tspan > 42 chars
            if fs_val <= 14.0 and len(txt) > 42:
                # filter out full-width page footers or utility bar
                if not any(k in txt.lower() for k in ['copyright', '©', 'rights reserved', 'fictional', 'serving residential']):
                    card_overflows.append((fs_val, len(txt), txt))
    
    if card_overflows:
        print(f"[WARN OVERFLOW] {filename} has {len(card_overflows)} potential card text overflows:")
        for fs, l, snippet in card_overflows[:5]:
            print(f"    (size {fs}, len {l}): {snippet[:50]}")
    else:
        print(f"[PASS] {filename}")

print(f"\nAudit complete. Total XML/Entity errors: {total_errors}")

