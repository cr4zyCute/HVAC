import os, sys, base64
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

images = [
    ('hero-technician-ac.jpg', (1000, 750), 'hero_opt.jpg'),
    ('technician-furnace-inspection.jpg', (900, 675), 'furnace_opt.jpg'),
    ('emergency-service-van.jpg', (900, 675), 'van_opt.jpg')
]

img_dir = os.path.join(os.getcwd(), 'assets', 'images')

for src, size, opt_name in images:
    src_p = os.path.join(img_dir, src)
    dst_p = os.path.join(img_dir, opt_name)
    im = Image.open(src_p)
    im.thumbnail(size, Image.Resampling.LANCZOS)
    im.save(dst_p, 'JPEG', quality=82, optimize=True)
    size_kb = os.path.getsize(dst_p) / 1024
    print(f"Created {opt_name}: {im.size} ({size_kb:.1f} KB)")

