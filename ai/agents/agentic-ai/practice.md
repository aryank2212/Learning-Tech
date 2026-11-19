# Practice: Agentic AI & Orchestration

Work through the levels in order. Spend at least 30 minutes on a task before looking anything up. At the end, a short quiz checks the key ideas, and each answer is hidden until you click it.

How to check yourself: write tests for each task, or compare your output with a known answer. For maths and theory, check by hand and then with code.

## Level 1 — Easy (warm-up)

- [ ] Call an LLM with a JSON schema and validate its output.
- [ ] Write a tool definition for a calculator.
- [ ] Log every tool call in an agent loop.

## Level 2 — Medium (apply it)

- [ ] Build retrieval over ten documents, with citations.
- [ ] Write a writer and critic loop with a clear stop condition.
- [ ] Write an evaluation set of 20 cases and report the pass rate.

## Level 3 — Hard (build and explain)

- [ ] Build an MCP server that exposes a folder of notes.
- [ ] Run ten prompt-injection attacks against your agent and fix what breaks.

## Quick quiz

Answer each question out loud or on paper first, then open the answer.

1. What is tool use?

   <details><summary>Show answer</summary>

   The model emits a structured call to a function (search, code, an API). Your code runs it and returns the result to the model.

   </details>

2. What is prompt injection?

   <details><summary>Show answer</summary>

   Untrusted content, such as a web page or document, contains instructions that try to take over the model's behaviour.

   </details>

3. Name two orchestration patterns.

   <details><summary>Show answer</summary>

   Prompt chaining and orchestrator–workers. Others are routing, parallelisation and evaluator–optimiser.

   </details>

4. Why cap iterations and budget in an agent loop?

   <details><summary>Show answer</summary>

   To stop runaway cost and endless loops when the agent doesn't converge on an answer.

   </details>

## Stuck?

Go back to the syllabus for the phase the task belongs to, and to [tutorial.md](../../../tutorial.md) for the matching tutorial. Ask for help by opening an issue; a good question includes what you tried.
