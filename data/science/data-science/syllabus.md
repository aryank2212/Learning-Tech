# Data science syllabus

Tick items in [progress/TRACKER.md](../../../progress/TRACKER.md).

### Phase 1 – Problem framing and data literacy
- [ ] Asking questions that data can answer
- [ ] Data types: numeric, categorical, time, text
- [ ] Data sources and their limits
- [ ] Data ethics: consent, bias, representation (see [tech-ethics](../../../security/ethics/tech-ethics/README.md))

🛠️ Project: write a one-page project brief for a dataset you choose.

### Phase 2 – Data wrangling
- [ ] Reading CSV, JSON and Parquet
- [ ] Missing values, types, duplicates, outliers
- [ ] Joins, grouping, reshaping (pivot and melt)
- [ ] pandas vs polars

🛠️ Project: clean a messy public dataset and document every change in a log.

### Phase 3 – SQL for analysis
- [ ] Joins, aggregation, window functions
- [ ] Local analytics with DuckDB

🛠️ Project: answer ten business questions on a sales dataset using SQL only.

### Phase 4 – Exploratory data analysis (EDA)
- [ ] Summary statistics, distributions, correlation
- [ ] Group comparisons; spotting data errors
- [ ] Forming hypotheses from data

🛠️ Project: an EDA notebook with five findings, each backed by a chart.

### Phase 5 – Visualisation and storytelling
- [ ] Choosing the right chart for the question
- [ ] matplotlib, seaborn, plotly
- [ ] Colour-blind-safe palettes
- [ ] Dashboards with Streamlit or Metabase

🛠️ Project: a four-chart dashboard with a short written narrative.

### Phase 6 – Statistical thinking
- [ ] Sampling bias; confidence intervals
- [ ] What p-values do and don't tell you
- [ ] Effect sizes

🛠️ Project: explain a p-value to a non-technical friend in 100 words, then test whether they understood.

### Phase 7 – Machine learning workflow
- [ ] Train/validation/test splits; cross-validation
- [ ] Baseline models first
- [ ] Feature engineering; scikit-learn pipelines
- [ ] Hyperparameter tuning
- [ ] Data leakage: how it happens and how to stop it

🛠️ Project: an end-to-end prediction project with a baseline and a tuned model.

### Phase 8 – Experiment design
- [ ] A/B tests; randomisation
- [ ] Sample size and statistical power
- [ ] The peeking problem
- [ ] Uplift and practical significance

🛠️ Project: simulate an A/B test and compute the sample size needed.

### Phase 9 – Communication
- [ ] Writing a report for a non-technical reader
- [ ] Presenting results and their uncertainty
- [ ] Documenting assumptions

🛠️ Project: a five-slide deck or a one-page memo on one of your projects.

### Phase 10 – Deployment and monitoring
- [ ] Versioning data and models (DVC, MLflow)
- [ ] Turning notebooks into scripts
- [ ] Serving a model with FastAPI; containerising it
- [ ] Detecting data drift in production

🛠️ Project: wrap a model in a FastAPI endpoint, containerise it, and log predictions.

## Capstone
Pick a Kaggle competition or a dataset you care about. Take it from question to deployed model, with a written report and a reproducible repository.
