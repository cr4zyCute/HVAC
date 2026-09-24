import type { APIRoute } from 'astro';
import { registerClient, unregisterClient } from '@/lib/realtime';

export const prerender = false;

export const GET: APIRoute = async ({ request }) => {
  let streamController: ReadableStreamDefaultController<string> | null = null;
  let heartbeatInterval: NodeJS.Timeout | null = null;

  const stream = new ReadableStream<string>({
    start(controller) {
      streamController = controller;
      registerClient(controller);

      // Send initial connection handshake
      const initialPayload = `event: connected\ndata: ${JSON.stringify({
        status: 'connected',
        timestamp: Date.now(),
        message: 'NorthStar Realtime Sync Active'
      })}\n\n`;
      controller.enqueue(initialPayload);

      // Periodic heartbeat ping to prevent connection drops across proxies
      heartbeatInterval = setInterval(() => {
        try {
          controller.enqueue(`event: ping\ndata: ${Date.now()}\n\n`);
        } catch {
          if (heartbeatInterval) clearInterval(heartbeatInterval);
        }
      }, 25000);
    },
    cancel() {
      if (heartbeatInterval) {
        clearInterval(heartbeatInterval);
      }
      if (streamController) {
        unregisterClient(streamController);
      }
    }
  });

  return new Response(stream, {
    status: 200,
    headers: {
      'Content-Type': 'text/event-stream; charset=utf-8',
      'Cache-Control': 'no-cache, no-transform',
      'Connection': 'keep-alive',
      'X-Accel-Buffering': 'no'
    }
  });
};
