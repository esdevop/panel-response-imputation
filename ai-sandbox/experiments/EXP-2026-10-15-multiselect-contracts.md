# EXP-2026-10-15-multiselect-contracts

- **Date:** 2026-10-15 · **Status:** complete
- **Question:** Can the frozen survey and instrument distinguish blank life-change selections from explicit no-selection, supporting binary targets without inventing ground truth?

## Reproducibility

| Field | Value |
|-------|-------|
| Git SHA | `9e9027a6a11509484aa8c7c817dde5eda15af067` (final run); `76395f95a7448957929e80bbc03295d3992ba0b0` (initial run) |
| Environment lock | `uv.lock`, SHA256 `20570fbc44d81f1794051ac61105faa5826c1c46deba46e5e81c2704dce5c4b6` |
| Entry point | `src/experiments/multiselect_contracts.py` |
| Data source | S-dataverse-yglydy; local `data/raw/archive/dataverse_files.zip`; archive SHA256 `cfdf3aebd0d6d3516e28a927446a4ecf9d4ea751eb6b3dc436924042fde239c6` |
| Snapshot date | Local snapshot downloaded 2026-10-14 per DATA_ENVIRONMENT.md; read 2026-10-15T15:55:53.270486+00:00. Dataverse version remains unknown; member hashes are in results. |
| Filters / slice | Full survey for encoding counts; life-changes for binary encoding; fields and survey instrument for semantics. No purchase data, model fitting, split construction or test-performance evaluation. |
| Runtime / compute | Python 3.13.7, Linux x86_64 WSL2; local single-process script. Polars 2.0.0, pytest 9.1.1, pypdf 6.20.1. Polars installed but not used by this prototype. |
| Run duration | Final analysis 0.3802241049997974 seconds, as measured inside the script; excludes dependency setup and tests |
| Run ID (remote/async) | n/a — ran locally |

Commands:

```bash
uv sync --locked
uv run --locked pytest -q
uv run --locked python src/experiments/multiselect_contracts.py --output results/multiselect-contracts-rerun.json
```

Evidence: `results/multiselect-contracts-v2.json` (final), `results/multiselect-contracts.json` (initial), and `tests/test_multiselect_contracts.py`. Raw archive and extracted instrument text are intentionally gitignored, not repository evidence files; hashes, aggregate results, page references, and the extraction script stand in for them. No participant-level records are saved in tracked artifacts.

## Setup

Prior, recorded before running: explicit coding or instrument evidence might distinguish missing from none; absent such evidence, remain inconclusive. No model benchmark was attempted. The conservative encoding maps blank to unknown as an explicit provisional policy, not a claim that blanks are genuine nonresponse.

Initial execution used a literal phrase search over extracted PDF text. The PDF separated words with line breaks, so the automated page search missed the question. Reading the extracted text revealed this. A committed fix normalized whitespace and added a regression test before the final execution. The initial output is preserved, not silently overwritten.

A separate, explicitly synthetic example contains two participants, two binary targets from one multi-select question and one binary target from another question. One ground-truth value is unknown. Predictions are deliberately chosen to illustrate aggregation, not learned from data.

## Result

Observed in this frozen snapshot:

- 5,027 survey rows; 3,384 blank life-change responses and 1,643 nonblank responses. Other survey columns have zero blank cells under whitespace-stripped empty-string detection.
- Five observed life-change options and 22 distinct nonblank raw combinations. The older caveat's 23 combinations must not be read as 23 nonblank combinations.
- 596 nonblank rows contain option-boundary whitespace requiring trimming.
- All nonblank responses round-trip through the five binary indicators after whitespace normalization.
- The instrument's page 10 explicitly offers `None of the above`; zero nonblank CSV rows contain that text. The available audit does not establish how that option became a published CSV value or whether blank also represents skipped answers.
- Under the provisional blank-as-unknown policy, each binary life-change target has 1,643 eligible rows and 3,384 unknown rows. These are policy-dependent eligibility counts, not proof of missingness.
- Field wording identifies race as another multi-select question. It has no blank cells, but its encoding was not otherwise audited here.
- Several columns contain refusal labels (`Prefer not to say`, case-insensitive); aggregate counts are preserved. Whether these are valid response-profile labels or excluded ground truth remains a separate policy choice.

Synthetic result only: per-target accuracies are 1, 1, and 0; target-macro is 2/3, question-macro is 1/2. There are five eligible participant-target pairs out of six expected. This demonstrates the effect of source-question grouping and explicitly records the excluded ground truth; it is not survey model performance.

## Verdict

**inconclusive** — binary encoding of nonblank responses works, but the published CSV and static instrument do not establish whether blank means explicit none, skipped response, or a mixture. Do not infer ground truth from the blank cells automatically.

## Verification

- **Verified by:** self
- **How verified:** manual cross-check of extracted instrument page 10; 11 deterministic pytest tests passed, including hand-calculated synthetic metrics, key alignment, invalid coverage/labels, whitespace, and undefined metrics. Fresh command-line Pyright reported zero errors for project script/tests. No independent data recount or external semantic verification was performed.

The editor LSP still reports unresolved imports despite the configured environment; command-line type checking and runtime tests succeed. Third-party library diagnostics surfaced during source navigation are not project-code failures and were not modified.

## What this changes

- Keeps 1/0/null as a viable representation, but does not validate a semantic mapping of this dataset's blank values to either 0 or null.
- Supports preserving `source_question_id` and explicit expected/eligible counts in the proposed contracts; this is a small synthetic mechanics check, not certification of the entire evaluator.
- Requires the dataset's export/cleaning logic or clarification from its authors before choosing definitive life-change eligibility.
- Qualifies the inferred blank-means-none caveat. No conclusion promoted to docs, no target selection or main metric chosen.

## Threats to this result

- Static PDF text does not expose all interactive validation or export behavior; successful extraction is not proof of how a participant's response was stored.
- Observed options are discovered from nonblank responses for this audit only. Production target schemas must be explicit, not learned from held-out labels.
- Whole-survey schema/count inspection sees aggregate outcome information. No predictive performance was measured, but this is not a claim of never having inspected any outcomes.
- Restricting evaluation to nonblank life-change responses could select participants who experienced at least one event, producing a different evaluation population. The conservative policy is not automatically unbiased.
- Dictionary-based synthetic inputs cannot represent duplicate keys; this prototype therefore does not certify duplicate-row detection in future table validators. Probability-table validation, Polars integration, artifact storage and general plugin interfaces are not tested.
- No independent verification, no performance benchmark, and no author clarification of blank semantics.
