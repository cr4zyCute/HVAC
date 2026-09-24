/**
 * Real-Time CMS Event Bus & Synchronization Engine
 * Handles Server-Sent Events (SSE) connections, broadcast notifications,
 * and live synchronization between the Admin Dashboard and the Public Website.
 */

export interface CmsEvent {
  type: 'homepage' | 'services' | 'settings' | 'navigation' | 'reviews' | 'media';
  section_key?: string;
  action?: 'create' | 'update' | 'delete' | 'reorder';
  id?: string;
  timestamp: number;
}

interface RealtimeState {
  clients: Set<ReadableStreamDefaultController<string>>;
  lastVersion: number;
  lastEvents: CmsEvent[];
}

declare global {
  var __cmsRealtimeState: RealtimeState | undefined;
}

if (!globalThis.__cmsRealtimeState) {
  globalThis.__cmsRealtimeState = {
    clients: new Set(),
    lastVersion: Date.now(),
    lastEvents: []
  };
}

const state = globalThis.__cmsRealtimeState;

/**
 * Register an active SSE stream controller
 */
export function registerClient(controller: ReadableStreamDefaultController<string>) {
  state.clients.add(controller);
}

/**
 * Remove a disconnected SSE stream controller
 */
export function unregisterClient(controller: ReadableStreamDefaultController<string>) {
  state.clients.delete(controller);
}

/**
 * Broadcast a CMS update to all connected browser clients in real time
 */
export function broadcastCmsUpdate(event: Omit<CmsEvent, 'timestamp'>) {
  const fullEvent: CmsEvent = {
    ...event,
    timestamp: Date.now()
  };

  state.lastVersion = fullEvent.timestamp;
  state.lastEvents.unshift(fullEvent);
  if (state.lastEvents.length > 20) {
    state.lastEvents.pop();
  }

  const payload = `event: cms-update\ndata: ${JSON.stringify(fullEvent)}\n\n`;

  for (const client of state.clients) {
    try {
      client.enqueue(payload);
    } catch (err) {
      state.clients.delete(client);
    }
  }
}

/**
 * Get current system version and recent events
 */
export function getRealtimeStatus() {
  return {
    version: state.lastVersion,
    activeListeners: state.clients.size,
    recentEvents: state.lastEvents
  };
}
