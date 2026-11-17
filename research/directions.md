# Research directions by subject

For each subject: open questions, and papers to start with. Check each paper on arXiv or the publisher's site before you cite it.

## AI and machine learning
Open questions: why do scaling laws hold, and where do they stop? How do we measure reasoning reliably? Can models explain their own internal computation (interpretability)? How do we train with less data and less compute?
- Kaplan et al., *Scaling Laws for Neural Language Models* — [2001.08361](https://arxiv.org/abs/2001.08361)
- Hoffmann et al., *Training Compute-Optimal Large Language Models* (Chinchilla) — [2203.15556](https://arxiv.org/abs/2203.15556)
- Hu et al., *LoRA* — [2106.09685](https://arxiv.org/abs/2106.09685)
- Dao et al., *FlashAttention* — [2205.14135](https://arxiv.org/abs/2205.14135)
- Elhage et al., *A Mathematical Framework for Transformer Circuits* — [transformer-circuits.pub](https://transformer-circuits.pub/)

## Agentic AI
Open questions: how do we make agents reliable on long tasks? How do we evaluate them fairly? How do we defend against prompt injection? How do several agents coordinate without wasting compute?
- ReAct — [2210.03629](https://arxiv.org/abs/2210.03629)
- Reflexion — [2303.11366](https://arxiv.org/abs/2303.11366)
- Generative Agents — [2304.03442](https://arxiv.org/abs/2304.03442)
- SWE-bench — [2310.06770](https://arxiv.org/abs/2310.06770)
- AutoGen — [2308.08155](https://arxiv.org/abs/2308.08155)

## Operating systems and systems
Open questions: how do we schedule work across heterogeneous hardware (GPUs, accelerators)? How do we verify kernels? How do we make storage and networking stacks faster without losing correctness?
- Ghemawat et al., *The Google File System* (SOSP 2003)
- Dean & Ghemawat, *MapReduce* (OSDI 2004)
- Klein et al., *seL4: Formal Verification of an OS Kernel* (SOSP 2009)

## Computer networking
Open questions: congestion control in datacentres vs on the open internet; latency under load; new transports; secure routing (BGP security).
- Cardwell et al., *BBR: Congestion-Based Congestion Control* (ACM Queue, 2016)
- Langley et al., *The QUIC Transport Protocol* (SIGCOMM 2017)

## Cryptography
Open questions: migrating to post-quantum cryptography; zero-knowledge proofs fast enough for everyday use; computing on private data; side-channel-resistant implementations.
- NIST FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA) — [csrc.nist.gov](https://csrc.nist.gov/projects/post-quantum-cryptography)
- Boneh & Shoup, *A Graduate Course in Applied Cryptography* — [free](https://toc.cryptobook.us/)

## Blockchain
Open questions: scaling without losing decentralisation; cross-chain security; privacy on public ledgers; energy and governance trade-offs.
- Nakamoto, *Bitcoin: A Peer-to-Peer Electronic Cash System* (2008) — [bitcoin.org](https://bitcoin.org/bitcoin.pdf)
- Ethereum whitepaper — [ethereum.org](https://ethereum.org/en/whitepaper/)
- Narayanan et al., *Bitcoin and Cryptocurrency Technologies* — [free draft](https://bitcoinbook.cs.princeton.edu/)

## Data science and analytics
Open questions: causal inference from observational data; data quality and labelling; experiments at scale; fairness in predictive models.
- Hernán & Robins, *Causal Inference: What If* — [free](https://miguelhernan.org/whatifbook)
- Kohavi, Tang, Xu, *Trustworthy Online Controlled Experiments* (book)
- Hyndman & Athanasopoulos, *Forecasting: Principles and Practice* — [free](https://otexts.com/fpp3/)

## Statistics and statistical computing
Open questions: valid inference after model selection; uncertainty in ML predictions; scalable MCMC; methods for reproducible science.
- Efron & Tibshirani, *An Introduction to the Bootstrap* (book)
- Gelman et al., *Bayesian Data Analysis* — free PDF from the authors
- Benjamini & Hochberg (1995), *Controlling the False Discovery Rate*

## Algorithms and data structures
Open questions: learned data structures; faster graph algorithms; approximation for very large inputs; parallel algorithms.
- Kraska et al., *The Case for Learned Index Structures* — [1712.01208](https://arxiv.org/abs/1712.01208)
- Roughgarden (ed.), *Beyond the Worst-Case Analysis of Algorithms* (book)

## Compilers and programming languages
Open questions: machine-learning-guided optimisation; verified compilers; memory safety without runtime cost; compilers for AI accelerators.
- Lattner et al., *MLIR* — [2002.11054](https://arxiv.org/abs/2002.11054)
- Leroy, *Formal Verification of a Realistic Compiler* (CACM 2009) — CompCert
- Jung et al., *RustBelt: Securing the Foundations of the Rust Programming Language* (POPL 2018)

## Maths and formal methods
Open questions: AI-assisted proof; formalising large areas of maths (Lean's Mathlib library); verified software.
- [Mathematics in Lean](https://leanprover-community.github.io/mathematics_in_lean/)

## Digital electronics and computer architecture
Open questions: energy-efficient accelerators; open hardware (RISC-V); memory bottlenecks; computing inside memory.
- Hennessy & Patterson, *Computer Organization and Design* (RISC-V edition)
- [RISC-V specifications](https://riscv.org/technical/specifications/)

## Tech ethics and society
Open questions: auditing algorithms; trade-offs between fairness definitions; accountability for AI harms; environmental cost of AI.
- Buolamwini & Gebru, *Gender Shades* (FAT* 2018)
- Gebru et al., *Datasheets for Datasets* — [1803.09010](https://arxiv.org/abs/1803.09010)
- Mitchell et al., *Model Cards for Model Reporting* — [1810.03993](https://arxiv.org/abs/1810.03993)
