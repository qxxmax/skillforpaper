# Audience Tiering, Poster, And QA Bank

Use this reference with reference 46 when the audience is not a specialist
seminar, when the format is a poster, or when preparing for questions.

## Audience Tiers Change Vocabulary, Not Evidence

Fix the tier in `presentation_contract.md`:

| tier | assume known | core message phrased in |
|---|---|---|
| specialist (same subfield) | the problem, the baselines, the notation | method-level terms |
| cross-field (department colloquium) | the field's goals, not its tools | mechanism-level terms, one notation slide max |
| general (public, funders, admissions) | nothing technical | consequence-level terms |

Re-tiering a talk rewrites assertions and cuts depth; it never upgrades a
claim level or drops a boundary statement. The plain-language version of a
`candidate_claim` is still phrased as preliminary ("early results suggest"),
whatever the audience. Simplification that silently promotes a claim is the
Part 6 failure mode this table exists to prevent.

## Poster Discipline

A poster is the projection at its most compressed. Map the deck machinery
onto it directly:

- **Main finding, center, plain language**: the core message sentence from
  the contract — set at the highest *promoted* level, not the most
  impressive phrasing;
- **Evidence panel**: the two or three figures whose provenance rows are
  strongest, each with its assertion as caption (a caption names the
  message, not the figure);
- **Silent-presenter strip**: problem, method, boundary — readable in under
  a minute with the author absent;
- a QR code or short link to the public export (respecting
  `PUBLIC_EXPORT_BOUNDARY.md`).

A poster still gets a `slide_claim_map.csv` (panels are slides) and
`figure_provenance.md`. Wall-to-wall text is the poster equivalent of a
bulleted-list slide: it signals that no core message was chosen.

## QA Bank

Questions are reviews delivered orally. Before the talk, write `qa_bank.md`
(from `templates/qa_bank_template.md`): the questions this audience tier is
most likely to ask, each with

- the basis of the answer: ClaimID, EvidenceID, ledger row — or an explicit
  boundary statement;
- a two-sentence answer at the promoted level;
- status `ready` or `needs_evidence`.

Bank laws:

1. Every boundary slide's implicit question ("why didn't you test X?") is in
   the bank with an honest answer.
2. An answer with no basis row is a guess; if the true answer is "we do not
   know", that sentence — delivered plainly — is the prepared answer.
   Improvised claims under questioning are how validated decks acquire
   unvalidated statements.
3. Questions actually received at the talk get appended afterward with what
   was answered; a question the bank missed is Part 6's version of a
   reviewer comment and feeds the next revision of the deck (and, when it
   exposes a real gap, a Part 1/2/3 run).

## Sources Of This Design

Reference 46's assertion-per-slide law adapts the assertion-evidence
approach (Alley); the one-core-message and signal-over-noise laws adapt
Doumont's three laws of communication; the poster mapping adapts Morrison's
Better Poster layout. See `DESIGN_PROVENANCE.md` for what was retained from
each. The claim-level cap, figure provenance gate, and QA bank contract are
original to this repository.
