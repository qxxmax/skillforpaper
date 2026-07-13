# Dijkstra Effect Evaluation

## What actually changed

- Candidate graph: 3,300 nodes, 8,187 weighted edges and 593 reachable paper candidates.
- Relevance-only and Dijkstra each selected 30 papers; **20** overlap, **10** enter only through Dijkstra, and **10** leave the first reading set.
- Dijkstra retained **21** exact root-bibliography papers versus **19** for relevance-only ranking.
- Both arms still cover 7 coarse facets and 8 method groups; Dijkstra is not a completeness proof.
- The gap loop later recovered **5** useful baseline-only papers and added **2** genuinely new boundary/frontier papers.
- In the verified graph, 36 non-root shortest paths are citation-only; author/method shortcuts do not displace checked citations.

## Decision

**Keep Dijkstra as a navigation and reading-priority mechanism, but keep source gates and gap closure mandatory.** The run shows a real selection effect, not a demonstrated universal quality gain.

## Papers changed by the candidate gate

| Entered with Dijkstra | Left the first reading set |
|---|---|
| Regressive and generative neural networks for scalar field theory | Sampling QCD field configurations with gauge-equivariant flow models |
| Introduction to Normalizing Flows for Lattice Field Theory | An optimal control perspective on diffusion-based generative modeling |
| Scaling Up Machine Learning For Quantum Field Theory with Equivariant Continuous Flows | Detecting and Mitigating Mode-Collapse for Flow-based Sampling of Lattice Field Theories |
| Flow-based sampling in the lattice Schwinger model at criticality | Sampling U(1) gauge theory using a re-trainable conditional flow-based model |
| Learning lattice quantum field theories with equivariant continuous flows | Diffusion models as stochastic quantization in lattice field theory |
| Fourier-flow model generating Feynman paths | Group-Equivariant Diffusion Models for Lattice Field Theory |
| Sampling Nambu-Goto theory using Normalizing Flows | Analytic Bijections for Smooth and Interpretable Normalizing Flows |
| Simulating the Hubbard Model with Equivariant Normalizing Flows | A scalable flow-based approach to mitigate topological freezing |
| Variational Autoregressive Networks Applied to $^4$ Field Theory Systems | Diffusion Models for SU(2) Lattice Gauge Theory in Two Dimensions |
| Scalable Generative Sampling and Multilevel Estimation for Lattice Field Theories Near Criticality | Machine learning for four-dimensional SU(3) lattice gauge theories |
