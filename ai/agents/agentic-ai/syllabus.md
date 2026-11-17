# Agentic AI & orchestration syllabus

Tick items in [progress/TRACKER.md](../../../progress/TRACKER.md).

### Phase 1 – LLM basics for agents
- [ ] Tokens, context windows, temperature
- [ ] Structured outputs (JSON) and schema validation with Pydantic
- [ ] Function calling / tool schemas
- [ ] Cost and latency per call

🛠️ Project: call an LLM with a JSON schema, validate the output, and reject and retry bad outputs.

### Phase 2 – Tool use
- [ ] Defining a tool: name, description, parameters
- [ ] Running tool calls and returning results
- [ ] Error handling and retries
- [ ] Limits on loop length

🛠️ Project: a calculator and a web-search tool in one agent loop, with a log line per tool call.

### Phase 3 – Single-agent patterns
- [ ] ReAct: alternate reasoning and acting
- [ ] Plan-and-execute
- [ ] Reflection and self-critique (Reflexion)
- [ ] When an agent is overkill, and a single prompt is enough

🛠️ Project: a research agent that plans its searches, reads sources, and writes a summary with citations.

### Phase 4 – Memory and context
- [ ] Short-term memory: the conversation window
- [ ] Long-term memory with a vector store (Chroma, pgvector)
- [ ] Summarising old context; compaction
- [ ] Retrieval strategies for memory

🛠️ Project: an assistant that remembers your preferences across sessions.

### Phase 5 – Retrieval-augmented generation (RAG)
- [ ] Chunking and embeddings
- [ ] Hybrid search (keyword + vector) and reranking
- [ ] Citations and source attribution
- [ ] Measuring retrieval quality

🛠️ Project: a PDF question-answering agent that cites page numbers.

### Phase 6 – Orchestration patterns
Based on Anthropic's *Building effective agents*:
- [ ] Prompt chaining
- [ ] Routing
- [ ] Parallelisation (sectioning and voting)
- [ ] Orchestrator–workers
- [ ] Evaluator–optimiser

🛠️ Project: implement all five patterns on one task (for example, write and review an article). Compare cost and quality.

### Phase 7 – Multi-agent systems
- [ ] Roles and responsibilities
- [ ] Message passing and shared state
- [ ] Supervisor agents; critic agents
- [ ] Preventing loops and runaway cost

🛠️ Project: a three-agent software team (planner, coder, reviewer) that writes and tests a small Python function.

### Phase 8 – Graph-based orchestration
- [ ] State machines: nodes, edges, shared state
- [ ] Checkpoints and persistence
- [ ] Human-in-the-loop approval steps
- [ ] LangGraph (or an equivalent)

🛠️ Project: a support-ticket triage graph that asks a human to approve refunds.

### Phase 9 – Tool protocols and interoperability
- [ ] Model Context Protocol (MCP): servers, clients, resources, tools
- [ ] The Agent2Agent (A2A) protocol at a conceptual level
- [ ] Designing tool schemas that models use correctly

🛠️ Project: an MCP server that exposes a folder of your notes as search and read tools.

### Phase 10 – Durable and production orchestration
- [ ] Retries, idempotency and timeouts
- [ ] Durable execution (Temporal concepts)
- [ ] Scheduled batch agents with Airflow or Prefect
- [ ] Concurrency and rate limits

🛠️ Project: a nightly agent job, scheduled with Prefect or Airflow, with retries and failure alerts.

### Phase 11 – Evaluation and observability
- [ ] Evaluation sets (golden datasets)
- [ ] LLM-as-judge, and its biases
- [ ] Trace logging with Langfuse or OpenTelemetry
- [ ] Cost and latency dashboards
- [ ] Regression tests for prompts

🛠️ Project: a 30-case evaluation set, with pass rates tracked across prompt versions.

### Phase 12 – Safety and security
- [ ] Prompt injection: direct and indirect
- [ ] Least-privilege tool permissions
- [ ] Sandboxed code execution
- [ ] Human approval for risky actions
- [ ] Budget and rate limits; data leakage

🛠️ Project: attack your own agent with ten injected web pages, then harden it until it refuses every attack.

### Phase 13 – Research frontier
- [ ] Long-horizon planning
- [ ] Computer-use and browser agents
- [ ] Agent benchmarks: SWE-bench, WebArena, GAIA
- [ ] Evaluation methodology (see [research](../../../research/README.md))

🛠️ Project: reproduce one small benchmark result from a paper and write a short report.
