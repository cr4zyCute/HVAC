import sys, glob, re

sys.stdout.reconfigure(encoding='utf-8')

home_files = sorted(glob.glob('svgs/home/[0-9]*.svg'))
for hf in home_files:
    with open(hf, 'r', encoding='utf-8-sig') as f:
        c = f.read()
    # Find root svg opening
    svg_open = re.search(r'<svg[^>]*>', c)
    # Find any top comments
    print(f"File: {hf}")
    if svg_open:
        print(f"  SVG tag: {svg_open.group(0)[:80]}...")

