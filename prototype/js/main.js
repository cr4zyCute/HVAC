/**
 * NorthStar HVAC - Main Site Interactions
 */

document.addEventListener('DOMContentLoaded', () => {
  // Sticky header shadow on scroll
  const header = document.querySelector('.main-header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    });
  }

  // FAQ Accordion Toggle
  const accordionHeaders = document.querySelectorAll('.accordion-header');
  accordionHeaders.forEach(headerBtn => {
    headerBtn.addEventListener('click', () => {
      const item = headerBtn.closest('.accordion-item');
      const isActive = item.classList.contains('active');
      
      // Close sibling items
      const parent = item.parentElement;
      if (parent) {
        parent.querySelectorAll('.accordion-item').forEach(sibling => {
          sibling.classList.remove('active');
          const icon = sibling.querySelector('.accordion-icon');
          if (icon) icon.textContent = '+';
        });
      }

      // Toggle current
      if (!isActive) {
        item.classList.add('active');
        const icon = item.querySelector('.accordion-icon');
        if (icon) icon.textContent = '−';
      }
    });
  });

  // Mobile menu drawer toggle
  const mobileBtn = document.querySelector('.mobile-menu-btn');
  const navMenu = document.querySelector('.nav-menu');
  if (mobileBtn && navMenu) {
    mobileBtn.addEventListener('click', () => {
      navMenu.classList.toggle('mobile-open');
    });
  }
});
