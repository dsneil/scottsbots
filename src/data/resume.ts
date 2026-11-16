// Resume copy. Sources: LinkedIn experience, the 2015 resume, and each project's repo; no invented numbers.

export const LINKEDIN_URL = 'https://www.linkedin.com/in/dsneil/';

export interface Role {
  title: string;
  team?: string;
  dates: string;
  bullets: string[];
}

export interface Employer {
  org: string;
  place?: string;
  dates?: string;
  // Labeled bullets directly under the employer, for entries without separate roles.
  bullets?: { lead: string; text: string }[];
  roles: Role[];
}

export const EXPERIENCE: Employer[] = [
  {
    org: 'Self-employed',
    dates: '2022 – Present',
    bullets: [
      {
        lead: 'Social media',
        text: 'Work with my wife (@fashionbyally, 1.5M+ followers across platforms) on content creation: strategy, video concepting, videography and photography. Partnered with global brands such as Amazon, Apple, Waymo/Google, Four Seasons, United Airlines, and more. Authored a travel guide that sold hundreds of copies and drove thousands of newsletter subscribers.',
      },
      {
        lead: 'Startup consulting',
        text: 'Trained ML models and built extraction pipelines that turn raw building plans into structured data for pre-construction planning. Iterated on internal training environment to speed up dataset creation and labeling. Improved data models and chat functionality for a better user experience.',
      },
      {
        lead: 'Trading & crypto',
        text: 'Traded and experimented extensively across stocks and crypto, supported by custom research tools I built.',
      },
      {
        lead: 'Personal projects',
        text: 'Built a wide range of projects for trading, crypto and sealed MTG, some shared at scottsbots.vercel.app. General theme across projects is finding datasets and YouTube video catalogs and turning them into actionable tools.',
      },
    ],
    roles: [],
  },
  {
    org: 'Meta',
    dates: '2013 – 2021',
    roles: [
      {
        title: 'AI Product Manager',
        team: 'Messenger Business AI',
        dates: 'Jun 2018 – Jun 2021',
        bullets: [
          'Ads Optimization: grew revenue and business transactions in Messenger through improved ad models and delivery. Led project for future version of Click-to-Message (CTM) ads optimization, partnering closely with privacy, legal, and policy to deliver a compliant strategy.',
          'Quality/Integrity: drove cross-company workstream, aligning group leads, and consistently reducing bad and policy-violating ad experiences in Messenger and CTM ads.',
          'Growth: built person-to-business messaging tools, additionally increasing outcomes and feeding back into model improvements.',
        ],
      },
      {
        title: 'Data Scientist, Analytics',
        team: 'Instagram Core Business',
        dates: 'Feb 2017 – Jun 2018',
        bullets: [
          'Handled sensitive analytics projects around the Instagram API through a complex regulatory environment following Cambridge Analytica.',
          'Sized and prioritized opportunities to help businesses grow on Instagram, partnering with Product and Engineering on the Insights and account-tips roadmap.',
          'Built pipelines and dashboards, filling in gaps for Data Engineering.',
        ],
      },
      {
        title: 'Data Scientist, Analytics',
        team: 'Facebook Videos',
        dates: 'Aug 2014 – Feb 2017',
        bullets: [
          'Led A/B test design, evaluation and ship decisions on new Videos products; informed changes that helped grow Videos to 10B+ daily views.',
          'Covered Performance, Live, Suggested Videos and Facebook Watch.',
          'Scaled analysis capacity via tooling, education and mentoring as the engineering team grew 4x.',
          'Defined core metrics and validated logging with Data Engineering; built datasets and dashboards.',
        ],
      },
      {
        title: 'Product Analyst Intern',
        team: 'Facebook Groups',
        dates: '2013',
        bullets: ['Sized and prioritized growth opportunities for Groups, regularly sharing work with senior leadership. Defined metrics, built pipelines and dashboards to support team’s analysis.'],
      },
    ],
  },
  {
    org: 'Other',
    bullets: [
      { lead: 'Periscope Capital', text: 'Investment Assistant / Technical Lead' },
      { lead: 'BMO Capital Markets', text: 'Fixed Income / Money Market Trading Analyst' },
    ],
    roles: [],
  },
];

export const EDUCATION = {
  school: 'University of Waterloo',
  degree: 'BASc, Systems Design Engineering',
};
