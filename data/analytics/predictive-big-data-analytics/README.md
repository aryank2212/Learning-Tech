# Predictive & Big Data Analytics

Forecasting the future from past data, at a scale where one laptop is not enough. It covers time-series forecasting, predictive models in production, and distributed processing with Spark, Kafka and warehouses.

Two halves:
- **Predictive analytics:** time series, forecasting, classification and regression, evaluated honestly over time.
- **Big data:** distributed storage and processing, streams, pipelines, warehouses and lakehouses.

## Prerequisites
- Python, SQL, and the [data science](../../science/data-science/README.md) syllabus up to Phase 7 (or equivalent)
- Some Java helps: Spark and Kafka run on the JVM (see [Java](../../../languages/general/java/README.md))

## Install
```bash
sudo pacman -S --needed jdk-openjdk docker docker-compose
sudo systemctl enable --now docker
sudo usermod -aG docker $USER      # log out and back in afterwards
mkdir -p ~/bigdata-lab && cd ~/bigdata-lab
uv init bigdata-lab && cd bigdata-lab
uv add pyspark duckdb pandas statsmodels scikit-learn lightgbm mlflow
uv run python -c "import pyspark; print(pyspark.__version__)"
```
- Spark needs Java. If PySpark fails with a Java error, check the Spark release notes for which JDK versions it supports, and install a matching `jdk` package.
- Kafka locally (official image): `docker run -p 9092:9092 apache/kafka:latest` — check the Kafka docs for the current quick-start command.
- Prophet is a popular forecasting library, but it's heavy to install. Add it later with `uv add prophet`.

## Weekly rhythm
- Forecast one public series each week and compare three methods on a hold-out window.
- Build one pipeline piece per week: ingest → store → transform → serve.

## Files
- [syllabus.md](syllabus.md) — topics, with projects
- [resources.md](resources.md) — books, docs, datasets, papers

## My personal take

*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- Start with simple forecasts, such as naive and seasonal baselines. Many fancy models lose to them on honest tests.
- Don't reach for Spark until the data really doesn't fit one machine. DuckDB handles more than people expect.
- Backtest over time. A model that looks good on a random split can fail badly in production.
