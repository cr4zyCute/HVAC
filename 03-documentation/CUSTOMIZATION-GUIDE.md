# NorthStar HVAC — Customization Guide

This guide walks you through customizing the NorthStar HVAC template for a new brand, client, or company in just a few minutes.

---

## 1. Changing Brand Colors

All colors are controlled globally through CSS variables in `02-html-website-template/css/tokens.css` and `01-figma-and-svgs/design-system/figma-design-tokens.json`.

To change the primary accent color from safety orange (`#E65100`) to your brand color (e.g., Royal Blue `#2563EB`):

1. Open `css/tokens.css`.
2. Update the accent variables:
   ```css
   --color-brand-accent: #2563EB;
   --color-brand-accent-hover: #1D4ED8;
   --color-brand-accent-subtle: #EFF6FF;
   ```
3. Save the file. All primary buttons, badges, active tabs, and highlights will update automatically.

---

## 2. Changing the Company Name & Phone Number

1. **Company Name:** Search and replace `NorthStar HVAC` across the HTML files with your company name (e.g., `Apex Heating & Cooling`).
2. **Phone Number:** Search and replace `(555) 014-7824` with your active dispatch phone number.
3. **Email:** Update `hello@northstarhvac.example` in the footer.

---

## 3. Connecting Form Endpoints

By default, the forms in `02-html-website-template/js/modals.js` simulate successful submissions with confirmation screens.

To connect them to a real backend, email service, or CRM (such as Formspree, Zapier, Web3Forms, or ServiceTitan):

1. Open `js/modals.js`.
2. Locate the form submit listeners (`nextBtn` on Step 3, `reviewForm.addEventListener`, and `callbackForm.addEventListener`).
3. Replace the local simulation with a `fetch()` call:
   ```javascript
   fetch('https://your-api-endpoint.com/book', {
     method: 'POST',
     headers: { 'Content-Type': 'application/json' },
     body: JSON.stringify(bookingData)
   })
   .then(response => response.json())
   .then(data => {
     // show confirmation screen
   });
   ```

---

## 4. Replacing Images

All images are stored in `02-html-website-template/assets/images/`:
* `hero-technician-ac.jpg`: Hero technician photo (recommended ratio 4:3 or 16:9, min width 1200px).
* `emergency-service-van.jpg`: Branded service vehicle photo.
* `technician-furnace-inspection.jpg`: Equipment diagnostics & inspection photo.

Simply overwrite these files with your client's real photos using the same filenames, or update the `src` attribute in the HTML files.

