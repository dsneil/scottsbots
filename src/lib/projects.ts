import { getCollection, type CollectionEntry } from 'astro:content';

export type Project = CollectionEntry<'projects'>;

export async function getProjects(): Promise<Project[]> {
  const all = await getCollection('projects');
  return all.sort((a, b) => a.data.built.getTime() - b.data.built.getTime());
}

export function builtLabel(d: Date): string {
  return d.toLocaleDateString('en-US', { month: 'short', year: 'numeric', timeZone: 'UTC' });
}

const TILTS = ['-1.6deg', '1.1deg', '-0.7deg', '1.5deg', '-1.2deg', '0.8deg', '-1.9deg', '1.3deg', '-0.9deg'];

export function tilt(i: number): string {
  return TILTS[i % TILTS.length];
}

export const AREA_LABEL: Record<Project['data']['area'], string> = {
  markets: 'Markets',
  crypto: 'Crypto',
  cards: 'Trading cards',
  home: 'Home',
  money: 'Personal finance',
};
