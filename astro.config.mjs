import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel/serverless';

export default defineConfig({
  integrations: [tailwind(), vercel()],
  output: 'server',
  adapter: vercel(),
});