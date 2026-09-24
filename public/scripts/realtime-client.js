/**
 * NorthStar Real-Time CMS Client Engine
 * Connects to Server-Sent Events (SSE) stream.
 * Automatically synchronizes public website content when changes are saved in the Admin Dashboard.
 */

(function initRealtimeSync() {
  // Only run in browser environment
  if (typeof window === 'undefined' || !window.EventSource) return;

  // Don't run inside admin dashboard pages to prevent self-conflict
  if (window.location.pathname.startsWith('/admin')) return;

  let eventSource = null;
  let retryCount = 0;
  let maxRetries = 10;
  let lastReceivedVersion = 0;

  function showUpdatePill(message) {
    let pill = document.getElementById('realtime-sync-pill');
    if (!pill) {
      pill = document.createElement('div');
      pill.id = 'realtime-sync-pill';
      pill.className = 'fixed bottom-20 right-20 z-50 flex items-center gap-8 bg-brand-primary text-white text-xs font-semibold px-16 py-10 rounded-full shadow-2xl border border-white/20 transition-all duration-300 transform translate-y-10 opacity-0 pointer-events-none';
      pill.innerHTML = `
        <span class="relative flex h-8 w-8">
          <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
          <span class="relative inline-flex rounded-full h-8 w-8 bg-emerald-500"></span>
        </span>
        <span id="realtime-sync-text">Content updated live from CMS</span>
      `;
      document.body.appendChild(pill);
    }

    const textEl = document.getElementById('realtime-sync-text');
    if (textEl && message) textEl.textContent = message;

    // Animate in
    requestAnimationFrame(() => {
      pill.classList.remove('translate-y-10', 'opacity-0');
      pill.classList.add('translate-y-0', 'opacity-100');
    });

    // Auto dismiss after 3.5 seconds
    setTimeout(() => {
      if (pill) {
        pill.classList.remove('translate-y-0', 'opacity-100');
        pill.classList.add('translate-y-10', 'opacity-0');
      }
    }, 3500);
  }

  async function syncCurrentPage(eventData) {
    try {
      const response = await fetch(window.location.href, {
        headers: { 'X-Requested-With': 'CMS-Realtime-Sync' },
        cache: 'no-store'
      });

      if (!response.ok) return;

      const htmlText = await response.text();
      const parser = new DOMParser();
      const newDoc = parser.parseFromString(htmlText, 'text/html');

      // 1. Sync Document Title
      if (newDoc.title && document.title !== newDoc.title) {
        document.title = newDoc.title;
      }

      // 2. Sync Header if present
      const currentHeader = document.querySelector('header');
      const newHeader = newDoc.querySelector('header');
      if (currentHeader && newHeader) {
        currentHeader.innerHTML = newHeader.innerHTML;
      }

      // 3. Sync Main content / dynamic sections
      const currentMain = document.querySelector('main');
      const newMain = newDoc.querySelector('main');
      if (currentMain && newMain) {
        currentMain.innerHTML = newMain.innerHTML;
      }

      // 4. Sync Footer if present
      const currentFooter = document.querySelector('footer');
      const newFooter = newDoc.querySelector('footer');
      if (currentFooter && newFooter) {
        currentFooter.innerHTML = newFooter.innerHTML;
      }

      // Notify user visually
      const eventType = eventData?.type ? eventData.type.charAt(0).toUpperCase() + eventData.type.slice(1) : 'CMS';
      showUpdatePill(`✨ ${eventType} updated in real time`);
    } catch (err) {
      console.warn('[NorthStar Realtime] Background sync failed, page remains interactive:', err);
    }
  }

  function connect() {
    if (eventSource) {
      eventSource.close();
    }

    eventSource = new EventSource('/api/realtime/stream');

    eventSource.addEventListener('connected', (e) => {
      retryCount = 0;
      try {
        const data = JSON.parse(e.data);
        lastReceivedVersion = data.timestamp;
      } catch {}
    });

    eventSource.addEventListener('cms-update', (e) => {
      try {
        const eventData = JSON.parse(e.data);
        if (eventData.timestamp > lastReceivedVersion) {
          lastReceivedVersion = eventData.timestamp;
          syncCurrentPage(eventData);
        }
      } catch (err) {
        console.error('[NorthStar Realtime] Parse error:', err);
      }
    });

    eventSource.onerror = () => {
      eventSource.close();
      eventSource = null;
      if (retryCount < maxRetries) {
        const delay = Math.min(1000 * Math.pow(1.5, retryCount), 15000);
        retryCount++;
        setTimeout(connect, delay);
      }
    };
  }

  // Initial connect when document is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', connect);
  } else {
    connect();
  }

  // Periodic status poll fallback in case SSE connection is suspended in background
  setInterval(async () => {
    try {
      const res = await fetch('/api/realtime/status', { cache: 'no-store' });
      if (!res.ok) return;
      const data = await res.json();
      if (data.version && lastReceivedVersion && data.version > lastReceivedVersion) {
        lastReceivedVersion = data.version;
        syncCurrentPage({ type: 'Content' });
      }
    } catch {}
  }, 30000);
})();
