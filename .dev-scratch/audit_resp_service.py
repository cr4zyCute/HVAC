import re

def audit_file(path):
    print(f"==================== {path} ====================")
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # viewBox
    vb = re.search(r'viewBox="([^"]+)"', c)
    print("viewBox:", vb.group(1) if vb else "none")
    
    # find all transforms
    transforms = re.findall(r'<g\s+id="([^"]+)"[^>]*transform="translate\(([^)]+)\)"', c)
    for gid, tr in transforms:
        print(f"  Section: {gid:<25} at {tr}")

audit_file('svgs/responsive/tablet/02-service-detail-tablet-834.svg')
audit_file('svgs/responsive/mobile/02-service-detail-mobile-390.svg')

