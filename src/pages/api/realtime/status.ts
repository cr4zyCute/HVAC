import type { APIRoute } from 'astro';
import { getRealtimeStatus } from '@/lib/realtime';

export const prerender = false;

export const GET: APIRoute = async () => {
  return new Response(JSON.stringify(getRealtimeStatus()), {
    status: 200,
    headers: {
      'Content-Type': 'application/json',
      'Cache-Control': 'no-cache, no-store, must-revalidate'
    }
  });
};
