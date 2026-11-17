# Software Engineering

Building software that many people can change safely for years: requirements, design, testing, version control at team scale, code review, continuous delivery, maintenance and working with other people. Writing a script is programming. Keeping a product healthy for five years with a team is software engineering.

## Prerequisites
- At least one language at Level 2 or better (see [languages](../../../languages/README.md))
- Git basics (commit, branch, merge)

## Install
```bash
sudo pacman -S --needed git github-cli docker docker-compose shellcheck act
uv tool install pre-commit
uv tool install ruff
```
- `github-cli` (`gh`) creates repositories and pull requests from the terminal.
- `act` runs GitHub Actions workflows on your own machine, so you can debug CI without pushing.
- `pre-commit` runs formatters and linters before each commit. Add a `.pre-commit-config.yaml` to any project.

VS Code extensions: `eamodio.gitlens` (see history inline) and `usernamehw.errorlens` (show errors in the editor).

Infrastructure tools for the later phases: `terraform` and `kubectl` are in the official repos.

## How to practise
- Pick one small project and run it through the whole cycle every month: requirements, design, tests, pull request, CI, release, retrospective.
- Work in pairs when you can. Review each other's pull requests.

## Files
- [syllabus.md](syllabus.md) — topics, with projects
- [resources.md](resources.md) — books, courses, standards, tools

## My personal take

*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- This is the subject that turns a personal script into something a team can maintain. I think it's underrated by people who only write code alone.
- Start with tests and version control. They teach more about design than most books do.
- Read code reviews from large open-source projects. You'll learn judgement, which no checklist gives you.
