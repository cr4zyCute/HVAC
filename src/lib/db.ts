import { createClient } from '@libsql/client';
import bcrypt from 'bcryptjs';

const dbUrl = process.env.DATABASE_URL || 'file:northstar.db';
const dbAuthToken = process.env.DATABASE_AUTH_TOKEN || undefined;

export const db = createClient({
  url: dbUrl,
  authToken: dbAuthToken,
});

let isInitialized = false;

export async function ensureDbInitialized() {
  if (isInitialized) return;

  // 1. Create base tables
  await db.batch([
    // Users table
    `CREATE TABLE IF NOT EXISTS users (
      id TEXT PRIMARY KEY,
      email TEXT UNIQUE NOT NULL,
      password_hash TEXT NOT NULL,
      role TEXT NOT NULL CHECK(role IN ('owner', 'staff')),
      name TEXT NOT NULL,
      failed_login_attempts INTEGER NOT NULL DEFAULT 0,
      locked_until TEXT NULL,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL
    )`,

    // Sessions table
    `CREATE TABLE IF NOT EXISTS sessions (
      id TEXT PRIMARY KEY,
      user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
      expires_at TEXT NOT NULL,
      created_at TEXT NOT NULL
    )`,

    // Password reset tokens table
    `CREATE TABLE IF NOT EXISTS password_reset_tokens (
      id TEXT PRIMARY KEY,
      user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
      token_hash TEXT NOT NULL UNIQUE,
      expires_at TEXT NOT NULL,
      used INTEGER NOT NULL DEFAULT 0,
      created_at TEXT NOT NULL
    )`,

    // Services table
    `CREATE TABLE IF NOT EXISTS services (
      id TEXT PRIMARY KEY,
      slug TEXT UNIQUE NOT NULL,
      title TEXT NOT NULL,
      short_desc TEXT NOT NULL,
      full_desc TEXT NOT NULL,
      starting_price REAL NOT NULL,
      features_json TEXT NOT NULL DEFAULT '[]',
      is_active INTEGER NOT NULL DEFAULT 1,
      display_order INTEGER NOT NULL DEFAULT 0,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL
    )`,

    // Reviews table
    `CREATE TABLE IF NOT EXISTS reviews (
      id TEXT PRIMARY KEY,
      author_name TEXT NOT NULL,
      author_location TEXT NOT NULL,
      rating INTEGER NOT NULL CHECK(rating >= 1 AND rating <= 5),
      service_type TEXT NOT NULL,
      content TEXT NOT NULL,
      is_approved INTEGER NOT NULL DEFAULT 0,
      is_featured INTEGER NOT NULL DEFAULT 0,
      source TEXT NOT NULL DEFAULT 'Google',
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL
    )`,

    // Booking & contact submissions
    `CREATE TABLE IF NOT EXISTS booking_submissions (
      id TEXT PRIMARY KEY,
      customer_name TEXT NOT NULL,
      customer_email TEXT NOT NULL,
      customer_phone TEXT NOT NULL,
      service_requested TEXT NOT NULL,
      preferred_date TEXT NOT NULL,
      preferred_time TEXT NOT NULL,
      urgency TEXT NOT NULL DEFAULT 'standard',
      message TEXT,
      status TEXT NOT NULL DEFAULT 'new' CHECK(status IN ('new', 'contacted', 'scheduled', 'completed', 'cancelled')),
      notes TEXT,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL
    )`,

    // Site settings
    `CREATE TABLE IF NOT EXISTS site_settings (
      key TEXT PRIMARY KEY,
      value TEXT NOT NULL,
      category TEXT NOT NULL DEFAULT 'general',
      updated_at TEXT NOT NULL
    )`,

    // Audit logs
    `CREATE TABLE IF NOT EXISTS audit_logs (
      id TEXT PRIMARY KEY,
      user_id TEXT REFERENCES users(id) ON DELETE SET NULL,
      action TEXT NOT NULL,
      entity_type TEXT NOT NULL,
      entity_id TEXT,
      details_json TEXT,
      ip_address TEXT,
      created_at TEXT NOT NULL
    )`,

    // Homepage sections CMS table
    `CREATE TABLE IF NOT EXISTS homepage_sections (
      id TEXT PRIMARY KEY,
      section_key TEXT UNIQUE NOT NULL,
      title TEXT NOT NULL,
      subtitle TEXT,
      badge TEXT,
      description TEXT,
      image_url TEXT,
      image_alt TEXT,
      primary_btn_text TEXT,
      primary_btn_url TEXT,
      secondary_btn_text TEXT,
      secondary_btn_url TEXT,
      extra_data_json TEXT,
      is_enabled INTEGER NOT NULL DEFAULT 1,
      display_order INTEGER NOT NULL DEFAULT 0,
      updated_at TEXT NOT NULL
    )`,

    // Media library table
    `CREATE TABLE IF NOT EXISTS media (
      id TEXT PRIMARY KEY,
      file_name TEXT NOT NULL,
      url TEXT NOT NULL,
      mime_type TEXT NOT NULL,
      file_size INTEGER NOT NULL,
      alt_text TEXT,
      width INTEGER,
      height INTEGER,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL
    )`,

    // Navigation items table
    `CREATE TABLE IF NOT EXISTS navigation_items (
      id TEXT PRIMARY KEY,
      label TEXT NOT NULL,
      href TEXT NOT NULL,
      position TEXT NOT NULL DEFAULT 'header',
      display_order INTEGER NOT NULL DEFAULT 0,
      is_enabled INTEGER NOT NULL DEFAULT 1,
      created_at TEXT NOT NULL,
      updated_at TEXT NOT NULL
    )`
  ], 'write');

  // 2. Safe migrations for existing services table (add columns if missing)
  const serviceColumnsRes = await db.execute('PRAGMA table_info(services)');
  const existingColNames = new Set(serviceColumnsRes.rows.map(r => r.name as string));

  if (!existingColNames.has('image_url')) {
    await db.execute('ALTER TABLE services ADD COLUMN image_url TEXT').catch(() => {});
  }
  if (!existingColNames.has('cta_text')) {
    await db.execute('ALTER TABLE services ADD COLUMN cta_text TEXT').catch(() => {});
  }
  if (!existingColNames.has('cta_url')) {
    await db.execute('ALTER TABLE services ADD COLUMN cta_url TEXT').catch(() => {});
  }
  if (!existingColNames.has('seo_title')) {
    await db.execute('ALTER TABLE services ADD COLUMN seo_title TEXT').catch(() => {});
  }
  if (!existingColNames.has('seo_description')) {
    await db.execute('ALTER TABLE services ADD COLUMN seo_description TEXT').catch(() => {});
  }
  if (!existingColNames.has('faqs_json')) {
    await db.execute("ALTER TABLE services ADD COLUMN faqs_json TEXT DEFAULT '[]'").catch(() => {});
  }

  // 3. Seed default owner account if not present
  const existingOwner = await db.execute({
    sql: 'SELECT id FROM users WHERE email = ? LIMIT 1',
    args: ['admin@northstarhvac.com']
  });

  const now = new Date().toISOString();

  if (existingOwner.rows.length === 0) {
    const saltRounds = 12;
    const defaultPassword = process.env.ADMIN_INITIAL_PASSWORD || 'NorthStarAdmin2026!';
    const passwordHash = await bcrypt.hash(defaultPassword, saltRounds);

    await db.execute({
      sql: `INSERT INTO users (id, email, password_hash, role, name, failed_login_attempts, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, 0, ?, ?)`,
      args: ['usr_owner_default', 'admin@northstarhvac.com', passwordHash, 'owner', 'NorthStar Admin', now, now]
    });
  }

  // 4. Seed site_settings if missing key values
  const defaultSettings = [
    ['company_name', 'NorthStar Heating & Air Conditioning', 'company'],
    ['brand_first', 'NorthStar', 'company'],
    ['brand_accent', 'HVAC', 'company'],
    ['tagline', 'Comfort You Can Count On', 'company'],
    ['description', 'Comfort You Can Count On. Licensed, insured, and certified technicians delivering precision heating, cooling repairs, and upfront flat-rate pricing.', 'company'],
    ['license_number', 'MN HVAC License #HV-89421-B', 'company'],
    ['phone_primary', '(555) 014-7824', 'contact'],
    ['phone_raw', '5550147824', 'contact'],
    ['emergency_phone', '(555) 014-7824', 'contact'],
    ['email_primary', 'dispatch@northstarhvac.example', 'contact'],
    ['address', '742 Evergreen Terrace, Minneapolis, MN 55401', 'contact'],
    ['operating_hours', 'Open 24 Hours / 7 Days a Week', 'operations'],
    ['emergency_hours', '24/7 Available for Heating & Cooling Emergencies', 'operations'],
    ['service_area', 'Minneapolis, St. Paul & Twin Cities Metro', 'operations'],
    ['dispatch_notice', 'Serving Residential & Light Commercial Across Metro Region', 'operations'],
    ['booking_url', '/book', 'contact'],
    ['social_facebook', 'https://facebook.com', 'social'],
    ['social_instagram', 'https://instagram.com', 'social'],
    ['social_linkedin', 'https://linkedin.com', 'social'],
    ['social_twitter', 'https://twitter.com', 'social'],
    ['social_youtube', 'https://youtube.com', 'social'],
    ['header_cta_text', 'Book a Service', 'navigation'],
    ['header_cta_url', '/book', 'navigation'],
    ['footer_copyright', 'NorthStar HVAC Services. All rights reserved.', 'footer']
  ];

  for (const [key, value, category] of defaultSettings) {
    const exists = await db.execute({
      sql: 'SELECT key FROM site_settings WHERE key = ? LIMIT 1',
      args: [key]
    });
    if (exists.rows.length === 0) {
      await db.execute({
        sql: 'INSERT INTO site_settings (key, value, category, updated_at) VALUES (?, ?, ?, ?)',
        args: [key, value, category, now]
      });
    }
  }

  // 5. Seed default services if empty
  const serviceCheck = await db.execute('SELECT COUNT(*) as count FROM services');
  if (Number(serviceCheck.rows[0]?.count || 0) === 0) {
    await db.batch([
      {
        sql: `INSERT INTO services (id, slug, title, short_desc, full_desc, starting_price, features_json, image_url, cta_text, cta_url, is_active, display_order, created_at, updated_at)
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, 1, ?, ?)`,
        args: [
          'srv_ac_repair',
          'air-conditioning-repair',
          'Air Conditioning Repair & Installation',
          'Rapid diagnostics, precision refrigerant charging, and certified heat pump/AC installations.',
          'Complete diagnostic and repair service for all central AC models, heat pumps, and ductless mini-splits. Includes seasonal refrigerant leak detection, compressor maintenance, and full replacements backed by 10-year parts & labor warranties.',
          89.00,
          JSON.stringify(['24/7 Emergency AC repair', 'NATE-certified technicians', 'Same-day diagnostic response', '10-year parts & labor warranty']),
          '/images/hero-technician-ac.jpg',
          'Book AC Service',
          '/book',
          now,
          now
        ]
      },
      {
        sql: `INSERT INTO services (id, slug, title, short_desc, full_desc, starting_price, features_json, image_url, cta_text, cta_url, is_active, display_order, created_at, updated_at)
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, 2, ?, ?)`,
        args: [
          'srv_furnace_heat',
          'heating-furnace-service',
          'Furnace Repair & Heating Systems',
          'High-efficiency furnace tune-ups, heat exchangers inspection, and winter emergency service.',
          'High-performance heating care to keep your Twin Cities home safe and warm during severe sub-zero weather. Comprehensive 21-point safety inspection, carbon monoxide checks, burner calibration, and high-efficiency furnace upgrades.',
          79.00,
          JSON.stringify(['21-point furnace tune-up', 'Heat exchanger crack detection', 'Emergency no-heat priority', 'Energy-star high-efficiency units']),
          '/images/technician-furnace-inspection.jpg',
          'Book Heating Service',
          '/book',
          now,
          now
        ]
      },
      {
        sql: `INSERT INTO services (id, slug, title, short_desc, full_desc, starting_price, features_json, image_url, cta_text, cta_url, is_active, display_order, created_at, updated_at)
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, 3, ?, ?)`,
        args: [
          'srv_maintenance_plan',
          'annual-maintenance-plan',
          'NorthStar Shield™ Maintenance Club',
          'Bi-annual preventative tune-ups, zero diagnostic fees, and 15% discount on all repairs.',
          'Our signature NorthStar Shield membership ensures seasonal peak performance, lowers electric & gas utility costs, and extends HVAC equipment lifespan with guaranteed VIP appointment booking.',
          14.99,
          JSON.stringify(['Bi-annual seasonal tune-ups', '$0 diagnostic trip fees', '15% discount on all repairs', 'Priority queue during weather peaks']),
          '/images/emergency-service-van.jpg',
          'Join Shield Club',
          '/book',
          now,
          now
        ]
      }
    ], 'write');
  }

  // 6. Seed default reviews if empty
  const reviewCheck = await db.execute('SELECT COUNT(*) as count FROM reviews');
  if (Number(reviewCheck.rows[0]?.count || 0) === 0) {
    await db.batch([
      {
        sql: `INSERT INTO reviews (id, author_name, author_location, rating, service_type, content, is_approved, is_featured, source, created_at, updated_at)
              VALUES (?, ?, ?, 5, ?, ?, 1, 1, 'Google', ?, ?)`,
        args: [
          'rev_marcus_k',
          'Marcus K.',
          'Minneapolis, MN',
          'Furnace Emergency Repair',
          'Our furnace stopped blowing warm air on the coldest night of January (-12°F). Dave from NorthStar was at our house in under 45 minutes, replaced the igniter and flame sensor, and tested the CO levels before leaving. Lifesavers!',
          now,
          now
        ]
      },
      {
        sql: `INSERT INTO reviews (id, author_name, author_location, rating, service_type, content, is_approved, is_featured, source, created_at, updated_at)
              VALUES (?, ?, ?, 5, ?, ?, 1, 1, 'Google', ?, ?)`,
        args: [
          'rev_sarah_p',
          'Sarah & David P.',
          'Edina, MN',
          'Heat Pump & AC Replacement',
          'Replaced our 18-year-old AC unit with a dual-fuel heat pump system. The crew covered our hardwood floors, finished the entire job in one day, and our summer electric bills dropped by nearly $80/month.',
          now,
          now
        ]
      },
      {
        sql: `INSERT INTO reviews (id, author_name, author_location, rating, service_type, content, is_approved, is_featured, source, created_at, updated_at)
              VALUES (?, ?, ?, 5, ?, ?, 1, 1, 'Google', ?, ?)`,
        args: [
          'rev_brian_l',
          'Brian L.',
          'St. Paul, MN',
          'NorthStar Shield Maintenance',
          'Been on their Shield maintenance plan for 3 years. They catch small capacitor issues before they become $1,000 breakdowns. Polite, clean, and upfront pricing with zero high-pressure sales tactics.',
          now,
          now
        ]
      }
    ], 'write');
  }

  // 7. Seed homepage_sections if empty
  const sectionCheck = await db.execute('SELECT COUNT(*) as count FROM homepage_sections');
  if (Number(sectionCheck.rows[0]?.count || 0) === 0) {
    const sectionsToSeed = [
      {
        id: 'sec_hero',
        section_key: 'hero',
        title: 'Reliable Heating & AC Solutions for Lasting Comfort.',
        subtitle: 'From precision emergency AC repairs to high-efficiency furnace installations, licensed NorthStar technicians deliver transparent flat-rate pricing and respectful service across your neighborhood.',
        badge: 'Fast Same-Day Response Guaranteed',
        description: '',
        image_url: '/images/hero-technician-ac.jpg',
        image_alt: 'Certified NorthStar HVAC technician testing outdoor condensing unit with digital manifold gauges',
        primary_btn_text: 'Schedule Service',
        primary_btn_url: '/book',
        secondary_btn_text: 'Call (555) 014-7824',
        secondary_btn_url: 'tel:5550147824',
        extra_data_json: JSON.stringify({
          rating_score: '4.9 / 5.0 Rating',
          rating_subtext: 'across Google & Yelp',
          trust_card_title: 'Full 90-Day Workmanship Guarantee',
          trust_card_desc: 'Zero hidden trip charges on all diagnostic calls'
        }),
        is_enabled: 1,
        display_order: 1
      },
      {
        id: 'sec_trust_signals',
        section_key: 'trust_signals',
        title: 'Trust Signals Bar',
        subtitle: '',
        badge: '',
        description: '',
        image_url: '',
        image_alt: '',
        primary_btn_text: '',
        primary_btn_url: '',
        secondary_btn_text: '',
        secondary_btn_url: '',
        extra_data_json: JSON.stringify([
          { icon: 'shield', title: 'NATE & EPA Certified', text: 'Rigorous master technician standards' },
          { icon: 'check', title: 'Upfront Flat Pricing', text: 'Written quotes before any work begins' },
          { icon: 'star', title: '4.9★ Rated Locally', text: 'Over 1,200+ verified homeowner reviews' },
          { icon: 'clock', title: '24/7 Live Dispatch', text: 'Average 45-min emergency van response' }
        ]),
        is_enabled: 1,
        display_order: 2
      },
      {
        id: 'sec_services_intro',
        section_key: 'services_intro',
        title: 'Comprehensive HVAC Services',
        subtitle: 'Engineered for high SEER2 energy efficiency, indoor air purity, and year-round indoor comfort.',
        badge: 'PRECISION CLIMATE SOLUTIONS',
        description: '',
        image_url: '',
        image_alt: '',
        primary_btn_text: 'Explore All Services',
        primary_btn_url: '/services',
        secondary_btn_text: '',
        secondary_btn_url: '',
        extra_data_json: '{}',
        is_enabled: 1,
        display_order: 3
      },
      {
        id: 'sec_emergency_cta',
        section_key: 'emergency_cta',
        title: 'HVAC Failure During Extreme Weather?',
        subtitle: 'Our fully stocked mobile service vans are radio-dispatched 24/7 across the metro territory with genuine OEM parts on board.',
        badge: 'URGENT EMERGENCY CALLOUT',
        description: '',
        image_url: '',
        image_alt: '',
        primary_btn_text: 'Emergency Dispatch',
        primary_btn_url: '/emergency',
        secondary_btn_text: 'Call (555) 014-7824',
        secondary_btn_url: 'tel:5550147824',
        extra_data_json: '{}',
        is_enabled: 1,
        display_order: 4
      },
      {
        id: 'sec_why_us',
        section_key: 'why_us',
        title: 'Why Local Homeowners Trust NorthStar',
        subtitle: '',
        badge: 'THE NORTHSTAR STANDARD',
        description: 'We believe you deserve honest heating and cooling craftsmanship without manufactured sales pressure. When you call NorthStar, an experienced technician troubleshoots the root cause, explains your options clearly, and respects your home.',
        image_url: '/images/technician-furnace-inspection.jpg',
        image_alt: 'Licensed HVAC technician performing multi-point furnace combustion safety inspection',
        primary_btn_text: 'Read Our Full Story',
        primary_btn_url: '/about',
        secondary_btn_text: '',
        secondary_btn_url: '',
        extra_data_json: JSON.stringify({
          badge_overlay: 'Clean Drop Cloth & Boot Covers on Every Call',
          features: [
            { title: 'Transparent Flat Pricing', desc: 'We quote all repairs in writing before beginning. No hidden diagnostic surprises.' },
            { title: 'Fully Stocked Service Vans', desc: 'Over 90% of cooling and heating issues fixed on the very first trip.' },
            { title: 'EPA & NATE Certified', desc: 'Work performed by technicians holding national HVAC engineering certifications.' },
            { title: 'Zero Sales Pressure', desc: 'If a repair solves your comfort issue safely, we will never force a premature replacement.' }
          ]
        }),
        is_enabled: 1,
        display_order: 5
      },
      {
        id: 'sec_how_it_works',
        section_key: 'how_it_works',
        title: 'How It Works in 3 Simple Steps',
        subtitle: 'Restoring your home comfort should be straightforward and stress-free.',
        badge: 'SEAMLESS PROCESS',
        description: '',
        image_url: '',
        image_alt: '',
        primary_btn_text: '',
        primary_btn_url: '',
        secondary_btn_text: '',
        secondary_btn_url: '',
        extra_data_json: JSON.stringify([
          { step: 1, title: 'Schedule Online or Call', desc: 'Pick your preferred arrival window through our 60-second booking form or speak directly with our 24/7 dispatcher.', variant: 'primary' },
          { step: 2, title: 'Diagnostic & Upfront Quote', desc: 'Technician conducts digital manifold testing, identifies the problem, and presents a written flat-rate quote before touching any tools.', variant: 'accent' },
          { step: 3, title: 'Precision Fix & Guarantee', desc: 'Repairs are completed with OEM factory parts, load-tested for cooling delta T, and backed by our full 90-day guarantee.', variant: 'success' }
        ]),
        is_enabled: 1,
        display_order: 6
      },
      {
        id: 'sec_service_areas',
        section_key: 'service_areas',
        title: 'Serving Neighborhoods Across the Metro Region',
        subtitle: 'Our radio-dispatched mobile technicians are strategically positioned for 45-minute response times.',
        badge: 'LOCAL COMMUNITY DISPATCH',
        description: '',
        image_url: '',
        image_alt: '',
        primary_btn_text: 'Check Your ZIP Code',
        primary_btn_url: '/service-areas',
        secondary_btn_text: '',
        secondary_btn_url: '',
        extra_data_json: JSON.stringify([
          'Downtown Metro', 'Oak Ridge Estates', 'Westlake Heights',
          'Pine Valley', 'Riverdale Crossing', 'Eastridge Park'
        ]),
        is_enabled: 1,
        display_order: 7
      },
      {
        id: 'sec_reviews_intro',
        section_key: 'reviews_intro',
        title: '5-Star Reputations in Every Neighborhood',
        subtitle: 'Real feedback from local residents who trust NorthStar for honest heating and cooling craftsmanship.',
        badge: 'VERIFIED LOCAL FEEDBACK',
        description: '',
        image_url: '',
        image_alt: '',
        primary_btn_text: 'View All 1,200+ Reviews',
        primary_btn_url: '/reviews',
        secondary_btn_text: '',
        secondary_btn_url: '',
        extra_data_json: '{}',
        is_enabled: 1,
        display_order: 8
      },
      {
        id: 'sec_financing_cta',
        section_key: 'financing_cta',
        title: 'Need a Replacement System? Flexible Payment Options Available.',
        subtitle: 'Plans starting as low as $89/month for qualifying high-efficiency SEER2 heat pumps and furnaces.',
        badge: '0% APR AVAILABLE FOR 36 MONTHS',
        description: '',
        image_url: '',
        image_alt: '',
        primary_btn_text: 'Explore Financing Plans',
        primary_btn_url: '/financing',
        secondary_btn_text: '',
        secondary_btn_url: '',
        extra_data_json: '{}',
        is_enabled: 1,
        display_order: 9
      },
      {
        id: 'sec_final_cta',
        section_key: 'final_cta',
        title: 'Restore Your Home Comfort Today',
        subtitle: 'Same-day emergency AC and furnace repair appointments available across our local service territory.',
        badge: 'PROMPT COMFORT RESTORATION',
        description: '',
        image_url: '',
        image_alt: '',
        primary_btn_text: 'Book Service Online',
        primary_btn_url: '/book',
        secondary_btn_text: 'Call (555) 014-7824',
        secondary_btn_url: 'tel:5550147824',
        extra_data_json: '{}',
        is_enabled: 1,
        display_order: 10
      }
    ];

    for (const sec of sectionsToSeed) {
      await db.execute({
        sql: `INSERT OR REPLACE INTO homepage_sections
              (id, section_key, title, subtitle, badge, description, image_url, image_alt, primary_btn_text, primary_btn_url, secondary_btn_text, secondary_btn_url, extra_data_json, is_enabled, display_order, updated_at)
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
        args: [
          sec.id, sec.section_key, sec.title, sec.subtitle, sec.badge, sec.description,
          sec.image_url, sec.image_alt, sec.primary_btn_text, sec.primary_btn_url,
          sec.secondary_btn_text, sec.secondary_btn_url, sec.extra_data_json,
          sec.is_enabled, sec.display_order, now
        ]
      });
    }
  }

  // 8. Seed navigation_items if empty
  const navCheck = await db.execute('SELECT COUNT(*) as count FROM navigation_items');
  if (Number(navCheck.rows[0]?.count || 0) === 0) {
    const navItems = [
      { id: 'nav_home', label: 'Home', href: '/', position: 'header', order: 1 },
      { id: 'nav_services', label: 'Services', href: '/services', position: 'header', order: 2 },
      { id: 'nav_about', label: 'About', href: '/about', position: 'header', order: 3 },
      { id: 'nav_areas', label: 'Service Areas', href: '/service-areas', position: 'header', order: 4 },
      { id: 'nav_financing', label: 'Financing', href: '/financing', position: 'header', order: 5 },
      { id: 'nav_reviews', label: 'Reviews', href: '/reviews', position: 'header', order: 6 },
      { id: 'nav_contact', label: 'Contact', href: '/contact', position: 'header', order: 7 }
    ];

    for (const item of navItems) {
      await db.execute({
        sql: 'INSERT INTO navigation_items (id, label, href, position, display_order, is_enabled, created_at, updated_at) VALUES (?, ?, ?, ?, ?, 1, ?, ?)',
        args: [item.id, item.label, item.href, item.position, item.order, now, now]
      });
    }
  }

  // 9. Seed existing images into media table if empty
  const mediaCheck = await db.execute('SELECT COUNT(*) as count FROM media');
  if (Number(mediaCheck.rows[0]?.count || 0) === 0) {
    const initialMedia = [
      {
        id: 'med_hero_ac',
        name: 'hero-technician-ac.jpg',
        url: '/images/hero-technician-ac.jpg',
        mime: 'image/jpeg',
        size: 963915,
        alt: 'Certified NorthStar HVAC technician testing outdoor condensing unit with digital manifold gauges'
      },
      {
        id: 'med_furnace_inspect',
        name: 'technician-furnace-inspection.jpg',
        url: '/images/technician-furnace-inspection.jpg',
        mime: 'image/jpeg',
        size: 773901,
        alt: 'Licensed HVAC technician performing multi-point furnace combustion safety inspection'
      },
      {
        id: 'med_emergency_van',
        name: 'emergency-service-van.jpg',
        url: '/images/emergency-service-van.jpg',
        mime: 'image/jpeg',
        size: 1029048,
        alt: 'NorthStar fully equipped emergency HVAC response service van'
      },
      {
        id: 'med_auth_bg',
        name: 'admin-auth-bg.jpg',
        url: '/images/admin-auth-bg.jpg',
        mime: 'image/jpeg',
        size: 156881,
        alt: 'NorthStar technician inspecting heating and air equipment'
      }
    ];

    for (const m of initialMedia) {
      await db.execute({
        sql: 'INSERT INTO media (id, file_name, url, mime_type, file_size, alt_text, width, height, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, NULL, NULL, ?, ?)',
        args: [m.id, m.name, m.url, m.mime, m.size, m.alt, now, now]
      });
    }
  }

  isInitialized = true;
}

// ============================================================================
// CMS Content Helper Functions
// ============================================================================

export interface HomepageSection {
  id: string;
  section_key: string;
  title: string;
  subtitle: string;
  badge: string;
  description: string;
  image_url: string;
  image_alt: string;
  primary_btn_text: string;
  primary_btn_url: string;
  secondary_btn_text: string;
  secondary_btn_url: string;
  extra_data_json: string;
  is_enabled: number;
  display_order: number;
  updated_at: string;
}

export async function getHomepageSections(): Promise<Record<string, HomepageSection>> {
  await ensureDbInitialized();
  const res = await db.execute('SELECT * FROM homepage_sections ORDER BY display_order ASC');
  const sections: Record<string, HomepageSection> = {};
  for (const row of res.rows) {
    const key = row.section_key as string;
    sections[key] = {
      id: row.id as string,
      section_key: key,
      title: (row.title as string) || '',
      subtitle: (row.subtitle as string) || '',
      badge: (row.badge as string) || '',
      description: (row.description as string) || '',
      image_url: (row.image_url as string) || '',
      image_alt: (row.image_alt as string) || '',
      primary_btn_text: (row.primary_btn_text as string) || '',
      primary_btn_url: (row.primary_btn_url as string) || '',
      secondary_btn_text: (row.secondary_btn_text as string) || '',
      secondary_btn_url: (row.secondary_btn_url as string) || '',
      extra_data_json: (row.extra_data_json as string) || '{}',
      is_enabled: Number(row.is_enabled ?? 1),
      display_order: Number(row.display_order ?? 0),
      updated_at: (row.updated_at as string) || ''
    };
  }
  return sections;
}

export async function getSiteSettings(): Promise<Record<string, string>> {
  await ensureDbInitialized();
  const res = await db.execute('SELECT key, value FROM site_settings');
  const settings: Record<string, string> = {};
  for (const row of res.rows) {
    settings[row.key as string] = (row.value as string) || '';
  }
  return settings;
}

export async function getNavigationItems(position = 'header') {
  await ensureDbInitialized();
  const res = await db.execute({
    sql: 'SELECT * FROM navigation_items WHERE position = ? AND is_enabled = 1 ORDER BY display_order ASC',
    args: [position]
  });
  return res.rows.map(r => ({
    id: r.id as string,
    label: r.label as string,
    href: r.href as string,
    position: r.position as string,
    display_order: Number(r.display_order),
    is_enabled: Number(r.is_enabled)
  }));
}
