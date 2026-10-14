# panel-response-imputation — Assumption Register

- **Updated:** 2026-10-14

> What the method **bets on, and where it could be wrong**. Not "what I understood about the
> project" — that belongs in `docs/`. The test: *if this turned out false, what breaks?*
>
> Two resting types: `ASSUMED` (plausible, unverified) · `INFERRED` (derived logically).
>
> **There is no `CONFIRMED` entry in this file.** Confirmation is a transition, not a state:
> the moment an assumption is verified it becomes a fact, moves to `docs/`, and is deleted
> from here. `checkpoint.md` performs that move. Anything sitting here is by definition still
> unverified — which is what keeps the register bounded and worth reading.
>
> **IDs are slugs, not numbers** — `A-keeper-latency`, not `A4`. Same reason as
> `OPEN_QUESTIONS.md`: deletion pits a numbered sequence and old cross-references silently
> point at the wrong entry. A register inherited from before adoption keeps its numbers, frozen,
> and takes slugs for everything new — see §11; renumbering breaks citations in files this system
> declares immutable.

> **`Owner:` takes a human name, not a git address.** It names who is accountable for the
> entry — a possession that outlives any clone — and is deliberately not the `Held by:`
> value, which names a temporary write claim and is bound to `git config user.email`
> (`ADR-012`).
>
> When creating a new entry and no human name has been supplied, **ask the user who should own
> it before filling `Owner:`**. Never substitute `git config user.email` or another available
> identity.
>
> If the user says no owner is assigned yet, or does not provide one, leave `Owner:` blank and
> record the assumption anyway. Blank means nobody has claimed this; it must not mean an owner was
> known and omitted. Fill it as soon as someone takes the entry.
>
> **`Basis:` accepts `—`** when no reference genuinely exists. That is a legitimate value, not a
> gap to fill — never point it at the nearest similar entry instead; a wrong pointer looks
> exactly as valid as a right one and is far more expensive to catch.
>
> **If this file grows for months with no deletions, it has quietly become a journal**, not a
> registry — the two behave differently and the label matters. Either resume deleting confirmed
> or killed entries (into `docs/` or `CAVEATS.yaml`), or declare it a journal explicitly and give
> current state its own file. Do not leave the registry label on a file that has stopped acting
> like one.

---

## A-purchases-precede-responses · A panelist's purchase history ends at about the time they answered the survey — `INFERRED`

- **Raised:** 2026-10-14 · **Owner:** esdevop
- **Basis:** last-purchase dates cluster between 2022-09 and 2023-03 (p10–p90), consistent with
  each history being exported when the survey was taken; Q-life-changes asks about 2021
  [S-dataverse-yglydy; sessions/2026-10-14-project-scoping.md]
- **If false:** purchase features may contain behaviour that happened after the answers were given,
  inflating every purchase-based method relative to the demographic-only baselines
- **What would settle it:** the survey timestamp per panelist, or the dataset documentation on
  how histories were collected
- **Does not license:** using the latest few purchases of the 2024 outliers without checking their dates

## A-dataset-is-open-ecommerce · The DOI is the "Open e-Commerce 1.0" dataset (Berke et al., Scientific Data, 2024) — `ASSUMED`

- **Raised:** 2026-10-14 · **Owner:** esdevop
- **Basis:** recollection of the dataset's structure (Amazon purchase histories of ~5k US users
  plus a demographic survey); not checked against the Dataverse landing page
- **If false:** any description or citation of the dataset by that name is wrong
- **What would settle it:** the Dataverse landing page for DOI 10.7910/DVN/YGLYDY
- **Does not license:** citing the paper's collection method or sampling claims in `docs/`

## A-jev-probabilities-calibrated · Jev's per-option probabilities are calibrated well enough to sample from — `ASSUMED`

- **Raised:** 2026-10-14 · **Owner:** esdevop
- **Basis:** vendor claim that the model is trained for calibrated decisions; no calibration
  curves published [S-typesafe-jev-launch]
- **If false:** multiple imputation by sampling from Jev's distribution reproduces the wrong
  answer shares; argmax accuracy is unaffected
- **What would settle it:** a reliability curve of Jev's probabilities on validation panelists
- **Does not license:** using raw Jev probabilities as answer shares without a validation check
