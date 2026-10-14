# 2026-10-14 · project scoping and memory adoption

- **Status:** closed
- **Tags:** #scoping #memory-adoption #jev
- **Configuration:** Solo
- **Participants:** author — Claude Opus 5.5 (Claude Code), with esdevop
- **Signed off:** no

> `open` means **this session, right now**. Append to this file as the session runs —
> a decision reached is a decision written down, not something to reconstruct at the end.
> `checkpoint.md` sets it to `closed`, after which the file is immutable.
>
> Any `open` file that is **not** the current session is an interrupted one. Freeze it as
> `abandoned` exactly as it stands; never backfill from memory.
>
> **Participants matters only when the configuration has a check step** — independence is a
> property of the pair doing the checking, not something the configuration's name alone
> recovers. Review by a model of the same family as the author does not count as independent
> and does not license `Signed off:` on its own.

---

## Objective

Explore the repository and dataset, decide whether the dataset supports the intended study
(imputing a panelist's full missing response profile from demographics and purchase history,
benchmarked against random-donor hot-deck), assess Jev as a candidate method, name the project,
and adopt the rnd-project-memory skeleton.

> This file was created after most of the session had already run — the memory system was
> adopted mid-session. Everything below the Objective is written from the session as it stood at
> adoption, not appended live.

## Reasoning

**Dataset fit.** The archive [S-dataverse-yglydy] holds `survey.csv` (5,027 panelists, 23
columns) and `amazon-purchases.csv` (1,850,717 rows), linked by `Survey ResponseID`. Every
panelist has a complete survey, so hiding a response block gives exact ground truth — the study
design fits. Natural missingness is almost absent; evaluation therefore rests on deliberate
hiding, as the user's design already specifies. Data traps found during profiling are in
`CAVEATS.yaml` (subjects `survey.csv:*`, `amazon-purchases.csv:*`). Profiling scripts ran from a
temporary scratch directory with the standard library only, outside the repository; no `uv`
environment was created. Their outputs are summarised here and in the registers, not stored as
`results/` files — re-derive them before citing any number in `docs/`.

**Benchmark strength.** Expected accuracy of a random donor on one question is Σp²; predicting the
most common answer gives max p. Over 15 candidate target questions on the full survey: random
donor 0.531, mode 0.635. Any method that leans toward common answers beats the benchmark without
using panelist information, so mode and cell-mode baselines are required before the benchmark
comparison means anything. Accuracy also rewards collapsing to the mode, which hot-deck does not
do by design (`Q-metric-beyond-accuracy`).

**Jev.** Read the launch post and documentation [S-typesafe-jev-launch, S-typesafe-docs]. Jev
takes a text/JSON state plus typed questions and returns per-option probabilities; no fine-tuning
is documented; one model, `jev-1.13`, with a 32k token budget and documented weaknesses (option
order, numbers, dates, long states — see `CAVEATS.yaml`, subject `jev-1.13`). Since the design
allows training on a training split, Jev's question becomes whether general knowledge adds to what
a supervised model learns from ~3,000 training panelists. Ways for training data to reach Jev:
validation-based recalibration (prior-shift correction changes argmax; temperature scaling does
not), Jev answers as features for a gradient-boosting model, or examples in the state.

**An earlier AI answer the user brought in** proposed Jev as a zero-shot rung of a "validation
ladder" and cited SocioBench results for an "InnerJev-27B" model and election simulations. None of
these appear in the vendor's blog, documentation or a web search on 2026-10-14. Treat those
figures as unverified, possibly fabricated; the structural ideas (ladder, calibration on holdout,
multiple imputation from the distribution) stand on their own.

**Features and methods.** The user proposed grouping SKUs into categories, aggregating behaviour
(buyer flags, spend per period), turning numeric aggregates into soft-binned compositions with
triangular membership, and comparing them with Hellinger distance for k-NN. Refinements
discussed: Hellinger suits unordered compositions and tolerates zeros, unlike log-ratio
distances; for ordered bins an earth mover's distance keeps the order; share of wallet across
category groups is a second natural composition; "zero spend" as its own crisp bin replaces a
separate buyer flag; scaling solves comparability but not relevance, so a block weight between
demographics and purchases is tuned on validation; one-donor k-NN keeps whole-profile coherence,
which per-question feature weights would break. Coarse category grouping can erase rare but
informative categories (`Q-category-grouping`).

**Tabular base.** One panelist feature table in raw units is shared by all methods; each method
applies its own transform (soft bins for k-NN, raw values for gradient boosting, labelled bins
for Jev, which takes JSON state). Targets, split and predictions share one format and one
evaluator.

**Retrainable Jev-like options on this machine** (i5-12500H, 7.6 GiB RAM visible in WSL, RTX 3050
Ti with 4 GB): TabPFN (pretrained tabular model, in-context prediction, fits ~3k rows),
a small open LLM scoring answer options (≈0.5B comfortable, ≈1.5B tight in 4-bit, 7B+ not
local), or an encoder classifier. They test different hypotheses from Jev's and are not
substitutes for it.

## Decisions

- Project renamed `panel-response-imputation` (pyproject, README). The directory is still
  `zero-shot-imputer`; the user renames it after the session.
- rnd-project-memory v3.5.0 installed (skeleton @ dbdaec6); first thread `baseline-ladder`, held
  by esdevop@gmail.com. `Owner:` fields use the name esdevop, as instructed.
- `data/` added to `.gitignore` above the upstream marker.
- `refactor` added to the commit types in `AGENTS.md`; `ASSISTANT_PROFILE.md` imported there.
- Remote `origin` set to https://github.com/esdevop/panel-response-imputation (empty on
  2026-10-14).
- Closed with `checkpoint.md`: no promotion candidates (every number from this session is still
  unverified inside the repository); `CHECKPOINT-baseline-ladder.md` stands as written. First
  commit made on `master`, not pushed.

## Found along the way

- Claude Code reads `AGENTS.md` natively only while no `CLAUDE.md` exists
  (`C-claude-md-shadows-agents-md`).
- The template installer lists setting `user.email` as a todo even when it is already set
  (`C-installer-email-todo-false-positive`) — a defect to report upstream.
- The pre-commit hook does not block `.zip` (`C-precommit-hook-allows-archives`).

## Next

- Resolve `Q-profile-vs-target-columns` and `Q-sensitive-targets`, then build the feature table,
  target table, fixed split, and the random-donor, mode and cell-mode baselines as experiments.
- Fill `docs/problem.md` (one blank remains) — a `docs/` change, reviewed before it lands.
- Verify instruction loading in a fresh session: ask for a rule that appears only in `RULES.md`.
