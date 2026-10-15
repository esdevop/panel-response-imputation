# Commit messages

Read this guide before drafting a commit message or creating a commit. These are
project-owned instructions, not template-managed rules.

## Structure

Use Conventional Commits with a short subject, a blank line, and one concise body
paragraph:

```text
<type>: <short description>

<What changed, why it changed, and any important boundary or consequence.>
```

Types used here: `docs`, `feat`, `fix`, `refactor`, `chore`, `exp`.
Write messages in English. Prefer an imperative subject without a trailing period.
Choose the type that best describes the actual change.

## Suggested length

- Subject: roughly 5–12 words, preferably around 50–72 characters including the
  type prefix. Clarity matters more than satisfying both ranges.
- Body: roughly 40–80 words in 2–4 sentences, forming one paragraph.
- Wrap body lines at about 72 characters when practical; wrapping does not create
  additional paragraphs.
- Small changes may have a much shorter body. Never add filler to meet a minimum.
- Use more space when necessary to preserve an important rationale or limitation.

These are editorial guidelines, not hard limits or commit-blocking checks. The
common Git 50/72 convention concerns subject length and body line wrapping, not
paragraph word count. The word ranges above are project preferences, not a
Conventional Commits requirement or a proven optimum for AI readers.

## Content

Explain what changed, why, and the important consequence or boundary. Make the
message useful to a person or an AI reader reviewing history without the diff.
Avoid a file-by-file inventory, repetition of the subject, and unsupported claims
of verification. Distinguish a design draft from an implemented workflow and a
chosen policy from an established data fact.

Example:

```text
feat: encode life-change blanks and finalize research design draft

Map blank life-change responses to five eligible negative labels under
the user-selected policy, with tests covering encoding and evaluation
inclusion. Preserve the earlier audit and its inconclusive finding on
original blank semantics. Record the modular design draft and baseline
handoff, including remaining target and split decisions. The baseline
pipeline is not implemented yet.
```

Commit authorization and session closure still follow
`ai-sandbox/playbooks/checkpoint.md`; this guide defines message format, not
permission to commit.
