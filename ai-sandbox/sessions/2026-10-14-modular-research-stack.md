# 2026-10-14 · Modular research stack and gated experimentation

- **Status:** closed
- **Closed:** 2026-10-15
- **Tags:** #stack #framework #architecture #contracts
- **Configuration:** Solo
- **Participants:** user; assistant — brainstorming partner (no independent review)
- **Signed off:** no

## Objective

Define the Python technical stack and module boundaries for an exploratory research framework on one frozen dataset. The user explicitly requested opening this session. This is not production software and need not generalize to other datasets.

## Reasoning

### Opening requirements supplied by the user

- Prioritize convenient exploration, flexibility and high-level abstractions.
- Allow user-defined models, features, data transformations and metrics.
- Compose the workflow from modules that can be added, removed or replaced while retaining shared modules.
- Use gates to enable or disable new functionality for testing without breaking the overall workflow.
- Share raw-to-model data preparation where suitable across models.
- Use common evaluation across models for comparable results.

### Repository context checked at opening

- Clone hooks and email are configured; `git pull` reported already up to date.
- The active `baseline-ladder` checkpoint describes pending profile/target decisions and lower-rung baselines; it is dated today, so no staleness notice is due.
- The previous research-framework session is already marked abandoned and logged as interrupted; it contains only a header, not design conclusions.
- Pre-existing changes to that session file and `sessions/LOG.md` are left untouched.
- `DATA_ENVIRONMENT.md` specifies Python 3.13 and project-local uv, with environment creation still pending in its recorded state.

### Module boundaries and gates discussed

The assistant proposed a small research package rather than a general-purpose workflow platform:

`canonical tables + fixed split -> feature blocks -> model-specific preparation -> model adapter -> standard predictions -> shared evaluation`

Shared preparation does not require every model to consume the same final matrix. Learned transformations must be fitted without validation/test leakage. The user agreed to the proposed module boundaries and added that evaluation should return/save metric tables, while representation and cross-comparison of models or runs should belong to a separate module.

The assistant subsequently proposed keeping metric computation separate from persistence: evaluation returns tables, simple run-storage functions save them, and reporting/comparison consumes them. This finer storage boundary has not yet been explicitly approved. Checking split, targets, metric definitions and aggregation rules before comparison is also an assistant proposal, not an implemented guarantee.

The user fully agreed to gates at experiment assembly rather than scattered conditional branches. Proposed properties are: disabled components preserve the baseline workflow; enabled components satisfy the same contracts; resolved component selection is recorded; incompatible combinations fail explicitly before training rather than silently substituting inputs.

The user also agreed with the risk of premature framework design and with validating the architecture through a small vertical slice: common data, random-donor and mode baselines, one evaluator, and one switchable feature block.

### Technical stack discussion — candidates, not final selections

The initial assistant proposal was Python 3.13 + uv, pandas + NumPy, Parquet/PyArrow, scikit-learn, JupyterLab, Matplotlib/seaborn, dataclasses + typing.Protocol, pytest + Ruff, and local JSON/Parquet run artifacts. No orchestration platform, plugin discovery, MLflow or dedicated configuration framework was proposed for the initial implementation.

The user mostly agreed with the stack but asked to consider Polars instead of pandas, Pydantic instead of dataclasses, and abstract base classes instead of Protocol. The user also suggested YAML for data contracts and metadata and asked whether Pydantic should implement data contracts. These requests are proposals for evaluation, not final approval of the replacements.

The assistant's revised recommendation, still awaiting approval and implementation checks:

- Use Polars as the main table layer, converting to NumPy or another model-specific input format at adapter boundaries. Do not assume all model libraries accept Polars or that pandas can be absent from transitive dependencies. Performance and compatibility have not been measured here.
- Use Pydantic for experiment configuration, gate settings, run metadata and declarative contract specifications. Keep bulk tables in Polars rather than creating one Pydantic object per row. Reject unknown configuration fields and inappropriate coercions where they could conceal mistakes.
- Distinguish YAML serialization, Pydantic validation of a contract specification, and validation of actual tables against that specification. Pydantic validation of metadata alone does not establish table correctness.
- Use YAML for human-authored settings and stable declarative specifications; prefer generated JSON for completed-run metadata and Parquet for tables. Avoid duplicating every Python type in YAML.
- Start table checks with required columns, types, nullability, key uniqueness and needed value constraints. Check cross-table invariants separately: disjoint splits, expected participant IDs and target coverage, and explicit ID alignment rather than reliance on row order. Avoid building a general contract language; retain ordinary Python checks where clearer.
- Use abc.ABC for a few extension points such as Model, FeatureBlock and, if needed, learned Transformer. Wrap third-party implementations in small adapters. Simple metrics may remain functions. ABC does not replace signature checks, behavioral tests or output validation.
- Retain separate evaluation and reporting/comparison modules, with local artifacts rather than a tracking service initially.

The main objections discussed were premature abstractions, adapter friction, and a custom YAML contract language growing into a separate project. The proposed test of the design is practical extensibility in the small vertical slice, not architectural completeness. No library documentation verification, compatibility test, benchmark or experiment was performed during this discussion.

### Predictions and metric-table contracts — agreed initial direction

The user agreed to the proposed contracts below and explicitly confirmed that the first stage supports categorical targets only. Multi-select questions are represented as separate binary targets. This agreement does not select the actual survey target columns or resolve treatment of sensitive items.

Predictions:

- Long-format table with `participant_id`, `target_id`, and `predicted_label`, using canonical answer codes.
- One artifact belongs to one run and one evaluation partition; run/split identity lives in artifact metadata and is added as columns when combining artifacts.
- Unique participant/target pairs, complete expected coverage, no unexpected pairs, and labels from each target's declared domain.
- Missing predictions fail validation rather than being silently excluded. Ground truth remains separate and is joined by explicit keys.
- Optional probabilities are a separate long-format table with `participant_id`, `target_id`, `label`, and `probability`. For each covered target, require complete class coverage and finite probabilities in [0, 1] summing to one within a tolerance still to be specified.
- Predicted labels need not be probability argmax: sampling is allowed, with the selection rule and seed recorded.

Evaluation outputs:

- `metrics_by_target`: `target_id`, `metric_id`, `value`, `n_eligible`, `status`, `reason`; unique target/metric pairs per evaluation.
- `metrics_summary`: `metric_id`, `aggregation_id`, `value`, `n_targets`, `n_observations`, `status`, `reason`.
- Status distinguishes valid results from mathematically undefined metrics; execution failures and invalid inputs remain errors. Counts describe included observations, not a universal denominator for every metric.
- Within-run metric aggregation belongs to Evaluation; cross-run comparison and presentation belong to Reporting/Comparison. Macro and pooled aggregation must have explicit, distinct definitions.
- A generated evaluation manifest links `evaluation_id`, `run_id`, `dataset_snapshot_id`, `split_id`, `evaluated_partition`, `target_schema_version`, `evaluation_spec_id`, and `prediction_artifact_id`.
- The evaluation specification records metric definitions/versions/parameters, eligibility and aggregation rules. Saved predictions may be evaluated again without retraining, producing a new evaluation ID for the same run.

The proposed implementation assigns specification/manifest validation to Pydantic and actual table checks to Polars-based validation; library choices remain subject to the outstanding stack confirmation. Models may use other internal representations and convert at their output boundary. These contracts have not been exercised in code.

Open details include missing-ground-truth eligibility, canonical binary labels, multi-select missingness semantics, probability tolerance, concrete metric definitions, and aggregate weighting of binary targets derived from a common question.

## Decisions

User-approved discussion direction:

- Adopt the proposed module boundaries, separating shared tables/features from model-specific preparation.
- Separate metric evaluation from representation and cross-comparison; evaluation produces metric tables.
- Assemble gates centrally, preserving the disabled baseline and recording enabled components.
- Validate the design with the small vertical slice before expanding the framework.
- Adopt the initial predictions, optional probabilities, metric-table and evaluation-manifest contracts described above, subject to unresolved details and implementation validation.
- Limit initial targets to categorical outcomes; represent multi-select questions as separate binary targets.
- Encode blank life-change responses as five eligible zeros, per the user's explicit subsequent decision; this does not establish the original export semantics.

The user authorized recording these agreements and the still-unapproved stack alternatives in this session file. Stack replacements, detailed interfaces, storage boundaries and contract schemas remain proposals. This is Solo brainstorming, not independent verification or implementation sign-off. Nothing promoted to `docs/`.

## Found along the way

### Experiment authorized: multi-select encoding and contract mechanics

The user requested an experiment and authorized dependency installation and a pre-run code commit. Question, stated before execution: can the frozen survey and instrument distinguish blank life-change selections from explicit no-selection, supporting 1/0/null targets without inventing ground truth? Prior: explicit coding or instrument evidence may distinguish these states; absent that evidence, the verdict must remain inconclusive.

The run audits encoding only across the survey, without model training, split selection or test-performance evaluation. A separate synthetic example checks eligibility counts and target-macro versus question-macro. These synthetic metrics are not dataset performance.

The existing `C-life-changes-blank-means-none` caveat explicitly marks the none interpretation as inferred. The experiment must not treat it as established. `fields.csv` also describes race as a multi-select question, so life changes must not be assumed to be the only multi-select field.

`pyproject.toml` existed with no dependencies at execution preparation, correcting the older opening description. Added Polars, pytest, and pypdf (for reproducible instrument text extraction); generated uv.lock. The small contract prototype uses standard-library structures, not a production Polars evaluator, and does not certify the full proposed table contract.

The running editor LSP reports unresolved imports despite the configured project environment; a fresh `uvx pyright src/experiments/multiselect_contracts.py tests/test_multiselect_contracts.py` reports zero errors. This is an editor diagnostic discrepancy, not suppressed diagnostics.

### Experiment completed on 2026-10-15

Record: `experiments/EXP-2026-10-15-multiselect-contracts.md`. Analysis code was committed before each execution (`76395f9`, then PDF search fix `9e9027a`). Eleven synthetic tests passed; command-line Pyright reported no project-code errors. Both initial and corrected aggregate artifacts are preserved under `results/`.

Main finding: instrument page 10 includes `None of the above`, but the CSV has zero explicit occurrences and 3,384 blanks among 5,027 rows. The verdict is inconclusive on blank semantics. Nonblank responses round-trip through five binary indicators; 596 rows require option whitespace trimming. There are 22 nonblank raw combinations, not 23. The caveats were qualified with this evidence.

The synthetic example yields target-macro 2/3 versus question-macro 1/2, with five eligible pairs out of six expected. These are invented test data, not model performance. The proposed contract needs `source_question_id` and explicit expected/eligible counts; neither a primary aggregation rule nor definitive missingness policy was selected.

The audit does not certify Polars integration, duplicate-row detection or probability contracts. Treating blanks as unknown is a conservative provisional encoding, not proof of actual nonresponse; excluding them could bias the evaluation population. Next semantic evidence needed: export/cleaning logic or clarification from dataset authors. Nothing promoted to docs; session remains open.

### Subsequent user decision: blank life-change responses are eligible zeros

The user explicitly instructed: convert blank `Q-life-changes` to five zeros and include those rows in evaluation. This replaces the experiment's provisional blank-as-unknown policy for future project workflows. It is an operational decision about published response indicators, not proof of the original export behavior. Missingness policies for other questions are unchanged.

Implemented the narrow transformation in `src/life_changes.py`: fixed five-option vocabulary and stable target IDs, binary string labels, whitespace normalization, and blank strings or parser nulls mapped to five zeros. Unknown or duplicate options fail explicitly. No extra target is created for `None of the above`.

`tests/test_life_changes.py` checks encoding and confirms that all five blank-derived zeros are eligible under the synthetic evaluator. The full suite passes 20 tests; fresh command-line Pyright reports zero errors for the new files. The existing editor import-resolution discrepancy remains. No dataset analysis was rerun; the earlier experiment script, outputs and immutable experiment record remain unchanged. The full pipeline is not implemented yet, so this establishes a tested transformation, not an end-to-end integration.

## Closing assessment

The user asked whether the design is sufficient to proceed to baseline execution and requested closure if so. The session objective is met at design-draft level: module boundaries, shared evaluation, separate comparison, gates, initial artifact contracts and the life-change encoding policy are sufficient to guide a small baseline implementation. Further general architecture discussion is not a prerequisite.

This is readiness to implement, not an already runnable baseline or an assertion that all experiment choices are settled. Exact target columns (including sensitive items), split proportions/seed/IDs and relevant refusal-label eligibility remain to be specified. A per-target accuracy report can avoid choosing an overall aggregation rule initially. Probability contracts, advanced reporting and additional model dependencies need not block random-donor/mode implementation. Pydantic/ABC/YAML remain proposed choices rather than completed integrations.

No promotion to docs in this closure: the architecture is still a Solo draft awaiting the vertical-slice check. The data experiment and its limitations already have their own record. A later deliberate promotion may cover the exercised design and the user-selected encoding policy.

## Next

1. Open a baseline-implementation session: choose the concrete target schema and split specification, then implement random donor and mode against the draft contracts. Keep test evaluation reserved for a final-evaluation experiment.
2. Produce common predictions, per-target validation metrics and saved run metadata. Add a gated feature block only where it tests composition; do not pretend feature-independent baselines validate feature utility.
3. Confirm only the dependencies/interfaces needed by this vertical slice; defer broader framework and aggregate-metric choices.

Session closed; no full baseline pipeline or baseline performance measurement was produced. Final pending changes require a separately confirmed commit.
