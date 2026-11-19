# Agentic AI & Orchestration

Building AI systems that plan, use tools, remember things and finish multi-step work. Then coordinating several agents (multi-agent orchestration) so the whole system is reliable enough to trust.

## Key terms
- **Agent:** a language model in a loop that can call tools and decide the next step.
- **Tool use:** the model calls a function (search, files, an API) with structured arguments.
- **Orchestration:** deciding which agent or step runs next, what data it gets, and what happens when something fails.
- **Workflow orchestration:** the same ideas for pipelines and business processes, handled by tools like Airflow, Prefect or Temporal.
- **Container orchestration:** Kubernetes runs services. It's a different topic, covered in [system architecture](../../../systems/architecture/system-architecture/README.md).

## Prerequisites
- Python at Level 2 or better
- [AI/ML](../../machine-learning/ai-ml/README.md) Phase 5 (using LLMs in apps)
- An API key from Anthropic or OpenAI (keep it in a `.env` file, never in code)

## Install
```bash
mkdir -p ~/agents && cd ~/agents
uv init agent-lab && cd agent-lab
uv add anthropic openai python-dotenv httpx pydantic
```
Frameworks: install one at a time, once you know the basics.
```bash
uv add langgraph      # graph-based orchestration
uv add mcp            # official Model Context Protocol SDK
uv add crewai         # optional: role-based multi-agent framework
```
Keep keys out of git: add `.env` to `.gitignore`, and load it with `python-dotenv`.

Use a budget for every experiment. Set a spending limit in the provider console, and cap iterations in your loop (for example, at 10 tool calls).

## Weekly rhythm
- Build one small agent each week, with logs of every model call and tool call.
- Break it on purpose: bad tool output, prompt injection, timeouts. Then fix it.

## Files
- [syllabus.md](syllabus.md) — topics, with projects
- [resources.md](resources.md) — docs, papers, frameworks, evaluation tools

## My personal take

*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- Agents are useful, and most of the hype overstates how reliable they are. Build small ones, measure their failures, and add complexity only after that.
- Keep a human in the loop for anything that spends money or changes data.
- Treat prompt injection as a real threat from your first project, not something to fix later.
