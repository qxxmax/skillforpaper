# Presentation Contract And Slide Claim Map

Use this reference when the user asks to prepare a talk, seminar, slide
deck, or lecture from existing research material (Part 6): conference talks,
group seminars, colloquia, defense presentations, or updating a deck after
the evidence changed.

A presentation is a **projection of the ledgers under a time budget**. Like
Part 5, Part 6 creates no new evidence: missing sources go back to Part 1,
missing technical understanding to Part 2, missing results to Part 3. What
Part 6 adds is a per-slide discipline that survives an audience asking "how
do you know that?" about any slide.

## Presentation Contract Before The First Slide

Write `presentation_contract.md` (from
`templates/presentation_contract_template.md`) before drafting slides. It
pre-registers:

- audience tier and what they can be assumed to know (reference 47);
- duration, venue, and format (talk, seminar, poster, lecture);
- **the one core message**, as a single complete sentence. Everything in the
  deck either serves this sentence or is noise to be cut. If two messages
  compete, that is two talks or one decision to make now, not a longer deck;
- the source runs and ledgers this talk consumes (paths);
- the highest claim level the talk is allowed to assert (a talk about
  work-in-progress may cap itself at `candidate_claim`);
- what the audience should be able to do or decide after the talk.

Slides written before the contract get reverse-audited against it — the
usual result is that half of them serve no registered message.

## Slide Claim Map

Every content slide gets one row in `slide_claim_map.csv` (from
`templates/slide_claim_map_template.csv`):

| column | content |
|---|---|
| SlideID | stable ID, e.g. `S07` |
| Assertion | the slide's headline as one complete sentence — the message, not a topic phrase |
| Level | `background` / `observation` / `candidate_claim` / `validated_claim` / `boundary` |
| EvidenceRefs | ClaimID(s), EvidenceID(s), or ledger row(s) backing the assertion; `—` only for `background` |
| FigureIDs | figures on this slide, resolved in `figure_provenance.md` |
| TimeSec | planned seconds for this slide |
| Note | one line: why this slide serves the core message |

Map laws:

1. **Assertion, not topic.** "Results" is a topic; "the learned sampler
   halves the autocorrelation time at β = 6.2" is an assertion the audience
   can remember, question, and check against the evidence column.
2. **A slide may not assert above its source's promoted level.** A
   `candidate_claim` in the claim promotion ledger cannot appear on a slide
   phrased as established fact. Scope and caveats travel with the claim onto
   the slide, abbreviated but not dropped.
3. **Boundary slides are first-class.** What was not tested, where the
   method fails, and what is future work each get honest assertions with
   Level `boundary`. A talk with zero boundary slides is claiming
   completeness by omission.
4. TimeSec must sum to at most the contracted duration minus question time.
   The cut list when time shrinks is the map sorted by distance from the
   core message, not whichever slides were made last.

## Figure Provenance

Every figure on any slide gets a row in `figure_provenance.md` (from
`templates/figure_provenance_template.md`): the file, the script or run that
produced it, and the run/ledger it came from. Reused figures from a paper or
earlier deck point at their original manifest entry. A figure whose
provenance is "found it in an old folder" is treated like an unverified
citation: it does not go on a slide until re-derived or re-sourced.

## Refresh After Evidence Changes

Decks age the same way papers do. When a claim is retracted or re-scoped in
the claim promotion ledger, the slide claim map is greppable by ClaimID —
find the affected slides, fix them, and log the change in the map's Note
column. Export and refresh of the deck artifact follow
`references/31_artifact_refresh_and_export_gate.md`. Run
`scripts/validate_part6_talk_package.py <run-directory>` before the talk is
given or the deck is shared.
