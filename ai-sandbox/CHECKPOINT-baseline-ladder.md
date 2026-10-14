# panel-response-imputation — Checkpoint · baseline-ladder

- **Held by:** esdevop@gmail.com · since 2026-10-14
- **Status:** active
- **Resume from:** no code, environment or split exists yet; the next step is deciding the
  profile/target column split (`Q-profile-vs-target-columns`, `Q-sensitive-targets`), then
  building the feature table, target table and a fixed train / validation / test split.
  **Do not do until re-verified:** cite any profiling number in `docs/` before it is re-derived
  inside the repository as an `EXP-…` record — the session-1 numbers came from scripts outside it.
  Never evaluate on the test split outside a final-evaluation experiment.

> **This file belongs to one thread, named for what is being worked on, not who is doing it.**
> `Held by:` is the exact output of `git config user.email` in your clone — never initials,
> never inferred. Only whoever this file names writes it; other `CHECKPOINT-*.md` files are
> colleagues' threads and are read-only to you. Taking over a thread is an event — record it in
> your session file and in `sessions/LOG.md`, don't just edit the field.
>
> Only what is **in progress and not yet settled** in `docs/`. This file is **rewritten**, not
> appended. Delete what is no longer true — do not strike it out.
> An entry unchanged for 3+ weeks is a conclusion, not a process: promote it.
> Write each entry so someone who missed the session could act on it — in three months,
> that someone is you.
>
> **No personal reasoning here.** What was tried, what didn't make sense, what is suspected —
> that lives in the session file. This file holds facts about the thread: where it stands, what
> not to trust yet, what not to do until that changes.
>
> **If this thread has a `Plan:` file**, this checkpoint does not restate it. No task
> identifiers (e.g. `T-###`) belong in this header — if they start appearing here, the pointer
> has stopped working and needs a mechanical check, not a reminder. State for a planned thread
> lives in three places, jointly: the plan (contract — tasks, dependencies, gates), run
> artefacts (what actually happened — produced by execution, never written by hand; a missing
> artefact means "not yet certified", not "assume it's fine"), and this header (what artefacts
> can't express: distrust and prohibitions).
>
> **Closing a thread** splits what's left to both addresses at once, never a choice between
> them: settled parts go to `docs/` via `promote.md`, anything still hanging becomes one
> `OPEN_QUESTIONS.md` entry — then this file is deleted. Nothing is lost for facts; each already
> has a single-purpose home elsewhere. What has no other home is the synthesis of holding
> several sessions' state together in one place — accept that as the real, bounded cost of
> closing, not a gap to work around.

---

## Current state

| Item | Value | Source |
|------|-------|--------|
| Random-donor expected accuracy, mean of 15 candidate targets | 0.531 (unverified in repo) | sessions/2026-10-14-project-scoping.md |
| Mode imputation accuracy, same questions | 0.635 (unverified in repo) | sessions/2026-10-14-project-scoping.md |
| Python environment | not created — no `uv.lock`, no `.venv` | — |

---

## In progress

### Gap 1 — profile/target split of the survey columns (priority: high)

Blocks every baseline. Depends on `Q-profile-vs-target-columns` and `Q-sensitive-targets`.

### Gap 2 — baseline ladder, lower rungs (priority: high)

Random donor, mode, cell-mode, each recorded as an `EXP-…` with `results/*.json`. Depends on Gap 1
and on the shared feature table, target table and split.

---

## Promotion candidates

None yet.

---

## Out of scope for this session

Jev, TabPFN and k-NN runs — they need the lower rungs first.
