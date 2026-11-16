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
  dates: string;
  // Labeled bullets directly under the employer, for entries without separate roles.
  bullets?: { lead: string; text: string }[];
  roles: Role[];
}

export const SINCE_2022: { label: string; text: string }[] = [
  {
    label: 'Personal projects',
    text: 'Designed, built and shipped 9 tools end to end: market dashboards, Chrome extensions, on-chain analytics and market-data pipelines, several running daily.',
  },
  {
    label: 'Contract startup work',
    text: 'Contract ML engineer at VAWN, an AI tool that reads electrical construction drawings. Took fire-alarm detection from nothing to 0.849 F1 on a locked test set and unified panel data across 3 sources.',
  },
  {
    label: 'Investing & trading',
    text: 'Invest and trade across stocks, crypto, prediction markets and sealed collectibles, using research tools I built for each market.',
  },
  {
    label: 'Social media',
    text: 'Content creation with @fashionbyally (1.5M+ followers across platforms) for brands such as Amazon, Apple, Waymo/Google, Four Seasons and United Airlines. Authored a travel guide that sold hundreds of copies.',
  },
];

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
        lead: 'Trading & crypto',
        text: 'Traded and experimented extensively across stocks and crypto, supported by custom research tools I built.',
      },
      {
        lead: 'Startup consulting',
        text: 'Trained ML models and built extraction pipelines that turn raw building plans into structured data for pre-construction planning. Iterated on the internal data engine (labeling and training tooling) to speed up dataset creation and labeling. Improved data models and chat functionality for a better user experience.',
      },
      {
        lead: 'Personal projects',
        text: 'Built a wide range of projects for trading, crypto and Magic: The Gathering cards, some shared at scottsbots.vercel.app. Common thread: finding datasets and YouTube video catalogs and turning them into actionable tools.',
      },
    ],
    roles: [],
  },
  {
    org: 'Facebook',
    place: 'Menlo Park, CA',
    dates: '2014 – 2021',
    roles: [
      {
        title: 'AI Product Manager',
        team: 'Messenger Business AI',
        dates: 'Jun 2018 – Jun 2021',
        bullets: [
          'Click-to-Message ads: grew revenue and adoption by improving ad delivery and models, driving more business outcomes in Messenger.',
          'Quality and integrity: reduced bad and policy-violating ads across Messenger and Click-to-Message.',
          'Growth: increased business outcomes from person-to-business conversations, feeding better models and more valuable conversations.',
          'Also covered privacy for Messenger Business AI.',
        ],
      },
      {
        title: 'Data Scientist, Analytics',
        team: 'Instagram Core Business',
        dates: 'Feb 2017 – Jun 2018',
        bullets: ['Growth, Insights, API and Discovery.'],
      },
      {
        title: 'Data Scientist, Analytics',
        team: 'Facebook Videos',
        dates: 'Aug 2014 – Feb 2017',
        bullets: [
          'Led experiment design, evaluation and decisions on new Videos products; informed changes that helped grow Videos to 5B+ daily views.',
          'Covered Performance, Live, Suggested Videos and Facebook Watch.',
          'Scaled the engineering team’s analysis through tooling, education and mentoring as the team grew 4x.',
          'Worked with Data Engineering on datasets, metrics, logging validation and dashboards.',
        ],
      },
      {
        title: 'Product Analyst Intern',
        team: 'Facebook Groups',
        dates: '2013',
        bullets: ['Identified and prioritized growth opportunities for Groups; defined metrics and built pipelines for ongoing analysis.'],
      },
    ],
  },
  {
    org: 'Periscope Capital',
    place: 'Toronto, ON',
    dates: '2012 – 2013',
    roles: [
      {
        title: 'Investment Assistant / Technical Lead',
        dates: '2012 – 2013',
        bullets: [
          'Architected and built the internal accounting system; started the move to technology-centric operations.',
          'Analyzed and improved the automated trading system.',
        ],
      },
    ],
  },
  {
    org: 'BMO Capital Markets',
    place: 'Toronto, ON',
    dates: '2012',
    roles: [
      {
        title: 'Fixed Income / Money Market Trading Analyst',
        dates: '2012',
        bullets: [
          'Co-developed and released a new money-market trading platform.',
          'Built the foundation for a real-time system delivering market and trade data to traders.',
        ],
      },
    ],
  },
];

export const EDUCATION = {
  school: 'University of Waterloo',
  degree: 'BASc, Systems Design Engineering',
  dates: '2009 – 2014',
};
