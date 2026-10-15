# panel-response-imputation — Checkpoint · baseline-ladder

- **Held by:** esdevop@gmail.com · since 2026-10-14
- **Status:** active
- **Updated:** 2026-10-15
- **Resume from:** architecture draft is sufficient for the first implementation slice. Choose concrete targets and split specification, then implement random donor and mode with shared predictions and per-target validation metrics.
- **Do not do until re-verified:** do not cite session-1 model-performance figures as repository-verified results. Never evaluate the test split outside a final-evaluation experiment. Do not interpret the user-selected blank-as-zero policy as proof of original survey export semantics.

## Current state

- Design draft and decisions: `sessions/2026-10-14-modular-research-stack.md` (closed). Common canonical tables, replaceable feature/model components, centrally assembled gates, shared evaluation, separate comparison. Predictions/metric-table contracts are drafted, not fully integrated.
- Python/uv environment and lock exist. Polars is installed; pytest and pypdf are dev dependencies. Pydantic/ABC/YAML remain proposed integration choices. See `DATA_ENVIRONMENT.md`.
- `src/life_changes.py` implements the user-selected rule: blank life-change responses become five binary zeros and remain eligible. This supersedes the audit's provisional blank-as-unknown policy for future runs.
- Encoding audit: `experiments/EXP-2026-10-15-multiselect-contracts.md`. Original blank semantics remain inconclusive; the operational decision removes this as an implementation blocker.
- Twenty tests pass, covering the audit prototype and new encoding. Fresh command-line Pyright passes; editor LSP import resolution still disagrees. No full baseline runner, fixed split or predictive evaluation exists yet.
- No design promoted to docs; validate the draft through the small implementation slice first.

## Remaining decisions for the first run

1. Concrete target columns and treatment of sensitive items (`Q-profile-vs-target-columns`, `Q-sensitive-targets`). Multi-select binary representation and life-change blank handling are decided, but the full column assignment is not.
2. Fixed split proportions, seed and participant IDs. Use train donors/train-fitted mode and validation evaluation; retain test for final evaluation.
3. Treatment of refusal labels for selected targets. Preserve a common eligibility rule across compared runs.

Per-target accuracy is a proposed minimal first report; extra metrics and target/question aggregation need not block implementation. Do not silently select them as settled scientific choices.

## Implementation slice

Canonical target table and split -> random donor / mode -> standardized predictions -> common per-target metrics -> saved run artifacts. Exercise gate composition without requiring feature-independent baselines to demonstrate feature benefit. Shared purchase features and cell-mode can follow; category grouping and advanced models do not block the first two baselines.

## Promotion candidates

None ready for promotion during this closure. Revisit after the vertical slice validates the design. The explicit blank-as-zero policy can be reviewed in that separate promotion.
