import re

def update_components():
    with open('svgs/design-system/components-library.svg', 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Card 1
    old_c1 = '''      <text x="24" y="132" fill="#475569" font-family="'Inter', sans-serif" font-size="13" font-weight="400">
        <tspan x="24" dy="0">Standard card used across Home and Services directory.</tspan>
        <tspan x="24" dy="20">Fixed 12px corner radius with subtle 1px border stroke.</tspan>
      </text>'''
    
    new_c1 = '''      <text x="24" y="130" fill="#475569" font-family="'Inter', sans-serif" font-size="13" font-weight="400">
        <tspan x="24" dy="0">Standard card used across Home</tspan>
        <tspan x="24" dy="20">and Services directory pages.</tspan>
        <tspan x="24" dy="20">Fixed 12px radius, 1px border.</tspan>
      </text>'''
    c = c.replace(old_c1, new_c1)

    # Card 2
    old_c2 = '''      <text x="24" y="75" fill="#1E293B" font-family="'Inter', sans-serif" font-size="14" font-weight="400" font-style="italic">
        <tspan x="24" dy="0">"The technician arrived on time, diagnosed the faulty</tspan>
        <tspan x="24" dy="22">capacitor within 15 minutes, and had cold air blowing</tspan>
        <tspan x="24" dy="22">before lunchtime. Upfront pricing with no surprises."</tspan>
      </text>'''
    
    new_c2 = '''      <text x="24" y="75" fill="#1E293B" font-family="'Inter', sans-serif" font-size="13" font-weight="400" font-style="italic">
        <tspan x="24" dy="0">"The technician arrived on time,</tspan>
        <tspan x="24" dy="20">diagnosed the faulty capacitor in</tspan>
        <tspan x="24" dy="20">15 minutes, and had cold air blowing</tspan>
        <tspan x="24" dy="20">fast. Upfront flat-rate pricing."</tspan>
      </text>'''
    c = c.replace(old_c2, new_c2)

    # Card 3
    old_c3 = '''      <text x="24" y="126" fill="#475569" font-family="'Inter', sans-serif" font-size="13" font-weight="400">
        <tspan x="24" dy="0">Numbered container for multi-step onboarding,</tspan>
        <tspan x="24" dy="20">booking milestones, or equipment installation stages.</tspan>
      </text>'''
    
    new_c3 = '''      <text x="24" y="126" fill="#475569" font-family="'Inter', sans-serif" font-size="13" font-weight="400">
        <tspan x="24" dy="0">Numbered container for multi-step</tspan>
        <tspan x="24" dy="20">booking, appointment milestones,</tspan>
        <tspan x="24" dy="20">or HVAC installation stages.</tspan>
      </text>'''
    c = c.replace(old_c3, new_c3)

    # Accordion FAQ (Section 5)
    old_faq = '''        <tspan x="24" dy="0">Yes. Our on-call service vans operate 24 hours a day, 7 days a week including</tspan>
        <tspan x="24" dy="20">holidays for urgent no-cooling, gas leaks, and frozen heating systems.</tspan>'''
    
    new_faq = '''        <tspan x="24" dy="0">Yes. Our on-call service vans operate 24 hours a day, 7 days</tspan>
        <tspan x="24" dy="20">a week for urgent no-cooling, gas odors, and furnace outages.</tspan>'''
    c = c.replace(old_faq, new_faq)

    with open('svgs/design-system/components-library.svg', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated components-library.svg successfully!")

update_components()

