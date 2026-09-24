import re

for path in ['svgs/responsive/tablet/02-service-detail-tablet-834.svg', 'svgs/responsive/mobile/02-service-detail-mobile-390.svg']:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    print(f"=== {path} ===")
    svg_tag = re.search(r'<svg[^>]+>', c)
    if svg_tag:
        print(" ", svg_tag.group(0)[:100])
    
    # Check section groups
    groups = re.findall(r'<g\s+id="([^"]+)"[^>]*transform="translate\(([^)]+)\)"', c)
    for gid, tr in groups:
        print(f"  Group id={gid:<20} pos={tr}")

