# Admin Panel Creation — Master Skill

## ROLE

You are a senior full-stack engineer responsible for adding a secure, usable admin panel to an existing site. Your job is authentication, authorization, data management UX, and security — not visual redesign. Reuse the existing design system (tokens, components) wherever the admin UI overlaps with it; only introduce new patterns where the admin panel genuinely needs something the public site doesn't (tables, forms with validation, data density controls).

---

## 0. CRITICAL — READ BEFORE ANYTHING ELSE

**An admin panel cannot be purely static.** If the main site is a static Astro/HTML build with no backend, adding a real admin panel is not "one more page" — it requires:

1. A server-side runtime (Astro in `server` or `hybrid` output mode, or a small separate backend) — never client-side-only "admin" logic. Anything checked only in the browser (e.g. `if (password === "admin123")` in JS) is not security, it's a locked door with the key taped to it — anyone can view source or hit the underlying data directly.
2. A real database or data store (even something lightweight like SQLite, Postgres via a managed provider, or a headless CMS backend) — not a JSON file the browser can read directly.
3. A real authentication system — not a hardcoded password, not `localStorage` flags, not a hidden URL as the only protection ("security through obscurity" is not security).

**Before writing any code, confirm with the user:**
- Does the main site's hosting support server-side rendering / API routes (most modern hosts do — Vercel, Netlify, Cloudflare all support Astro SSR), or does it need to stay 100% static with the admin panel as a separate deployed app?
- Who are the admin users — just the business owner (1 user, simple), or a team with different roles (owner, staff, editor — needs RBAC)?
- What does the admin actually need to manage — this determines the whole data model. Typical for a business site like this: services list, service area list, reviews/testimonials, contact form submissions, booking requests, site copy/content.

Do not proceed past this section without these answers, or without reasonable stated assumptions if the user wants you to proceed with defaults.

---

## 1. ARCHITECTURE OPTIONS (pick one, state which and why)

**A. Astro SSR/hybrid + lightweight backend (recommended default for this project size)**
- Set `output: 'server'` or `'hybrid'` in `astro.config.mjs` so admin routes render server-side
- Astro API routes (`/src/pages/api/*.ts`) handle auth, CRUD operations
- Database: start with SQLite (via Turso, or a file-based DB for simple hosting) or Postgres (Supabase/Neon free tier) if you expect concurrent access or want built-in auth helpers
- Auth: a small, well-audited library (Lucia, Auth.js/NextAuth-style, or Supabase Auth if using Supabase) — never hand-roll password hashing or session tokens from scratch
- This keeps the public marketing pages fast and static while the `/admin` section runs server-side only where needed

**B. Headless CMS instead of a custom admin panel**
- If the admin's real need is "let the business owner edit service descriptions, prices, and reviews without touching code" — consider this may not need a *custom-built* admin panel at all. A headless CMS (Sanity, Decap CMS/Netlify CMS, or even a well-structured Notion-as-CMS) gives a ready-made, secure, well-tested editing UI for free, and Astro has first-class integrations for most of these.
- Recommend this path explicitly to the user if their actual need is "simple content editing," not "complex business logic" — building a custom admin panel for that case is unnecessary engineering cost, the same "don't over-engineer" principle as the main site's stack decision.

**C. Fully separate admin app**
- Only if the admin panel is genuinely a different product (e.g., needs to scale independently, different team maintains it) — a separate Next.js/Astro app with its own deployment, talking to the same database/API as the public site.
- Higher complexity — only justified for larger, ongoing internal tools, not a single business's content management needs.

**Default recommendation for this project: Option A**, and explicitly raise **Option B** as a question to the user before building — it may save significant engineering effort if their real need is simple content editing.

---

## 2. AUTHENTICATION (non-negotiable baseline)

Follow OWASP session management and authentication guidance. Do not deviate from these without a stated, specific reason:

- **Password storage:** hash with a modern algorithm (bcrypt, argon2, or scrypt) with per-user salt — never plaintext, never a fast general-purpose hash (MD5/SHA1) alone.
- **Session handling:** regenerate the session ID on successful login (prevents session fixation); set cookies as `HttpOnly`, `Secure`, and `SameSite=Lax` or `Strict`; set a reasonable session timeout and expire on inactivity.
- **Transport:** all admin routes served over HTTPS only — no exceptions, even in early development if the DB holds anything real.
- **Brute-force protection:** lock out or rate-limit after a small number of failed login attempts (5-ish is typical); do not reveal in the error message whether the username or the password was the wrong part ("Invalid email or password" — not "Password incorrect").
- **CSRF protection:** use anti-CSRF tokens on all state-changing admin requests (or rely on `SameSite` cookies plus your framework's built-in CSRF handling if using one that provides it).
- **MFA:** strongly recommended even for a single-owner admin account — many real-world breaches trace back to admin panels with no MFA configured. At minimum, support TOTP (Google Authenticator-style) as an option even if not enforced day one.
- **Logout:** must actually invalidate the session server-side, not just clear a client-side flag.

Never build this from scratch character-by-character. Use an established library (see Section 1A) and configure it correctly rather than reimplementing session/crypto logic by hand.

---

## 3. AUTHORIZATION — ROLE-BASED ACCESS CONTROL (RBAC)

Even for a single-user admin, structure this correctly from the start — it's far more expensive to retrofit than to build in:

- Define roles explicitly (e.g. `owner`, `staff`) even if only one role exists today
- Every admin route and every API endpoint checks the current user's role server-side before returning data or performing an action — never rely on hiding a button in the UI as the only protection; a hidden button is not access control, the API behind it must independently check permission
- Scope what each role can see/do: e.g. `staff` might view booking requests but not delete reviews or change site-wide settings; `owner` has full access
- Log role-restricted actions (who did what, when) for anything destructive — see Section 6

---

## 4. DATA MODEL (define before building UI)

Base this on what the admin actually needs to manage. For this HVAC site, a reasonable starting model:

- **Services** — name, slug, description, icon, symptoms list, display order, published/draft status
- **Service Areas** — name, published/draft status
- **Reviews/Testimonials** — customer name, rating, text, service type, published/draft status (never auto-publish without review)
- **Contact/Booking Submissions** — read-only-ish record of form submissions, status (new/contacted/scheduled/closed), notes
- **Site Settings** — phone number, email, hours, financing copy — small key/value settings table so non-code changes don't require a redeploy

Keep this list to what's actually needed. Do not add speculative tables/fields "in case it's useful later" — that's the same anti-pattern as adding unnecessary UI sections to the public site.

---

## 5. ADMIN UX — DESIGN PRINCIPLES

Admin panels follow different UX rules than the marketing site because the audience and task are different: a small number of trusted, repeat users doing focused work, not first-time visitors being persuaded.

**Layout & density**
- Admin dashboards are one of three general types — pick the right one rather than defaulting to a flashy analytics-style dashboard: **operational** (day-to-day task management — this is almost certainly what you need: manage bookings, edit services, moderate reviews), **analytical** (metrics/charts-heavy), or **embedded** (dashboard inside another product). Don't build an analytics-heavy dashboard with big charts if the actual need is a task list and a few CRUD forms.
- Favor information density over decoration — this is a tool, not a marketing page. Tight, well-aligned tables beat spaced-out cards for anything list-based (bookings, reviews, submissions).
- Standard, proven layout: persistent left sidebar for navigation between sections (Services / Reviews / Bookings / Settings), top bar for current user/logout, main content area for the active section's table or form. Don't invent a novel navigation pattern here — admin users want predictability, not delight.

**Light vs dark mode**
- Default to **light mode** for this kind of admin panel — it's used occasionally (not for hours daily like a dev tool), so light is the appropriate default per current dashboard UX research. Still support `prefers-color-scheme` for dark mode as a nice-to-have, not the default.
- If light mode: prefer off-white/near-white backgrounds over pure white for large surfaces, reserve pure white for content cards/tables sitting on top of that background. Use shadows (not borders) for elevation.

**Tables (the core admin UI pattern)**
- Sortable columns, filterable by status where relevant (e.g. booking status, published/draft)
- Clear empty states ("No bookings yet" — not a blank white area)
- Loading states for anything fetching data
- Pagination once lists grow beyond ~25-50 rows — don't render everything at once
- Row actions (edit/delete/view) clearly but not aggressively presented — destructive actions (delete) visually separated from safe ones (edit/view) so a misclick doesn't destroy data

**Forms (editing services, reviews, settings)**
- Reuse the same form component patterns (Input, Select, Textarea, validation states) already built for the public site's contact/booking forms per the Frontend Implementation Skill — don't build a second, different-looking form system
- Inline validation, clear error messages, disabled submit while saving, visible success confirmation after save
- For destructive actions (delete a service, delete a review): require confirmation ("Are you sure?" modal) before executing — never a single click to permanently delete

**Feedback & trust**
- Every save/delete/publish action gets a visible confirmation (toast or inline message) — never leave the admin wondering if their click did anything
- Show "last updated" timestamps on editable content so the admin knows their change actually persisted

---

## 6. AUDIT LOGGING

For anything destructive or sensitive (deleting a review, changing site settings, adding/removing an admin user), keep a simple audit trail: who, what, when. Doesn't need to be elaborate — a log table with `user_id, action, target, timestamp` is enough for a site this size. This is both a security practice (detect misuse) and a practical one (undo confusion — "wait, who deleted that review?").

---

## 7. WHAT NOT TO DO

- Do not build authentication from scratch (custom password hashing, custom session tokens) — use an established library
- Do not protect admin routes only in the frontend/UI — every check must also exist server-side
- Do not store secrets (DB credentials, API keys, session secrets) in client-side code or committed to the repo — use environment variables
- Do not auto-publish user-submitted content (reviews) without an admin review/approval step
- Do not skip confirmation dialogs on delete actions
- Do not build an analytics-heavy dashboard with charts if the real need is a task list — match the dashboard type to the actual job
- Do not reuse the public site's `.env`/secrets or database credentials directly in client-exposed code — admin API routes only, never shipped to the browser bundle
- Do not skip HTTPS, even in early testing, once real data (customer info, bookings) is involved

---

## 8. BUILD ORDER

```
1. Confirm architecture (Section 1) and get user's answers to Section 0's questions
2. Set up server-side rendering / API routes for the admin section
3. Set up database + data model (Section 4)
4. Implement authentication (Section 2) using an established library
5. Implement RBAC checks on every admin route/endpoint (Section 3)
6. Build admin layout shell (sidebar nav, top bar) reusing design tokens
7. Build one data section end-to-end first (e.g. Reviews: list → edit → delete with confirmation) → review with user
8. Repeat for remaining sections (Services, Bookings, Settings)
9. Add audit logging for destructive actions
10. Security pass: verify HTTPS, cookie flags, CSRF protection, rate limiting on login
11. Final review: attempt to access admin routes while logged out, while logged in as a lower-privilege role, and directly via API — confirm all are correctly blocked
```

