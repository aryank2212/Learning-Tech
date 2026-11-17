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
