# 2026-10-16 · sensitive targets and participant consent

- **Status:** closed
- **Tags:** #consent #sensitive-targets
- **Configuration:** Solo
- **Participants:** author — AI assistant · brainstorming
- **Signed off:** no

## Objective

Record the user's decision on `Q-sensitive-targets`, assess it against the study consent and survey instruments, answer and remove the open question, and close this session. This is a discussion; no raw response rows or predictive analyses are run.

## Reasoning

The user confirmed the proposed decision: include health, substance-use and sexual-orientation questions as targets in the research evaluation; report these sensitive targets separately; do not publish respondent-level predictions. The user also confirmed that the provided consent PDF was downloaded through the link in the main survey instrument. This session therefore treats it as the participant consent form for this study, while recording that the file-to-study link is confirmed by the user.

The consent form identifies the study purpose as creating a public repository of online purchases and consumer-demographics data (pp. 1–2). It says sensitive survey questions are optional and participants may still complete the survey if they decline to answer them or decline to share purchase data (pp. 1–3). The form lists sexual orientation, smoking cigarettes, smoking marijuana, drinking alcohol, wheelchair use and diabetes among the data collected and potentially disclosed (pp. 5–6). It also acknowledges re-identification risk from uncommon demographic combinations or known purchases (pp. 3–4).

Most relevant to this project, the form permits de-identified survey and purchase data to be stored, shared for future research without additional consent, and used for any research question; it gives as an example research into which demographics or personal attributes are most easily inferred from purchases (p. 7). This directly supports including sensitive survey answers in a research evaluation of imputation from demographics and purchase history. This reading is an interpretation of the supplied consent, not legal advice or a claim that every possible use is authorized.

The main survey instrument's participant-facing text separately says data may be made publicly available and describes consent to share the purchase data after showing the requested fields (`data/raw/archive/dataverse_files.zip`, `survey-instrument.pdf`, pp. 3–4, 11–13). The consent form, rather than CC0 alone, is the key evidence for the participant-facing scope. The Dataverse record page could not be fetched in this environment because it returned a WAF challenge; the user confirmed the consent PDF came from the instrument's link.

The target wording matters for interpretation: the sexual-orientation item asks about the respondent, while the smoking, drinking, diabetes and wheelchair items can refer to the respondent, someone in the household, or someone sharing the Amazon account (`data/raw/archive/dataverse_files.zip`, `survey-instrument.pdf`, pp. 9–10). Those latter targets should be described as answers to household/account-inclusive questions, not necessarily as verified personal traits.

No respondent-level data rows were inspected, and no predictive analysis or experiment was run. The session establishes a scope decision only; it does not establish predictive performance or justify individual-level use.

## Decisions

- Answer `Q-sensitive-targets`: retain health, substance-use and sexual-orientation survey items as eligible targets for research evaluation; report the sensitive targets separately; do not publish respondent-level predictions.
- Record the basis as the user's acceptance of this decision and the consent form's explicit scope for public sharing and future research, including research on inferring personal attributes from purchases. Retain the caveat that this is not a legal determination.
- Do not promote this brainstorm's conclusion to `docs/` in this session. A durable project-policy statement, if wanted, requires a separate deliberate promotion and review.

## Found along the way

- The separately downloaded consent form is linked from the main survey instrument; the user confirmed this provenance. The source register previously noted that the prescreen instrument had not yet been read; both prescreen and main instruments have now been read.
- Consent allows broad future research, but target semantics still vary between individual-level and household/account-inclusive questions.

## Next

Continue the `response-signal` thread by specifying a falsifiable validation-only, item-level signal analysis. Choose exact targets and metrics, and state what result would kill the purchase-signal hypothesis before running anything. No raw-data predictive evidence exists yet.
