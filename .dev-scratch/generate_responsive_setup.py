import os, sys, base64

sys.stdout.reconfigure(encoding='utf-8')

img_dir = os.path.join(os.getcwd(), 'assets', 'images')
with open(os.path.join(img_dir, 'hero_opt.jpg'), 'rb') as f:
    b64_hero = base64.b64encode(f.read()).decode('ascii')
with open(os.path.join(img_dir, 'furnace_opt.jpg'), 'rb') as f:
    b64_furnace = base64.b64encode(f.read()).decode('ascii')
with open(os.path.join(img_dir, 'van_opt.jpg'), 'rb') as f:
    b64_van = base64.b64encode(f.read()).decode('ascii')

tablet_dir = os.path.join(os.getcwd(), 'svgs', 'responsive', 'tablet')
mobile_dir = os.path.join(os.getcwd(), 'svgs', 'responsive', 'mobile')
os.makedirs(tablet_dir, exist_ok=True)
os.makedirs(mobile_dir, exist_ok=True)

print("Directories prepared. Beginning responsive artboard generation...")

