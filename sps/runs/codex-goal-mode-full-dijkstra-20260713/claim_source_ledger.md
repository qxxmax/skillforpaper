# Claim-Source Ledger

| Claim | Safe sentence | Evidence | Do not overclaim |
|---|---|---|---|
| C01 | SPS learns a low-irreversibility path between prior and target. | `E-260613790-M` | This is the SPS v1 formulation; do not replace it with terminal-density KL training. |
| C02 | The learned SPS proposal is followed by an exactness gate. | `E-260613790-M;E-260613790-R` | Do not call uncorrected SPS samples exact. |
| C03 | SPS sits at the intersection of path-space control and nonequilibrium transport. | `E-211115141-M;E-230213834-M;E-230701050-M;E-241002711-M;E-260613790-M` | This is a checked synthesis, not a claim that the algorithms are identical. |
| C04 | Learned lattice proposals are repeatedly paired with an explicit correction mechanism. | `E-190412072-M;E-200306413-M;E-210605934-M;E-220108862-M;E-220803832-M` | Shared correction logic does not imply equal scaling or performance. |
| C05 | Diffusion helps only when architecture and physics match the slow modes. | `E-260512597-R;E-260512597-L;E-260708505-L` | The quadratic-to-logarithmic result is controlled in the Gaussian O(n to infinity) setting, not universally. |
| C06 | Transfer, multiscale structure and locality are three distinct routes to larger lattices. | `E-260708505-R;E-260410209-R;E-260120708-R` | Each result is benchmark-specific; production-QCD scaling is not established. |
| C07 | Efficiency means physical error per total compute, not a single ESS number. | `E-221107541-R;E-221107541-L;E-190412072-L;E-260410209-R;E-240918861-L` | The literature does not yet supply one uniform cross-paper cost benchmark. |
| C08 | A sampler can look good globally and still miss the modes that matter. | `E-210700734-R;E-210700734-L;E-260708505-R;E-260613790-L` | Diagnostics expose risk; they do not by themselves correct it. |
| C09 | The field is active, but production-scale lattice-QCD evidence is still sparse. | `E-260412416-R;E-260412416-L;E-220803832-L;E-260120708-R` | Do not describe these methods as mature at production QCD scale. |
| C10 | The next SPS step is to close correctness, scaling and physics-cost loops together. | `E-260613790-L;E-210700734-L;E-260512597-L;E-260708505-L;E-260410209-L;E-210605934-L` | These are literature-grounded directions, not SPS results already achieved. |
