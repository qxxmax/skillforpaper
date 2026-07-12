# Reviewer Comparison Matrix

| Reviewer question | Evidence-backed answer | Evidence | Residual risk |
|---|---|---|---|
| Why is SPS exact? | Extended-space IMH targets the joint trajectory construction. | EV-26-M | Finite support/implementation assumptions must still hold. |
| Is path-space KL new? | No; PIS/DDS/NETS are precedents. SPS contributes an LFT-specific bidirectional path construction and correction. | EV-07-M;EV-12-M;EV-14-M | Novelty wording must stay narrow. |
| Does SPS beat HMC computationally? | Not established; only algorithm-unit autocorrelation values are reported. | EV-26-R;EV-26-L | Training and generation costs prevent a speedup claim. |
| What about mode collapse? | The benchmark histograms are encouraging, but general tail/sector coverage is not proved. | EV-05-L;EV-26-L | Require explicit tail/sector diagnostics. |
| Will it scale to gauge/fermion systems? | Adjacent literature supplies architectures, not SPS evidence. | EV-02-M;EV-04-M;EV-16-M | Future work only. |
| Can one model transfer across volume? | Adjacent CNF/diffusion studies show transfer; current SPS trains each pair separately. | EV-10-R;EV-27-R;EV-26-L | Direct SPS transfer remains open. |
| Can learned diffusion avoid critical slowing? | Architecture matters; a controlled analysis finds one-layer slowing and locality/depth mitigation. | EV-25-R | Large-n Gaussian result, not universal theorem. |
