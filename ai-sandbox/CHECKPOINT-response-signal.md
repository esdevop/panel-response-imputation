# panel-response-imputation — Checkpoint · response-signal

- **Held by:** esdevop@gmail.com · since 2026-10-16
- **Status:** active
- **Updated:** 2026-10-17
- **Resume from:** resolve `Q-publication-boundary` before drafting a binding delivery constraint or
  ADR. The user has supplied `esdevop` as the sign-off name for the schema/caveat promotion, but the
  publication rule itself remains underspecified.
- **Do not do until re-verified:** no raw-data predictive evidence exists and no respondent-level
  analysis has been run. Do not evaluate the test split outside a final-evaluation experiment. Do
  not describe household/account-inclusive answers as verified personal traits.

## Current state

- The user-approved survey schema and reporting partition are promoted to `docs/method.md`; the
  household/account-inclusive wording trap is recorded in `CAVEATS.yaml`. See
  `sessions/2026-10-17-sensitive-target-scope-promotion.md` and
  `sessions/2026-10-17-sensitive-targets-scope-followup.md`.
- The existing decision says not to publish respondent-level predictions. It does not specify
  whether this bars private storage, restricted collaborator access, respondent-level figures, or
  only public release; `Q-publication-boundary` tracks clarification. Do not turn an assumed meaning
  into a binding constraint. An ADR also needs a qualifying independent reviewer; the provided
  `esdevop` sign-off name alone does not satisfy that configuration.
- Remaining study-design work: specify targets, metrics, model, and kill criterion for the
  validation-only item-level signal analysis; define `Q-demos-race` feature encoding and
  purchase-derived features. No performance claim is established, and the test split remains
  reserved for final evaluation.

## Next

Ask the user to define the no-publication boundary and whether non-identifying aggregate reporting is
permitted. Then, if a binding policy is still wanted, arrange the required independent review and
sign-off against exact wording. Separately specify the falsifiable validation-only signal analysis
before any run; follow `ai-sandbox/playbooks/run-experiment.md`.
