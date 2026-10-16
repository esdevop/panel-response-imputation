# 2026-10-16 · response signal in demographics and purchase history

- **Status:** closed
- **Tags:** #hypothesis #purchase-signal
- **Configuration:** Solo
- **Participants:** author — AI assistant · brainstorming
- **Signed off:** no

## Objective

Brainstorm whether raw demographic and purchase-history data contain enough signal to recover different kinds of survey responses, and identify a disciplined exploratory path. No raw-data analysis or experiment has yet been run.

## Reasoning

Session opened after clone checks and pull. `./check.sh` confirmed `core.hooksPath=.githooks` and `user.email=esdevop@gmail.com`; `git pull` reported already up to date. The existing project hypothesis and scope are recorded in `AGENTS.md` and the session-indexed project materials. Prior project scoping claims dataset suitability, but its noted accuracy figures are explicitly unverified in the repository (`ai-sandbox/sessions/LOG.md`). Existing questions still leave profile/target column assignment and sensitive targets unresolved (`ai-sandbox/OPEN_QUESTIONS.md`). No prior session-log match specifically addressed behavioral-vs-purchase-linked item signal.

The source register says the dataset contains a complete survey per respondent plus linked Amazon order rows, which permits evaluation against held-out answers [в репозитории: `ai-sandbox/SOURCES.md`, `ai-sandbox/sessions/2026-10-14-project-scoping.md`]. `fields.csv` and the instrument show importantly different target mechanisms: some questions ask about an individual, others about a household or all people sharing the Amazon account; many are opinions, while health/behavior questions explicitly combine respondent, household, and account-sharing group [в репозитории: `data/raw/fields.csv`, `data/raw/survey-instrument-extracted.txt`]. The observed purchase table is therefore not an individual-level diary by construction: the instrument defines the submitted account's purchase rows, but the person responsible for or recipient of each item is not identified [в репозитории: `data/raw/survey-instrument-extracted.txt`].

The survey instrument selected participants with active Amazon accounts and purchase histories since 2018; order histories start at 2018 and end at varying times. This is both useful coverage and a selection/time-window limitation [в репозитории: `data/raw/survey-instrument-extracted.txt`, `ai-sandbox/CAVEATS.yaml`]. Prior profiling found category-label noise, long-tailed categories, missing title/category rows, and different observation-window lengths [в репозитории: `ai-sandbox/CAVEATS.yaml`]. These are potential attenuation mechanisms, not evidence that purchase signal is absent.

The categorical examples suggest item-specific plausibility, not a general guarantee: disability-related or smoking-related purchases could be evidence for a household/account-level report, but purchases do not establish who uses them; no purchase is not evidence of no condition or behavior. Attitude questions about data-sale/use appear especially unlikely to have a direct product-level mechanism, though demographics and broad consumption patterns might correlate indirectly [гипотеза]. Confirm or reject these claims with validation-only feature ablations and item-level comparisons, not intuition or test-set probing.

## Decisions

No scientific conclusion was settled, and no experiment was run. The broad hypothesis should be assessed item by item, distinguishing direct purchase-history mechanisms from indirect associations. No claim is promoted to `docs/`.

## Found along the way

The session-start search step found no session-log hit for the specific behavioral/purchase-history signal question. The local archive exists but is not extracted into the working tree; archive listing and the already-extracted field/instrument documentation were inspected. No respondent-level analysis was run. The archive is raw data and must remain uncommitted (`ai-sandbox/SOURCES.md`).

## Next

The user reports that `Q-sensitive-targets` has been resolved independently and wants to document that resolution first. The resolution itself has not yet been provided or recorded here; do not infer it or close the register entry. After it is documented, open a follow-up session to choose the item-level validation protocol and continue the signal investigation. For a recorded experiment, follow `ai-sandbox/playbooks/run-experiment.md`, including committed analysis code before the run. No raw-row analysis was performed in this session.
