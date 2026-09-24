# NorthStar HVAC — Commercial Figma UI Kit & Astro Website Template

> **Commercial-Grade Digital Product Package**  
> Designed for HVAC contractors, home services companies, UI/UX agencies, and template marketplace buyers. Built on a strict 8px grid system, featuring official Lucide icons, full responsive breakpoints, and two implementation packages:
> 1. **Figma Vector Package (`01-FIGMA-DESIGN/`)**: 30 responsive SVG artboards + Design System Tokens.
> 2. **Coded Astro Website (`/src`)**: Production-ready Astro v5 + Tailwind CSS v3 + TypeScript website with 13 pre-rendered static routes and zero runtime JavaScript bloat.

---

## 📦 What's Inside This Package

```text
📁 NorthStar-HVAC-Commercial-Package/
├── 📄 README.md                        <-- Quick Start & Documentation
├── 📄 figma-design-tokens.json         <-- Core Design Tokens (Colors, Spacing, Typography)
├── 📄 tailwind.config.mjs              <-- Tailwind Configuration matching Tokens 1:1
│
├── 📁 01-FIGMA-DESIGN/                 <-- High-Resolution Vector Assets for Figma
│   ├── 📁 desktop-1440/                <-- 10 Desktop Artboards (1440px wide)
│   ├── 📁 tablet-834/                  <-- 10 Tablet Artboards (834px wide)
│   ├── 📁 mobile-390/                  <-- 10 Mobile Artboards (390px wide)
│   ├── 📁 design-system/               <-- Components Library & JSON Design Tokens
│   └── 📄 FIGMA-README.md              <-- Figma Import & Usage Guide
│
├── 📁 src/                             <-- Astro + Tailwind Multi-Page Website Source
│   ├── 📁 pages/                       <-- 10 Static Page Routes + /style-guide
│   │   ├── index.astro                 <-- Homepage (12 comprehensive sections)
│   │   ├── services/index.astro        <-- Services Catalog Directory
│   │   ├── services/[slug].astro       <-- Dynamic Service Detail Page Template
│   │   ├── about.astro                 <-- Company Story, Team & Fleet
│   │   ├── service-areas.astro         <-- 6 Regional Hubs + Interactive ZIP Checker
│   │   ├── financing.astro             <-- Payment Plans + Real-Time Loan Calculator
│   │   ├── reviews.astro               <-- 4.9★ Rating Breakdown + Interactive Review Form
│   │   ├── contact.astro               <-- 24/7 Hotline + Accessible Contact Form
│   │   ├── book.astro                  <-- 4-Step Interactive Online Booking Wizard
│   │   ├── emergency.astro             <-- Urgent 24/7 Emergency Dispatch Hotline
│   │   └── style-guide.astro           <-- Component Review Matrix
│   ├── 📁 components/                  <-- Modular UI & Section Components
│   ├── 📁 content/                     <-- Structured JSON Data (Services, Reviews)
│   └── 📁 styles/                      <-- Global Tailwind Entry & Typography
│
├── 📁 dist/                            <-- Pre-Built Static Production Build (Deploy-ready)
└── 📁 03-documentation/                <-- Buyer Customization Guide
```

---

## 🚀 Quick Start: Running the Coded Website (Astro + Tailwind)

### 1. Requirements
- Node.js `v18.17+` or `v20+` or `v22+`
- npm installed

### 2. Development Mode
Run the local development server:
```bash
npm install
npm run dev
```
Open [http://localhost:4321](http://localhost:4321) in your browser.

### 3. Production Static Build
Generate clean, lightning-fast static HTML/CSS ready to deploy anywhere (Vercel, Netlify, Cloudflare Pages, GitHub Pages):
```bash
npm run build
```
Built output will be in `/dist`.

### 4. Preview Build Locally
```bash
npm run preview
```

---

## ⚡ How to Customize & Rebrand the Website

This package includes **two easy ways** to edit company names, phone numbers, text, and guarantees without having to hunt through 13 HTML files:

### Method 1: For Developers & Template Buyers (`src/data/siteConfig.json`)
All global company branding and booking text is centralized into **one file**:
👉 [`src/data/siteConfig.json`](src/data/siteConfig.json)

Edit this single file to update:
- `company.name`: Your business name (e.g. "Apex Heating & Cooling")
- `company.phone` & `company.phoneRaw`: Dispatch phone numbers
- `company.email`: Support email address
- `company.address`: Physical business address
- `company.license`: State/City trade license number
- `booking.heroTitle` & `booking.heroSubtitle`: Booking wizard headlines
- `booking.guarantees`: 4 customer guarantee points

Save the file and **the entire website (Header, Footer, Booking Wizard, and Contact pages) updates automatically**.

### Method 2: For Non-Technical Business Owners (`/admin` Visual Dashboard)
This template features a built-in visual Content Management Dashboard powered by **Decap CMS**:
1. When deployed to your live domain, navigate to: `https://yourdomain.com/admin/`
2. Log in with your email and password (powered by free Netlify Identity or GitHub authentication).
3. You get a clean, user-friendly visual dashboard with forms to edit:
   - **Company Information & Phone Numbers**
   - **Booking Page Content & Guarantees**
   - **HVAC Services & Symptoms**
   - **Customer Reviews**
4. Click **Publish** to update your live website instantly — **zero monthly database fees, zero WordPress security headaches**.

---

## 🎨 Design System & Typography

This template uses 100% free open-source fonts available directly on Google Fonts:

1. **Headings:** [Plus Jakarta Sans](https://fonts.google.com/specimen/Plus+Jakarta+Sans) (Weights: 600, 700, 800)
2. **Body & Controls:** [Inter](https://fonts.google.com/specimen/Inter) (Weights: 400, 500, 600, 700)
3. **Icons:** Official [Lucide Icons](https://lucide.dev/) (24×24 crisp vector strokes)

### Core Brand Colors
* **Primary Brand Navy:** `#003366`
* **Deep Brand Secondary:** `#001F3F`
* **Brand Action Accent:** `#E65100` (Hover: `#CC4400`)
* **Emergency Red:** `#DC2626`
* **Success Green:** `#16A34A`
* **Surface Background:** `#F8FAFC`

---

## 🛠️ How to Import into Figma

1. Open **Figma**.
2. Create a new design file.
3. Open `01-FIGMA-DESIGN/` in your file explorer.
4. Drag and drop any SVG file into your Figma canvas:
   - For desktop: drag files from `desktop-1440/`
   - For tablet: drag files from `tablet-834/`
   - For mobile: drag files from `mobile-390/`
5. All artboards will import with fully selectable, editable text layers and organized vector groupings.

---

## 📄 Commercial License

* **Commercial Rights:** You are licensed to use this template for personal and client projects.
* **Support:** For customization guidance, see [CUSTOMIZATION-GUIDE.md](03-documentation/CUSTOMIZATION-GUIDE.md).
