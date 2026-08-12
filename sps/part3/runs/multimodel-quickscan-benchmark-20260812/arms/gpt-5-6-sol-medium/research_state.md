# Research State

## Project

**Research question:** Which prior learned/neural samplers for unnormalized target distributions and lattice field theory does “Stochastic Path Sampler for Lattice Field Theory” (arXiv:2606.13790) directly build on, and what are their exact titles, authors, and arXiv IDs?  
**Scan level:** quick  
**Primary intent:** locate  
**Secondary intent:** learn  
**Risk level:** medium  
**Current round:** R0001  
**Current status:** stopped  
**Current action:** audit_exclusions  
**Output mode:** evidence_table

## Scope

- Include only predecessor methods directly identified from the focal paper’s own source record/full text and individually verified through visited authoritative web pages.
- Cover both learned/neural samplers for unnormalized targets and learned samplers for lattice field theory.
- Exclude conceptually adjacent work not shown to be a direct predecessor.
- Sources: live web calls only; no facts imported from other benchmark arms or SPS run directories.
- Web-call budget: 10/10 used (mirror; `round_log.md` is authoritative).
- Used: 10
- Screenshot policy: on-demand.

## Current Next Best Action

No further web action: the call cap is exhausted. Preserve unvisited LFT citations as outside this quick-scan claim set.

## Stop Status

**Current stop status:** stopped_with_known_risk  
**Reason:** Verified six direct path-space/unnormalized-target predecessors and three representative learned LFT predecessors within the 10-call cap.  
**Remaining risks:** This quick scan did not independently verify every learned-LFT citation in the focal Introduction; those unvisited works are not asserted here.

## Verified Result

- Direct path-space family: Path Integral Sampler (arXiv:2111.15141); Denoising Diffusion Samplers (arXiv:2302.13834); An optimal control perspective on diffusion-based generative modeling (arXiv:2211.01364); Improved sampling via learned diffusions (arXiv:2307.01198); Transport meets Variational Inference: Controlled Monte Carlo Diffusions (arXiv:2307.01050); NETS: A Non-Equilibrium Transport Sampler (arXiv:2410.02711).
- Learned LFT lineage: Flow-based generative models for Markov chain Monte Carlo in lattice field theory (arXiv:1904.12072); Diffusion Models as Stochastic Quantization in Lattice Field Theory (arXiv:2309.17082); Variational Autoregressive Networks Applied to φ4 Field Theory Systems (arXiv:2512.19575).
- Evidence: E0001–E0010 in `evidence_registry.md`.

## Validation

**Command:** `python3 ~/Desktop/skillforpaper/play-the-toy-with-children/scripts/validate_run_state.py ~/Desktop/skillforpaper/sps/part3/runs/multimodel-quickscan-benchmark-20260812/arms/gpt-5-6-sol-medium`  
**Result:** final pass exited 0 with `profile: literature` and `status: CONSISTENT` (no warnings). An initial pass warning about the budget mirror was corrected by adding `Used: 10`.
