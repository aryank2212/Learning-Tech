# Data Science

Turning raw data into decisions and predictions: collecting, cleaning, exploring, modelling, communicating and deploying. It sits between statistics, programming and domain knowledge.

## The workflow
```
Question → Collect → Clean → Explore (EDA) → Model → Evaluate → Communicate → Deploy & monitor
```
This is the same cycle the CRISP-DM framework describes. Most of the time goes into collecting and cleaning, not modelling.

## Prerequisites
- Python at Level 2 or better (see [languages/python](../languages/python/README.md))
- SQL basics (see [languages/sql](../languages/sql/README.md))
- Statistics basics (see [statistical-computing](../statistical-computing/README.md))

## Install
```bash
mkdir -p ~/data-science && cd ~/data-science
uv init ds-lab && cd ds-lab
uv add pandas polars numpy scikit-learn matplotlib seaborn plotly jupyter duckdb sqlalchemy
uv run jupyter lab
```
- Use [VS Code's Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) to run notebooks inside the editor.
- For Kaggle datasets, install the CLI with `uv tool install kaggle`. Store your `kaggle.json` token in `~/.kaggle/` with permissions `600`. Never commit it.

Dashboards: [Metabase](https://www.metabase.com/) (open source), [Streamlit](https://streamlit.io/) (Python apps), [Tableau Public](https://public.tableau.com/) (free, public work only).

## Weekly rhythm
- One dataset per week, end to end: question → clean → analyse → write up.
- Publish one write-up a month: a notebook on GitHub or a short blog post.

## Files
- [syllabus.md](syllabus.md) — topics, with projects
- [resources.md](resources.md) — books, courses, datasets, tools
