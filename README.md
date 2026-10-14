# Panel Response Imputation

Can calibrated decision models (Jev-like) impute a panelist's missing survey responses from
demographics and purchase history better than donor hot-deck?

## Problem

A panelist with missing responses has answered none of the questions in the query. The goal is to
predict that full response profile from what is known about the panelist: their demographic
profile and their purchase history.

## Evaluation setup

- Panelists are split into training, validation, and test sets.
- **Training:** demographic profile, purchase history, and full response profile are available.
- **Validation:** response profiles are hidden from the method; the set may be used for tuning.
- **Test:** response profiles are hidden and the set is never exposed to the method; it is used
  only for the final evaluation.
- **Metric:** accuracy of the predicted responses.
- **Benchmark:** random donor allocation — each recipient receives the full response profile of a
  randomly assigned donor (hot-deck imputation).

## Data

Harvard Dataverse, DOI [10.7910/DVN/YGLYDY](https://doi.org/10.7910/DVN/YGLYDY). The raw archive
is kept under `data/raw/archive/`.

## Status

Early exploration. No methods implemented yet.
