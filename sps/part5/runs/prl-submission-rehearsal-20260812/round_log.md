# Round Log

Run: Part 5 submission rehearsal, SPS paper (arXiv:2606.13790)
Date: 2026-08-12

## Round 1: Venue Profiling

Goal: build dated venue profiles for PRL and SciPost Physics from current
official guidelines.

Result: both official pages are bot-protected; the blocked-channel
substitution rule of `references/34_channel_lineage_and_cross_validation_gate.md`
was applied. Substitute search channels returned the official pages' content
(PRL authors page retrieved in full through the search cache) plus the APS
length-guide. Facts recorded in the venue profiles cite these channels.

Blind spot: SciPost facts rest on search snippets of scipost.org pages, not a
full page render. Items marked "confirm at portal" in the profiles must be
re-checked during actual submission.

## Call Ledger

| # | type | target | result | running total |
|---|---|---|---|---|
| 1 | fetch | journals.aps.org/prl/authors | blocked (Cloudflare bot check) | 1/6 |
| 2 | fetch | scipost.org/SciPostPhys/about | blocked (Anubis proof-of-work) | 2/6 |
| 3 | search | PRL length limit information for authors 2026 | ok; returned full PRL authors page + APS length-guide | 3/6 |
| 4 | search | SciPost Physics submission requirements acceptance criteria | ok; authoring guidelines + FAQ snippets | 4/6 |

Budget: 6 calls planned, 4 used, backfilled at stop.

## File Patches

- venue_profile_prl.md, venue_profile_scipost_physics.md: written from round 1.
- claim_evidence_ledger.md: written from the Part 2 review core (no new calls).
- submission_package_manifest.md: gate run against repository contents.
- output_manifest.md: rows updated as files landed.
