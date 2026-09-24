import os, re

target = os.path.join(os.getcwd(), 'prototype', 'index.html')
with open(target, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS for modern badges, status dots, and high-contrast alert callout
extra_css = '''
    /* Modern Status Badges & Linear/Stripe-Style Micro-Tags */
    .status-badge {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 4px 10px;
      border-radius: var(--radius-full);
      font-size: 11px;
      font-weight: 600;
      letter-spacing: 0.03em;
      text-transform: uppercase;
      line-height: 1;
    }
    .status-badge-live {
      background: rgba(16, 185, 129, 0.08);
      border: 1px solid rgba(16, 185, 129, 0.25);
      color: #065F46;
    }
    .status-badge-urgent {
      background: rgba(220, 38, 38, 0.08);
      border: 1px solid rgba(220, 38, 38, 0.25);
      color: #991B1B;
    }
    .status-badge-neutral {
      background: #F8FAFC;
      border: 1px solid var(--color-neutral-border);
      color: var(--color-text-secondary);
      border-radius: var(--radius-sm);
    }
    .status-dot-container {
      position: relative;
      width: 8px;
      height: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .status-dot-core {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background-color: #10B981;
    }
    .status-dot-pulse {
      position: absolute;
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background-color: rgba(16, 185, 129, 0.35);
      animation: pulse-ring 2s infinite ease-in-out;
    }
    .status-dot-urgent .status-dot-core {
      background-color: #DC2626;
    }
    .status-dot-urgent .status-dot-pulse {
      background-color: rgba(220, 38, 38, 0.35);
    }
    @keyframes pulse-ring {
      0% { transform: scale(0.9); opacity: 0.8; }
      50% { transform: scale(1.4); opacity: 0.2; }
      100% { transform: scale(0.9); opacity: 0.8; }
    }

    /* Modernized Utility Badge */
    .utility-badge {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.16);
      color: #F8FAFC;
      padding: 4px 11px;
      border-radius: var(--radius-full);
      font-weight: 600;
      font-size: 11px;
      letter-spacing: 0.4px;
    }
    .utility-badge .live-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background-color: #10B981;
      box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.25);
    }

    /* Modern Emergency Banner */
    .emergency-banner {
      background-color: #0A1829;
      border: 1px solid #1E293B;
      border-left: 4px solid #DC2626;
      border-radius: var(--radius-md);
      padding: 40px;
      color: #FFFFFF;
      box-shadow: var(--shadow-lg);
    }
    .emergency-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(220, 38, 38, 0.15);
      border: 1px solid rgba(220, 38, 38, 0.3);
      color: #FCA5A5;
      padding: 4px 12px;
      border-radius: var(--radius-full);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.5px;
      margin-bottom: 12px;
    }
'''

# Insert extra CSS before </style>
html = html.replace('</style>', extra_css + '\n  </style>')

# 2. Modernize Utility Bar
old_util_badge = '<span class="utility-badge">24/7 RAPID DISPATCH</span>'
new_util_badge = '<span class="utility-badge"><span class="live-dot"></span>24/7 RAPID DISPATCH ACTIVE</span>'
html = html.replace(old_util_badge, new_util_badge)

# 3. Modernize Hero Assurances with Lucide CheckCircle
lucide_check_svg = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/></svg>'
html = html.replace('<span class="assurance-check">&check;</span>', f'<span class="assurance-check">{lucide_check_svg}</span>')

# 4. Modernize Floating Cards on Hero
old_floating_1 = '''        <!-- Floating Badge 1: Dispatch Status -->
        <div class="floating-card-1">
          <div class="pulse-icon">&bull;</div>
          <div>
            <div class="status-label">Technicians On Call</div>
            <div class="status-sub">Avg. Arrival: Under 45 Mins</div>
          </div>
        </div>'''

new_floating_1 = '''        <!-- Floating Badge 1: Dispatch Status (Linear-style live badge) -->
        <div class="floating-card-1">
          <div class="status-dot-container" style="width: 36px; height: 36px; background: rgba(16, 185, 129, 0.1); border-radius: 50%;">
            <span class="status-dot-pulse" style="width: 18px; height: 18px;"></span>
            <span class="status-dot-core" style="width: 8px; height: 8px;"></span>
          </div>
          <div>
            <div class="status-label">Technicians On Call</div>
            <div class="status-sub" style="display: flex; align-items: center; gap: 5px;">
              <span>Priority Metro Dispatch</span> &bull; <span>&lt; 45 Mins</span>
            </div>
          </div>
        </div>'''
html = html.replace(old_floating_1, new_floating_1)

# Floating Card 2 with 5 crisp Lucide gold stars
lucide_star_svg = '<svg width="15" height="15" viewBox="0 0 24 24" fill="#F59E0B" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'
five_stars = f'{lucide_star_svg}{lucide_star_svg}{lucide_star_svg}{lucide_star_svg}{lucide_star_svg}'
html = html.replace('<span class="rating-stars">&starf;&starf;&starf;&starf;&starf;</span>', f'<span class="rating-stars" style="display: inline-flex; gap: 2px;">{five_stars}</span>')

# 5. Modernize Trust Signals with Lucide ShieldCheck, Clock, Award, ThumbsUp
old_trust = '''      <div class="trust-card">
        <div class="trust-icon-box">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
        </div>
        <div>
          <div class="trust-title">Licensed &amp; Insured</div>
          <div class="trust-meta">&bull; Full Liability Coverage</div>
        </div>
      </div>

      <div class="trust-card">
        <div class="trust-icon-box">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
        </div>
        <div>
          <div class="trust-title">24/7 Emergency Service</div>
          <div class="trust-meta" style="color: var(--color-brand-emergency);">&bull; Priority Dispatch Active</div>
        </div>
      </div>

      <div class="trust-card">
        <div class="trust-icon-box">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
        </div>
        <div>
          <div class="trust-title">10+ Years Experience</div>
          <div class="trust-meta">&bull; Senior Master Technicians</div>
        </div>
      </div>

      <div class="trust-card">
        <div class="trust-icon-box">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M8 14s1.5 2 4 2 4-2 4-2"></path><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line></svg>
        </div>
        <div>
          <div class="trust-title">100% Satisfaction Focused</div>
          <div class="trust-meta">&bull; Fixed Right Guarantee</div>
        </div>
      </div>'''

new_trust = '''      <div class="trust-card">
        <div class="trust-icon-box" style="background: rgba(16, 185, 129, 0.08); color: #059669;">
          <!-- Lucide ShieldCheck -->
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/></svg>
        </div>
        <div>
          <div class="trust-title">Licensed &amp; Insured</div>
          <div class="trust-meta" style="color: #059669; font-weight: 600;">&bull; Full Liability Coverage</div>
        </div>
      </div>

      <div class="trust-card">
        <div class="trust-icon-box" style="background: rgba(220, 38, 38, 0.08); color: #DC2626;">
          <!-- Lucide Clock -->
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        </div>
        <div>
          <div class="trust-title">24/7 Emergency Service</div>
          <div class="trust-meta" style="color: var(--color-brand-emergency); font-weight: 600;">&bull; Priority Dispatch Active</div>
        </div>
      </div>

      <div class="trust-card">
        <div class="trust-icon-box" style="background: rgba(15, 34, 56, 0.06); color: var(--color-brand-primary);">
          <!-- Lucide Award -->
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/></svg>
        </div>
        <div>
          <div class="trust-title">10+ Years Experience</div>
          <div class="trust-meta">&bull; Senior Master Technicians</div>
        </div>
      </div>

      <div class="trust-card">
        <div class="trust-icon-box" style="background: rgba(230, 81, 0, 0.08); color: var(--color-brand-accent);">
          <!-- Lucide ThumbsUp -->
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 10v12M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2h0a3.13 3.13 0 0 1 3 3.88Z"/></svg>
        </div>
        <div>
          <div class="trust-title">100% Satisfaction Focused</div>
          <div class="trust-meta">&bull; Fixed Right Guarantee</div>
        </div>
      </div>'''
html = html.replace(old_trust, new_trust)

# 6. Modernize Services Icons with Lucide Snowflake, Layers, Flame, Wrench, Wind, AlertTriangle
lucide_snowflake = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h20M12 2v20M20 16l-4-4 4-4M4 8l4 4-4 4M16 4l-4 4-4-4M8 20l4-4 4 4"/></svg>'
lucide_installation = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>'
lucide_flame = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z"/></svg>'
lucide_wrench = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>'
lucide_wind = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.7 7.7A2.5 2.5 0 1 1 16 12H2M19.7 17.7A2.5 2.5 0 1 0 18 13H2M14.5 4A2.5 2.5 0 0 0 12 6.5V7H2"/></svg>'
lucide_alert = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" x2="12" y1="9" y2="13"/><line x1="12" x2="12.01" y1="17" y2="17"/></svg>'

# Replace service icons
html = re.sub(
    r'<div class="service-icon-box" style="background-color: #EFF6FF; color: #2563EB;">.*?</div>',
    f'<div class="service-icon-box" style="background-color: #EFF6FF; color: #2563EB;">{lucide_snowflake}</div>',
    html, flags=re.DOTALL
)
html = re.sub(
    r'<div class="service-icon-box" style="background-color: #F0FDF4; color: #16A34A;">.*?</div>',
    f'<div class="service-icon-box" style="background-color: #F0FDF4; color: #16A34A;">{lucide_installation}</div>',
    html, flags=re.DOTALL
)
html = re.sub(
    r'<div class="service-icon-box" style="background-color: #FFF7ED; color: #EA580C;">.*?</div>',
    f'<div class="service-icon-box" style="background-color: #FFF7ED; color: #EA580C;">{lucide_flame}</div>',
    html, flags=re.DOTALL
)
html = re.sub(
    r'<div class="service-icon-box" style="background-color: #F8FAFC; color: #0F172A; border: 1px solid var\(--color-neutral-border\);">.*?</div>',
    f'<div class="service-icon-box" style="background-color: #F8FAFC; color: #0F172A; border: 1px solid var(--color-neutral-border);">{lucide_wrench}</div>',
    html, flags=re.DOTALL
)
html = re.sub(
    r'<div class="service-icon-box" style="background-color: #F0FDFA; color: #0D9488;">.*?</div>',
    f'<div class="service-icon-box" style="background-color: #F0FDFA; color: #0D9488;">{lucide_wind}</div>',
    html, flags=re.DOTALL
)
html = re.sub(
    r'<div class="service-icon-box" style="background-color: #FEE2E2; color: #DC2626;">.*?</div>',
    f'<div class="service-icon-box" style="background-color: #FEE2E2; color: #DC2626;">{lucide_alert}</div>',
    html, flags=re.DOTALL
)

# 7. Modernize Why Choose Us Workmanship Checklist
html = html.replace('<span class="check-icon">&check;</span>', f'<span class="check-icon" style="display: inline-flex; align-items: center; justify-content: center; width: 20px; height: 20px; background: rgba(16, 185, 129, 0.2); border-radius: 50%; color: #10B981;">{lucide_check_svg}</span>')

# 8. Modernize Reviews Section Stars
star_row = f'<div style="display: flex; gap: 3px; margin-bottom: 12px;">{five_stars}</div>'
html = html.replace('<div class="review-stars">&starf;&starf;&starf;&starf;&starf;</div>', f'<div class="review-stars">{star_row}</div>')

with open(target, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated prototype/index.html with modern badges, live status dots, and Lucide vector icons!")

