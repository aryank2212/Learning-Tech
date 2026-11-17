# Statistical computing syllabus

Tick items in [progress/TRACKER.md](../progress/TRACKER.md).

### Phase 1 – Descriptive statistics and plots
- [ ] Mean, median, variance, quantiles
- [ ] Histograms, box plots, density plots
- [ ] Choosing summaries for skewed data

🛠️ Project: describe a dataset in a one-page summary with three plots.

### Phase 2 – Distributions and simulation
- [ ] Discrete and continuous distributions
- [ ] Random sampling; inverse-transform and rejection sampling
- [ ] Law of large numbers and the central limit theorem, by simulation

🛠️ Project: simulate the central limit theorem from three different distributions and show how fast it converges.

### Phase 3 – Estimation
- [ ] Bias, variance, consistency
- [ ] Method of moments
- [ ] Maximum likelihood estimation (MLE) with numerical optimisation

🛠️ Project: fit a distribution to data by MLE using `scipy.optimize`.

### Phase 4 – Resampling
- [ ] Sampling distributions
- [ ] Bootstrap confidence intervals
- [ ] Permutation tests

🛠️ Project: bootstrap a confidence interval for a median, and compare it with a normal approximation.

### Phase 5 – Hypothesis testing
- [ ] Null and alternative hypotheses; type I and II errors
- [ ] Power analysis
- [ ] t-tests, chi-squared, Wilcoxon
- [ ] Multiple testing: Bonferroni, Benjamini–Hochberg (FDR)

🛠️ Project: a power analysis, then a 20-test study with FDR correction.

### Phase 6 – Linear models
- [ ] Simple and multiple regression
- [ ] Assumptions and residual diagnostics
- [ ] Interaction terms
- [ ] Model selection: AIC, cross-validation

🛠️ Project: a regression on a real dataset, with diagnostic plots and a written interpretation.

### Phase 7 – Generalised linear models
- [ ] Logistic regression; odds ratios
- [ ] Poisson regression for counts
- [ ] Overdispersion

🛠️ Project: a logistic model for a binary outcome, reporting odds ratios with intervals.

### Phase 8 – Mixed-effects and hierarchical models
- [ ] Random intercepts and slopes
- [ ] Repeated measures
- [ ] Shrinkage

🛠️ Project: analyse a repeated-measures study with `lme4` (R) or `statsmodels` MixedLM.

### Phase 9 – Bayesian statistics
- [ ] Priors, likelihoods, posteriors
- [ ] Conjugate priors (Beta–Binomial)
- [ ] MCMC: Metropolis–Hastings
- [ ] Convergence diagnostics (R-hat, effective sample size)

🛠️ Project: a Beta–Binomial model for click-through rates. Then fit the same model in PyMC.

### Phase 10 – Computational methods and reproducibility
- [ ] Monte Carlo integration
- [ ] Gibbs sampling
- [ ] Seeds, environments and version control for analyses
- [ ] Quarto reports

🛠️ Project: a reproducible Quarto report for one full analysis, rerunnable from a clean machine.
