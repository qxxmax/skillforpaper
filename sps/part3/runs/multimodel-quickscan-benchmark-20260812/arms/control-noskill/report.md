# SPS 论文(arXiv:2606.13790)直接依赖的先前方法调研报告

**目标论文**: *Stochastic Path Sampler For Lattice Field Theory*, Shiyang Chen, Moxian Qian, Gert Aarts, Biagio Lucini, Kai Zhou, arXiv:2606.13790 (2026-08-11)。

**方法概要**: SPS 通过学习可训练的前向/后向 Langevin 动力学(含可学习的漂移项与扩散系数),最小化路径空间 KL 散度(等价于熵产生上界 / 变分自由能),实现无需训练数据(data-free)的格点 phi^4 理论采样;采样端点由轨迹级 Independence Metropolis–Hastings(IMH)修正保证精确性。

依据论文正文(引言 §1、§2)与参考文献列表,该工作直接建立在以下两类先前方法之上。

---

## 一、面向未归一化目标分布的学习式/神经采样器(data-free,路径空间变分家族)

论文 §1 明确指出:"data-free diffusion-based samplers that minimize a path-space Kullback-Leibler objective closely related to the one employed in this work have been developed",并将 SPS 定位为"这一路径空间变分采样器家族向格点场论的随机量子化式改编"。所引的核心先前方法为:

1. **Path Integral Sampler: a stochastic control approach for sampling**
   - 作者: Qinsheng Zhang, Yongxin Chen
   - arXiv: **2111.15141** (ICLR 2022)
   - 关系: 最早的路径空间 KL 变分扩散采样器之一,SPS 的损失函数与之同族。

2. **Denoising Diffusion Samplers**
   - 作者: Francisco Vargas, Will Grathwohl, Arnaud Doucet
   - arXiv: **2302.13834** (ICLR 2023)
   - 关系: 基于去噪扩散的 data-free 采样器,同样最小化前向/后向路径测度间的 KL。

3. **An optimal control perspective on diffusion-based generative modeling**
   - 作者: Julius Berner, Lorenz Richter, Karen Ullrich
   - arXiv: **2211.01364** (TMLR 2024)
   - 关系: 扩散生成建模的最优控制表述,为路径空间变分目标提供理论框架。

4. **Improved sampling via learned diffusions**
   - 作者: Lorenz Richter, Julius Berner
   - arXiv: **2307.01198** (ICLR 2024)
   - 关系: 学习式扩散采样器的统一与改进(时间反演视角),属于同一最优控制/路径 KL 家族。

5. **Transport meets Variational Inference: Controlled Monte Carlo Diffusions**
   - 作者: Francisco Vargas, Shreyas Padhy, Denis Blessing, Nikolas Nüsken
   - arXiv: **2307.01050** (ICLR 2024)
   - 关系: 论文特别指出 CMCD "like the present work, learn both the forward and the backward drifts",是与 SPS 最接近的先前方法(前后向漂移均可学习)。

6. **NETS: A Non-Equilibrium Transport Sampler**
   - 作者: Michael S. Albergo, Eric Vanden-Eijnden
   - arXiv: **2410.02711**
   - 关系: 非平衡输运采样器(基于 Jarzynski 等式的退火动力学),与 SPS 的非平衡热力学出发点直接呼应。

7. **轨迹级平衡(Trajectory-Level Balance)概念来源 —— GFlowNets**(论文 §2 引用为 "Trajectory Level Balance [8; 9; 34]"):
   - **Flow network based generative models for non-iterative diverse candidate generation**, Emmanuel Bengio, Moksh Jain, Maksym Korablyov, Doina Precup, Yoshua Bengio, arXiv: **2106.04399** (NeurIPS 2021)
   - **GFlowNet Foundations**, Yoshua Bengio, Salem Lahlou, Tristan Deleu, Edward J. Hu, Mo Tiwari, Emmanuel Bengio, arXiv: **2111.09266** (JMLR 2023)
   - **Trajectory balance: Improved credit assignment in GFlowNets**, Nikolay Malkin, Moksh Jain, Emmanuel Bengio, Chen Sun, Yoshua Bengio, arXiv: **2201.13259** (NeurIPS 2022)
   - 关系: SPS 的核心目标——令前向/后向路径测度之比在整条轨迹上趋于全局常数——正是 GFlowNet 轨迹平衡条件的连续路径空间版本。

此外,SPS 的物理基础为 **随机量子化**(Parisi & Wu 1981, *Sci. Sin.* 24, 483;Damgaard & Hüffel 1987, *Phys. Rept.* 152, 227;经典文献,无 arXiv 编号)。

## 二、格点场论中的学习式采样器

### (a) 变分自由能训练(data-free)流模型 —— SPS 的直接对标

8. **Flow-based generative models for Markov chain Monte Carlo in lattice field theory**
   - 作者: M. S. Albergo, G. Kanwar, P. E. Shanahan
   - arXiv: **1904.12072** (Phys. Rev. D 100, 034515)
   - 关系: 格点场论中归一化流 + Metropolis 独立性修正范式的开创性工作;SPS 的 "学习式提议 + IMH 精确修正" 流程直接沿用该范式,只是把提议分布从可逆流换成随机路径。

9. **Equivariant flow-based sampling for lattice gauge theory**
   - 作者: G. Kanwar, M. S. Albergo, D. Boyda, K. Cranmer, D. C. Hackett, S. Racanière, D. J. Rezende, P. E. Shanahan
   - arXiv: **2003.06413** (Phys. Rev. Lett. 125, 121601)

10. **Estimation of Thermodynamic Observables in Lattice Field Theories with Deep Generative Models**
    - 作者: K. A. Nicoli, C. J. Anders, L. Funcke, T. Hartung, K. Jansen, P. Kessel, S. Nakajima, P. Stornati
    - arXiv: **2007.07115** (Phys. Rev. Lett. 126, 032001)
    - 关系: SPS 的 phi^4 有限温格点几何设置(L×8)与自由能估计方式直接沿用此文(论文 §3 明确引用)。

### (b) 随机化流(引入 Langevin 步的流)—— 通往随机路径采样的桥梁

11. **Stochastic Normalizing Flows**
    - 作者: Hao Wu, Jonas Köhler, Frank Noé
    - arXiv: **2002.06707** (NeurIPS 2020)
    - 关系: 在流中引入随机采样块并用非平衡统计力学(重要性权重)端到端训练,是 SPS "非平衡热力学 + 可学习随机动力学" 思路的直接前驱。

12. **Stochastic normalizing flows as non-equilibrium transformations**
    - 作者: M. Caselle, E. Cellini, A. Nada, M. Panero
    - arXiv: **2201.08862** (JHEP 07 (2022) 015)
    - 关系: 把 SNF 与 Jarzynski 等式/非平衡变换联系起来并应用于格点场论,与 SPS 的熵产生/Jarzynski 视角(论文 Eq. (14))一脉相承。

### (c) 格点场论中的扩散模型(数据驱动,SPS 试图去掉其数据需求)

13. **Diffusion models as stochastic quantization in lattice field theory**
    - 作者: L. Wang, G. Aarts, K. Zhou
    - arXiv: **2309.17082** (JHEP 05 (2024) 060)
    - 关系: 建立扩散模型与随机量子化的对应,并在 phi^4 上验证(论文引用为参考文献 [51],用于 phi^4 中的 DM 以及 Langevin 扩散系数的手工选取对比);SPS 自称 "stochastic-quantization-inspired",直接承接此文思路,但改为无数据训练。三位作者中 Aarts 与 Zhou 也是 SPS 作者。

---

## 结论(最核心的直接基础)

按与 SPS 的方法学距离排序,最直接的先前方法为:

- **Controlled Monte Carlo Diffusions** (Vargas, Padhy, Blessing, Nüsken, arXiv:2307.01050) —— 唯一被论文点名"同样学习前向与后向漂移"的方法;
- **Path Integral Sampler** (Zhang & Chen, arXiv:2111.15141) 与 **Denoising Diffusion Samplers** (Vargas, Grathwohl, Doucet, arXiv:2302.13834) —— 路径空间 KL 变分采样器的奠基工作;
- **Trajectory Balance / GFlowNets** (Malkin et al., arXiv:2201.13259; Bengio et al., arXiv:2106.04399, arXiv:2111.09266) —— 轨迹级平衡目标的来源;
- **Flow-based generative models for MCMC in LFT** (Albergo, Kanwar, Shanahan, arXiv:1904.12072) —— 格点场论中"学习式提议 + Metropolis 精确化"范式的来源;
- **Diffusion models as stochastic quantization** (Wang, Aarts, Zhou, arXiv:2309.17082) 与 **Stochastic Normalizing Flows** (Wu, Köhler, Noé, arXiv:2002.06707;格点应用 Caselle et al., arXiv:2201.08862) —— 随机量子化/非平衡视角的直接前驱。

## 来源与调用记录

- 论文全文(含完整参考文献列表): https://arxiv.org/abs/2606.13790 (WebFetch, 1 次)
- SNF arXiv 编号确认(2002.06707): arXiv / NeurIPS 2020 / noegroup GitHub (WebSearch, 1 次)
- Trajectory Balance arXiv 编号确认(2201.13259): arXiv / NeurIPS 2022 (WebSearch, 1 次)

**共使用 3 次 web 调用(1 次抓取 + 2 次搜索),限额 10 次。** 其余 arXiv 编号、标题、作者均直接取自目标论文自带的参考文献列表(单次抓取已包含),未额外消耗调用。
