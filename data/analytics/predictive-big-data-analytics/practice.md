# Practice: Predictive & Big Data Analytics

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Plot a time series and decompose it into trend, seasonality and remainder.
- [ ] Compute the MAE of a naive forecast.
- [ ] Convert a CSV file to Parquet with DuckDB.

## Level 2 — Medium (apply it)

- [ ] Fit a Holt-Winters forecast and backtest it on a hold-out window.
- [ ] Write a PySpark job that groups a dataset by key.
- [ ] Write a Kafka producer and consumer in Python.

## Level 3 — Hard (build and explain)

- [ ] Forecast with LightGBM and lag features, with prediction intervals.
- [ ] Write an Airflow DAG with retries for a daily ETL job.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What is a naive forecast?

   <details><summary>Show answer</summary>

   Predict the next value as the last observed value. A seasonal naive forecast uses the value from the same point in the last season.

   </details>

2. Why backtest with a rolling origin?

   <details><summary>Show answer</summary>

   Time order matters. Training on the past and testing on later data avoids leaking the future into the model.

   </details>

3. What is a shuffle in Spark?

   <details><summary>Show answer</summary>

   Redistributing data across partitions, for example for a join or group-by. It's costly because data moves across the network.

   </details>

4. Why store analytics data as Parquet?

   <details><summary>Show answer</summary>

   It's columnar and compressed, so queries that read a few columns read much less data.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
