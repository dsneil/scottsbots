import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const projects = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/projects' }),
  schema: z.object({
    name: z.string(),
    built: z.coerce.date(),
    area: z.enum(['markets', 'crypto', 'cards', 'home', 'money']),
    tagline: z.string(),
    stack: z.array(z.string()),
    // live = open the running product; code = public repo; soon = repo going public; none = clip only
    link: z.object({
      kind: z.enum(['live', 'code', 'soon', 'none']),
      url: z.string().url().optional(),
      note: z.string().optional(),
    }),
    // Position on the home page; unordered projects follow, oldest first.
    order: z.number().optional(),
    // Spans the full row on the home page.
    featured: z.boolean().optional(),
    clip: z.string().optional(),
    poster: z.string().optional(),
  }),
});

export const collections = { projects };
