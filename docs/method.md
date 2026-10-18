# panel-response-imputation — Method

- **Updated:** 2026-10-17

> Current best understanding of how the method works. **No history here** — no "we used to
> think". Rationale for contested choices lives in `decisions/`; evidence lives in
> `ai-sandbox/experiments/`.

## Overview

<Intuitive picture first, then the precise description.>

## Steps

## Inputs and outputs

### Survey-column assignment

The study's survey schema and reporting partitions, set on 2026-10-17, are documented in
[sessions/2026-10-17-sensitive-targets-scope-followup.md]:

- **Profile (8):** `Q-demos-age`, `Q-demos-hispanic`, `Q-demos-race`, `Q-demos-education`,
  `Q-demos-income`, `Q-demos-gender`, `Q-demos-state`, and `Q-amazon-use-hh-size`.
- **Targets (11 questions; 15 IDs):** `Q-substance-use-cigarettes`, `Q-substance-use-marijuana`,
  `Q-substance-use-alcohol`, `Q-personal-diabetes`, `Q-personal-wheelchair`, `Q-life-changes`
  (five binary IDs), `Q-sell-YOUR-data`, `Q-sell-consumer-data`, `Q-small-biz-use`, `Q-census-use`,
  and `Q-research-society`.
- **Excluded from this study (3):** `Q-sexual-orientation`, `Q-amazon-use-howmany`, and
  `Q-amazon-use-how-oft`; none is used as a profile input or target.
- **Reporting:** report the five substance/health questions separately; report the five
  `Q-life-changes` IDs and five opinion targets with the other targets.

This records study scope, not predictive performance or the reasons for the exclusions. The
multi-select `Q-demos-race` feature encoding and purchase-derived features are not specified here.

## Evidence

<Which experiments support this, by ID — e.g. `EXP-<YYYY-MM-DD>-<slug>`.>

## Known limitations

## Open questions

- [ ] <question tracked in `ai-sandbox/OPEN_QUESTIONS.md`>
