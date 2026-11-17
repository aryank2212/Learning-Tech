# Predictive & big data analytics syllabus

Tick items in [progress/TRACKER.md](../../../progress/TRACKER.md).

### Phase 1 – Time-series basics
- [ ] Trend, seasonality, residuals
- [ ] Stationarity and differencing
- [ ] Autocorrelation (ACF) and partial autocorrelation (PACF)
- [ ] Decomposition

🛠️ Project: decompose ten years of monthly sales and describe each component.

### Phase 2 – Classical forecasting
- [ ] Naive and seasonal-naive baselines (always start here)
- [ ] Moving averages; exponential smoothing and Holt–Winters
- [ ] ARIMA and SARIMA
- [ ] Model selection with AIC and BIC

🛠️ Project: forecast a public series with three methods. Compare MAE and RMSE on a hold-out window.

### Phase 3 – Modern forecasting
- [ ] Backtesting with rolling origin
- [ ] Gradient boosting with lag features
- [ ] Prophet
- [ ] Prediction intervals and calibration

🛠️ Project: a demand forecast with lag features and LightGBM, with prediction intervals.

### Phase 4 – Predictive modelling in practice
- [ ] Class imbalance: resampling, class weights, threshold choice
- [ ] Calibration of predicted probabilities
- [ ] Concept drift and data drift
- [ ] Retraining schedules

🛠️ Project: a churn model with monthly monitoring of its predictions.

### Phase 5 – Big data concepts
- [ ] The four Vs: volume, velocity, variety, veracity
- [ ] Batch vs stream processing
- [ ] Partitioning and replication (see [system-architecture](../../../systems/architecture/system-architecture/README.md))
- [ ] Columnar storage: Parquet

🛠️ Project: convert a 1 GB CSV to Parquet and compare query times in DuckDB and pandas.

### Phase 6 – Distributed processing with Spark
- [ ] DataFrames; lazy evaluation
- [ ] Transformations vs actions
- [ ] Partitions and shuffles
- [ ] Joins at scale; caching

🛠️ Project: a PySpark job that aggregates a multi-gigabyte dataset.

### Phase 7 – Streams and messaging
- [ ] Kafka topics, partitions, consumer groups, offsets
- [ ] Windowing: tumbling, sliding, session windows
- [ ] Watermarks and late data
- [ ] Spark Structured Streaming (or Flink basics)

🛠️ Project: stream simulated sensor readings through Kafka and compute one-minute averages.

### Phase 8 – Warehouses and lakehouses
- [ ] Star schemas; dimensional modelling
- [ ] Table formats: Delta Lake and Apache Iceberg
- [ ] Transformations with dbt
- [ ] Orchestration with Airflow

🛠️ Project: a small warehouse in DuckDB with dbt models and a daily Airflow DAG.

### Phase 9 – Machine learning at scale
- [ ] Spark MLlib basics
- [ ] Feature stores (concepts)
- [ ] Model registries with MLflow
- [ ] Batch vs online prediction

🛠️ Project: train a Spark MLlib model and log it to MLflow.

### Phase 10 – Capstone
- [ ] Ingest, process at scale, forecast, serve, monitor

🛠️ Project: a two-page report on a prediction problem you solved end to end.
