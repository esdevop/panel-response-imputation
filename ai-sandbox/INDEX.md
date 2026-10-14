# panel-response-imputation — Session Index

- **Updated:** 2026-10-14

Entry point for every session. Loaded automatically through `AGENTS.md`.

---

## Routing rule

| What | Where |
|------|-------|
| Settled conclusion | `docs/` |
| In-flight reasoning on one thread | `CHECKPOINT-<thread>.md` (one per thread, holder-only write) |
| What happened in a session | `sessions/<date>-<slug>.md` |
| What an analysis produced | `experiments/EXP-<YYYY-MM-DD>-<slug>.md` |
| Where a fact came from | `SOURCES.md` |

`ai-sandbox/` is **not a second copy** of `docs/`. Matured conclusions move out.

---

## Artifacts

| File | Contents | Write mode |
|------|----------|-----------|
| `CHECKPOINT-<thread>.md` | Current unresolved state, one per thread | rewrite, ≤150 lines, holder only |
| `OPEN_QUESTIONS.md` | Active questions (resolved are deleted) | edit |
| `ASSUMPTIONS.md` | What the method bets on | edit |
| `SOURCES.md` | Source register with IDs | append |
| `CAVEATS.yaml` | Data and tool traps, found by subject | append, corrected in place |
| `PUBLICATIONS.md` | What was published externally, and its status | edit |
| `CONFIGURATIONS.md` | Named session configurations and what basis each licenses | edit |
| `DATA_ENVIRONMENT.md` | How to obtain data and run analyses | edit |
| `RATIONALE.md` | Why each rule exists; failure modes | read on demand |
| `sessions/LOG.md` | One row per session | append only |
| `experiments/LOG.md` | One row per experiment | append only |

---

## Threads

| Thread | Held by (`user.email`) | Status | Since |
|--------|---------|--------|-------|
| `baseline-ladder` | esdevop@gmail.com | active | 2026-10-14 |

---

## Current focus

Build the lower rungs of the method ladder — a shared panelist feature table, a fixed
train / validation / test split, and the random-donor, mode and cell-mode baselines — so that any
later method (k-NN, GBM, TabPFN, Jev) is measured against a known floor. Blocked on decisions
recorded in `OPEN_QUESTIONS.md`: which survey columns are the demographic profile and which are
targets, and whether accuracy alone is the metric.

---

## What a new session does

1. Read this file — including the thread table — then the `CHECKPOINT-<thread>.md` file(s)
   relevant to today's focus, then `OPEN_QUESTIONS.md`.
2. Do not read `docs/` wholesale — open a document when it is actually needed.
3. Ask for the session focus if it was not given.
4. Close with `playbooks/checkpoint.md`.
