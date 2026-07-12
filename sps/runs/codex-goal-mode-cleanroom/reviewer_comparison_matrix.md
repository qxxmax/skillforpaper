# Reviewer Comparison Matrix

| Family | Data | Learned object | Correction | Supported claim | Boundary |
|---|---|---|---|---|---|
| SPS | data-free | forward/backward path drifts | extended-space IMH | Corrected independent proposals match tested HMC observables with shorter critical-region autocorrelation. | One 2D phi4 study; support tails and total-cost comparison remain open. |
| Path-space control/data-free diffusion | data-free | stochastic control or reverse path | trajectory weights | Path objectives can lower weight variance for unnormalized targets. | Discretization, training and benchmark transfer to lattice physics vary by method. |
| Normalizing-flow MCMC | data-free | terminal invertible map | MH or reweighting | Learned independent proposals can be made asymptotically exact and symmetry aware. | Training/support cost and realistic QCD scaling are unresolved. |
| Stochastic normalizing flow | data-free | interleaved maps and stochastic protocol | Jarzynski/reweighting | Learned layers improve nonequilibrium estimator quality while retaining path correction. | Protocol length and affected degrees of freedom can still dominate cost. |
| Diffusion with physics/symmetry | usually target-data trained | score/reverse drift | reweighting or MALA/HMC refinement | Symmetry, force regularization and cross-volume training improve sample quality. | Raw samples can remain biased; score evaluations and correction cost are substantial. |
| Autoregressive network | data-free | site/block conditional density | MH | Sequential models plus local/block MH reproduce tested scalar/spin observables. | Small systems and no realistic gauge/fermion scaling. |
| Multiscale generative flow | data-free | coarse-to-fine conditional hierarchy | importance sampling and MLMC | Explicit scale separation improves near-critical large-volume sampling and enables variance reduction. | Only 2D scalar evidence; fine-level ESS still declines. |
| Diagnostics / theory | reference data or analytic target | operator errors or training dynamics | none | Mode-resolved diagnostics and controlled theory reveal failures hidden by aggregate metrics. | They diagnose or explain failure but are not complete samplers. |
