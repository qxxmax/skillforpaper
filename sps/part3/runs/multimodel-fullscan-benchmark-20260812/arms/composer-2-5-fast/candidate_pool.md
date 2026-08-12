# Candidate Pool

Status legend: **confirmed** = identity verified ≥C1; **unconfirmed** = relevant but weak ID; **excluded** = out of scope/noise.

| PaperID | Title | arXiv | Status | C-level | Role | Correction mechanism (if known) |
|---|---|---|---|---|---|---|
| P0001 | Stochastic Path Sampler For Lattice Field Theory | 2606.13790 | confirmed | C3 | **seed** | IMH with trajectory-extended proposal ratio (§2.4) |
| P0002 | Flow-based generative models for MCMC in lattice field theory | 1904.12072 | confirmed | C3 | predecessor baseline | Independence Metropolis with flow proposal |
| P0003 | Equivariant Flow-Based Sampling for Lattice Gauge Theory | 2002.02428 | confirmed | C3 | adjacent LFT flow | MH correction (PRL; flow q[φ] + accept) |
| P0004 | Path Integral Sampler: a stochastic control approach for sampling | 2111.15141 | confirmed | C3 | ML predecessor | Importance weights / path integral correction |
| P0005 | Transport meets Variational Inference: Controlled Monte Carlo Diffusions | 2307.01050 | confirmed | C3 | ML adjacent | Forward+backward control; Jarzynski/Crooks; AIS-style |
| P0006 | Diffusion Models as Stochastic Quantization in Lattice Field Theory | 2309.17082 | confirmed | C3 | adjacent LFT diffusion | Optional accept–reject after trajectory (abstract); mainly data-driven |
| P0007 | Denoising Diffusion Samplers | 2302.13834 | confirmed | C1 | ML predecessor | Variational reverse diffusion; IS/SMC connections |
| P0008 | NeuMC — package for neural sampling for lattice field theories | 2503.11482 | confirmed | C1 | tooling / adjacent | MH after flow (package docs; not C3 read) |
| P0009 | Flow-based sampling for lattice field theories (proceedings) | 2401.01297 | confirmed | C1 | review context | MH or reweighting p/q |
| P0010 | Scaling of Stochastic Normalizing Flows in SU(3) LGT | 2412.00200 | confirmed | C1 | adjacent SNF | Jarzynski / NE-MCMC weights |
| P0011 | Scalable Generative Sampling and Multilevel Estimation near Criticality | 2604.10209 | confirmed | C1 | adjacent multiscale | IS + IMH chains (abstract) |
| P0012 | Diffusion models for Sampling Near Criticality in LFT | unverified | unconfirmed | C0 | forward cite of SPS (SS title only) | unknown |
| P0013 | Neural Non-Equilibrium Hamiltonian Monte Carlo | unverified | unconfirmed | C0 | forward cite (SS title only) | unknown |
| P0014 | Stochastic Quantization as Optimal Control | unverified | unconfirmed | C0 | forward cite (SS title only) | unknown |
| P0015 | Trajectory balance (GFlowNets) | no arXiv locked | unconfirmed | C1 | conceptual TB predecessor | TB objective; not LFT |
| P0016 | Generative Diffusion Models for Lattice Field Theory | 2311.03578 | confirmed | C1 | duplicate line of P0006? | check relation — likely related preprint variant |
| P0017 | Introduction to Normalizing Flows for LFT (notebook) | 2101.08176 | confirmed | C1 | tutorial | MCMC correction after flows |
| P0018 | Lecture notes normalizing flows for LQFT | SciPost Lect. Notes 110 | confirmed | C1 | tutorial | SNF mention |
| P0019 | Estimation of Thermodynamic Observables with Deep Generative Models | unverified | unconfirmed | C0 | INSPIRE ref title from seed | unknown |
| P0020 | Continuous-Mixture Autoregressive Networks (KT transition) | unverified | unconfirmed | C0 | INSPIRE ref title | unknown |
| EX001 | Quantum Key Distribution Network Simulator | — | excluded | C0 | INSPIRE noise query | n/a |
| EX002 | Quest: Quality-Aware MH for Machine Translation | 2406.00049 | excluded | C0 | wrong domain | MH but not physics |

**Pool counts:** 38 deduplicated rows (20 active + 2 excluded + 16 monitor/unconfirmed metadata-only from INSPIRE title harvest not fully listed).

## Landscape summary (evidence-bounded)

1. **LFT neural samplers** split into variational/data-free (flows, SNF, VFE training) vs data-driven (GAN, diffusion/score).
2. **SPS positions** in the data-free path-space family alongside PIS, CMCD, DDS; adapts to LFT via action-only training + **IMH exactness**.
3. **Dominant exactness pattern in LFT flows:** learned independent proposals + **Metropolis–Hastings** (Albergo et al.; equivariant flows).
4. **Diffusion LFT (Wang–Aarts–Zhou line)** connects to stochastic quantization; typically needs HMC data but notes accept–reject extension.
