# panel-response-imputation — Checkpoint · response-signal

- **Held by:** esdevop@gmail.com · since 2026-10-16
- **Status:** active
- **Updated:** 2026-10-16
- **Resume from:** document the user's independently reached resolution of `Q-sensitive-targets` before opening a follow-up session. The resolution is not yet known to the assistant; ask for its exact decision and basis rather than infer it.
- **Do not do until re-verified:** do not claim raw-data predictive evidence; no respondent-level analysis has been run. Do not delete `Q-sensitive-targets` until its answer is recorded in the relevant session and any durable conclusion has an approved destination.

## Current state

- Brainstorm session: `sessions/2026-10-16-response-signal-brainstorm.md` (closed). The raw instrument distinguishes individual, household, and shared-account questions. Purchase history plausibly offers different signal by item; no predictive claims are established.
- Local source files inspected: `data/raw/fields.csv`, `data/raw/survey-instrument-extracted.txt`; raw archive exists at `data/raw/archive/dataverse_files.zip`. No raw data rows were analyzed.
- Candidate follow-up: compare demographics-only, purchases-only, and combined features for a small, predeclared set of targets, including purchase-linked behaviors versus opinion items. Keep validation separate from the untouched test set. Exact targets, metrics, model, and kill criterion remain to be fixed before running.
- User reports `Q-sensitive-targets` is resolved independently. Record the user's actual resolution first; then determine whether that resolution changes the candidate targets.

## Next

Obtain and document the user's `Q-sensitive-targets` resolution in a dedicated follow-up session. Then agree a falsifiable experiment specification before any run. Do not modify `docs/` based on this brainstorm.
