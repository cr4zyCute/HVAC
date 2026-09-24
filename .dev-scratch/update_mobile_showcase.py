import os

fpath = 'svgs/responsive/mobile-390.svg'
with open(fpath, 'r', encoding='utf-8') as f:
    c = f.read()

# Replace mobile actions in mobile-390.svg
old_sub = '''      <!-- Phone Call Trigger -->
      <circle cx="20" cy="20" r="20" fill="#FEF3C7"/>
      <path d="M14 11C14 16 18 20 23 20L25 18C25.3 17.7 25.7 17.6 26.1 17.8L28.7 18.9C29.2 19.1 29.5 19.6 29.5 20.1V23C29.5 23.55 29.05 24 28.5 24C18.01 24 9.5 15.49 9.5 5C9.5 4.45 9.95 4 10.5 4H13.4C13.9 4 14.4 4.3 14.6 4.8L15.7 7.4C15.9 7.8 15.8 8.2 15.5 8.5L13.5 10.5" stroke="#D97706" stroke-width="1.6" stroke-linecap="round"/>

      <!-- Hamburger Menu (48px Touch Target) -->
      <g transform="translate(48, 0)">
        <rect width="40" height="40" rx="8" fill="#F1F5F9"/>
        <line x1="12" y1="14" x2="28" y2="14" stroke="#0F2238" stroke-width="2" stroke-linecap="round"/>
        <line x1="12" y1="20" x2="28" y2="20" stroke="#0F2238" stroke-width="2" stroke-linecap="round"/>
        <line x1="12" y1="26" x2="28" y2="26" stroke="#0F2238" stroke-width="2" stroke-linecap="round"/>
      </g>'''

new_sub = '''      <!-- Phone Call Trigger (Official Lucide Phone) -->
      <rect width="40" height="40" rx="8" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>
      <svg x="10" y="10" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
      </svg>

      <!-- Hamburger Menu (Official Lucide Menu) -->
      <g transform="translate(48, 0)">
        <rect width="40" height="40" rx="8" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"/>
        <svg x="10" y="10" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0F2238" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="4" x2="20" y1="12" y2="12"/>
          <line x1="4" x2="20" y1="6" y2="6"/>
          <line x1="4" x2="20" y1="18" y2="18"/>
        </svg>
      </g>'''

if old_sub in c:
    c = c.replace(old_sub, new_sub)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated svgs/responsive/mobile-390.svg successfully!")
else:
    print("Substring not found in mobile-390.svg")

