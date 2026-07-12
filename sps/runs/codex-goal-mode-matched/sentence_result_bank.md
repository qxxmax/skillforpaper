# Sentence and Result Bank

| Type | Sentence | Support | Strength | Forbidden expansion |
|---|---|---|---|---|
| background | Learned global proposals can reduce rejection-driven autocorrelation, while an accept-reject or weighting layer supplies correctness. | EV-01-M;EV-01-R | established | Do not equate lower autocorrelation with lower wall time. |
| method distinction | SPS optimizes reversibility in trajectory space and then applies extended-space IMH to corrected independent proposals. | EV-26-M | supported | Do not call uncorrected endpoints exact. |
| result | In the tested Lx8 phi4 family, corrected SPS reproduces HMC observables through L=64. | EV-26-R | supported | Keep geometry and parameter range. |
| limitation | The reported SPS and HMC autocorrelation times use different update units and do not constitute a cost-matched speed comparison. | EV-26-L | supported | No speedup ratio. |
| related work | PIS, DDS, and NETS establish a broader path-space stochastic-control and nonequilibrium-transport lineage. | EV-07-M;EV-12-M;EV-14-M | established | Do not claim SPS invented path-space objectives. |
| gap | SPS volume transfer remains untested because a separate network is trained for every coupling-size pair. | EV-26-L | supported | Do not import transfer from adjacent papers. |
| reviewer response | Recent cross-volume diffusion evidence makes transfer plausible but leaves observable-specific residual bias. | EV-27-R;EV-27-L | supported | External addition, not a direct SPS result. |
| adversarial | A controlled large-n analysis shows that learned diffusion can inherit critical slowing unless locality and depth change the scaling. | EV-25-R | supported | Model limit must be named. |
