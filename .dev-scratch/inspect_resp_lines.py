import sys, re

sys.stdout.reconfigure(encoding='utf-8')

for fn in ['svgs/responsive/mobile-390.svg', 'svgs/responsive/tablet-834.svg']:
    print(f"\n=================== {fn} ===================")
    with open(fn, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if any(w in line for w in ['Technicians on call', 'Accurate testing', 'Fast diagnostics', 'High-efficiency central', 'Gas furnace ignition', 'Seasonal 24-point', 'Our emergency HVAC team']):
            for j in range(max(0, i-2), min(len(lines), i+4)):
                print(f"{j+1}: {lines[j]}", end='')

