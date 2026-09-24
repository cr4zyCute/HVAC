/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}',
  ],
  theme: {
    container: {
      center: true,
      padding: {
        DEFAULT: '16px',
        md: '24px',
        lg: '32px',
      },
      screens: {
        sm: '100%',
        md: '100%',
        lg: '1024px',
        xl: '1280px',
        '2xl': '1280px',
      },
    },
    screens: {
      'sm': '390px',      // Mobile Artboard
      'md': '768px',      // Tablet Portrait
      'tablet': '834px',  // Tablet Artboard
      'lg': '1024px',     // Small Laptop / Large Tablet
      'xl': '1280px',     // Standard Laptop
      'desktop': '1440px',// Desktop Artboard (Figma Primary)
      '2xl': '1920px',    // Wide Display
    },
    extend: {
      colors: {
        brand: {
          primary: '#0F2238',
          secondary: '#1E3A5F',
          accent: '#E65100',
          'accent-hover': '#CC4400',
          emergency: '#DC2626',
          'emergency-hover': '#B91C1C',
        },
        neutral: {
          background: '#F8FAFC',
          surface: '#FFFFFF',
          'surface-alt': '#F1F5F9',
          border: '#E2E8F0',
          'border-focus': '#1E3A5F',
        },
        text: {
          primary: '#0F172A',
          secondary: '#334155',
          muted: '#64748B',
          inverse: '#FFFFFF',
        },
        feedback: {
          success: '#15803D',
          warning: '#B45309',
          error: '#B91C1C',
        },
      },
      spacing: {
        '2': '2px',
        '4': '4px',
        '6': '6px',
        '8': '8px',
        '10': '10px',
        '12': '12px',
        '14': '14px',
        '16': '16px',
        '20': '20px',
        '24': '24px',
        '28': '28px',
        '32': '32px',
        '36': '36px',
        '40': '40px',
        '44': '44px',
        '48': '48px',
        '56': '56px',
        '64': '64px',
        '72': '72px',
        '80': '80px',
        '88': '88px',
        '96': '96px',
        '120': '120px',
      },
      borderRadius: {
        none: '0px',
        sm: '4px',
        md: '8px',
        lg: '12px',
        xl: '16px',
        full: '9999px',
      },
      boxShadow: {
        sm: '0 1px 2px 0 rgba(15, 23, 42, 0.05)',
        md: '0 4px 6px -1px rgba(15, 23, 42, 0.07), 0 2px 4px -2px rgba(15, 23, 42, 0.05)',
        lg: '0 10px 15px -3px rgba(15, 23, 42, 0.08), 0 4px 6px -4px rgba(15, 23, 42, 0.04)',
        hover: '0 20px 25px -5px rgba(15, 23, 42, 0.10), 0 8px 10px -6px rgba(15, 23, 42, 0.04)',
      },
      fontFamily: {
        heading: ['"Plus Jakarta Sans"', 'sans-serif'],
        body: ['Inter', 'sans-serif'],
      },
      fontSize: {
        caption: ['12px', { lineHeight: '16px' }],
        small: ['14px', { lineHeight: '20px' }],
        body: ['16px', { lineHeight: '24px' }],
        'body-large': ['18px', { lineHeight: '28px' }],
        h3: ['24px', { lineHeight: '32px' }],
        h2: ['32px', { lineHeight: '40px' }],
        h1: ['40px', { lineHeight: '48px' }],
        display: ['56px', { lineHeight: '64px' }],
      },
    },
  },
  plugins: [],
}

