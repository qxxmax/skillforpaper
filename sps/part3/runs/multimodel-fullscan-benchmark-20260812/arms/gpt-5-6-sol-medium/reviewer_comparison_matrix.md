# Reviewer Comparison Matrix

| Question | Answer | Evidence | Risk |
|---|---|---|---|
| Is SPS just PIS/DDS/CMCD? | Same path-space/control lineage; SPS adds LFT paired drifts and extended-space trajectory IMH. | E0002,E0006,E0010,E0012,E0014 | Do not claim path-space objectives are unprecedented. |
| Why not normalizing flows? | Flows have tractable endpoint densities and standard IMH/reweighting; SPS trades this for stochastic paths. | E0004,E0008,E0021 | Both families retain scaling/support risks. |
| Is exactness unconditional? | No: it belongs to a specific invariant chain, consistent SMC system, or weighted estimator, with support/implementation assumptions. | E0002–E0016,E0022–E0025 | Never equate unbiased weights with exact iid samples. |
| Closest nonequilibrium neighbors? | SNF, AFT/CRAFT, NETS and SCLD. | E0008,E0022,E0024 | Scope-limited, not a priority claim. |
| Does LFT diffusion solve the same setting? | Mostly data-driven in the checked LFT branch; SPS uses target action without HMC training data. | E0016,E0021 | Newer data-free diffusions exist outside LFT. |
