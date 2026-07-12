# SPS Literature Research Report

## Identity and contribution

The oral clue identifies **Stochastic Path Sampler For Lattice Field Theory** (arXiv:2606.13790) by Chen, Qian, Aarts, Lucini, and Zhou. SPS learns forward and backward stochastic dynamics by minimizing a path-space variational free energy, then uses the full trajectory in an extended-space independence Metropolis-Hastings correction [EV-26-M]. The defensible novelty is this lattice-field-theory adaptation and correction package, not the invention of path-space stochastic-control sampling: PIS, DDS, SNF, and NETS establish nearby precedents [EV-07-M; EV-12-M; EV-08-M; EV-14-M].

## Evidence

In the tested two-dimensional Lx8 phi4 family, corrected SPS reproduces HMC observables through L=64. At kappa=0.27, the reported integrated autocorrelation values are approximately 0.5 IMH steps for SPS+IMH and 160 HMC trajectories [EV-26-R]. These are different units. They do not establish a wall-clock or training-inclusive speedup [EV-26-L]. Acceptance decreases with volume; the current convolution kernels and parameter count grow with L; and a distinct network is trained for each (kappa,L) [EV-26-L].

## Landscape

Flow samplers supply tractable global proposals with MH correction, including gauge-equivariant and fermionic constructions [EV-01-M; EV-02-M; EV-04-M]. Stochastic flows and nonequilibrium transports connect learned maps, stochastic evolution, work fluctuations, and free-energy estimation [EV-08-M; EV-11-M; EV-14-M]. Diffusion samplers connect reverse stochastic dynamics to lattice stochastic quantization and can be MH/MALA-adjusted when a likelihood or local correction is available [EV-13-M; EV-16-M; EV-20-M]. Multimodal work shows why pure reverse-KL proposals need mode/sector diagnostics or composite transitions [EV-05-M; EV-05-L].

## Closure findings

Three external additions materially sharpen the review. A multiscale coarse-to-fine sampler adds a direct near-critical scaling and MLMC baseline [EV-22-M; EV-22-R]. A controlled large-n study shows that diffusion training and generation can inherit critical slowing, while depth and locality can change the scaling [EV-25-R]. A July 2026 cross-volume diffusion study transfers from small lattices to unseen L=64 but retains zero-mode/action-density and broken-phase susceptibility residuals [EV-27-R; EV-27-L]. That July paper lists SPS as bibliography reference 40 but never cites [40] in the body; it is therefore a bibliography-only forward citation, not discussion, extension, or benchmarking evidence.

## Bounded conclusion

SPS is a serious data-free proposal-construction method whose exactness claim belongs to its trajectory IMH correction. Its scalar benchmark is promising, especially in corrected-chain autocorrelation, but current evidence does not support a cost-matched HMC speedup, universal mode coverage, volume transfer, or gauge/fermion scalability. The next decisive experiment is an end-to-end matched-cost study with local/multiscale architecture, transfer across volume/coupling, and sector/tail diagnostics.

## Coverage statement

This run screened all 58 root references, executed 30 fresh and six fixed legacy routes, completed two closure rounds, and read 27 primary PDFs across 611 pages. Coverage is auditable under the declared scope; it is not absolute completeness.
