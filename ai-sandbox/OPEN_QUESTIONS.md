# panel-response-imputation — Open Questions

- **Updated:** 2026-10-14

> **Open questions only.** A question leaves this file in one of two ways, and both are
> deletions — status `Resolved` is never used, because a register of resolved entries is one
> nobody reads.
>
> **Answered** — the answer goes into the session record and, if durable, into `docs/`.
>
> **Obsolete** — it stopped mattering: the scope moved, the branch died, or the question was
> wrongly posed. Delete it with a `LOG.md` row reading *"dropped: no longer blocks anything"*
> and one clause of why. Projects abandon questions more often than they answer them, and
> without this exit the register fills with zombie 🟢 entries — the same landfill, built from
> dead questions instead of resolved ones.
>
> Either way the `LOG.md` row is what keeps the deletion discoverable.

**IDs are slugs, not numbers** — `Q-latency-budget`, not `Q3`. Deleting resolved entries
would pit and reuse a numbered sequence, so `Q3` cited in an old session file would later
resolve to a different question. A slug, once assigned, is never changed.

If this register arrived from before adoption and already numbers its entries, they are **not**
renumbered — the counter is frozen, new entries take slugs, and the two schemes coexist
permanently. The handbook's §11 says why, and an adoption note in this file should say it too.

- **Priority:** 🔴 high · 🟡 medium · 🟢 low

> **`Owner:` takes a human name, not a git address.** It names who is accountable for the
> entry — a possession that outlives any clone — and is deliberately not the `Held by:`
> value, which names a temporary write claim and is bound to `git config user.email`
> (`ADR-012`).
>
> When creating a new entry and no human name has been supplied, **ask the user who should own
> it before filling this field**. Never substitute `git config user.email` or another available
> identity.
>
> If the user says no owner is assigned yet, or does not provide one, leave `Owner:` blank and
> raise the entry anyway. Blank means nobody has claimed this; it must not mean an owner was known
> and omitted. Fill it as soon as someone takes the entry.

---

## Q-profile-vs-target-columns · Which survey columns are the profile and which are targets 🔴

- **Raised:** 2026-10-14 · **Owner:** esdevop
- **Source:** sessions/2026-10-14-project-scoping.md
- **Question:** which columns of `survey.csv` form the demographic profile given to every method,
  and which form the hidden response profile; whether Q-life-changes is split into its five
  atomic options
- **Why it matters:** blocks the feature table, the target table and every baseline
- **Progress:** the eight `Q-demos-*` columns are the natural profile; Q-sexual-orientation is
  ambiguous (not `Q-demos-*`, but demographic in kind)

## Q-sensitive-targets · Whether sensitive survey items should be imputation targets 🔴

- **Raised:** 2026-10-14 · **Owner:** esdevop
- **Source:** sessions/2026-10-14-project-scoping.md
- **Question:** whether questions on health conditions, substance use and sexual orientation stay
  in the target set, are reported separately, or are excluded
- **Why it matters:** decides the target set and how results may be described or published
- **Progress:** none

## Q-metric-beyond-accuracy · Is accuracy the only metric 🟡

- **Raised:** 2026-10-14 · **Owner:** esdevop
- **Source:** sessions/2026-10-14-project-scoping.md
- **Question:** whether to add a secondary check that imputed answer shares match true shares
- **Why it matters:** accuracy rewards predicting the most common answer for everyone, which
  hot-deck does not do by design; without a second check the comparison favours mode collapse
- **Progress:** on the full survey, mode imputation averages 0.635 accuracy over 15 candidate
  target questions vs 0.531 expected for random donor — a mode baseline is required in any case

## Q-category-grouping · How to group 1,872 purchase categories 🟡

- **Raised:** 2026-10-14 · **Owner:** esdevop
- **Source:** sessions/2026-10-14-project-scoping.md
- **Question:** how the categories are mapped to ~30–50 macro groups, and which specific
  categories are kept separate
- **Why it matters:** sets the width of the feature table (TabPFN has feature limits) and decides
  whether rare but informative categories survive grouping
- **Progress:** proposal — macro groups via a one-off, frozen mapping file, plus a short list of
  separately kept categories chosen before looking at answers or on training data only

## Q-jev-api-access · Is Jev API access available 🟡

- **Raised:** 2026-10-14 · **Owner:** esdevop
- **Source:** S-typesafe-jev-launch
- **Question:** whether the project has early-access credentials for the TypeSafe API
- **Why it matters:** blocks every Jev rung of the ladder
- **Progress:** none

## Q-tabpfn-license · TabPFN weight licence 🟢

- **Raised:** 2026-10-14 · **Owner:** esdevop
- **Source:** sessions/2026-10-14-project-scoping.md
- **Question:** under which licence the TabPFN version to be used is distributed, and whether it
  permits the intended use
- **Why it matters:** TabPFN is the main locally runnable candidate with Jev-like properties
- **Progress:** none — recalled that licences differ between versions, unverified

## Q-local-memory-limit · Memory available for local models 🟢

- **Raised:** 2026-10-14 · **Owner:** esdevop
- **Source:** sessions/2026-10-14-project-scoping.md
- **Question:** how much RAM the Windows host has, and whether the WSL limit (7.6 GiB visible)
  should be raised
- **Why it matters:** with a 4 GB GPU, RAM bounds which local models (TabPFN, small LLMs) can run
- **Progress:** machine has an i5-12500H (16 threads), RTX 3050 Ti Laptop with 4 GB VRAM

## Q-dataset-version · Which Dataverse version was downloaded 🟢

- **Raised:** 2026-10-14 · **Owner:** esdevop
- **Source:** S-dataverse-yglydy
- **Question:** the dataset version number of the local archive
- **Why it matters:** results must cite a data snapshot; a later version may differ
- **Progress:** archive files are dated 2026-10-14
