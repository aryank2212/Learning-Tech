# Python

Readable, huge ecosystem, and the main language of AI, data science and scripting. Start here if you want to build something quickly.

## Install

```bash
sudo pacman -S --needed uv python
uv python install 3.13
uv init hello-python && cd hello-python
uv run python main.py
```

`uv` manages Python versions, virtual environments and packages. Use it instead of `pip install` on the system Python.

VS Code: install `ms-python.python` and `ms-python.vscode-pylance`.

## Syllabus

### Level 1 – Basics
- [ ] Variables, numbers, strings, f-strings
- [ ] Lists, tuples, dicts, sets
- [ ] `if`, `for`, `while`, `break`, `continue`
- [ ] Functions, arguments, `*args`, `**kwargs`, return values
- [ ] Reading and writing files, `pathlib`

### Level 2 – Intermediate
- [ ] List comprehensions, generators, `yield`
- [ ] Exceptions: `try`, `except`, custom errors
- [ ] Modules, packages, `import`, `uv` projects
- [ ] Classes, dataclasses, `__init__`, inheritance
- [ ] Type hints and `mypy`
- [ ] `argparse` / `typer` for command-line tools

### Level 3 – Practical tools
- [ ] `requests` and JSON APIs
- [ ] `pytest` for testing
- [ ] Virtual environments and `pyproject.toml`
- [ ] Regex (`re`)
- [ ] Concurrency: `asyncio`, `threading`, `multiprocessing`

### Level 4 – Data and science
- [ ] NumPy arrays and vectorisation
- [ ] pandas dataframes
- [ ] Matplotlib / Seaborn plotting
- [ ] Jupyter notebooks
- [ ] Clean code: `ruff`, `black`, logging

## Resources

| | Resource | Notes |
|---|---|---|
| ⭐🆓 | [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) | Free, practical, great for beginners |
| ⭐🆓 | [Python official tutorial](https://docs.python.org/3/tutorial/) | Official, clear |
| ⭐🆓 | [Python Tutor](https://pythontutor.com/) | Step through code visually |
| 🆓 | [Real Python](https://realpython.com/) | Tutorials for every level |
| 🆓 | [Exercism Python track](https://exercism.org/tracks/python) | Practice with feedback |
| 🆓 | [CS50P (Harvard, Python)](https://cs50.harvard.edu/python/) | Free course |
| 🆓 | [Corey Schafer – Python (YouTube)](https://www.youtube.com/@coreyms) | Video tutorials |
| 🆓 | [uv documentation](https://docs.astral.sh/uv/) | Package and version manager used in this repo |
| 💲 | *Python Crash Course* – Eric Matthes | Beginner book with projects |
| 💲 | *Fluent Python* – Luciano Ramalho (O'Reilly) | Deep, idiomatic Python |

## Projects

1. 🛠️ **Password generator** and strength checker
2. 🛠️ **Expense tracker** that saves to CSV
3. 🛠️ **Web scraper** that saves headlines to a file
4. 🛠️ **Weather CLI** with an API key and `requests`
5. 🛠️ **Data dashboard** in a Jupyter notebook with pandas and matplotlib
6. 🛠️ **Discord or Telegram bot**

## Tips

- Use `ruff check` and `ruff format` before committing.
- Learn to read tracebacks from the bottom up.
- Start every project with `uv init`, so dependencies stay separate.

## Study timeline (about 8 weeks)
| Weeks | Focus | Done when |
|---|---|---|
| 1–2 | Level 1: basics | A script reads a file and summarises it |
| 3–4 | Level 2: intermediate | A typed, tested command-line tool |
| 5–6 | Level 3: practical tools | A small API client with pytest tests |
| 7–8 | Level 4: data | A notebook analysis of a real dataset with pandas |

## Common pitfalls
- **Mutable default arguments:** `def f(x=[])` shares one list across calls. Use `None` and create the list inside.
- **Late binding in closures** created inside loops.
- **`is` instead of `==`.** `is` compares identity; use `==` to compare values.
- **Shadowing built-ins** such as `list`, `str` or `input`.
- **Comparing floats with `==`.** Use `math.isclose`.
- **Installing into the system Python.** Use a `uv` project for each piece of work.

## Where Python is used
AI and machine learning (PyTorch, Hugging Face), data science, web backends (FastAPI, Django, Flask), automation, scientific computing, and as the glue language in most engineering teams.

## Ecosystem
- **Web:** FastAPI, Django, Flask
- **Testing:** pytest
- **Data:** pandas, polars, NumPy
- **Validation:** pydantic
- **Quality:** ruff (lint and format), mypy (type checks)

## More reading
- *Effective Python* — Brett Slatkin (💲)
- *Python Cookbook* — David Beazley & Brian Jones (💲)
- [PEP 8 — the style guide](https://peps.python.org/pep-0008/)
- Run `import this` in Python to read the Zen of Python.

## Libraries for data, ML and AI
- **Arrays and data:** NumPy, pandas, Polars, DuckDB
- **Plots:** Matplotlib, Seaborn, Plotly
- **Classical ML:** scikit-learn ([guide](../../../ai/frameworks/scikit-learn/README.md)), XGBoost, LightGBM
- **Deep learning:** PyTorch ([guide](../../../ai/frameworks/pytorch/README.md)), TensorFlow and Keras ([guide](../../../ai/frameworks/tensorflow/README.md)), JAX
- **Language models and agents:** Hugging Face Transformers, then [agentic AI](../../../ai/agents/agentic-ai/README.md)
- **Sharing models:** ONNX Runtime and FastAPI (see [ML libraries in other languages](../../../ai/frameworks/ml-libraries-other-languages/README.md))

```bash
uv add numpy pandas matplotlib scikit-learn
```

## My personal take

*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- If you only learn one language first, I'd choose Python. It gets you building early, and most AI and data work uses it.
- Don't let it make you careless about types and speed. Learn type hints and a profiler early.
- Use uv for every project. Messy dependencies are the most common early frustration.
