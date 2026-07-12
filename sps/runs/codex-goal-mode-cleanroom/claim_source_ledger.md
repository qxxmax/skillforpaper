# Claim–Source Ledger

| Claim | Safe sentence | Evidence | Boundary |
|---|---|---|---|
| C01 | SPS learns a low-irreversibility path between prior and target. | `E-260613790-M` | This is the formulation in SPS v1; do not replace it by terminal-density KL training. |
| C02 | The learned proposal is followed by an exactness gate. | `E-260613790-M;E-260613790-R` | Do not call the uncorrected SPS output exact; the paper itself reports tail and susceptibility deviations before IMH. |
| C03 | SPS sits at the intersection of path-space control and nonequilibrium transport. | `E-211115141-M;E-230213834-M;E-230701050-M;E-241002711-M;E-260613790-M` | This is a synthesis from direct SPS references and shared path-measure objectives, not a claim that the algorithms are identical. |
| C04 | The lattice lineage repeatedly pairs learned proposals with a correction mechanism. | `E-190412072-M;E-200306413-M;E-210605934-M;E-220108862-M;E-220803832-M;E-260120708-M` | The methods differ in proposal construction, target system and scaling; shared correction logic does not imply equal performance. |
| C05 | Diffusion helps only when architecture and physics match the slow modes. | `E-260512597-R;E-260512597-L;E-260708505-L` | The quadratic-to-logarithmic result is established in the Gaussian O(n to infinity) setting, not universally for interacting lattice theories. |
| C06 | Transfer, multiscale structure and locality are three distinct routes to larger lattices. | `E-260708505-R;E-260410209-R;E-260120708-R` | Evidence is method- and benchmark-specific; realistic full-QCD scaling is not yet established. |
| C07 | Efficiency means physical error per total compute, not a single ESS number. | `E-221107541-R;E-221107541-L;E-190412072-L;E-260410209-R` | The literature supplies components of this standard but not one uniform cross-paper benchmark. |
| C08 | A sampler can look good globally and still miss the modes that matter. | `E-210700734-R;E-210700734-L;E-260511199-R;E-260708505-R` | Diagnostics identify risk; they do not by themselves correct a sampler. |
| C09 | The field is active, but realistic lattice-QCD evidence is still sparse. | `E-260412416-R;E-260412416-L;E-220803832-L;E-260120708-R` | Do not describe the approach as mature or proven at production QCD scale. |
| C10 | The next step is to close correctness, scaling and physics-cost loops together. | `E-260613790-L;E-260511199-L;E-260512597-L;E-260708505-L;E-260410209-L;E-210605934-L` | These are literature-grounded directions, not results already achieved by SPS. |
