import sys, glob, re
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

home_files = sorted(glob.glob('svgs/home/[0-9]*.svg'))
for hf in home_files:
    with open(hf, 'r', encoding='utf-8-sig') as f:
        c = f.read()
    
    # Try parsing XML
    try:
        root = ET.fromstring(c)
    except Exception as e:
        print(f"XML Error in {hf}: {e}")
        continue
    
    # Check text lengths
    long_lines = []
    for text_el in root.iter('{http://www.w3.org/2000/svg}text'):
        tspans = list(text_el.iter('{http://www.w3.org/2000/svg}tspan'))
        if tspans:
            for ts in tspans:
                txt = (ts.text or '').strip()
                if len(txt) > 42:
                    long_lines.append(('tspan', len(txt), txt))
        else:
            txt = (text_el.text or '').strip()
            if len(txt) > 42:
                long_lines.append(('text', len(txt), txt))
    
    print(f"=== {hf} ({len(long_lines)} long items) ===")
    for kind, l, t in long_lines:
        print(f"   [{kind}] ({l}): {t}")

