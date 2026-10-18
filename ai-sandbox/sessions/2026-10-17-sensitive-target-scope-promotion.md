# 2026-10-17 · sensitive-target scope promotion

- **Status:** closed
- **Tags:** #consent #sensitive-targets #target-scope #promotion
- **Configuration:** Solo
- **Participants:** author — AI assistant; user — esdevop
- **Signed off:** esdevop

## Objective

Promote the user-approved survey profile/target/reporting schema to `docs/method.md` and add the
household/account wording caveat to `ai-sandbox/CAVEATS.yaml`. Also clarify the unresolved scope of
the no-publication decision without inferring a policy the user has not specified.

## Reasoning

The user explicitly authorized promotion of the schema and caveat and supplied `esdevop` as the
human sign-off name. The current schema is recorded in
`sessions/2026-10-17-sensitive-targets-scope-followup.md`. The publication-boundary question is
separate: the existing decision says not to publish respondent-level predictions, but does not say
whether this covers repository artifacts, figures, aggregate results, or sharing with collaborators.
No broader interpretation will be written into `docs/` without the user's clarification.

The method document has no existing substantive schema to replace. `docs/CLAIMS.md` has only its
template row. The caveat is grounded in the registered survey instrument citation
`S-dataverse-yglydy §survey-instrument.pdf pp. 9–10`; no response rows are needed to record the
wording trap.

## Decisions

- Promoted the agreed survey schema and reporting partitions into `docs/method.md`, with the
  follow-up session as basis, and indexed the claim in `docs/CLAIMS.md`.
- Added the household/account-inclusive question wording caveat to `ai-sandbox/CAVEATS.yaml`, based
  on the registered survey instrument, pp. 9–10.
- Did not promote a binding interpretation of the no-publication decision. Its scope remains
  unresolved: the current record does not say whether it covers private project storage, restricted
  collaborators, public figures, or aggregate findings.

## Found along the way

- The profile/target assignment includes no purchase-derived features yet; those remain unspecified.
- The five substance/health targets are reported separately; the five `Q-life-changes` IDs and five
  opinion targets are reported with the other targets, as recorded in the source session.

## Next

The approved schema and caveat changes are complete and checked. `Q-publication-boundary` is now
tracked in `OPEN_QUESTIONS.md`. Ask the user to confirm whether the ban concerns only public
release of row-level predictions or also internal storage, collaborator access, and any
per-respondent figures; confirm whether non-identifying aggregate results remain permitted. Do not
draft a delivery constraint or ADR until this boundary is agreed and the ADR's review requirements
are met.
