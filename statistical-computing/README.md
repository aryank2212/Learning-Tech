# Statistical Computing

Doing statistics with code: simulation, estimation, inference, modelling and reproducible analysis. It bridges mathematical statistics and everyday data-science practice.

## Prerequisites
- Probability (see [maths](../maths/syllabus.md), Phase 6)
- Programming in R or Python

## Install
R (the main language for statistics):
```bash
sudo pacman -S --needed r
R --version
```
Inside R, install the core packages:
```r
install.packages(c("tidyverse", "broom", "lme4", "boot", "pwr"))
```
- [RStudio](https://posit.co/download/rstudio-desktop/) for a full IDE (download from the Posit site)
- [Quarto](https://quarto.org/) for reproducible reports, which combine code and text

Python alternative:
```bash
mkdir -p ~/stats-lab && cd ~/stats-lab
uv init stats-lab && cd stats-lab
uv add numpy scipy statsmodels pingouin matplotlib arviz
```
Bayesian work later: `uv add pymc`. It's a large install.

## Weekly rhythm
- Simulate first: before a formula, write code that generates the data it describes.
- Every analysis gets a short written conclusion, including what you can't conclude.

## Files
- [syllabus.md](syllabus.md) — topics, with projects
- [resources.md](resources.md) — books, courses, tools
