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
    label: 'Social media & publishing',
    text: 'Co-authored a travel guide that sold hundreds of copies, and gave away thousands of copies of free info products.',
  },
];

export const EXPERIENCE: Employer[] = [
  {
    org: 'Self-employed',
    dates: '2022 – Present',
    roles: [
      {
        title: 'Contract ML Engineer',
        team: 'VAWN · AI electrical blueprint analysis',
        dates: '2026',
        bullets: [
          'Built fire-alarm device detection on construction drawings from zero: dataset, three model generations, tiled inference, false-positive filtering and the production pipeline. Locked-test F1 0.849; an unseen project scored 41 of 43 devices with zero false positives.',
          'Unified panels detected from single-line diagrams, schedule tables and floor plans into one record with per-field source authority. Breaker extraction rose from 0.596 to 0.872; every cross-source disagreement is logged as one of 19 issue types.',
          'Built labeling tools (template-match proposals, legend viewer, one-click box correction) that cut cross-class false positives from 54 per run to 0.',
          'Shipped chat answers that jump to the referenced panel on the drawing, and an upload flow that runs only the disciplines requested. 381 commits.',
        ],
      },
      {
        title: 'Personal projects',
        team: 'scottsbots',
        dates: '2022 – Present',
        bullets: [
          'MagicStats: daily pipeline over 243 sealed Magic sets and 3,100+ products from 6 sources, plus LLM extraction of 7,100 market calls from 700+ videos.',
          'BiKnow: real-time tracker of 1,000+ curated Solana wallets processing thousands of transactions a day; WalletMatcher clusters wallets the same person controls.',
          'PolyHolders and fomo Wallet Matcher: Chrome extensions that surface who holds each side of a Polymarket bet and the real wallets behind fomo traders.',
        ],
      },
      {
        title: 'Investing & trading',
        dates: '2022 – Present',
        bullets: [
          'ScottStats: real-time charting and breakout alerts over custom universes, including 500+ AI stocks across 20+ subsectors.',
          'Distilled a breakout strategy from a transcribed playlist of trading videos, with every rule cited to a quote and timestamp, then backtested and ported it into ScottStats.',
          'CMR Scorecard: turned 500+ market videos and reports into calls plotted on their charts.',
        ],
      },
    ],
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
