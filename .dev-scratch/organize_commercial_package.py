import os
import shutil

# 1. Desktop SVGs
desktop_src = 'svgs/pages'
desktop_dst = '01-figma-and-svgs/desktop-1440'
desktop_map = {
    '00-home-desktop-1440 1.svg': '00-home.svg',
    '01-services-page 1.svg': '01-services.svg',
    '02-service-detail-page 1.svg': '02-service-detail.svg',
    '03-about-page 1.svg': '03-about.svg',
    '04-service-areas-page 1.svg': '04-service-areas.svg',
    '05-financing-page 1.svg': '05-financing.svg',
    '06-reviews-page 1.svg': '06-reviews.svg',
    '07-contact-page 1.svg': '07-contact.svg',
    '08-book-a-service-page 1.svg': '08-book-a-service.svg',
    '09-emergency-hvac-page 1.svg': '09-emergency-hvac.svg',
}

for src_name, dst_name in desktop_map.items():
    src_file = os.path.join(desktop_src, src_name)
    if os.path.exists(src_file):
        shutil.copy2(src_file, os.path.join(desktop_dst, dst_name))
        print(f"Copied desktop: {src_name} -> {dst_name}")

# 2. Tablet SVGs
tablet_src = 'svgs/responsive/tablet'
tablet_dst = '01-figma-and-svgs/tablet-834'
tablet_map = {
    '00-home-tablet-834.svg': '00-home.svg',
    '01-services-tablet-834.svg': '01-services.svg',
    '02-service-detail-tablet-834.svg': '02-service-detail.svg',
    '03-about-tablet-834.svg': '03-about.svg',
    '04-service-areas-tablet-834.svg': '04-service-areas.svg',
    '05-financing-tablet-834.svg': '05-financing.svg',
    '06-reviews-tablet-834.svg': '06-reviews.svg',
    '07-contact-tablet-834.svg': '07-contact.svg',
    '08-book-a-service-tablet-834.svg': '08-book-a-service.svg',
    '09-emergency-hvac-tablet-834.svg': '09-emergency-hvac.svg',
}

for src_name, dst_name in tablet_map.items():
    src_file = os.path.join(tablet_src, src_name)
    if os.path.exists(src_file):
        shutil.copy2(src_file, os.path.join(tablet_dst, dst_name))
        print(f"Copied tablet: {src_name} -> {dst_name}")

# 3. Mobile SVGs
mobile_src = 'svgs/responsive/mobile'
mobile_dst = '01-figma-and-svgs/mobile-390'
mobile_map = {
    '00-home-mobile-390.svg': '00-home.svg',
    '01-services-mobile-390.svg': '01-services.svg',
    '02-service-detail-mobile-390.svg': '02-service-detail.svg',
    '03-about-mobile-390.svg': '03-about.svg',
    '04-service-areas-mobile-390.svg': '04-service-areas.svg',
    '05-financing-mobile-390.svg': '05-financing.svg',
    '06-reviews-mobile-390.svg': '06-reviews.svg',
    '07-contact-mobile-390.svg': '07-contact.svg',
    '08-book-a-service-mobile-390.svg': '08-book-a-service.svg',
    '09-emergency-hvac-mobile-390.svg': '09-emergency-hvac.svg',
}

for src_name, dst_name in mobile_map.items():
    src_file = os.path.join(mobile_src, src_name)
    if os.path.exists(src_file):
        shutil.copy2(src_file, os.path.join(mobile_dst, dst_name))
        print(f"Copied mobile: {src_name} -> {dst_name}")

# 4. Design System
shutil.copy2('svgs/design-system/components-library.svg', '01-figma-and-svgs/design-system/components-library.svg')
shutil.copy2('figma-design-tokens.json', '01-figma-and-svgs/design-system/figma-design-tokens.json')
print("Copied design system files.")

# 5. Images to HTML template
for img in os.listdir('assets/images'):
    shutil.copy2(os.path.join('assets/images', img), os.path.join('02-html-website-template/assets/images', img))
print("Copied images to template.")
