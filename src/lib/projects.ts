import { getCollection, type CollectionEntry } from 'astro:content';

export type Project = CollectionEntry<'projects'>;

export async function getProjects(): Promise<Project[]> {
  const all = await getCollection('projects');
  const rank = (p: Project) => p.data.order ?? Infinity;
  return all.sort((a, b) => rank(a) - rank(b) || a.data.built.getTime() - b.data.built.getTime());
}

export function builtLabel(d: Date): string {
  return d.toLocaleDateString('en-US', { month: 'short', year: 'numeric', timeZone: 'UTC' }).toUpperCase();
}

// Units are numbered in listing order.
export function unitLabel(i: number): string {
  return `UNIT-${String(i + 1).padStart(2, '0')}`;
}

export const AREA_LABEL: Record<Project['data']['area'], string> = {
  markets: 'Markets',
  crypto: 'Crypto',
  cards: 'Trading cards',
  home: 'Home',
  money: 'Personal finance',
};
