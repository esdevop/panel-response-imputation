# 2026-10-17 · sensitive targets and survey-scope follow-up

- **Status:** closed
- **Tags:** #consent #sensitive-targets #target-scope
- **Configuration:** Solo
- **Participants:** author — AI assistant
- **Signed off:** no

> **Amendment (2026-10-17):** At the user's explicit request, this closed record was amended to
> preserve the material review findings and decisions from the exported discussion so that the
> export need not be retained. The record remains a reconstruction, not a contemporaneous transcript;
> user decisions and reviewer observations are distinguished below. This is a one-time, user-authorized
> exception for this session file only; it does not authorize editing any other closed record.

## Objective

Record the follow-up to `sessions/2026-10-16-sensitive-targets-consent.md`: document the user's
final assignment of survey columns to profile, target, or dropped; record the reporting groups; then
reassess what can be promoted to `docs/`. Do not modify the earlier closed session.

## Reasoning

The earlier session recorded a broader decision to include sexual-orientation questions as targets,
report sensitive targets separately, and not publish respondent-level predictions. In the exported
follow-up discussion, the user specified a narrower study schema. First, the user said
`Q-sexual-orientation` is neither profile nor target. The user confirmed household size is an exposed
profile feature, then later supplied the complete lists: the profile includes `Q-amazon-use-hh-size`
but not `Q-amazon-use-howmany`; the target list excludes `Q-amazon-use-how-oft`. The user then
explicitly dropped both `Q-amazon-use-howmany` and `Q-amazon-use-how-oft` from the study.

The final user-provided lists contain eight demographic-profile questions and eleven target
questions. The target questions expand to fifteen IDs under the already recorded five-binary-item
contract for `Q-life-changes`. The three remaining survey questions are dropped: sexual orientation,
household count (`Q-amazon-use-howmany`), and order frequency (`Q-amazon-use-how-oft`). No reasons
for the three exclusions were supplied; none is inferred here.

The user placed `Q-life-changes` with the other targets, not with the sensitive group. Read together
with the earlier accepted decision, the reporting groups are five sensitive questions (the three
substance-use items plus diabetes and wheelchair) and ten ordinary-reporting IDs (five life-change
IDs and five opinion questions). This is the user's chosen reporting boundary; this record does not
assert that pregnancy or other life-change answers are inherently non-sensitive.

The final assignment supersedes the broader target eligibility in the earlier session as the
current study scope. That earlier closed record remains unchanged as a record of what was decided
then. This follow-up makes no findings about predictive performance and no respondent rows were
inspected.

## Review findings retained from the discussion

The conversation included a review of the earlier consent session for promotion readiness. These
are review findings and process conclusions, not new user decisions:

- The reviewer reported checking the linked consent PDF against the cited pages: p. 1 describes
  optional sensitive questions and purchase-data sharing and acknowledges re-identification risk;
  pp. 5–6 list collected data, including the sensitive items; p. 7 permits future research without
  additional consent and use for any research question, with inferring personal attributes from
  purchases as an example. The user confirmed that the PDF was reached through the main survey
  instrument's link. The repository's source register records this provenance and the PDF as part
  of `S-dataverse-yglydy`. This is not a legal determination.
- The reviewer reported that the main survey instrument's participant-facing text discusses
  public availability and purchase-data sharing (pp. 3–4, 11–13). The instrument asks about
  sexual orientation as the respondent's own answer, while the substance-use and personal-health
  questions can refer to the respondent, household members, or people sharing the Amazon account
  (pp. 9–10). The exact phrase about “uncommon demographic combinations” on pp. 3–4 was not
  independently confirmed in that review; do not treat that wording as verified solely from this
  discussion.
- The user had accepted the sensitive-target decision, so it was not merely an unaccepted proposal.
  However, the original `Solo` session configuration does not license an ADR: the configuration
  requires a reviewer and a named human sign-off. No such sign-off was recorded. The review also
  found no existing substantive `docs/` claims to conflict with; the relevant files were templates.
  No experiment underlies the consent interpretation, and no respondent-level rows or predictive
  analysis were used.
- The first promotion blocker—an undefined sensitive-target boundary—is resolved here by the final
  target and reporting lists below. `Q-life-changes` remains in ordinary reporting because that is
  the user's choice; its pregnancy and child options may nevertheless be viewed as health-related.
  The record does not infer a rationale or assert that ordinary reporting means the items are
  inherently non-sensitive.
- The no-publication decision is still too vague for a binding delivery constraint: “publish” has
  not been defined to say whether it includes repository files, figures, or sharing with
  collaborators. This is a project choice, stricter than the consent scope described above; it
  must not be presented as something the consent form itself forbids.
- The household/account-inclusive wording should be recorded as a data caveat, with the survey
  instrument as its basis. This was identified as missing from `CAVEATS.yaml`; the caveat was not
  added in this session.
- A suggested implementation safeguard was an explicit dropped-column list in the schema and a
  check that excluded columns never enter features or targets. This was a recommendation, not a
  user-approved implementation decision.
- Earlier benchmark values 0.531 and 0.635 were calculated over the prior 15-question candidate
  target set and were already marked unverified. They do not describe the current 11-question
  target set and must be recomputed before use. The current study's five binary life-change IDs
  follow the previously established expansion contract. `Q-demos-race` is multi-select and still
  needs a profile-feature encoding rule; purchase-derived features are also still undefined.

## Decisions

- **Profile (8 questions):** `Q-demos-age`, `Q-demos-hispanic`, `Q-demos-race`, `Q-demos-education`,
  `Q-demos-income`, `Q-demos-gender`, `Q-demos-state`, and `Q-amazon-use-hh-size`.
- **Targets (11 questions; 15 IDs):** `Q-substance-use-cigarettes`, `Q-substance-use-marijuana`,
  `Q-substance-use-alcohol`, `Q-personal-diabetes`, `Q-personal-wheelchair`, `Q-life-changes` (five
  binary IDs), `Q-sell-YOUR-data`, `Q-sell-consumer-data`, `Q-small-biz-use`, `Q-census-use`, and
  `Q-research-society`.
- **Dropped from this study (3 questions):** `Q-sexual-orientation`, `Q-amazon-use-howmany`, and
  `Q-amazon-use-how-oft`.
- Report the five substance/health target questions separately. Report `Q-life-changes` with the
  other targets, as the user specified.
- The earlier no-publication decision remains in force: do not publish respondent-level
  predictions. Its operational scope (for example, repository artifacts, figures, and collaborator
  sharing) remains undefined and must not be silently broadened or narrowed.
- `Q-profile-vs-target-columns` is answered and can be deleted from `OPEN_QUESTIONS.md`. Race
  feature encoding and purchase-derived features remain separate unresolved design tasks.

## Found along the way

- The user-supplied final lists omit `Q-amazon-use-howmany` despite an earlier confirmation that it
  was a profile input; the later explicit statement that both `howmany` and `how-oft` are dropped
  resolves that conflict.
- `Q-life-changes` wording refers to the respondent or someone sharing the Amazon account, while
  the retained household feature is household size. This is a scope/interpretation limitation, not
  evidence that a predicted answer belongs to the respondent personally.
- The prior review identified that household/account-inclusive target wording should be indexed in
  `CAVEATS.yaml`; the source instrument wording is recorded in `S-dataverse-yglydy` and the prior
  consent session. Add or refine the caveat during an approved promotion pass, with a precise basis.
- Promotion remains distinct from recording this scope. The consent basis can be cited to the
  registered source, but the policy choice has no named human sign-off or qualifying independent
  review, and the meaning of “publish” is still undefined. Do not write a binding ADR or delivery
  constraint until those gaps are addressed. A narrow study-schema description may be considered
  separately, with this session as its basis and a deliberate diff review.

## Next

Promotion review resumed but no `docs/` changes were made. The final schema and reporting groups
are explicit; a binding ADR and delivery constraint still require a named human sign-off, a
qualifying review, and a precise publication boundary. The household/account caveat should be
recorded with the instrument as its basis. Next, agree which limited claims to promote and settle
those policy gaps. Separately specify race encoding and purchase-based features before
implementation.
