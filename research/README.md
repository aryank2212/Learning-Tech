# Research

Research is how a field moves forward. This section explains how to do research in AI and the other subjects in this repo: how to read papers, find a question, run an experiment, write it up and get it seen. For specific open questions by subject, see [directions.md](directions.md).

## The research loop
1. **Read** — map the field: surveys first, then recent papers.
2. **Question** — find a gap, a failure, or a claim that doesn't hold up.
3. **Hypothesis** — state what you expect, and why.
4. **Experiment** — run the smallest test that could prove you wrong.
5. **Analyse** — statistics, ablations, error analysis.
6. **Write** — a paper, a blog post or a notebook, with reproducible code.
7. **Share** — preprint, talk, workshop or open source.
8. **Repeat** — every result suggests the next question.

## Reading papers (three passes)
- **Pass 1 (5 minutes):** title, abstract, figures and conclusion. Decide whether to continue.
- **Pass 2 (1 hour):** read the body, study the figures and tables, and note each claim and its evidence.
- **Pass 3 (a few hours):** re-derive the key idea, check its assumptions, and try to reproduce one result.

Search "S. Keshav How to Read a Paper" for the full method.

## Tools
| Need | Tool |
|---|---|
| Find papers | [arXiv](https://arxiv.org/), [Semantic Scholar](https://www.semanticscholar.org/), [Google Scholar](https://scholar.google.com/) |
| Map related work | [Connected Papers](https://www.connectedpapers.com/) |
| Papers with code | [Hugging Face Papers](https://huggingface.co/papers) |
| Manage references | [Zotero](https://www.zotero.org/) |
| Take notes | [Obsidian](https://obsidian.md/) |
| Write | [Overleaf](https://www.overleaf.com/) (LaTeX), [Typst](https://typst.app/) |
| Track experiments | [Weights & Biases](https://wandb.ai/), [MLflow](https://mlflow.org/) |
| Version data and code | [git](https://git-scm.com/), [DVC](https://dvc.org/) |

## Reproducibility checklist
- Fixed random seeds, and results reported over several seeds
- Pinned dependencies (`uv.lock`) and a recorded hardware setup
- Configuration in files, not hard-coded
- Data versions recorded, and any licence or consent noted
- One script that reruns every table and figure
- A README that explains how to reproduce the results from a clean machine

## Where research gets published
| Subject | Main venues |
|---|---|
| AI and machine learning | NeurIPS, ICML, ICLR |
| NLP and language models | ACL, EMNLP, NAACL |
| Computer vision | CVPR, ICCV, ECCV |
| Operating systems and systems | OSDI, SOSP, NSDI, EuroSys |
| Networking | SIGCOMM, NSDI |
| Databases and big data | VLDB, SIGMOD, ICDE |
| Algorithms and theory | STOC, FOCS, SODA |
| Programming languages and compilers | PLDI, POPL, OOPSLA, CGO |
| Security and cryptography | IEEE S&P, USENIX Security, ACM CCS, NDSS, CRYPTO, EUROCRYPT |
| Blockchain | Financial Cryptography (FC), IEEE S&P, CCS |
| Software engineering | ICSE, FSE |
| Fairness, ethics and society | FAccT, AIES |

Start with workshops and arXiv preprints. They are cheaper to enter and give useful feedback before you aim at the main conferences.

## Getting started as a student
- Email a professor or a senior PhD student with one specific question, and ask for 30 minutes.
- Join or start a paper-reading group.
- Apply to summer research programmes: [NSF REU sites](https://www.nsf.gov/crssprgm/reu/) in the US, and similar programmes elsewhere.
- Contribute to an open-source project in your area. Bug reproductions and benchmarks are real research artefacts.
- Keep a research log: date, question, what you tried, what you learned.

## Research ethics
- Get permission for any data about people. Anonymise it and document consent.
- Use only datasets you have the rights to use.
- Security research: follow responsible disclosure. Report to the vendor first, and give them time to fix the problem.
- Report negative results and limitations honestly.

## Files
- [directions.md](directions.md) — open questions and starting papers, by subject

## My personal take

*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- Research is less mysterious than it looks: read widely, pick a narrow question, and write down what you tried, including failures.
- Start by reproducing a paper. It's the fastest way to see what a claim really depends on.
- A clear replication, a bug report or a better benchmark is a real contribution.
