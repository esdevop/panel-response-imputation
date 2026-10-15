# panel-response-imputation — Session Index

- **Updated:** 2026-10-15

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

Implement the first baseline slice (random donor and mode) using the modular draft in
`sessions/2026-10-14-modular-research-stack.md`. Architecture discussion is sufficient to start
implementation; choose the concrete targets, refusal-label policy and fixed split specification
before a recorded run. Life-change blanks now map to five eligible zeros. Environment and
encoding tests exist; the runner and split do not. Start with common per-target validation
metrics; broader features, cell-mode and additional metrics can follow. See
`CHECKPOINT-baseline-ladder.md` and `OPEN_QUESTIONS.md` for remaining decisions.

---

## What a new session does

1. Read this file — including the thread table — then the `CHECKPOINT-<thread>.md` file(s)
   relevant to today's focus, then `OPEN_QUESTIONS.md`.
2. Do not read `docs/` wholesale — open a document when it is actually needed.
3. Ask for the session focus if it was not given.
4. Close with `playbooks/checkpoint.md`.
