import re

with open('svgs/pages/02-service-detail-page 1.svg', 'r', encoding='utf-8') as f:
    c = f.read()

matches = list(re.finditer(r'<path\s+d="([^"]+)"(.*?)/?>', c))
print(f"Total path elements: {len(matches)}")
for i in range(135, len(matches)):
    m = matches[i]
    print(f"Path {i}: attrs={m.group(2)[:80]}")

# Also let's check what is in svgs/home/13-footer.svg
with open('svgs/home/13-footer.svg', 'r', encoding='utf-8') as f:
    footer = f.read()
print(f"Home footer length: {len(footer)}, has text: {'<text' in footer}")

