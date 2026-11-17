# Software engineering syllabus

Tick items in [progress/TRACKER.md](../progress/TRACKER.md).

### Phase 1 – How teams build software
- [ ] Waterfall, iterative and agile approaches; what each is good at
- [ ] Sprints, backlogs, Kanban boards
- [ ] Definition of "done"

🛠️ Project: run a two-week personal sprint on a board. Write a retrospective at the end.

### Phase 2 – Requirements
- [ ] User stories and acceptance criteria
- [ ] Functional and non-functional requirements (speed, security, cost)
- [ ] Use cases and edge cases

🛠️ Project: write requirements for a small app: five user stories, each with acceptance criteria.

### Phase 3 – Version control at team scale
- [ ] Branching strategies: trunk-based development and GitFlow
- [ ] Pull requests and their etiquette
- [ ] Rebasing vs merging; resolving conflicts
- [ ] Semantic versioning and changelogs

🛠️ Project: with a partner, make ten pull requests on one repository. Resolve two real conflicts.

### Phase 4 – Design and modularity
- [ ] Coupling and cohesion
- [ ] SOLID principles, used as questions rather than rules
- [ ] Design patterns, and when they solve a real problem
- [ ] Architecture decision records (see [system architecture](../system-architecture/README.md))

🛠️ Project: refactor a messy module into clear layers. Write an ADR that explains the change.

### Phase 5 – Testing strategy
- [ ] The test pyramid: unit, integration, end-to-end
- [ ] Test doubles: stubs, mocks, fakes
- [ ] Test-driven development (TDD) cycle
- [ ] Property-based testing with Hypothesis
- [ ] Coverage: what it tells you, and what it doesn't

🛠️ Project: build a small library test-first. Add property-based tests that find at least one edge case you missed.

### Phase 6 – Code quality and review
- [ ] Naming, readability, and small functions
- [ ] Linters and formatters (ruff, shellcheck) in pre-commit
- [ ] Code review: what to look for, and how to write a useful comment
- [ ] Google's engineering practices for review

🛠️ Project: review a real open-source pull request, and leave three constructive comments.

### Phase 7 – Continuous integration and delivery
- [ ] CI pipelines: build, test, lint on every push
- [ ] Reproducible builds and artifacts
- [ ] Release strategies: canary and blue-green deployments
- [ ] Feature flags

🛠️ Project: a GitHub Actions workflow that tests, lints and builds a Docker image on every push. Debug it locally with `act` first.

### Phase 8 – Debugging, observability and incidents
- [ ] Logs, metrics and traces (see [system architecture](../system-architecture/README.md))
- [ ] Reproducing a bug before fixing it
- [ ] Blameless postmortems

🛠️ Project: write a postmortem for a real bug you hit, with a timeline and action items.

### Phase 9 – Maintaining and changing old code
- [ ] Characterisation tests: pin down what old code does before changing it
- [ ] Refactoring in small, safe steps
- [ ] Dependency upgrades and their risks
- [ ] Tracking technical debt on purpose

🛠️ Project: add characterisation tests to an old script, then refactor it without changing its output.

### Phase 10 – Documentation
- [ ] A README that lets a stranger run the project
- [ ] API documentation
- [ ] Design documents and changelogs
- [ ] Onboarding guides

🛠️ Project: write docs that let a friend run your project in ten minutes. Watch them try it.

### Phase 11 – Security in development
- [ ] Secrets: never in code or in git history
- [ ] Dependency scanning and supply-chain risk
- [ ] Threat modelling
- [ ] OWASP ASVS as a checklist (see [web technology](../web-technology/README.md))

🛠️ Project: run a dependency audit on a project. Fix the top findings and record what you did.

### Phase 12 – Working with people
- [ ] Estimation and its uncertainty
- [ ] Pair programming and mob programming
- [ ] Giving and receiving feedback
- [ ] On-call and sustainable work

🛠️ Project: run a pair-programming session, then write a reflection on what went well and what didn't.

### Capstone
- [ ] Take one small application through every phase

🛠️ Project: requirements → design → tests → CI → release → postmortem, all documented in one repository.
