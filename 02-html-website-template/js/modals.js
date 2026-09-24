/**
 * NorthStar HVAC - Production Modals & Interactive Flows
 * Multi-Step Booking Wizard, Write a Review, Quick Callback
 */

document.addEventListener('DOMContentLoaded', () => {
  // Modal Open / Close Helpers
  function openModal(modalId) {
    const backdrop = document.getElementById(modalId);
    if (backdrop) {
      backdrop.classList.add('open');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeModal(modalId) {
    const backdrop = document.getElementById(modalId);
    if (backdrop) {
      backdrop.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  function closeAllModals() {
    document.querySelectorAll('.modal-backdrop').forEach(modal => {
      modal.classList.remove('open');
    });
    document.body.style.overflow = '';
  }

  // Bind Open Buttons
  document.querySelectorAll('[data-open-modal]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const modalTarget = btn.getAttribute('data-open-modal');
      openModal(`modal-${modalTarget}`);
    });
  });

  // Bind Close Buttons
  document.querySelectorAll('[data-close-modal]').forEach(btn => {
    btn.addEventListener('click', () => {
      const modal = btn.closest('.modal-backdrop');
      if (modal) {
        closeModal(modal.id);
      }
    });
  });

  // Backdrop click to dismiss
  document.querySelectorAll('.modal-backdrop').forEach(backdrop => {
    backdrop.addEventListener('click', (e) => {
      if (e.target === backdrop) {
        closeModal(backdrop.id);
      }
    });
  });

  // ESC key to close
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeAllModals();
    }
  });

  // =========================================================================
  // 1. MULTI-STEP BOOKING WIZARD
  // =========================================================================
  let currentStep = 1;
  const totalSteps = 3;
  const bookingData = {
    service: 'Air Conditioning Repair',
    urgency: 'Same-Day Emergency',
    day: 'Today',
    timeSlot: 'Morning (8:00 AM – 12:00 PM)',
    name: '',
    phone: '',
    address: '',
    zip: '',
    notes: ''
  };

  const bookingModal = document.getElementById('modal-booking');
  if (bookingModal) {
    const nextBtn = document.getElementById('wizard-next-btn');
    const backBtn = document.getElementById('wizard-back-btn');
    const stepNodes = bookingModal.querySelectorAll('.wizard-step-node');
    const stepContents = bookingModal.querySelectorAll('.wizard-step-content');
    const confirmationView = document.getElementById('wizard-confirmation');
    const wizardFooter = document.getElementById('wizard-footer');

    // Service Selection
    bookingModal.querySelectorAll('.service-card-select').forEach(card => {
      card.addEventListener('click', () => {
        bookingModal.querySelectorAll('.service-card-select').forEach(c => c.classList.remove('selected'));
        card.classList.add('selected');
        bookingData.service = card.getAttribute('data-service');
      });
    });

    // Time Slot Selection
    bookingModal.querySelectorAll('.time-chip').forEach(chip => {
      chip.addEventListener('click', () => {
        bookingModal.querySelectorAll('.time-chip').forEach(c => c.classList.remove('selected'));
        chip.classList.add('selected');
        bookingData.timeSlot = chip.getAttribute('data-slot');
      });
    });

    function updateWizardUI() {
      // Step visibility
      stepContents.forEach(content => {
        const stepNum = parseInt(content.getAttribute('data-step'), 10);
        content.style.display = stepNum === currentStep ? 'block' : 'none';
      });

      // Progress bar nodes
      stepNodes.forEach((node, idx) => {
        const stepNum = idx + 1;
        node.classList.remove('active', 'completed');
        if (stepNum === currentStep) {
          node.classList.add('active');
        } else if (stepNum < currentStep) {
          node.classList.add('completed');
        }
      });

      // Buttons
      if (backBtn) {
        backBtn.style.visibility = currentStep === 1 ? 'hidden' : 'visible';
      }
      if (nextBtn) {
        nextBtn.textContent = currentStep === totalSteps ? 'Confirm Appointment' : 'Continue to Next Step';
      }
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (currentStep < totalSteps) {
          currentStep++;
          updateWizardUI();
        } else {
          // Submit booking
          bookingData.name = document.getElementById('book-name')?.value || 'Valued Customer';
          bookingData.phone = document.getElementById('book-phone')?.value || '(555) 014-7824';
          bookingData.address = document.getElementById('book-address')?.value || 'Metro Service Area';

          // Hide steps & footer, show confirmation
          stepContents.forEach(content => content.style.display = 'none');
          bookingModal.querySelector('.wizard-progress').style.display = 'none';
          if (wizardFooter) wizardFooter.style.display = 'none';

          if (confirmationView) {
            confirmationView.style.display = 'block';
            const randomCode = 'NS-' + Math.floor(1000 + Math.random() * 9000);
            const codeEl = document.getElementById('booking-ref-code');
            if (codeEl) codeEl.textContent = randomCode;

            const summaryEl = document.getElementById('booking-summary-text');
            if (summaryEl) {
              summaryEl.textContent = `${bookingData.service} scheduled for ${bookingData.day}, ${bookingData.timeSlot}. A certified NorthStar technician will call 15 minutes before arrival.`;
            }
          }
        }
      });
    }

    if (backBtn) {
      backBtn.addEventListener('click', () => {
        if (currentStep > 1) {
          currentStep--;
          updateWizardUI();
        }
      });
    }

    // Initialize
    updateWizardUI();
  }

  // =========================================================================
  // 2. WRITE A REVIEW MODAL
  // =========================================================================
  const reviewModal = document.getElementById('modal-review');
  if (reviewModal) {
    const starBtns = reviewModal.querySelectorAll('.star-btn');
    const ratingLabel = document.getElementById('rating-label');
    const reviewForm = document.getElementById('review-form');
    const reviewSuccess = document.getElementById('review-success');
    let selectedRating = 5;

    const ratingLabels = {
      1: '1 Star — Needs Improvement',
      2: '2 Stars — Fair Service',
      3: '3 Stars — Average Service',
      4: '4 Stars — Very Good Service',
      5: '5 Stars — Exceptional Service'
    };

    function highlightStars(rating) {
      starBtns.forEach(btn => {
        const starVal = parseInt(btn.getAttribute('data-rating'), 10);
        if (starVal <= rating) {
          btn.style.color = '#F59E0B';
        } else {
          btn.style.color = '#CBD5E1';
        }
      });
    }

    starBtns.forEach(btn => {
      btn.addEventListener('mouseenter', () => {
        const val = parseInt(btn.getAttribute('data-rating'), 10);
        highlightStars(val);
        if (ratingLabel) ratingLabel.textContent = ratingLabels[val];
      });

      btn.addEventListener('mouseleave', () => {
        highlightStars(selectedRating);
        if (ratingLabel) ratingLabel.textContent = ratingLabels[selectedRating];
      });

      btn.addEventListener('click', () => {
        selectedRating = parseInt(btn.getAttribute('data-rating'), 10);
        highlightStars(selectedRating);
        if (ratingLabel) ratingLabel.textContent = ratingLabels[selectedRating];
      });
    });

    if (reviewForm) {
      reviewForm.addEventListener('submit', (e) => {
        e.preventDefault();
        reviewForm.style.display = 'none';
        if (reviewSuccess) reviewSuccess.style.display = 'block';
      });
    }
  }

  // =========================================================================
  // 3. QUICK CALLBACK MODAL
  // =========================================================================
  const callbackForm = document.getElementById('callback-form');
  const callbackSuccess = document.getElementById('callback-success');
  if (callbackForm) {
    callbackForm.addEventListener('submit', (e) => {
      e.preventDefault();
      callbackForm.style.display = 'none';
      if (callbackSuccess) callbackSuccess.style.display = 'block';
    });
  }
});

