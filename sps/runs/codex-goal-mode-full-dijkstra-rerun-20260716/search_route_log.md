# Search Route Log

The protocol is intentionally wider than the final reading list. This avoids
equating a verbal clue with a settled literature boundary.

| route | round | family | facet | query |
|---|---|---|---|---|
| Q01 | L0 | root | identity | 2606.13790 |
| Q02 | L0 | root | identity | ti:"Stochastic Path Sampler For Lattice Field Theory" |
| Q03 | L1 | root_terms | method | all:"stochastic path sampler" |
| Q04 | L1 | domain | domain | all:"lattice field theory" AND all:"neural sampler" |
| Q05 | L1 | normalizing_flow | method | all:"lattice field theory" AND all:"normalizing flow" |
| Q06 | L2 | stochastic_flow | method | all:"stochastic normalizing flow" AND all:lattice |
| Q07 | L2 | nonequilibrium | mechanism | all:nonequilibrium AND all:"lattice field" |
| Q08 | L2 | path_space | mechanism | all:"path space" AND all:sampling |
| Q09 | L2 | entropy_production | mechanism | all:"entropy production" AND all:sampling |
| Q10 | L2 | diffusion | adjacent | all:diffusion AND all:"lattice field theory" |
| Q11 | L2 | critical_slowing | problem | all:"critical slowing down" AND all:lattice |
| Q12 | L3 | jarzynski | method_precedent | all:Jarzynski AND all:lattice |
| Q13 | L3 | author | author_lineage | au:Qian_M |
| Q14 | L3 | author | author_lineage | au:Aarts_G AND all:lattice |
| Q15 | L3 | author | author_lineage | au:Chen_S AND all:"stochastic" |
| Q16 | L4 | evaluation | verification | all:autocorrelation AND all:lattice AND all:sampling |
| Q17 | L4 | correction | exactness | all:"independence Metropolis" AND all:sampling |
| Q18 | L4 | adjacent | method | all:"Schrodinger bridge" AND all:sampling |
| Q19 | L5 | correction | exactness | all:"independence Metropolis" AND all:lattice |
| Q20 | L6 | path_lattice | mechanism | all:"path space" AND all:"lattice field theory" |
| Q21 | L7 | stochastic_quantization | mechanism | all:"stochastic quantization" AND all:"lattice field theory" |
| Q22 | L8 | topology | problem | all:"topological freezing" AND all:"normalizing flow" |
| Q23 | L9 | multiscale | scaling | all:multilevel AND all:"lattice field theory" |
| Q24 | L10 | author | author_lineage | au:Lucini_B AND all:sampling |
