# panel-response-imputation — Source Register

- **Updated:** 2026-10-14

> Every fact in `docs/` that came from outside is traceable to an ID here.
> Cite as `[S-latency-spec §3.2]`.
>
> **IDs are slugs, not numbers.** A slug names the **document's identity** — `S-arch-spec-v2`,
> `S-kickoff-call-0412` — not the claim you wanted from it. Once assigned it is **never
> changed**: renaming breaks every citation silently, because a stale citation still looks valid.
>
> **Sensitivity governs storage.** `committable` → the file lives in `sources/`.
> `reference-only` → the artifact is **never** placed in the repository; only the pointer is.
> Default is `reference-only`. Committing is a deliberate exception, and it is the one
> decision here that a later edit cannot undo — once committed, it is in git history.

## Never commit

Credentials · tokens · connection strings · PII · raw extracted data · customer names ·
anything whose sensitivity has not been established.

---

| ID | Type | Title | Sensitivity | Date read | Status |
|----|------|-------|-------------|-----------|--------|
| `S-dataverse-yglydy` | dataset | Harvard Dataverse archive, DOI 10.7910/DVN/YGLYDY | reference-only | 2026-10-14 | partial |
| `S-typesafe-jev-launch` | web page | TypeSafe blog: Introducing System One models and Jev | reference-only | 2026-10-14 | ingested |
| `S-typesafe-docs` | web docs | TypeSafe documentation (models, state, jaggedness, cookbooks) | reference-only | 2026-10-14 | partial |
| `S-claude-code-memory-docs` | web docs | Claude Code documentation: How Claude remembers your project | reference-only | 2026-10-14 | partial |

---

## S-dataverse-yglydy · Harvard Dataverse archive, DOI 10.7910/DVN/YGLYDY

- **Type:** dataset doc
- **Origin:** https://doi.org/10.7910/DVN/YGLYDY — local copy `data/raw/archive/dataverse_files.zip`
- **Source date:** not recorded; files inside the archive are dated 2026-10-14
- **Date read:** 2026-10-14
- **Sensitivity:** reference-only — raw data, never committed (`data/` is in `.gitignore`)
- **Status:** partial — main survey instrument text inspected on 2026-10-15, especially
  page 10; prescreen instrument not yet read. See EXP-2026-10-15-multiselect-contracts for
  the main instrument hash, encoding audit and limitations.
- **Answers:** what is observed per panelist (survey answers, purchase history), column semantics
  (`fields.csv`), how questions were asked (`survey-instrument.pdf`, `prescreen-survey-instrument.pdf`)
- **Notes:** contents — `survey.csv` (5,027 panelists × 23 columns), `amazon-purchases.csv`
  (1,850,717 rows; order date, unit price, quantity, shipping state, title, ASIN, category,
  response ID), `fields.csv` (question wording). Linked by `Survey ResponseID`. Dataset identity
  and version: see `A-dataset-is-open-ecommerce` and `Q-dataset-version`. Data traps:
  `CAVEATS.yaml`, subjects `survey.csv:*` and `amazon-purchases.csv:*`.

## S-typesafe-jev-launch · TypeSafe blog: Introducing System One models and Jev

- **Type:** web page (vendor announcement)
- **Origin:** https://typesafe.ai/blog/introducing-system-one-models-and-jev
- **Source date:** not recorded
- **Date read:** 2026-10-14
- **Sensitivity:** reference-only
- **Status:** ingested
- **Answers:** what Jev is — typed decisions with per-option probabilities, no text generation;
  vendor latency and cost claims
- **Notes:** all performance figures are vendor-reported; no calibration curves are published.
  The page does **not** mention SocioBench, an "InnerJev-27B" model, or election simulations.

## S-typesafe-docs · TypeSafe documentation

- **Type:** web docs (mutable)
- **Origin:** https://docs.typesafe.ai — pages read: `/introduction`, `/models.md`,
  `/concepts/state.md`, `/model-jaggedness/jev-1.13.md`,
  `/cookbooks/autoresearch_feature_discovery.md`, index `/llms.txt`
- **Source date:** not recorded
- **Date read:** 2026-10-14
- **Sensitivity:** reference-only
- **Status:** partial
- **Answers:** API shape (state as text or JSON; `Choice` / `Score` / `Noul` questions; `Choice`
  returns `choice`, `probabilities`, `confidence`), limits and known weaknesses of `jev-1.13`
- **Notes:** one model listed, `jev-1.13.0`: 32k token budget for state plus the longest question,
  $0.042 per million input tokens, 100K tokens/s and 80 requests/s. No fine-tuning or few-shot
  feature documented. Known weaknesses: `CAVEATS.yaml`, subject `jev-1.13`. Mutable — re-read
  before relying on a limit or price.

## S-claude-code-memory-docs · Claude Code documentation: How Claude remembers your project

- **Type:** web docs (mutable)
- **Origin:** https://code.claude.com/docs/en/memory
- **Source date:** not recorded
- **Date read:** 2026-10-14
- **Sensitivity:** reference-only
- **Status:** partial — the `AGENTS.md` section only
- **Answers:** whether Claude Code loads `AGENTS.md` and its `@` imports
- **Notes:** from v2.1.277 Claude Code reads `AGENTS.md` natively and expands `@` imports, **but
  only when no `CLAUDE.md`, `.claude/CLAUDE.md` or `CLAUDE.local.md` exists in the working
  directory or above it**; `~/.claude/CLAUDE.md` does not count. Installed version on 2026-10-14:
  2.1.299. See `C-claude-md-shadows-agents-md`.
