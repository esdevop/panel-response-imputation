# panel-response-imputation

> **This file is yours.** The template never overwrites it. The rules the assistant follows live
> in `ai-sandbox/RULES.md` and are replaced on upgrade — edit those there and the edit is lost.

## About this project

Whether calibrated decision models (Jev-like) can impute a panelist's missing survey responses
from their demographic profile and purchase history better than donor hot-deck. A panelist with
missing responses has answered none of the questions in the query; the method predicts the full
response profile. Methods are compared on accuracy against a random-donor hot-deck benchmark,
using a train / validation / test split of panelists in which the test set is never exposed to
the method.

R&D project. The method is being discovered, not implemented from a specification.

Knowledge arrives through discussion, vendor documentation (TypeSafe / Jev), and analysis of one
public dataset (Harvard Dataverse, DOI 10.7910/DVN/YGLYDY), kept under `data/` and never
committed. The analysis runs in Python with a project-level `uv` environment — see
`ai-sandbox/DATA_ENVIRONMENT.md`.

@ai-sandbox/ASSISTANT_PROFILE.md

## Session entry point

@ai-sandbox/RULES.md

@ai-sandbox/INDEX.md

## First run in a new clone

`core.hooksPath` and `user.email` live in `.git/config`, which **`git clone` never copies**. The
hook *file* travels with the repository; the setting that runs it does not. A fresh clone has
`.githooks/pre-commit` sitting in the working tree doing nothing, and git gives no warning that
anything is off. Every contributor runs these once, per clone:

```bash
git config core.hooksPath .githooks        # runs the secret scan — nothing else does
git config user.email "you@example.org"    # this clone's identity
```

**Assistant: check both at session start**, before other work. `./check.sh` reports them in its
first section. If the hooks path is unset, say so and stop there — until it is set, the one check
whose failure a later edit cannot repair is not running. If `user.email` is empty, ask for it;
never infer it from commit history or from another file.

If the project has CI, run the same secret scan there as well. It is the only layer that does not
depend on how an individual clone is configured.

## Commits

Conventional Commits. Types used here: `docs`, `feat`, `fix`, `refactor`, `chore`, `exp`.
