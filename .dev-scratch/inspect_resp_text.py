import sys, re

sys.stdout.reconfigure(encoding='utf-8')

print("=== MOBILE-390 TEXT NODES ===")
with open('svgs/responsive/mobile-390.svg', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', text, re.DOTALL):
    attribs = m.group(1)
    body = re.sub(r'<[^>]+>', ' ', m.group(2)).strip()
    if len(body) > 35:
        print(f"[{len(body):2d}] {body}")

print("\n=== TABLET-834 TEXT NODES ===")
with open('svgs/responsive/tablet-834.svg', 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', text, re.DOTALL):
    attribs = m.group(1)
    body = re.sub(r'<[^>]+>', ' ', m.group(2)).strip()
    if len(body) > 35:
        print(f"[{len(body):2d}] {body}")

