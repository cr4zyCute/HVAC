import os

pages = {
    'src/pages/index.astro': ('Home', 'Welcome to NorthStar HVAC Services.'),
    'src/pages/services/index.astro': ('Services Directory', 'Complete Heating, Cooling & Maintenance services.'),
    'src/pages/about.astro': ('About NorthStar', 'Local HVAC specialists focused on craftsmanship and upfront pricing.'),
    'src/pages/service-areas.astro': ('Service Areas', 'Serving residential & commercial properties across the metro region.'),
    'src/pages/financing.astro': ('Financing Plans', 'Flexible 0% APR financing options for new HVAC installations.'),
    'src/pages/reviews.astro': ('Customer Reviews', 'Verified homeowner ratings and feedback.'),
    'src/pages/contact.astro': ('Contact Us', 'Get in touch with our 24/7 service coordinators.'),
    'src/pages/book.astro': ('Book a Service Online', 'Schedule a certified technician with upfront flat-rate pricing.'),
    'src/pages/emergency.astro': ('24/7 Emergency HVAC', 'Immediate emergency dispatch across the local territory.'),
    'src/pages/style-guide.astro': ('Design System Style Guide', 'Interactive showcase of all primitive components and states.')
}

for filepath, (title, desc) in pages.items():
    content = f'''---
import Layout from '@/layouts/Layout.astro';
---

<Layout title="{title} — NorthStar HVAC" description="{desc}">
  <main class="py-80 container">
    <div class="max-w-3xl">
      <span class="text-caption font-bold tracking-wider text-brand-accent uppercase">NorthStar HVAC</span>
      <h1 class="text-h1 font-heading font-extrabold text-brand-primary mt-8 mb-16">{title}</h1>
      <p class="text-body text-text-secondary">{desc}</p>
    </div>
  </main>
</Layout>
'''
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {filepath}")

# Dynamic service page template /src/pages/services/[slug].astro
slug_template = '''---
import Layout from '@/layouts/Layout.astro';
import services from '@/content/services.json';

export async function getStaticPaths() {
  return services.map(service => ({
    params: { slug: service.slug },
    props: { service }
  }));
}

const { service } = Astro.props;
---

<Layout title={`${service.title} — NorthStar HVAC`} description={service.shortDescription}>
  <main class="py-80 container">
    <div class="max-w-3xl">
      <span class="text-caption font-bold tracking-wider text-brand-accent uppercase">{service.category}</span>
      <h1 class="text-h1 font-heading font-extrabold text-brand-primary mt-8 mb-16">{service.title}</h1>
      <p class="text-body text-text-secondary">{service.shortDescription}</p>
    </div>
  </main>
</Layout>
'''

with open('src/pages/services/[slug].astro', 'w', encoding='utf-8') as f:
    f.write(slug_template)
print("Created src/pages/services/[slug].astro")

