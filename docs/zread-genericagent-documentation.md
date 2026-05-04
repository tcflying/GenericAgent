# Zread Documentation Archive: lsdefine/GenericAgent

Source: https://zread.ai/lsdefine/GenericAgent
Archived: 2026-04-29

This file contains the numbered Zread documentation pages discovered for the repository, plus the Zread overview landing page.

## Pages

1. [Overview](https://zread.ai/lsdefine/GenericAgent)
2. [Overview](https://zread.ai/lsdefine/GenericAgent/1-overview)
3. [Quick Start](https://zread.ai/lsdefine/GenericAgent/2-quick-start)
4. [API Key Configuration](https://zread.ai/lsdefine/GenericAgent/3-api-key-configuration)
5. [Chat Frontend Options](https://zread.ai/lsdefine/GenericAgent/4-chat-frontend-options)
6. [Architecture Overview](https://zread.ai/lsdefine/GenericAgent/8-architecture-overview)
7. [Agent Loop and Task Runner](https://zread.ai/lsdefine/GenericAgent/9-agent-loop-and-task-runner)
8. [Tool Dispatch Handler](https://zread.ai/lsdefine/GenericAgent/10-tool-dispatch-handler)
9. [Nine Atomic Tools](https://zread.ai/lsdefine/GenericAgent/11-nine-atomic-tools)
10. [Session Classes and Backends](https://zread.ai/lsdefine/GenericAgent/12-session-classes-and-backends)
11. [SSE Stream Parsing](https://zread.ai/lsdefine/GenericAgent/13-sse-stream-parsing)
12. [Multi-Session Fallback](https://zread.ai/lsdefine/GenericAgent/14-multi-session-fallback)
13. [TMWebDriver Bridge](https://zread.ai/lsdefine/GenericAgent/15-tmwebdriver-bridge)
14. [HTML Simplification Engine](https://zread.ai/lsdefine/GenericAgent/16-html-simplification-engine)
15. [Memory Hierarchy Design](https://zread.ai/lsdefine/GenericAgent/17-memory-hierarchy-design)
16. [L4 Session Archive Compression](https://zread.ai/lsdefine/GenericAgent/18-l4-session-archive-compression)
17. [Memory Management SOPs](https://zread.ai/lsdefine/GenericAgent/19-memory-management-sops)
18. [Skill Crystallization Process](https://zread.ai/lsdefine/GenericAgent/20-skill-crystallization-process)
19. [Autonomous Task Management](https://zread.ai/lsdefine/GenericAgent/21-autonomous-task-management)
20. [Scheduled Reflection and Cron](https://zread.ai/lsdefine/GenericAgent/22-scheduled-reflection-and-cron)
21. [Context Compression Strategy](https://zread.ai/lsdefine/GenericAgent/26-context-compression-strategy)

---

<!-- Page 1: https://zread.ai/lsdefine/GenericAgent -->

# Overview

Level: Beginner

**GenericAgent** is a minimal, self-evolving autonomous agent framework that grants any LLM system-level control over a local computer. Its entire core weighs in at roughly **3,000 lines of code**, organized around **9 atomic tools** and a **~100-line agent execution loop**. Through these, the agent gains direct access to the browser, terminal, filesystem, keyboard/mouse input, screen vision, and even Android devices — all while preserving real login sessions in a live browser.

The project's design philosophy is radical in its simplicity: **don't preload skills — evolve them.** Every time GenericAgent solves a novel task, it automatically crystallizes the execution path into a reusable skill. The longer you use it, the richer your personal skill tree becomes — all grown organically from that same 3K-line seed.

![GenericAgent Workflow](https://github.com/lsdefine/GenericAgent/blob/main/assets/images/workflow.jpg?raw=true)

## What Makes GenericAgent Different

GenericAgent sits at a unique intersection of minimalism, autonomy, and token efficiency. Unlike heavyweight agent frameworks that ship with hundreds of modules and consume 200K–1M context tokens per task, GenericAgent operates within a **<30K context window** while achieving comparable or better task completion rates. This efficiency comes not from cutting corners, but from a deliberately layered architecture that ensures the right knowledge surfaces at the right time.

The self-bootstrap proof is perhaps the most striking testament to this design: **everything in this repository — from installing Git and running `git init` to every commit message — was completed autonomously by GenericAgent itself.** The author never opened a terminal.

Sources: [README.md](README.md#L1-L50)

## Architecture at a Glance

GenericAgent is organized into four concentric layers. The outermost layer handles **LLM communication and session management**; inward sits the **agent execution loop** that orchestrates tool calls; deeper still lies the **tool dispatch handler** with nine atomic tools; and at the core, the **layered memory system** that enables persistent learning across sessions. Two additional subsystems — browser control and self-evolution — weave through these layers.

The entry point is `agentmain.py`, which instantiates the `GeneraticAgent` class, initializes LLM sessions from `mykey.py` configuration, and manages a task queue processed by a background thread. When a user sends a message, it flows through the agent loop (`agent_loop.py`), which calls the LLM, interprets tool calls, dispatches them to `GenericAgentHandler` in `ga.py`, and loops until the task completes or hits the turn limit.

Sources: [agentmain.py](agentmain.py#L42-L72), [agent\_loop.py](agent_loop.py#L42-L98), [ga.py](ga.py#L258-L260)

## Project Structure

The repository layout follows a flat, convention-driven structure rather than a deep package hierarchy. This keeps the codebase navigable and makes the ~3K-line claim tangible.

Copy code

```
GenericAgent/
├── agentmain.py          ├── agent_loop.py         # Core execution loop (~100 lines): LLM → tool → loop
├── ga.py                 # Tool dispatch handler: 9 atomic tools + memory tools
├── llmcore.py            # LLM backends: sessions, SSE parsing, multi-backend fallback
├── TMWebDriver.py        # Browser bridge: HTTP/WS server for CDP communication
├── simphtml.py           # HTML simplification: token-efficient web page parsing
├── launch.pyw            # One-command launcher: Streamlit UI + optional bot frontends
├── hub.pyw               # GUI service manager: tkinter-based launcher with service control
├── mykey_template.py     # API key configuration template
│
├── memory/               # Layered memory system
│   ├── memory_management_sop.md   # Memory hierarchy rules & axioms
│   ├── autonomous_operation_sop.md # Autonomous task execution SOP
│   ├── plan_sop.md       # Task planning SOP
│   ├── skill_search/     # Skill search & discovery
│   ├── L4_raw_sessions/  # Archived session records
│   └── *_sop.md          # Domain-specific SOPs
│
├── reflect/              # Self-evolution subsystem
│   ├── autonomous.py     # Autonomous exploration trigger
│   └── scheduler.py      # Cron-based scheduled task runner
│
├── frontends/            # Chat frontend adapters
│   ├── stapp.py / stapp2.py      # Streamlit web UIs
│   ├── qtapp.py                  # Qt desktop app
│   ├── tgapp.py                  # Telegram bot
│   ├── qqapp.py                  # QQ bot
│   ├── fsapp.py                  # Feishu bot
│   ├── wecomapp.py              # WeCom bot
│   ├── dingtalkapp.py           # DingTalk bot
│   ├── chatapp_common.py        # Shared frontend utilities & commands
│   ├── desktop_pet.pyw / desktop_pet_v2.pyw  # Desktop pet interfaces
│   └── skins/                   # Desktop pet skin assets
│
├── assets/               # Configuration & bridge assets
│   ├── tools_schema.json          # 9 atomic tool definitions (EN)
│   ├── tools_schema_cn.json       # 9 atomic tool definitions (CN)
│   ├── sys_prompt.txt / sys_prompt_en.txt  # System prompts
│   ├── global_mem_insight_template*.txt     # L1 memory templates
│   ├── tmwd_cdp_bridge/           # Chrome extension for CDP bridge
│   └── demo/                      # Demo GIFs and screenshots
│
├── plugins/              # Optional integrations
│   └── langfuse_tracing.py        # Langfuse observability plugin
│
└── tests/                # Test suite
    ├── conftest.py
    ├── test_minimax.py
    └── test_minimax_integration.py
```

Sources: [agentmain.py](agentmain.py#L42-L263), [launch.pyw](launch.pyw#L1-L129), [hub.pyw](hub.pyw#L1-L200), [reflect/scheduler.py](reflect/scheduler.py#L11-L62), [reflect/autonomous.py](reflect/autonomous.py#L1-L6)

## Nine Atomic Tools

The entire capability surface of GenericAgent is defined by just nine tools. This is not a limitation — it's a design decision. By keeping the toolset minimal, the system maximizes token efficiency and minimizes the cognitive load on the underlying LLM, leading to fewer hallucinations and more reliable task execution.

| Tool | Purpose | Key Insight |
| --- | --- | --- |
| `code_run` | Execute arbitrary Python or PowerShell code | The "escape hatch" — lets the agent install packages, write scripts, call APIs, or control hardware at runtime |
| `file_read` | Read file contents with optional line/keyword targeting | Always read before modifying to ensure accurate context |
| `file_write` | Create, overwrite, or append entire files | Best for large-scale file creation; supports `{{file:}}` reference expansion |
| `file_patch` | Replace unique text blocks within files | Precise surgical edits — the preferred method for modifications |
| `web_scan` | Perceive simplified HTML content and tab list | Filters sidebars, floating elements, and noise for token efficiency |
| `web_execute_js` | Execute arbitrary JavaScript in the browser | Full browser control — click, scroll, fill forms, extract data |
| `ask_user` |

Additionally, the system includes a hidden `no_tool` tool — automatically invoked when the LLM doesn't explicitly call any tool in a turn — which serves as a safety net for verification and continuation.

The `code\_run` tool is GenericAgent's primary mechanism for \*\*dynamic capability extension\*\*. Through it, the agent can install Python packages, write new scripts, call external APIs, or control hardware at runtime — and then crystallize these temporary abilities into permanent tools stored as SOPs in the memory layer.

Sources: [assets/tools\_schema.json](assets/tools_schema.json#L1-L73), [ga.py](ga.py#L277-L516)

## Layered Memory System

Memory is what separates a stateless chatbot from an agent that genuinely improves over time. GenericAgent implements a four-layer memory hierarchy, each with distinct roles, size constraints, and update rules.

| Layer | File / Location | Size Constraint | Purpose |
| --- | --- | --- | --- |
| **L0 — Meta Rules** | `assets/sys_prompt.txt` | Fixed | Core behavioral rules, action principles, system constraints |
| **L1 — Insight Index** | `memory/global_mem_insight.txt` | ≤30 lines, <1K tokens | Minimal routing index: scenario keywords → memory pointers |
| **L2 — Global Facts** | `memory/global_mem.txt` | Grows organically | Stable environment facts: paths, configs, user preferences |
| **L3 — Task Skills / SOPs** | `memory/*.md`, `memory/*.py` | Per-task, concise | Reusable workflows, domain-specific SOPs, utility scripts |
| **L4 — Session Archive** | `memory/L4_raw_sessions/` | Auto-managed | Archived task records distilled from finished sessions |

The system enforces a strict principle: **"No Execution, No Memory."** Every piece of information written to persistent memory must originate from a verified tool call result — not from model inference or speculation. This prevents hallucinated facts from contaminating the agent's knowledge base over time.

L4 session archives are collected automatically by the scheduler's cron mechanism every 12 hours, ensuring that task execution records are preserved for long-horizon recall without any manual intervention. This enables the agent to reference past work even across weeks of operation.

Sources: [memory/memory\_management\_sop.md](memory/memory_management_sop.md#L1-L60), [agentmain.py](agentmain.py#L23-L37), [reflect/scheduler.py](reflect/scheduler.py#L62-L64)

## Multi-LLM Support

GenericAgent is model-agnostic by design. It supports Claude, GPT, Gemini, Kimi, MiniMax, and any OpenAI-compatible API through a unified abstraction layer in `llmcore.py`. The configuration is driven entirely by `mykey.py` — a single file where you declare one or more LLM sessions.

| Session Type | Variable Name Pattern | Tool Protocol | Best For |
| --- | --- | --- | --- |
| `NativeClaudeSession` | Contains `native` + `claude` | Native API tool fields | Claude Opus/Sonnet via CC relay or direct Anthropic |
| `NativeOAISession` | Contains `native` + `oai` | Native API tool fields | GPT-4o, o-series, DeepSeek via OpenAI-compatible endpoints |
| `ClaudeSession` | Contains `claude` (no `native`) | Text protocol (deprecated) | Legacy Claude integration |
| `LLMSession` | Contains  (no ) |

The recommended configuration is **MixinSession** with multiple native sessions — it automatically rotates through backends on failure, with exponential backoff and optional spring-back to the primary. Switching models at runtime is as simple as typing `/llm n` in the chat interface.

Sources: [llmcore.py](llmcore.py#L461-L944), [agentmain.py](agentmain.py#L43-L72), [mykey\_template.py](mykey_template.py#L1-L200)

## Self-Evolution Mechanism

The self-evolution cycle is what fundamentally distinguishes GenericAgent from every other agent framework. It operates on a simple but powerful loop:

On the first encounter with a task type (e.g., "read my WeChat messages"), the agent autonomously explores: it installs dependencies, reverse-engineers data structures, writes utility scripts, and verifies everything works. On completion, it distills this entire execution path into a concise SOP stored in L3. The next time a similar task arrives, the agent recalls the SOP and executes in a fraction of the time.

This is further enhanced by the **reflection and scheduler subsystem** (`reflect/`). The autonomous module (`autonomous.py`) triggers exploration tasks when the user is idle for 30+ minutes. The scheduler (`scheduler.py`) runs as a cron daemon, executing recurring tasks, performing L4 session archive maintenance, and proactively monitoring for work.

Sources: [reflect/autonomous.py](reflect/autonomous.py#L1-L6), [reflect/scheduler.py](reflect/scheduler.py#L11-L62), [memory/autonomous\_operation\_sop.md](memory/autonomous_operation_sop.md#L1-L44)

## Browser Control System

GenericAgent doesn't use a sandboxed or headless browser — it injects into your **real browser**, preserving all login sessions, cookies, and personalization. This is achieved through a lightweight bridge architecture:

1. **TMWebDriver** (`TMWebDriver.py`) — A dual HTTP + WebSocket server running locally that accepts JavaScript execution requests and session management commands
2. **CDP Chrome Extension** (`assets/tmwd_cdp_bridge/`) — A minimal Chrome extension that connects to the TMWebDriver via WebSocket and executes CDP commands in the target browser tab
3. **HTML Simplification Engine** (`simphtml.py`) — A sophisticated HTML optimizer that strips sidebars, floating elements, navigation, and other non-essential content, reducing page payloads by up to 90% while preserving the semantic core

This architecture means GenericAgent can perform complex browser tasks — ordering food, managing stock portfolios, filling government forms — exactly as a human would, with full session context.

Sources: [TMWebDriver.py](TMWebDriver.py#L37-L284), [simphtml.py](simphtml.py#L593-L744), <assets/tmwd_cdp_bridge/manifest.json>

## Demo Showcase

| Task | Description |
| --- | --- |
| Order Tea | *"Order me a milk tea"* — Navigates the delivery app, selects items, and completes checkout automatically. |
| Stock Selection | *"Find GEM stocks with EXPMA golden cross, turnover > 5%"* — Screens stocks with quantitative conditions. |
| Web Exploration | Autonomously browses and periodically summarizes web content. |
| Alipay Expense | *"Find expenses over ¥2K in the last 3 months"* — Drives Alipay via ADB. |
| WeChat Batch | Sends bulk WeChat messages, fully driving the WeChat client. |

Sources: [README.md](README.md#L56-L75)

## Comparison with Similar Tools

| Feature | GenericAgent | Claude Code | OpenClaw |
| --- | --- | --- | --- |
| **Codebase** | ~3K lines | Large (open-sourced) | ~530,000 lines |
| **Deployment** | `pip install` + API Key | CLI + subscription | Multi-service orchestration |
| **Browser Control** | Real browser (session preserved) | Via MCP plugin | Sandbox / headless |
| **OS Control** | Mouse, keyboard, vision, ADB | File + terminal | Multi-agent delegation |
| **Self-Evolution** | Autonomous skill growth | Stateless between sessions | Plugin ecosystem |
| **Context Window** | <30K tokens | 200K tokens | Variable |
| **Token Efficiency** | High (layered memory) | Moderate | Low |

Sources: [README.md](README.md#L131-L145)

## What's Next

Now that you have a high-level understanding of GenericAgent's architecture and capabilities, here's the recommended reading path:

1. **[Quick Start](/2-quick-start)**  — Get GenericAgent running in under 5 minutes with step-by-step installation instructions
2. **[API Key Configuration](/3-api-key-configuration)**  — Configure your LLM backend(s) in `mykey.py`
3. **[Chat Frontend Options](/4-chat-frontend-options)**  — Choose your preferred chat interface (Streamlit, Telegram, QQ, Feishu, WeCom, DingTalk, or Desktop Pet)

For deeper architectural understanding after setup:

* **[Architecture Overview](/8-architecture-overview)**  — Detailed component interaction diagrams
* **[Agent Loop and Task Runner](/9-agent-loop-and-task-runner)**  — How the ~100-line core loop orchestrates execution
* **[Nine Atomic Tools](/11-nine-atomic-tools)**  — In-depth look at each tool's implementation
* **[Memory Hierarchy Design](/17-memory-hierarchy-design)**  — How the layered memory system works in detail

|  |
| --- |
| Pause execution to ask the user a question |

|  |
| --- |
| Human-in-the-loop for decisions, clarifications, or blockers |

|  |  |  |
| --- | --- | --- |
| `update_working_checkpoint` | Short-term working notepad for multi-turn tasks | Auto-injected each turn to prevent context loss |

|  |  |  |
| --- | --- | --- |
| `start_long_term_update` | Trigger distillation of long-term memory | Crystallizes reusable knowledge into the memory layers |

`oai`

`native`

|  |
| --- |
| Text protocol (deprecated) |

|  |
| --- |
| Legacy OpenAI-compatible integration |

|  |  |  |  |
| --- | --- | --- | --- |
| `MixinSession` | Contains `mixin` | Wraps multiple sessions | **Automatic multi-backend fallback with spring-back** |

Overview | lsdefine/GenericAgent | Zread---

<!-- Page 2: https://zread.ai/lsdefine/GenericAgent/1-overview -->

# Overview

Level: Beginner

**GenericAgent** is a minimal, self-evolving autonomous agent framework that grants any LLM system-level control over a local computer. Its entire core weighs in at roughly **3,000 lines of code**, organized around **9 atomic tools** and a **~100-line agent execution loop**. Through these, the agent gains direct access to the browser, terminal, filesystem, keyboard/mouse input, screen vision, and even Android devices — all while preserving real login sessions in a live browser.

The project's design philosophy is radical in its simplicity: **don't preload skills — evolve them.** Every time GenericAgent solves a novel task, it automatically crystallizes the execution path into a reusable skill. The longer you use it, the richer your personal skill tree becomes — all grown organically from that same 3K-line seed.

![GenericAgent Workflow](https://github.com/lsdefine/GenericAgent/blob/main/assets/images/workflow.jpg?raw=true)

## What Makes GenericAgent Different

GenericAgent sits at a unique intersection of minimalism, autonomy, and token efficiency. Unlike heavyweight agent frameworks that ship with hundreds of modules and consume 200K–1M context tokens per task, GenericAgent operates within a **<30K context window** while achieving comparable or better task completion rates. This efficiency comes not from cutting corners, but from a deliberately layered architecture that ensures the right knowledge surfaces at the right time.

The self-bootstrap proof is perhaps the most striking testament to this design: **everything in this repository — from installing Git and running `git init` to every commit message — was completed autonomously by GenericAgent itself.** The author never opened a terminal.

Sources: [README.md](README.md#L1-L50)

## Architecture at a Glance

GenericAgent is organized into four concentric layers. The outermost layer handles **LLM communication and session management**; inward sits the **agent execution loop** that orchestrates tool calls; deeper still lies the **tool dispatch handler** with nine atomic tools; and at the core, the **layered memory system** that enables persistent learning across sessions. Two additional subsystems — browser control and self-evolution — weave through these layers.

The entry point is `agentmain.py`, which instantiates the `GeneraticAgent` class, initializes LLM sessions from `mykey.py` configuration, and manages a task queue processed by a background thread. When a user sends a message, it flows through the agent loop (`agent_loop.py`), which calls the LLM, interprets tool calls, dispatches them to `GenericAgentHandler` in `ga.py`, and loops until the task completes or hits the turn limit.

Sources: [agentmain.py](agentmain.py#L42-L72), [agent\_loop.py](agent_loop.py#L42-L98), [ga.py](ga.py#L258-L260)

## Project Structure

The repository layout follows a flat, convention-driven structure rather than a deep package hierarchy. This keeps the codebase navigable and makes the ~3K-line claim tangible.

Copy code

```
GenericAgent/
├── agentmain.py          ├── agent_loop.py         # Core execution loop (~100 lines): LLM → tool → loop
├── ga.py                 # Tool dispatch handler: 9 atomic tools + memory tools
├── llmcore.py            # LLM backends: sessions, SSE parsing, multi-backend fallback
├── TMWebDriver.py        # Browser bridge: HTTP/WS server for CDP communication
├── simphtml.py           # HTML simplification: token-efficient web page parsing
├── launch.pyw            # One-command launcher: Streamlit UI + optional bot frontends
├── hub.pyw               # GUI service manager: tkinter-based launcher with service control
├── mykey_template.py     # API key configuration template
│
├── memory/               # Layered memory system
│   ├── memory_management_sop.md   # Memory hierarchy rules & axioms
│   ├── autonomous_operation_sop.md # Autonomous task execution SOP
│   ├── plan_sop.md       # Task planning SOP
│   ├── skill_search/     # Skill search & discovery
│   ├── L4_raw_sessions/  # Archived session records
│   └── *_sop.md          # Domain-specific SOPs
│
├── reflect/              # Self-evolution subsystem
│   ├── autonomous.py     # Autonomous exploration trigger
│   └── scheduler.py      # Cron-based scheduled task runner
│
├── frontends/            # Chat frontend adapters
│   ├── stapp.py / stapp2.py      # Streamlit web UIs
│   ├── qtapp.py                  # Qt desktop app
│   ├── tgapp.py                  # Telegram bot
│   ├── qqapp.py                  # QQ bot
│   ├── fsapp.py                  # Feishu bot
│   ├── wecomapp.py              # WeCom bot
│   ├── dingtalkapp.py           # DingTalk bot
│   ├── chatapp_common.py        # Shared frontend utilities & commands
│   ├── desktop_pet.pyw / desktop_pet_v2.pyw  # Desktop pet interfaces
│   └── skins/                   # Desktop pet skin assets
│
├── assets/               # Configuration & bridge assets
│   ├── tools_schema.json          # 9 atomic tool definitions (EN)
│   ├── tools_schema_cn.json       # 9 atomic tool definitions (CN)
│   ├── sys_prompt.txt / sys_prompt_en.txt  # System prompts
│   ├── global_mem_insight_template*.txt     # L1 memory templates
│   ├── tmwd_cdp_bridge/           # Chrome extension for CDP bridge
│   └── demo/                      # Demo GIFs and screenshots
│
├── plugins/              # Optional integrations
│   └── langfuse_tracing.py        # Langfuse observability plugin
│
└── tests/                # Test suite
    ├── conftest.py
    ├── test_minimax.py
    └── test_minimax_integration.py
```

Sources: [agentmain.py](agentmain.py#L42-L263), [launch.pyw](launch.pyw#L1-L129), [hub.pyw](hub.pyw#L1-L200), [reflect/scheduler.py](reflect/scheduler.py#L11-L62), [reflect/autonomous.py](reflect/autonomous.py#L1-L6)

## Nine Atomic Tools

The entire capability surface of GenericAgent is defined by just nine tools. This is not a limitation — it's a design decision. By keeping the toolset minimal, the system maximizes token efficiency and minimizes the cognitive load on the underlying LLM, leading to fewer hallucinations and more reliable task execution.

| Tool | Purpose | Key Insight |
| --- | --- | --- |
| `code_run` | Execute arbitrary Python or PowerShell code | The "escape hatch" — lets the agent install packages, write scripts, call APIs, or control hardware at runtime |
| `file_read` | Read file contents with optional line/keyword targeting | Always read before modifying to ensure accurate context |
| `file_write` | Create, overwrite, or append entire files | Best for large-scale file creation; supports `{{file:}}` reference expansion |
| `file_patch` | Replace unique text blocks within files | Precise surgical edits — the preferred method for modifications |
| `web_scan` | Perceive simplified HTML content and tab list | Filters sidebars, floating elements, and noise for token efficiency |
| `web_execute_js` | Execute arbitrary JavaScript in the browser | Full browser control — click, scroll, fill forms, extract data |
| `ask_user` |

Additionally, the system includes a hidden `no_tool` tool — automatically invoked when the LLM doesn't explicitly call any tool in a turn — which serves as a safety net for verification and continuation.

The `code\_run` tool is GenericAgent's primary mechanism for \*\*dynamic capability extension\*\*. Through it, the agent can install Python packages, write new scripts, call external APIs, or control hardware at runtime — and then crystallize these temporary abilities into permanent tools stored as SOPs in the memory layer.

Sources: [assets/tools\_schema.json](assets/tools_schema.json#L1-L73), [ga.py](ga.py#L277-L516)

## Layered Memory System

Memory is what separates a stateless chatbot from an agent that genuinely improves over time. GenericAgent implements a four-layer memory hierarchy, each with distinct roles, size constraints, and update rules.

| Layer | File / Location | Size Constraint | Purpose |
| --- | --- | --- | --- |
| **L0 — Meta Rules** | `assets/sys_prompt.txt` | Fixed | Core behavioral rules, action principles, system constraints |
| **L1 — Insight Index** | `memory/global_mem_insight.txt` | ≤30 lines, <1K tokens | Minimal routing index: scenario keywords → memory pointers |
| **L2 — Global Facts** | `memory/global_mem.txt` | Grows organically | Stable environment facts: paths, configs, user preferences |
| **L3 — Task Skills / SOPs** | `memory/*.md`, `memory/*.py` | Per-task, concise | Reusable workflows, domain-specific SOPs, utility scripts |
| **L4 — Session Archive** | `memory/L4_raw_sessions/` | Auto-managed | Archived task records distilled from finished sessions |

The system enforces a strict principle: **"No Execution, No Memory."** Every piece of information written to persistent memory must originate from a verified tool call result — not from model inference or speculation. This prevents hallucinated facts from contaminating the agent's knowledge base over time.

L4 session archives are collected automatically by the scheduler's cron mechanism every 12 hours, ensuring that task execution records are preserved for long-horizon recall without any manual intervention. This enables the agent to reference past work even across weeks of operation.

Sources: [memory/memory\_management\_sop.md](memory/memory_management_sop.md#L1-L60), [agentmain.py](agentmain.py#L23-L37), [reflect/scheduler.py](reflect/scheduler.py#L62-L64)

## Multi-LLM Support

GenericAgent is model-agnostic by design. It supports Claude, GPT, Gemini, Kimi, MiniMax, and any OpenAI-compatible API through a unified abstraction layer in `llmcore.py`. The configuration is driven entirely by `mykey.py` — a single file where you declare one or more LLM sessions.

| Session Type | Variable Name Pattern | Tool Protocol | Best For |
| --- | --- | --- | --- |
| `NativeClaudeSession` | Contains `native` + `claude` | Native API tool fields | Claude Opus/Sonnet via CC relay or direct Anthropic |
| `NativeOAISession` | Contains `native` + `oai` | Native API tool fields | GPT-4o, o-series, DeepSeek via OpenAI-compatible endpoints |
| `ClaudeSession` | Contains `claude` (no `native`) | Text protocol (deprecated) | Legacy Claude integration |
| `LLMSession` | Contains  (no ) |

The recommended configuration is **MixinSession** with multiple native sessions — it automatically rotates through backends on failure, with exponential backoff and optional spring-back to the primary. Switching models at runtime is as simple as typing `/llm n` in the chat interface.

Sources: [llmcore.py](llmcore.py#L461-L944), [agentmain.py](agentmain.py#L43-L72), [mykey\_template.py](mykey_template.py#L1-L200)

## Self-Evolution Mechanism

The self-evolution cycle is what fundamentally distinguishes GenericAgent from every other agent framework. It operates on a simple but powerful loop:

On the first encounter with a task type (e.g., "read my WeChat messages"), the agent autonomously explores: it installs dependencies, reverse-engineers data structures, writes utility scripts, and verifies everything works. On completion, it distills this entire execution path into a concise SOP stored in L3. The next time a similar task arrives, the agent recalls the SOP and executes in a fraction of the time.

This is further enhanced by the **reflection and scheduler subsystem** (`reflect/`). The autonomous module (`autonomous.py`) triggers exploration tasks when the user is idle for 30+ minutes. The scheduler (`scheduler.py`) runs as a cron daemon, executing recurring tasks, performing L4 session archive maintenance, and proactively monitoring for work.

Sources: [reflect/autonomous.py](reflect/autonomous.py#L1-L6), [reflect/scheduler.py](reflect/scheduler.py#L11-L62), [memory/autonomous\_operation\_sop.md](memory/autonomous_operation_sop.md#L1-L44)

## Browser Control System

GenericAgent doesn't use a sandboxed or headless browser — it injects into your **real browser**, preserving all login sessions, cookies, and personalization. This is achieved through a lightweight bridge architecture:

1. **TMWebDriver** (`TMWebDriver.py`) — A dual HTTP + WebSocket server running locally that accepts JavaScript execution requests and session management commands
2. **CDP Chrome Extension** (`assets/tmwd_cdp_bridge/`) — A minimal Chrome extension that connects to the TMWebDriver via WebSocket and executes CDP commands in the target browser tab
3. **HTML Simplification Engine** (`simphtml.py`) — A sophisticated HTML optimizer that strips sidebars, floating elements, navigation, and other non-essential content, reducing page payloads by up to 90% while preserving the semantic core

This architecture means GenericAgent can perform complex browser tasks — ordering food, managing stock portfolios, filling government forms — exactly as a human would, with full session context.

Sources: [TMWebDriver.py](TMWebDriver.py#L37-L284), [simphtml.py](simphtml.py#L593-L744), <assets/tmwd_cdp_bridge/manifest.json>

## Demo Showcase

| Task | Description |
| --- | --- |
| Order Tea | *"Order me a milk tea"* — Navigates the delivery app, selects items, and completes checkout automatically. |
| Stock Selection | *"Find GEM stocks with EXPMA golden cross, turnover > 5%"* — Screens stocks with quantitative conditions. |
| Web Exploration | Autonomously browses and periodically summarizes web content. |
| Alipay Expense | *"Find expenses over ¥2K in the last 3 months"* — Drives Alipay via ADB. |
| WeChat Batch | Sends bulk WeChat messages, fully driving the WeChat client. |

Sources: [README.md](README.md#L56-L75)

## Comparison with Similar Tools

| Feature | GenericAgent | Claude Code | OpenClaw |
| --- | --- | --- | --- |
| **Codebase** | ~3K lines | Large (open-sourced) | ~530,000 lines |
| **Deployment** | `pip install` + API Key | CLI + subscription | Multi-service orchestration |
| **Browser Control** | Real browser (session preserved) | Via MCP plugin | Sandbox / headless |
| **OS Control** | Mouse, keyboard, vision, ADB | File + terminal | Multi-agent delegation |
| **Self-Evolution** | Autonomous skill growth | Stateless between sessions | Plugin ecosystem |
| **Context Window** | <30K tokens | 200K tokens | Variable |
| **Token Efficiency** | High (layered memory) | Moderate | Low |

Sources: [README.md](README.md#L131-L145)

## What's Next

Now that you have a high-level understanding of GenericAgent's architecture and capabilities, here's the recommended reading path:

1. **[Quick Start](/2-quick-start)**  — Get GenericAgent running in under 5 minutes with step-by-step installation instructions
2. **[API Key Configuration](/3-api-key-configuration)**  — Configure your LLM backend(s) in `mykey.py`
3. **[Chat Frontend Options](/4-chat-frontend-options)**  — Choose your preferred chat interface (Streamlit, Telegram, QQ, Feishu, WeCom, DingTalk, or Desktop Pet)

For deeper architectural understanding after setup:

* **[Architecture Overview](/8-architecture-overview)**  — Detailed component interaction diagrams
* **[Agent Loop and Task Runner](/9-agent-loop-and-task-runner)**  — How the ~100-line core loop orchestrates execution
* **[Nine Atomic Tools](/11-nine-atomic-tools)**  — In-depth look at each tool's implementation
* **[Memory Hierarchy Design](/17-memory-hierarchy-design)**  — How the layered memory system works in detail

|  |
| --- |
| Pause execution to ask the user a question |

|  |
| --- |
| Human-in-the-loop for decisions, clarifications, or blockers |

|  |  |  |
| --- | --- | --- |
| `update_working_checkpoint` | Short-term working notepad for multi-turn tasks | Auto-injected each turn to prevent context loss |

|  |  |  |
| --- | --- | --- |
| `start_long_term_update` | Trigger distillation of long-term memory | Crystallizes reusable knowledge into the memory layers |

`oai`

`native`

|  |
| --- |
| Text protocol (deprecated) |

|  |
| --- |
| Legacy OpenAI-compatible integration |

|  |  |  |  |
| --- | --- | --- | --- |
| `MixinSession` | Contains `mixin` | Wraps multiple sessions | **Automatic multi-backend fallback with spring-back** |

Overview | lsdefine/GenericAgent | Zread---

<!-- Page 3: https://zread.ai/lsdefine/GenericAgent/2-quick-start -->

# Quick Start

Level: Beginner

Get GenericAgent running on your machine in under five minutes. This guide walks you through the minimal path from a fresh clone to your first autonomous task — no prior agent framework experience required. By the end, you'll have a working agent that can execute code, read and write files, and talk to you through a desktop chat window.

The entire process follows four stages: **install Python → configure an API key → launch the CLI → upgrade to GUI**. Each stage is self-contained; if you already have Python 3.11+ installed, jump straight to Stage 2.---

## Prerequisites

GenericAgent runs on **Python 3.10–3.13**. Version 3.14 is not supported due to pywebview compatibility issues. Both macOS and Windows are fully supported.

### macOS

Open Terminal (search "Terminal" in Spotlight) and run:

```
brew install python
```

If you see `brew: command not found`, install Homebrew first:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then re-run the `brew install python` command.

### Windows

1. Download the installer from [python.org/downloads](https://www.python.org/downloads/)
2. Run the installer and **check "Add Python to PATH"** at the bottom — this is critical
3. Click "Install Now"

### Verify Installation

Run the following in your terminal or Command Prompt:

```
python3 --version
```

On Windows, you may also need to try `python --version`. You should see `Python 3.10` or higher. If you see `Python 3.14`, please downgrade — pywebview and other dependencies are incompatible with 3.14.---

## Get the Code

Clone the repository using Git, or download it as a ZIP archive if you don't have Git yet.

```
git clone https://github.com/lsdefine/GenericAgent.git
cd GenericAgent
```

Alternatively, download the ZIP from the GitHub page, extract it to any folder, and open a terminal in that location.

![GenericAgent banner](https://github.com/lsdefine/GenericAgent/blob/main/assets/images/bar.jpg?raw=true)---

## Configure Your API Key

GenericAgent needs at least one LLM backend to function. Configuration lives in a single file called `mykey.py` — create it from the provided template.

```
cp mykey_template.py mykey.py
```

Open `mykey.py` in any text editor. You only need to fill in one configuration block. The system determines which session protocol to use based on the **variable name**, not the model name.

Sources: [mykey\_template.py](mykey_template.py#L1-L50)

### Minimal Configuration (Fastest Path)

The quickest way to get started is with a single OpenAI-compatible endpoint. Uncomment and fill in the `oai_config` block at the bottom of the file:

```
oai_config = {
    'apikey': 'sk-your-api-key-here',
    'apibase': 'http://your-api-host:port',        'model': 'your-model-name',
}
```

> **How `apibase` works**: The system auto-detects which suffix to append. `http://host:2001` appends `/v1/chat/completions`; `http://host:2001/v1` appends `/chat/completions`; a full URL is used as-is.

For a more robust setup with automatic failover, use the **mixin configuration** pattern that ships pre-configured in the template — it tries multiple backends in order and falls back on failure.

Sources: [mykey\_template.py](mykey_template.py#L116-L136)

### Variable Naming Convention

This table shows how variable names map to session types. Only variables containing `api`, `config`, or `cookie` are scanned at startup, so the naming must include one of those keywords.

| Variable name contains | Session class | Tool protocol | Recommended for |
| --- | --- | --- | --- |
| `native` + `claude` | NativeClaudeSession | API native tool field | Claude, Claude Code relay |
| `native` + `oai` | NativeOAISession | API native tool field | GPT, Gemini, any OAI-compatible |
| `claude` (no `native`) | ClaudeSession | Text protocol (legacy) | Older setups |
| `oai` (no `native`) | LLMSession | Text protocol (legacy) | General proxy services |
| `mixin` | MixinSession | Failover wrapper | Production use |

Sources: [mykey\_template.py](mykey_template.py#L12-L29), [agentmain.py](agentmain.py#L46-L56)

> **For full configuration details** — including Anthropic direct, CC relay, MiniMax, Kimi, OpenRouter, and global proxy settings — see [API Key Configuration](/3-api-key-configuration) .---

## First Launch: Command-Line Mode

With `mykey.py` configured, you can start the agent immediately in its minimal REPL mode. No additional packages are required for this step — the core agent loop uses only the Python standard library and `requests`.

```
python3 agentmain.py
```

On Windows, use `python agentmain.py` instead. You'll see a `>` prompt. Type any task and press Enter:

Copy code

```
> 帮我在桌面创建一个 hello.txt，内容是 Hello World
```

Copy code

```
> Create a file called hello.txt on my Desktop with the content "Hello World"
```

The agent will read your request, decide which tool to call (in this case `code_run`), execute the code, and report back. If it encounters a missing dependency, it will tell you what to install.

Sources: [agentmain.py](agentmain.py#L249-L262)

### REPL Commands

The command-line interface supports a few slash commands:

| Command | Effect |
| --- | --- |
| `/new` | Start a fresh conversation, clearing current context |
| `/session.temperature=0.3` | Adjust a session parameter at runtime |
| `/session.max_tokens=16384` | Change max output tokens for the current session |
| `Ctrl+C` | Abort the current running task |---

## Install Dependencies (Agent-Assisted)

GenericAgent can install its own dependencies. Once the CLI is running, simply tell the agent:

Copy code

```
请查看你的代码，安装所有用得上的 python 依赖
```

The agent will read through its own source files, identify required packages, and install them all via `pip`. If the agent cannot reach the API due to network issues, install `requests` manually first:

```
pip install requests
```

After dependencies are installed, the agent gains access to its full toolset including browser automation, GUI launch, and advanced memory features.

Sources: [GETTING\_STARTED.md](GETTING_STARTED.md#L152-L165)---

## Upgrade to GUI Mode

Once dependencies are in place, you can switch to the desktop GUI — a Streamlit-based chat window wrapped in a lightweight native window using pywebview.

```
python3 launch.pyw
```

This launches a floating desktop window on the right side of your screen. The `launch.pyw` script starts a Streamlit server on a random port between 18501–18599, then opens it in a native webview window. It also includes an **idle monitor** — if no activity is detected for 30 minutes, it automatically injects an autonomous task prompt.

![GenericAgent Workflow](https://github.com/lsdefine/GenericAgent/blob/main/assets/images/workflow.jpg?raw=true)

Sources: [launch.pyw](launch.pyw#L1-L128)

### Alternative: Hub Launcher

For more control over which services to start, use the hub launcher instead:

```
python hub.pyw
```

This opens a Tkinter-based control panel that auto-discovers all available frontends and reflect scripts, letting you toggle each one on/off with checkboxes. It requires **zero third-party dependencies** — pure tkinter and standard library only.

Sources: [hub.pyw](hub.pyw#L1-L35), [hub.pyw](hub.pyw#L86-L99)

### Launch Flags

The `launch.pyw` script supports command-line flags to enable optional services alongside the GUI:

| Flag | Service |
| --- | --- |
| `--tg` | Telegram Bot |
| `--qq` | QQ Bot |
| `--feishu` / `--fs` | Feishu (Lark) Bot |
| `--wecom` | WeCom Bot |
| `--dingtalk` / `--dt` | DingTalk Bot |
| `--sched` | Task Scheduler (cron) |
| `--llm_no N` | Select LLM backend by index |

Example — launching with Telegram and the scheduler:

```
python3 launch.pyw --tg --sched
```

Sources: [launch.pyw](launch.pyw#L65-L76)---

## What Happens at Startup

When GenericAgent starts, it performs a deterministic initialization sequence. Understanding this helps with troubleshooting.

1. **Config scan** — `agentmain.py` imports the `mykeys` dict from `llmcore.py`, which reads `mykey.py` and filters variables containing `api`, `config`, or `cookie` in their names. Each matching variable is instantiated into the appropriate session class based on the naming keywords.
2. **Tool schema load** — The JSON tool definitions from `assets/tools_schema.json` are loaded into `TOOLS_SCHEMA`. These define the 9 atomic tools the agent can invoke.
3. **Memory load** — The system reads layered memory files from the `memory/` directory (insight index, global facts, SOPs, and session archives).
4. **REPL loop** — In CLI mode, the agent enters an input loop. In GUI mode, `launch.pyw` wraps the same core in a Streamlit frontend.

Sources: [agentmain.py](agentmain.py#L42-L72), [agentmain.py](agentmain.py#L118-L167)---

## The 9 Atomic Tools at a Glance

GenericAgent's entire capability surface is defined by these tools. You don't need to memorize them — the agent decides which to call — but understanding them helps you know what to expect.

| Tool | What it does |
| --- | --- |
| `code_run` | Execute Python or PowerShell code in a sandboxed subprocess |
| `file_read` | Read file contents with line numbers and keyword search |
| `file_write` | Create, overwrite, or append to files |
| `file_patch` | Find-and-replace a unique text block in a file |
| `web_scan` | Capture simplified HTML and tab list from the browser |
| `web_execute_js` | Run arbitrary JavaScript in the browser |
| `ask_user` | Pause execution and ask the human a question |
| `update_working_checkpoint` | Save key context for use within a multi-turn task |
| `start_long_term_update` | Write important findings to persistent memory |

Sources: [assets/tools\_schema.json](assets/tools_schema.json#L1-L50), [ga.py](ga.py#L258-L516)---

## Troubleshooting

| Symptom | Likely Cause | Fix |
| --- | --- | --- |
| `ModuleNotFoundError: No module named 'requests'` | Base dependency missing | `pip install requests` |
| `[WARN] Failed to init MixinSession` | Mixin references a name that doesn't exist | Check that `llm_nos` values match the `name` field in your config blocks |
| `[ERROR] BAD Mixin config` | Cannot share history between incompatible session types | Do not mix Native and non-Native sessions in a single mixin |
| Agent does nothing / loops silently | Missing `requests` or API unreachable | Check network, verify `apikey` and `apibase` values |
| `python3` not recognized (Windows) | Python not in PATH | Reinstall with "Add Python to PATH" checked, or use `python` instead |---

## Next Steps

Now that GenericAgent is running, you have several paths forward depending on your goals:

* **[API Key Configuration](/3-api-key-configuration)**  — Set up multiple backends, failover chains, and advanced session parameters for production use
* **[Chat Frontend Options](/4-chat-frontend-options)**  — Connect to Telegram, QQ, Feishu, WeCom, DingTalk, or WeChat as your chat interface
* **[Overview](/1-overview)**  — Revisit the high-level design philosophy and self-evolution mechanism
* **[Architecture Overview](/8-architecture-overview)**  — Dive into the internal system design: the agent loop, layered memory, and tool dispatch

Quick Start | lsdefine/GenericAgent | Zread---

<!-- Page 4: https://zread.ai/lsdefine/GenericAgent/3-api-key-configuration -->

# API Key Configuration

Level: Beginner

GenericAgent communicates with large language models through API keys stored in a single configuration file. Getting this file right is the essential first step before the agent can think, act, or interact with any tools. This page walks you through the entire process — from creating your config file, to picking the right session type, to securing your credentials with the built-in keychain.

## How Configuration Loading Works

When GenericAgent starts, it looks for a Python module called `mykey.py` in the project root. If that file is missing, it falls back to `mykey.json` as a plain JSON alternative. The loader (`_load_mykeys()` in [llmcore.py](/lsdefine/GenericAgent/blob/main/llmcore.py#L6-L12)) imports the module and extracts all public variables (those not starting with `_`), then passes them to the agent's constructor. The agent constructor in [agentmain.py](/lsdefine/GenericAgent/blob/main/agentmain.py#L43-L72) scans every variable whose name contains `api`, `config`, or , and uses keyword matching to decide which session class to instantiate.

`cookie`

The flow can be visualized as follows:

Sources: [llmcore.py](/lsdefine/GenericAgent/blob/main/llmcore.py#L6-L12), [agentmain.py](/lsdefine/GenericAgent/blob/main/agentmain.py#L43-L72)

## Step 1: Create Your Configuration File

The repository ships two ready-made templates. Copy the one matching your language preference to `mykey.py`:

| Template | Language | Content |
| --- | --- | --- |
| `mykey_template.py` | Chinese (中文) | Full documentation with every provider variant, extensive inline comments |
| `mykey_template_en.py` | English | Concise version covering the three core session types |

```
cp mykey_template_en.py mykey.py
 
# Chinese users (更详细的中文注释):
cp mykey_template.py mykey.py
```

Then open `mykey.py` in any text editor, uncomment **one** configuration block, and fill in your real API key. The three most important fields in every config are:

| Field | Required | Purpose |
| --- | --- | --- |
| `apikey` | **Yes** | Your provider's API credential (e.g., `sk-ant-...`, `sk-or-...`, `sk-...`) |
| `apibase` | **Yes** | The API endpoint URL. Auto-completion rules apply (see below) |
| `model` | **Yes** | Model identifier (e.g., `claude-opus-4-7`, `gpt-5.4`) |

Sources: [mykey\_template\_en.py](/lsdefine/GenericAgent/blob/main/mykey_template_en.py#L1-L77), [mykey\_template.py](/lsdefine/GenericAgent/blob/main/mykey_template.py#L1-L426)

## Step 2: Choose the Right Session Type

The variable name you choose determines everything. Here is the keyword-to-session mapping, ordered by priority (the agent checks top-to-bottom):

| Variable name contains | Session class | Tool protocol | Recommendation |
| --- | --- | --- | --- |
| `native` + `claude` | `NativeClaudeSession` | API native `tool` field (function calling) | ✅ **Best for Claude** |
| `native` + `oai` | `NativeOAISession` | API native `tool` field (function calling) | ✅ **Best for GPT / Gemini** |
| `claude` (without `native`) | `ClaudeSession` | Text-protocol tools in message body | ⚠️ Deprecated |
| `oai` (without `native`) | `LLMSession` | Text-protocol tools in message body | ⚠️ Deprecated |
| `mixin` | `MixinSession` | Failover wrapper (references other sessions by `name`) | ✅ For reliability |

**"Native"** means tool calls travel in the API's official `tool` / `function` field — the same way Claude Code and OpenAI Codex do it. This is the format that state-of-the-art models were trained on, so it produces the most reliable tool-use behavior. **Always prefer Native sessions for new setups.**

Sources: [mykey\_template.py](/lsdefine/GenericAgent/blob/main/mykey_template.py#L14-L38), [agentmain.py](/lsdefine/GenericAgent/blob/main/agentmain.py#L48-L57)

## Step 3: Provider-Specific Configuration

### Claude via NativeClaudeSession

There are two sub-cases depending on whether you connect to Anthropic's official API or a third-party relay:

**Official Anthropic direct connection** — your key starts with `sk-ant-`:

```
native_claude_config = {
    'name': 'claude',
    'apikey': 'sk-ant-<your-anthropic-key>',
    'apibase': 'https://api.anthropic.com',
    'model': 'claude-opus-4-7[1m]',       # [1m] triggers 1M context beta
    'thinking_type': 'adaptive',           # 'adaptive' | 'enabled' | 'disabled'
}
```

**CC switch / third-party relay** — the most common approach in the community. The relay transparently forwards Claude Code protocol requests to upstream Anthropic. You **must** set `fake_cc_system_prompt: True`:

```
native_claude_config0 = {
    'name': 'cc-relay-1',
    'apikey': 'sk-user-<your-relay-key>',
    'apibase': 'https://<your-cc-switch-host>/claude/office',
    'model': 'claude-opus-4-7',
    'fake_cc_system_prompt': True,          # Required for ALL relay/proxy channels
    'thinking_type': 'adaptive',
}
```

The `fake_cc_system_prompt` flag controls how the system prompt is injected. When `True` (relays), the system prompt is embedded into the first user message to pass through CC protocol validation. When `False` (direct), it uses Anthropic's standard `system` field. Setting this incorrectly for your endpoint will cause authentication failures. The `NativeClaudeSession` constructor in [llmcore.py](/lsdefine/GenericAgent/blob/main/llmcore.py#L565-L574) defaults it to `False`, and the `raw_ask` method at [llmcore.py](/lsdefine/GenericAgent/blob/main/llmcore.py#L575-L607) branches on this flag when constructing the payload.

Sources: [mykey\_template.py](/lsdefine/GenericAgent/blob/main/mykey_template.py#L147-L210), [llmcore.py](/lsdefine/GenericAgent/blob/main/llmcore.py#L565-L607)

### GPT / OpenAI-Compatible via NativeOAISession

```
native_oai_config = {
    'name': 'gpt-native',
    'apikey': 'sk-<your-openai-key>',
    'apibase': 'https://api.openai.com/v1',     # Auto-completed to /v1/chat/completions
    'model': 'gpt-5.4',
    'api_mode': 'chat_completions',             # or 'responses' for /v1/responses
}
```

This works for OpenAI directly and any compatible provider (DeepSeek, Google Gemini via OpenAI-compatible endpoints, local models via Ollama/LM Studio, etc.). The `NativeOAISession` inherits from `NativeClaudeSession` and shares most infrastructure, differing only in the HTTP request format ([llmcore.py](/lsdefine/GenericAgent/blob/main/llmcore.py#L645-L654)).

Sources: [mykey\_template\_en.py](/lsdefine/GenericAgent/blob/main/mykey_template_en.py#L42-L50), [llmcore.py](/lsdefine/GenericAgent/blob/main/llmcore.py#L645-L654)

### Mixin Failover for Reliability

The `MixinSession` wraps multiple Native sessions into a single endpoint with automatic failover. If the first backend returns an error, the mixin transparently tries the next one in the `llm_nos` list.

```
mixin_config = {
    'llm_nos': ['claude', 'gpt-native'],   # References session 'name' fields, by priority
    'max_retries': 10,                      # Total rotation retry limit
    'base_delay': 0.5,                      # Exponential backoff start (delay ≈ base_delay × 2^n)
    # 'spring_back': 300,                   # Seconds before retrying primary after fallback
}
```

**Constraint**: All sessions referenced by a mixin must be the same "generation" — you can mix `NativeClaudeSession` and `NativeOAISession` (both are Native), but you cannot mix Native with deprecated non-Native sessions. The mixin's `_pick` method in [llmcore.py](/lsdefine/GenericAgent/blob/main/llmcore.py#L882-L885) iterates through the `llm_nos` list and returns the first healthy backend.

Sources: [mykey\_template\_en.py](/lsdefine/GenericAgent/blob/main/mykey_template_en.py#L54-L63), [llmcore.py](/lsdefine/GenericAgent/blob/main/llmcore.py#L856-L885)

## Understanding apibase Auto-Completion

You don't need to type the full URL path. The `auto_make_url()` function in [llmcore.py](/lsdefine/GenericAgent/blob/main/llmcore.py#L91-L95) handles three patterns:

| What you provide | What gets sent |
| --- | --- |
| `http://host:2001` | `http://host:2001/v1/chat/completions` |
| `http://host:2001/v1` | `http://host:2001/v1/chat/completions` |
| `http://host:2001/v1/chat/completions` | `http://host:2001/v1/chat/completions` (unchanged) |

For `NativeClaudeSession`, the path becomes `/messages` with `?beta=true` appended automatically to activate Anthropic beta features.

Sources: [llmcore.py](/lsdefine/GenericAgent/blob/main/llmcore.py#L91-L95), [mykey\_template.py](/lsdefine/GenericAgent/blob/main/mykey_template.py#L63-L67)

## All Configuration Fields Reference

Every config dict is passed to `BaseSession.__init__()` ([llmcore.py](/lsdefine/GenericAgent/blob/main/llmcore.py#L462-L487)). Here is the complete field list organized by category:

### Authentication & Routing

| Field | Default | Description |
| --- | --- | --- |
| `apikey` | *(none)* | **Required.** Keys starting with `sk-ant-` use `x-api-key` header; all others use `Authorization: Bearer` |
| `apibase` | *(none)* | **Required.** See auto-completion rules above |
| `model` | *(none)* | **Required.** Suffix `[1m]` triggers the 1M-context beta (stripped before sending) |
| `name` | model value | Display name in REPL `/llms` command; also the reference key for `mixin_config['llm_nos']` |
| `proxy` | *(none)* | Per-session HTTP proxy URL (e.g., `'http://127.0.0.1:2082'`). Overrides global proxy if set |

### Capacity & Timeouts

| Field | Default | Description |
| --- | --- | --- |
| `context_win` | 24000 (28000 for NativeClaudeSession) | History trimming threshold in characters — not a hard context limit |
| `max_retries` | 1 | Auto-retry count on HTTP 429/408/5xx errors |
| `connect_timeout` | 5 (10 if `stream=False`) | Connection timeout in seconds (minimum 1) |
| `read_timeout` | 30 (240 if `stream=False`) | Stream read timeout in seconds (minimum 5) |

### Reasoning & Thinking

| Field | Default | Description |
| --- | --- | --- |
| `reasoning_effort` | *(none)* | Budget level: `none` / `minimal` / `low` / `medium` / `high` / `xhigh` |
| `thinking_type` | *(none)* | Claude native thinking: `adaptive` (model decides) / `enabled` (requires `thinking_budget_tokens`) / `disabled` |
| `thinking_budget_tokens` | *(none)* | Required when `thinking_type='enabled'`. Reference: low≈4096, medium≈10240, high≈32768 |

### Sampling

| Field | Default | Description |
| --- | --- | --- |
| `temperature` | 1.0 | Sampling temperature. Kimi/Moonshot forces 1.0; MiniMax clamps to (0, 1] |
| `max_tokens` | 8192 | Maximum response tokens |

### Transport

| Field | Default | Description |
| --- | --- | --- |
| `stream` | `True` | `True` = SSE streaming (faster); `False` = full JSON response (safer for CDN-truncated SSE) |
| `api_mode` | `chat_completions` | `chat_completions` or `responses` (OpenAI only) |

### NativeClaudeSession Exclusive

| Field | Default | Description |
| --- | --- | --- |
| `fake_cc_system_prompt` | `False` | **Must be `True`** for all CC-switch/proxy/relay channels |
| `user_agent` | `claude-cli/2.1.113 (external, cli)` | Some relays whitelist by User-Agent; pin an older version if an upgrade causes rejections |

Sources: [mykey\_template.py](/lsdefine/GenericAgent/blob/main/mykey_template.py#L69-L131), [llmcore.py](/lsdefine/GenericAgent/blob/main/llmcore.py#L462-L487)

## Securing Keys with the Keychain (Optional)

For users who want to avoid storing raw API keys in plain text, GenericAgent includes a lightweight keychain module at [memory/keychain.py](/lsdefine/GenericAgent/blob/main/memory/keychain.py). It encrypts secrets with a user-specific XOR mask derived from your OS login username and stores them at `~/ga_keychain.enc`.

**Usage pattern in `mykey.py`:**

```
from memory.keychain import keys
 
# One-time setup (run once, then remove):
# keys.set("anthropic", "sk-ant-xxxxxxx")
 
native_claude_config = {
    'apikey': keys.anthropic.use(),    # Retrieves decrypted value
    'apibase': 'https://api.anthropic.com',
    'model': 'claude-opus-4-7',
}
```

The `SecretStr` wrapper ([memory/keychain.py](/lsdefine/GenericAgent/blob/main/memory/keychain.py#L10-L22)) ensures that accidental `print()` calls display only a masked preview (e.g., `SecretStr(anthropic=sk-ant-3a···f8e2 len=42)`) rather than the raw credential. The `.use()` method returns the plaintext string for actual API calls.

The keychain uses deterministic encryption tied to your OS username (`os.getlogin()`). It is not intended as a high-security vault — it primarily protects against accidental key exposure in logs, screenshots, and version control. For production environments, prefer environment variables or a dedicated secrets manager.

Sources: [memory/keychain.py](/lsdefine/GenericAgent/blob/main/memory/keychain.py#L1-L47)

## Chat Platform Keys (Optional)

If you plan to connect GenericAgent to a chat platform frontend (covered in [Chat Frontend Options](/4-chat-frontend-options) ), add the corresponding credentials at the bottom of `mykey.py`. Platforms with no credentials configured simply won't start their adapter — there is no penalty for leaving them commented out.

| Variable | Platform | Required fields |
| --- | --- | --- |
| `tg_bot_token`, `tg_allowed_users` | Telegram | Bot token from @BotFather |
| `qq_app_id`, `qq_app_secret` | QQ | QQ Open Platform credentials |
| `fs_app_id`, `fs_app_secret` | Feishu (Lark) | Feishu Open Platform credentials |
| `wecom_bot_id`, `wecom_secret` | WeCom (Enterprise WeChat) | WeCom application credentials |
| `dingtalk_client_id`, `dingtalk_client_secret` | DingTalk | DingTalk Open Platform credentials |

Sources: [mykey\_template.py](/lsdefine/GenericAgent/blob/main/mykey_template.py#L401-L426)

## Runtime Overrides

You don't need to restart GenericAgent to tweak session parameters. Use the REPL slash commands inside the running agent to adjust settings on the fly:

| Command | Effect |
| --- | --- |
| `/session.reasoning_effort=high` | Change thinking budget level immediately |
| `/session.thinking_type=adaptive` | Switch Claude thinking mode |
| `/session.thinking_budget_tokens=32768` | Set explicit thinking token budget |
| `/session.temperature=0.3` | Lower sampling temperature |
| `/session.max_tokens=16384` | Increase response length ceiling |

These calls use `setattr` on the current session's backend object, so they take effect instantly until you switch models or restart the process.

Sources: [mykey\_template.py](/lsdefine/GenericAgent/blob/main/mykey_template.py#L52-L58)

## Quick-Start Checklist

1. **Copy** the template: `cp mykey_template_en.py mykey.py`
2. **Uncomment** one configuration block matching your provider
3. **Fill in** `apikey`, `apibase`, and `model`
4. **Set** `fake_cc_system_prompt: True` if using a relay/proxy (not direct Anthropic)
5. **(Optional)** Add `mixin_config` for automatic failover across multiple providers
6. **Run** `python agentmain.py` — if credentials are valid, you'll see the `>`  REPL prompt

## What's Next

Once your API keys are configured and the agent starts successfully, the next logical step is choosing how you want to interact with it. Head to [Chat Frontend Options](/4-chat-frontend-options)  to explore the various chat platform integrations (Telegram, WeChat, QQ, Feishu, DingTalk, desktop pet, and more). If you'd rather first understand how the agent uses these sessions internally, continue to [Session Classes and Backends](/12-session-classes-and-backends)  in the Deep Dive section.

API Key Configuration | lsdefine/GenericAgent | Zread---

<!-- Page 5: https://zread.ai/lsdefine/GenericAgent/4-chat-frontend-options -->

# Chat Frontend Options

Level: Intermediate

GenericAgent is designed as a single-agent, multi-channel system: **one brain, many mouths**. Every frontend you launch connects to the same `GeneraticAgent` instance (or a sibling process with its own agent) and translates platform-specific message formats into the agent's internal task queue. This page catalogs all available frontends, explains the two architectural patterns they follow, and shows you how to launch them individually or via the unified service managers.

## Frontend Architecture at a Glance

All frontends share a common runtime pattern. Each script instantiates a `GeneraticAgent`, starts it as a daemon thread, then enters a platform-specific event loop that feeds incoming messages into `agent.put_task()` and streams results back through the platform's native messaging API. The key architectural split is between frontends that inherit from the shared `AgentChatMixin` base class and those that implement their own message handling from scratch.

Sources: [chatapp\_common.py](frontends/chatapp_common.py#L248-L337), [hub.pyw](hub.pyw#L18-L35), [launch.pyw](launch.pyw#L65-L115)

## Two Architectural Patterns

### AgentChatMixin — Shared Base Class

Frontends for WeCom, DingTalk, and QQ inherit from `AgentChatMixin`, which provides a complete async command dispatch system and agent task runner. The mixin defines three abstract-like methods that each subclass implements for platform specifics: `send_text()`, plus lifecycle hooks for the platform SDK's event loop.

The mixin handles seven slash commands out of the box via `handle_command()` at [chatapp\_common.py#L263-L303](frontends/chatapp_common.py#L263-L303):

| Command | Description |
| --- | --- |
| `/help` | Show all available commands |
| `/status` | Show agent state (running/idle) and current LLM |
| `/stop` | Abort the current task |
| `/new` | Reset conversation context |
| `/restore` | Restore the most recent conversation from logs |
| `/continue` | List restorable sessions; `/continue N` restores the Nth |
| `/llm` | List LLM backends; `/llm N` switch to backend N |

The core execution path lives in `run_agent()` at [chatapp\_common.py#L305-L331](frontends/chatapp_common.py#L305-L331): it submits the user's text via `agent.put_task()`, then polls the returned queue in an async loop, sending periodic "still thinking" pings and finally delivering the cleaned response via `send_done()`.

### Standalone Implementations

Telegram, WeChat, and Feishu each implement their own message handling logic without inheriting from the mixin. This gives them freedom to leverage platform-specific capabilities — Telegram uses `python-telegram-bot`'s `edit_message_text` for streaming edits; Feishu uses its interactive card API for progressive task updates with collapsible panels; WeChat implements its own `WxBotClient` with AES-encrypted media upload/download. Despite different implementations, they all converge on the same command set (`/help`, `/stop`, `/llm`, `/new`, `/restore`, `/continue`) for consistency.

Sources: [tgapp.py](frontends/tgapp.py#L104-L177), [wechatapp.py](frontends/wechatapp.py#L259-L324), [fsapp.py](frontends/fsapp.py#L534-L619)

## Complete Frontend Reference

### Messaging Platform Frontends

![chat interfaces](https://github.com/lsdefine/GenericAgent/blob/main/assets/images/wechat_group.jpg?raw=true)

| Frontend | File | Protocol | Auth Config in `mykey.py` | Streaming | Media |
| --- | --- | --- | --- | --- | --- |
| **Telegram** | `tgapp.py` | Bot API (polling) | `tg_bot_token`, `tg_allowed_users` | ✅ Edit-based streaming | ✅ Photo download |
| **WeChat** | `wechatapp.py` | ilinkai reverse-API | QR login (no config needed) | ❌ Wait for completion | ✅ Image/video/file/voice |
| **WeCom** | `wecomapp.py` | WebSocket SDK | `wecom_bot_id`, `wecom_secret`, `wecom_allowed_users` | ❌ Wait for completion | ❌ |
| **DingTalk** | `dingtalkapp.py` | Callback WebSocket | `dingtalk_client_id`, `dingtalk_client_secret`, `dingtalk_allowed_users` | ❌ Wait for completion | ❌ |
| **QQ** | `qqapp.py` | Official Bot API | `qq_app_id`, `qq_app_secret`, `qq_allowed_users` | ❌ Wait for completion | ❌ |
| **Feishu** | `fsapp.py` | Lark SDK | `fs_app_id`, `fs_app_secret`, `fs_allowed_users` | ✅ Card patch updates | ✅ Full media (up/down) |

**Telegram** is the most full-featured messaging frontend. It supports real-time streaming via message edits, photo reception, proxy configuration, and graceful auto-restart on polling crashes. It **requires** `tg_allowed_users` to be set — it refuses to start without an allow list for security at [tgapp.py#L185-L187](frontends/tgapp.py#L185-L187).

**WeChat** stands out as the only frontend that needs zero pre-configuration. It uses a reverse-engineered API through `WxBotClient` (inline class at [wechatapp.py#L21-L173](frontends/wechatapp.py#L21-L173)) with QR code login on first run. It also has the richest media support, downloading and re-uploading images, videos, files, and even voice messages (`.silk` format). The response handling at [wechatapp.py#L287-L321](frontends/wechatapp.py#L287-L321) automatically parses `[FILE:filepath]` markers and sends them as appropriate media types.

**Feishu** is the most sophisticated in terms of UI integration. It uses a `_TaskCard` class ([fsapp.py#L460-L515](frontends/fsapp.py#L460-L515)) that creates an interactive message card which gets progressively patched with each agent step — each step appears as a collapsible panel with a summary header and expandable detail section. It also supports full bidirectional media: uploading images/files to send to users and downloading media from received messages.

Sources: [tgapp.py](frontends/tgapp.py#L179-L213), [wechatapp.py](frontends/wechatapp.py#L259-L338), [fsapp.py](frontends/fsapp.py#L225-L232)

### Desktop & Web Frontends

![desktop pet](https://github.com/lsdefine/GenericAgent/blob/main/frontends/pet.gif?raw=true)

| Frontend | File | Tech Stack | Standalone | Key Feature |
| --- | --- | --- | --- | --- |
| **PySide6 Chat Panel** | `qtapp.py` | PySide6 | ✅ | Native desktop UI, floating button, Markdown, model switching |
| **Streamlit v1** | `stapp.py` | Streamlit | ✅ | Simple web UI, autonomous mode toggle |
| **Streamlit v2** | `stapp2.py` | Streamlit | ✅ | Anthropic-themed design, streaming fragments |
| **Webview Launcher** | `launch.pyw` | pywebview + Streamlit | ✅ | Windowed Streamlit + idle auto-task injection |
| **Desktop Pet** | `desktop_pet.pyw` / `desktop_pet_v2.pyw` | Tkinter + PIL | ✅ | Animated desktop companion with skins |
| **Hub Launcher** | `hub.pyw` | Tkinter | ✅ | Service discovery + management GUI |

**`qtapp.py`** is the most feature-rich desktop frontend — a 1747-line single-file application that provides a frameless, always-on-top chat panel with a draggable floating button indicator. It features multi-tab sessions, chat history persistence, Markdown rendering, file attachments, model health checks with live status indicators, an SOP viewer, settings panel, and autonomous mode integration. Its `ChatPanel` class ([qtapp.py#L749-L1664](frontends/qtapp.py#L749-L1664)) implements the full lifecycle from UI construction through agent interaction to history management.

**`stapp2.py`** offers the most polished web experience with an Anthropic-inspired light theme (custom CSS at [stapp2.py#L24-L659](frontends/stapp2.py#L24-L659)), dynamic font scaling, streaming response fragments, and a sidebar for agent configuration. It uses Streamlit's `@st.fragment` decorator for efficient partial rerenders.

**`launch.pyw`** serves a dual purpose: it wraps the Streamlit frontend in a native `pywebview` window and can optionally launch any combination of messaging bots alongside it. Its `idle_monitor()` function at <launch.pyw#L50-L63> detects when the user has been away for 30 minutes and automatically injects an autonomous task prompt into the chat.

**`hub.pyw`** is a pure-Tkinter service manager that auto-discovers all frontend scripts and reflection modules, presenting them as toggleable checkboxes with per-service log output. Its `discover_services()` function at <hub.pyw#L18-L35> scans the `frontends/` and `reflect/` directories for runnable Python scripts.

Sources: [qtapp.py](frontends/qtapp.py#L1-L6), [stapp2.py](frontends/stapp2.py#L23-L659), [launch.pyw](launch.pyw#L19-L63), [hub.pyw](hub.pyw#L18-L84)

## How to Launch

### Running a Single Frontend

Each frontend can be started independently. First ensure your `mykey.py` has the required credentials (copy `mykey_template.py` and fill in values), then run:

```
python frontends/tgapp.py
python frontends/wechatapp.py
python frontends/fsapp.py
python frontends/wecomapp.py
python frontends/dingtalkapp.py
python frontends/qqapp.py
 
# Desktop
python frontends/qtapp.py
python frontends/stapp.py          # or: streamlit run frontends/stapp.py
python frontends/desktop_pet.pyw   # Windows only (.pyw = no console)
```

Each messaging frontend enforces a **single-instance lock** via a TCP port binding (e.g., Telegram on port 19527, WeCom on 19529). Attempting to start a second instance prints a message and exits cleanly.

### Running via `launch.pyw` (Multi-Service)

The `launch.pyw` launcher starts the Streamlit web UI in a native window and optionally spawns any combination of messaging bots via CLI flags:

```
# Web UI + Telegram + Feishu
python launch.pyw --tg --feishu
 
# Web UI + all messaging bots + task scheduler
python launch.pyw --tg --qq --feishu --wecom --dingtalk --sched
 
# Custom port for Streamlit
python launch.pyw --tg --port 18550
 
# Specify initial LLM backend index
python launch.pyw --tg --llm_no 1
```

The `--sched` flag launches the autonomous task scheduler ([scheduler.py](reflect/scheduler.py)), which periodically triggers reflection and cron-based tasks.

### Running via `hub.pyw` (GUI Manager)

`hub.pyw` provides a graphical service manager with zero configuration. Run it and toggle checkboxes:

```
python hub.pyw
```

It auto-discovers all services from `frontends/` and `reflect/` directories. Each row shows the service name, a start/stop checkbox, and a live status indicator. Clicking a row displays its stdout/stderr output in the bottom panel. The "Rescan" button re-discovers services if new scripts are added.

Sources: [launch.pyw](launch.pyw#L65-L128), [hub.pyw](hub.pyw#L86-L200), [chatapp\_common.py](frontends/chatapp_common.py#L219-L226)

## Configuration in `mykey.py`

All frontend credentials live in your project-root `mykey.py` (or `mykey.json`). Below is a summary of every frontend-specific configuration key:

| Key | Used By | Description | Required |
| --- | --- | --- | --- |
| `tg_bot_token` | Telegram | BotFather-issued token | ✅ |
| `tg_allowed_users` | Telegram | Set of allowed Telegram user IDs | ✅ (enforced at startup) |
| `proxy` | Telegram | HTTP proxy for Bot API requests | ❌ (defaults to `http://127.0.0.1:2082`) |
| `fs_app_id` | Feishu | Feishu open-platform App ID | ✅ |
| `fs_app_secret` | Feishu | Feishu open-platform App Secret | ✅ |
| `fs_allowed_users` | Feishu | Set of allowed Open IDs (empty = public) | ❌ |
| `wecom_bot_id` | WeCom | WeCom bot ID | ✅ |
| `wecom_secret` | WeCom | WeCom app secret | ✅ |
| `wecom_welcome_message` | WeCom | Custom welcome message for new chats | ❌ |
| `wecom_allowed_users` | WeCom | Set of allowed user IDs | ❌ |
| `dingtalk_client_id` | DingTalk | DingTalk app client ID | ✅ |
| `dingtalk_client_secret` | DingTalk | DingTalk app client secret | ✅ |
| `dingtalk_allowed_users` | DingTalk | Set of allowed user IDs | ❌ |
| `qq_app_id` | QQ | QQ Official Bot app ID | ✅ |
| `qq_app_secret` | QQ | QQ Official Bot app secret | ✅ |
| `qq_allowed_users` | QQ | Set of allowed user IDs | ❌ |

\*\*Access control is platform-dependent.\*\* Telegram enforces its allow list at startup (refuses to run without `tg\_allowed\_users`). Feishu, WeCom, DingTalk, and QQ treat empty allow lists as \*\*public access\*\* — anyone who can reach the bot can interact with it. WeChat requires no pre-configuration at all since it authenticates via QR code. For production deployments, always set the appropriate `\_allowed\_users` key.

Feishu requires additional setup documented in [SETUP\_FEISHU.md](assets/SETUP_FEISHU.md) — you must create a Feishu app on the open platform, grant `im:message` and `im:message:send_as_bot` permissions, publish it, and obtain your Open ID for the allow list.

Sources: [tgapp.py](frontends/tgapp.py#L16-L18), [fsapp.py](frontends/fsapp.py#L225-L228), [wecomapp.py](frontends/wecomapp.py#L16-L19), [dingtalkapp.py](frontends/dingtalkapp.py#L17-L19), [qqapp.py](frontends/qqapp.py#L17-L19)

## Shared Utilities

### Text Processing Pipeline

All frontends rely on shared text-cleaning functions from `chatapp_common.py`. Raw agent output contains internal XML tags (`<thinking>`, `<summary>`, `<tool_use>`, `<file_content>`) that must be stripped before display to end users. The `clean_reply()` function at [chatapp\_common.py#L45-L48](frontends/chatapp_common.py#L45-L48) handles this via regex substitution. The `split_text()` function at [chatapp\_common.py#L59-L67](frontends/chatapp_common.py#L59-L67) splits long responses at line boundaries (never mid-sentence) for platforms with message length limits.

Each frontend defines its own `split_limit` to match platform constraints:

| Platform | Split Limit | Notes |
| --- | --- | --- |
| WeCom | 1200 chars | WeCom message API limit |
| QQ | 1500 chars | QQ Official Bot limit |
| AgentChatMixin (default) | 1500 chars | Base class default |
| DingTalk | 1800 chars | DingTalk batch message limit |
| WeChat | 1800 chars | With collapse logic at 6 chunks max |

### Session Restore System

The `/continue` and `/restore` commands are powered by `continue_cmd.py`, which parses agent response log files to extract conversation history. The `list_sessions()` function at [continue\_cmd.py#L82-L97](frontends/continue_cmd.py#L82-L97) scans `temp/model_responses_*.txt` files for recoverable sessions, while `restore()` at [continue\_cmd.py#L175-L196](frontends/continue_cmd.py#L175-L196) reconstructs history by parsing prompt/response pairs. This is installed as a monkey-patch on `GeneraticAgent` via `_install_continue(_GA)` at [chatapp\_common.py#L336](frontends/chatapp_common.py#L336), making it available across all frontends automatically.

Sources: [chatapp\_common.py](frontends/chatapp_common.py#L45-L67), [continue\_cmd.py](frontends/continue_cmd.py#L82-L196)

## Choosing a Frontend

The right frontend depends on your deployment context and interaction preferences. Here's a decision framework:

| Scenario | Recommended Frontend | Reason |
| --- | --- | --- |
| **Quick personal testing** | `qtapp.py` or `stapp2.py` | Zero external service config needed |
| **Mobile access on the go** | Telegram or WeChat | Ubiquitous mobile apps, always connected |
| **Enterprise workplace** | Feishu, DingTalk, or WeCom | Native integration with company tools |
| **Chinese social ecosystem** | QQ or WeChat | Widely used in China |
| **Maximum UI richness** | `qtapp.py` | Native desktop with Markdown, file attachments, model switching |
| **Production multi-channel** | `launch.pyw` or `hub.pyw` | Manage all channels from one place |
| **Autonomous always-on** | `launch.pyw` with `--sched` | Idle detection + scheduled task execution |

\*\*Multiple frontends can run simultaneously.\*\* Each messaging bot binds its own lock port and maintains independent task queues. However, they all share the same underlying `GeneraticAgent` brain — tasks submitted from different channels are serialized through the agent's internal queue. If you need truly parallel agents, consider running separate project instances on different ports.

## Next Steps

Now that you understand the available frontends, here's the recommended reading progression:

* **[Quick Start](/2-quick-start)**  — If you haven't yet set up your environment and run your first frontend
* **[API Key Configuration](/3-api-key-configuration)**  — For detailed LLM backend setup in `mykey.py`
* **[Architecture Overview](/8-architecture-overview)**  — To understand how frontends connect to the agent loop internals
* **[Session Classes and Backends](/12-session-classes-and-backends)**  — To understand the LLM sessions that all frontends ultimately rely on

Chat Frontend Options | lsdefine/GenericAgent | Zread---

<!-- Page 6: https://zread.ai/lsdefine/GenericAgent/8-architecture-overview -->

# Architecture Overview

Level: Intermediate

GenericAgent is a **general-purpose autonomous agent framework** built around a tightly coupled LLM-tool loop, layered long-term memory, and a pluggable multi-frontend architecture. Unlike typical chatbot wrappers, it treats the LLM as a *dispatch brain* that orchestrates nine atomic tools — code execution, file I/O, browser control, and memory management — across up to 40 reasoning turns per task. This page maps the system's macro-architecture, tracing the data flow from user input through every major subsystem.

![workflow](https://github.com/lsdefine/GenericAgent/blob/main/assets/images/workflow.jpg?raw=true)

## System Architecture Diagram

## Core Components at a Glance

The system decomposes into five primary subsystems, each with clear boundaries and a defined role in the agent's cognitive pipeline.

| Subsystem | Key Files | Responsibility |
| --- | --- | --- |
| **Entry & Launch** | `agentmain.py`, `launch.pyw`, `hub.pyw` | Process bootstrapping, CLI argument parsing, GUI startup, service lifecycle management |
| **Core Engine** | `agent_loop.py`, `ga.py` | Turn-based LLM↔Tool loop, tool dispatch, streaming output, checkpoint memory |
| **LLM Layer** | `llmcore.py` | Multi-backend session management, SSE streaming, protocol translation, multi-session fallback |
| **Browser Control** | `TMWebDriver.py`, `simphtml.py`, `assets/tmwd_cdp_bridge/` | Chrome tab management via WebSocket, HTML simplification for token efficiency |
| **Memory & Evolution** | `memory/`, `reflect/` | Layered long-term memory, SOP-based knowledge, scheduled tasks, autonomous idle actions |

Sources: [agentmain.py](agentmain.py#L42-L50), [agent\_loop.py](agent_loop.py#L42-L98), [llmcore.py](llmcore.py#L461-L645), [TMWebDriver.py](TMWebDriver.py#L37-L280)

## Execution Pipeline: From Input to Action

Every user interaction — whether typed at a CLI, sent via WeChat, or injected by an idle monitor — follows the same pipeline through four stages. Understanding this flow is essential before diving into any individual subsystem.

**Stage 1 — Task Enqueue**: The `GeneraticAgent.put_task()` method serializes the user query, its source identifier, and any images into a `queue.Queue`. This design decouples input collection (which may block on stdin or a websocket) from execution, allowing the agent to process tasks sequentially while the frontend remains responsive [agentmain.py](agentmain.py#L97-L101).

**Stage 2 — Loop Bootstrap**: The `run()` method dequeues a task, assembles the system prompt (combining the base prompt template with the current date and global memory), creates a fresh `GenericAgentHandler`, and invokes `agent_runner_loop()` — the central turn-based loop [agentmain.py](agentmain.py#L118-L150).

**Stage 3 — Turn Cycle**: Each iteration of `agent_runner_loop` sends the accumulated message history to the LLM via `client.chat()`, streams the response back, parses any tool calls, dispatches them through `handler.dispatch()` (which routes to `do_<tool_name>` methods), collects results, and appends them to the conversation. The loop terminates when the model emits no actionable tool call or when `should_exit` is flagged, with a hard cap of 40 turns [agent\_loop.py](agent_loop.py#L42-L98).

**Stage 4 — Output Delivery**: Streaming chunks are pushed to the `display_queue` in real time. Once the loop completes, the final aggregated response is emitted as a `'done'` event, which frontends format and deliver to the user [agentmain.py](agentmain.py#L155-L170).

Sources: [agentmain.py](agentmain.py#L97-L170), [agent\_loop.py](agent_loop.py#L42-L98)

## Entry Points and Service Orchestration

GenericAgent offers three distinct entry points, each targeting a different operational mode. All ultimately converge on the same `GeneraticAgent` core.

**`agentmain.py` — The universal core**. This file serves dual purpose: it is both the importable agent runtime and a standalone CLI. When run directly with `--task <IODIR>`, it operates in **one-shot file-IO mode**, reading from `input.txt` and writing to `output.txt`, with support for multi-round conversations via `reply.txt`. With `--reflect <SCRIPT>`, it enters **monitoring mode**, periodically calling `check()` on a Python script and dispatching tasks when triggered. Without flags, it drops into an interactive REPL loop [agentmain.py](agentmain.py#L171-L262).

**`launch.pyw` — The Streamlit GUI launcher**. Designed for desktop use, this launcher starts a Streamlit web UI in a native window, optionally launching chat platform bots (Telegram, QQ, Feishu, WeCom, DingTalk) and the cron scheduler as background processes. It also runs an **idle monitor thread** that injects an autonomous task after 30 minutes of user inactivity, triggering the agent's self-directed SOP execution [launch.pyw](launch.pyw#L65-L129).

**`hub.pyw` — The service manager**. A zero-dependency Tkinter application that auto-discovers all frontend scripts and reflect modules, presenting them as toggleable services with real-time log output. It uses a singleton port lock (`19735`) to prevent duplicate instances. This is the recommended entry point for developers managing multiple services [hub.pyw](hub.pyw#L1-L100).

| Entry Point | UI Technology | Key Flags | Best For |
| --- | --- | --- | --- |
| `agentmain.py` | CLI / Programmatic | `--task`, `--reflect`, `--input`, `--bg` | Scripting, CI/CD, one-shot tasks |
| `launch.pyw` | Streamlit (pywebview) | `--tg`, `--qq`, `--fs`, `--wecom`, `--dt`, `--sched` | Desktop interactive use |
| `hub.pyw` | Tkinter | None (GUI-driven) | Service management, development |

Sources: [agentmain.py](agentmain.py#L171-L262), [launch.pyw](launch.pyw#L1-L129), [hub.pyw](hub.pyw#L13-L40)

## The Nine Atomic Tools

The agent's entire interaction with the external world is mediated through exactly nine tools, defined in `assets/tools_schema.json` and implemented as `do_*` methods on `GenericAgentHandler` in `ga.py`. This constraint forces the LLM to decompose complex tasks into discrete, auditable steps.

| |---|-----------|----------|---------|  
| 1 | `code_run` | Execution | Run Python scripts or shell commands with configurable timeout and cwd |  
| 2 | `file_read` | File I/O | Read file contents with line numbers, keyword search, and context window |  
| 3 | `file_patch` | File I/O | Surgical find-and-replace of unique text blocks within files |  
| 4 | `file_write` | File I/O | Create, overwrite, or append entire files (bulk operations) |  
| 5 | `web_scan` | Browser | Capture simplified HTML and tab list from the active browser page |  
| 6 | `web_execute_js` | Browser | Execute arbitrary JavaScript in the browser with tab switching and save-to-file |  
| 7 | `update_working_checkpoint` | Memory | Maintain a short-term notepad injected each turn to prevent context loss |  
| 8 | `ask_user` | Interaction | Pause execution to solicit user decisions or clarification |  
| 9 | `start_long_term_update` | Memory | Trigger distillation of task-learned information into persistent global memory |

The tool dispatch uses a \*\*convention-over-configuration\*\* pattern: `BaseHandler.dispatch()` dynamically resolves `do\_` methods, with a special `no\_tool` fallback triggered when the LLM produces no tool call in a turn. This "null tool" enables the engine to perform a second confirmation pass, catching cases where the model appears done but left critical actions uncompleted.

Sources: [ga.py](ga.py#L258-L516), [assets/tools\_schema.json](assets/tools_schema.json#L1-L73), [agent\_loop.py](agent_loop.py#L14-L30)

## LLM Integration Layer

The LLM subsystem in `llmcore.py` implements a **three-tier client architecture** that abstracts over API differences between Claude, OpenAI-compatible, and protocol-translated backends.

**Session Backends** handle raw HTTP communication. `ClaudeSession` and `LLMSession` wrap Claude and OpenAI APIs respectively, with `NativeClaudeSession` and `NativeOAISession` providing direct native API access (including extended thinking support). Each session manages its own message history, model configuration, and streaming SSE parsing [llmcore.py](llmcore.py#L461-L645).

**Tool Clients** bridge the gap between the session's raw response format and the agent loop's expectations. `ToolClient` adds tool instruction injection and text-based tool call parsing for non-native-tool models. `NativeToolClient` handles Claude's native `tool_use` / `tool_result` content blocks, managing pending tool ID tracking and thinking prompt injection [llmcore.py](llmcore.py#L683-L970).

**MixinSession** provides automatic multi-backend fallback with a "spring-back" strategy: when the primary session fails, it transparently switches to a backup, then returns to the primary after a configurable cooldown period (default 300s). Broadcast attributes like `system`, `tools`, and `history` are synchronized across all sessions in the pool [llmcore.py](llmcore.py#L856-L900).

Sources: [llmcore.py](llmcore.py#L461-L645), [llmcore.py](llmcore.py#L683-L780), [llmcore.py](llmcore.py#L856-L970)

## Browser Control System

The browser subsystem enables the agent to perceive and manipulate web pages through a three-layer architecture.

**TMWebDriver** (`TMWebDriver.py`) is a WebSocket server that Chrome's CDP bridge extension connects to. It maintains session state for each browser tab, provides `execute_js()` for arbitrary JavaScript execution, and supports tab listing, switching, and navigation. Communication flows through a persistent WebSocket rather than CDP's native protocol, keeping the bridge extension lightweight [TMWebDriver.py](TMWebDriver.py#L37-L280).

**HTML Simplification Engine** (`simphtml.py`) is the critical token-optimization layer. Before presenting web content to the LLM, it runs a comprehensive JavaScript pipeline (`optHTML`) that strips hidden elements, removes floating overlays, collapses redundant navigation, and extracts the main content block. The `smart_truncate` function then budgets the remaining HTML to fit within ~35,000 characters while preserving structural fidelity [simphtml.py](simphtml.py#L4-L744).

**CDP Bridge Extension** (`assets/tmwd_cdp_bridge/`) is a minimal Chrome extension with a background script that connects to the TMWebDriver WebSocket, a content script that exposes page-level DOM access, and a popup for configuration. Each installation generates a unique tab identifier (`__ljq_XXXXXX`) stored in `config.js` <assets/tmwd_cdp_bridge/manifest.json>.

The `simphtml.py` module contains over 600 lines of embedded JavaScript, executed server-side before being injected into the browser. This design allows the HTML simplification logic to be version-controlled alongside the Python codebase, avoiding the fragility of browser-side-only transformations.

Sources: [TMWebDriver.py](TMWebDriver.py#L37-L280), [simphtml.py](simphtml.py#L4-L744), [agentmain.py](agentmain.py#L36-L37)

## Layered Memory System

Memory in GenericAgent is not a single store but a **four-layer hierarchy** that balances immediacy, persistence, and retrieval efficiency.

**L1 — Working Checkpoint** is a volatile, turn-scoped notepad maintained by `update_working_checkpoint`. It is injected into every system prompt during a multi-turn task to carry forward key findings, user requirements, and progress markers. It explicitly warns when inherited from a previous conversation session, prompting the agent to evaluate relevance [ga.py](ga.py#L427-L437).

**L2 — Global Memory** consists of two files: `global_mem.txt` (the raw memory store, directly editable by the agent) and `global_mem_insight.txt` (a structured insight summary following a fixed template). Both are injected into the system prompt via `get_global_memory()`, giving the LLM persistent access to accumulated knowledge about the user, environment, and operational lessons [ga.py](ga.py#L545-L558).

**L3 — SOP Documents** are markdown files in `memory/` that encode operational procedures: browser setup, memory management, scheduled tasks, vision API usage, and more. The agent reads these on demand as part of task execution, treating them as authoritative knowledge sources rather than inference-time context <memory/>.

**L4 — Session Archives** store compressed raw conversation logs in `memory/L4_raw_sessions/`. The `compress_session.py` script distills these into compact summaries, periodically triggered by the scheduler to prevent unbounded storage growth <memory/L4_raw_sessions/compress_session.py>.

| Layer | Scope | Persistence | Injection Method |
| --- | --- | --- | --- |
| L1 Working Checkpoint | Single task | Volatile (reset per task) | System prompt each turn |
| L2 Global Memory | Cross-session | Permanent (file-backed) | System prompt on boot |
| L3 SOPs | Cross-session | Permanent (version-controlled) | On-demand via `file_read` |
| L4 Session Archives | Historical | Periodic compression | Cron-driven via scheduler |

Sources: [ga.py](ga.py#L427-L437), [ga.py](ga.py#L545-L558), [agentmain.py](agentmain.py#L23-L25), <memory/L4_raw_sessions/compress_session.py>

## Self-Evolution Mechanisms

Beyond reactive task execution, GenericAgent incorporates two autonomous behaviors that enable it to act without explicit user prompts.

**Idle Detection** (`launch.pyw` / `reflect/autonomous.py`): The `idle_monitor` thread in `launch.pyw` watches for 30 minutes of user inactivity, then injects a task instructing the agent to read its autonomous operation SOP and execute self-directed tasks. The `reflect/autonomous.py` module serves as a standalone monitor script with a configurable check interval (default 1800s) [launch.pyw](launch.pyw#L65-L80), [reflect/autonomous.py](reflect/autonomous.py#L1-L6).

**Cron Scheduler** (`reflect/scheduler.py`): A more sophisticated autonomous mechanism that reads scheduled task definitions from `sche_tasks/`, parses cron-like repeat intervals, and triggers due tasks through the same `put_task()` pipeline. It also handles L4 archive compression on a 12-hour cycle. The scheduler implements a cooldown-based deduplication strategy and logs all executions [reflect/scheduler.py](reflect/scheduler.py#L11-L132).

Both mechanisms share the `--reflect` entry point pattern: `agentmain.py --reflect <script>` loads a Python module, calls `check()` on a configurable interval, and dispatches the returned task string to the agent's queue. This design keeps autonomous behavior fully pluggable — any script implementing `check()` and optionally `on_done()` can become a reflect module [agentmain.py](agentmain.py#L218-L248).

Sources: [launch.pyw](launch.pyw#L65-L80), [reflect/autonomous.py](reflect/autonomous.py#L1-L6), [reflect/scheduler.py](reflect/scheduler.py#L11-L132), [agentmain.py](agentmain.py#L218-L248)

## Project Structure Reference

The repository is organized as a flat module layout — no nested packages, no abstract class hierarchies beyond what's strictly necessary. Each top-level file is a self-contained module with a clear single responsibility.

Copy code

```
GenericAgent/
├── agentmain.py          # Agent core: task queue, LLM wiring, CLI entry
├── agent_loop.py         # Turn loop: LLM ↔ Tool cycle, streaming, dispatch
├── ga.py                 # Tool implementations: 9 atomic tools, handler class
├── llmcore.py            # LLM layer: sessions, clients, SSE parsing, fallback
├── TMWebDriver.py        # Browser bridge: WebSocket server, tab management
├── simphtml.py           # HTML engine: simplification, truncation, JS injection
├── launch.pyw            # GUI launcher: Streamlit + bots + idle monitor
├── hub.pyw               # Service manager: Tkinter dashboard for all services
├── frontends/            # Chat adapters: Streamlit, WeChat, TG, QQ, Feishu, etc.
├── memory/               # Knowledge store: SOPs, global memory, L4 archives
├── reflect/              # Self-evolution: autonomous triggers, cron scheduler
├── assets/               # Static config: tool schemas, prompts, Chrome extension
├── plugins/              # Extensions: Langfuse tracing integration
└── tests/                # Test suite: minimax integration tests
```

## Where to Go Next

This overview maps the full architectural landscape. To understand any subsystem in depth, follow the logical reading path through the catalog:

* **Start with the execution engine**: [Agent Loop and Task Runner](/9-agent-loop-and-task-runner)  traces the turn-by-turn reasoning cycle, then [Tool Dispatch Handler](/10-tool-dispatch-handler)  examines how each of the nine tools is resolved and executed.
* **Explore the LLM backbone**: [Session Classes and Backends](/12-session-classes-and-backends)  details each backend type, [SSE Stream Parsing](/13-sse-stream-parsing)  covers the streaming protocol, and [Multi-Session Fallback](/14-multi-session-fallback)  explains the MixinSession resilience strategy.
* **Dive into browser control**: [TMWebDriver Bridge](/15-tmwebdriver-bridge)  walks through the WebSocket architecture, and [HTML Simplification Engine](/16-html-simplification-engine)  unpacks the token-optimization pipeline.
* **Understand memory and evolution**: [Memory Hierarchy Design](/17-memory-hierarchy-design)  provides the full L1–L4 model, [Skill Crystallization Process](/20-skill-crystallization-process)  covers how procedural knowledge is extracted from task experience, and [Autonomous Task Management](/21-autonomous-task-management)  details the self-directed operation loop.---

<!-- Page 7: https://zread.ai/lsdefine/GenericAgent/9-agent-loop-and-task-runner -->

# Agent Loop and Task Runner

Level: Intermediate

The Agent Loop is the beating heart of GenericAgent — a turn-based execution engine that repeatedly sends prompts to an LLM, parses its responses for tool calls, dispatches those calls through a handler, and stitches the results back into the next prompt. This page traces the complete lifecycle of a task from submission to completion, covering the two-layer architecture (orchestrator + runner), the generator-based streaming model, and every safety mechanism that prevents the agent from spiraling out of control.

## Two-Layer Task Architecture

GenericAgent separates task management from execution into two distinct layers. The outer layer — `GeneraticAgent` in <agentmain.py> — manages LLM client initialization, task queuing, and the lifecycle of a handler instance. The inner layer — `agent_runner_loop` in <agent_loop.py> — is a pure function that drives the multi-turn conversation loop itself. This separation means the runner is backend-agnostic: it accepts any `client` with a `.chat()` method, any `handler` with a `.dispatch()` method, and any  describing available tools.

`tools_schema`

Copy code

```
┌─────────────────────────────────────────────────────────┐
│  GeneraticAgent  (agentmain.py)                        │
│  ┌──────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │LLM Client│  │ Task Queue   │  │ Handler Lifecycle │  │
│  │ Pool     │  │ (threading)  │  │ (per-task)        │  │
│  └────┬─────┘  └──────┬───────┘  └────────┬──────────┘  │
│       │               │                    │             │
└───────┼───────────────┼────────────────────┼─────────────┘
        │               ▼                    ▼
        │    ┌─────────────────────────────────────────┐
        │    │  agent_runner_loop  (agent_loop.py)     │
        │    │  while turn < max_turns:                │
        │    │    response = client.chat(messages)     │
        │    │    tool_calls = parse(response)         │
        │    │    outcomes = handler.dispatch(···)      │
        │    │    messages = assemble(outcomes)         │
        │    └──────────┬──────────────────────────────┘
        │               │
        ▼               ▼
  ┌──────────┐  ┌──────────────────────┐
  │ToolClient│  │GenericAgentHandler   │
  │/Native   │  │(ga.py) — do_* tools │
  │ToolClient│  │  callbacks, memory   │
  └──────────┘  └──────────────────────┘
```

The `GeneraticAgent.__init__` method scans <mykey_template.py> for API configurations and instantiates a pool of `ToolClient` or `NativeToolClient` objects, supporting Claude, OpenAI-compatible, native Anthropic, and mixin (multi-backend fallback) sessions <agentmain.py#L42-L72>. A `task_queue` (`queue.Queue`) accepts tasks from any source — interactive REPL, file I/O mode, or reflect-mode cron scripts — and serializes them through a single worker thread's `run()` loop <agentmain.py#L118-L167>.

Sources: <agentmain.py#L42-L72>, <agent_loop.py#L42-L43>

## The Runner Loop in Detail

`agent_runner_loop` is a generator function — every `yield` is a streaming chunk destined for the frontend display. This is not an aesthetic choice; it is the mechanism by which partial progress (LLM tokens, tool invocation headers, tool output) reaches the user in real time. The function accepts six parameters: `client`, `system_prompt`, `user_input`, `handler`, `tools_schema`, and `max_turns` (default 40) <agent_loop.py#L42>.

Each turn follows a strict five-phase sequence:

| Phase | Action | Key Detail |
| --- | --- | --- |
| **1. LLM Call** | `client.chat(messages, tools)` | Yields streaming chunks to caller; resets tool schema every 10 turns to fight context bloat |
| **2. Parse Response** | Extract `tool_calls` from response | If no tools called, injects synthetic `no_tool` call |
| **3. Dispatch** | `handler.dispatch(tool_name, args, response)` | Routes to `do_{tool_name}` method via `BaseHandler` |
| **4. Collect Outcomes** | Gather `StepOutcome` from each dispatch | Checks `should_exit` and `next_prompt` flags |
| **5. Assemble** | `turn_end_callback` + new message | Only the latest message is forwarded; full history lives in the Session backend |

The message model is deliberately minimal. The runner sends only a single-element message list to `client.chat()` — a `{"role": "user", "content": ..., "tool_results": ...}` dict <agent_loop.py#L95>. The `client` (either `ToolClient` or `NativeToolClient`) is responsible for maintaining the full conversation history internally within its backend session. This means the runner never sees its own past, which keeps its state footprint to a single turn.

Sources: <agent_loop.py#L42-L97>

## StepOutcome: The Loop Control Contract

The `StepOutcome` dataclass is the sole mechanism by which a tool implementation communicates back to the loop <agent_loop.py#L4-L8>. It carries three fields:

* **`data`**: The tool's return value. If non-`None` and the tool is not `no_tool`, it is serialized as JSON and appended to `tool_results` for the LLM to read <agent_loop.py#L87-L89>.
* **`next_prompt`**: Instructions injected into the next user message. A `None` value signals "current task done" — the loop exits <agent_loop.py#L84-L85>. A string beginning with `"未知工具"` triggers a tool schema reset on the client, a recovery mechanism for when the model hallucinates a nonexistent tool name <agent_loop.py#L86>.
* **`should_exit`**: A hard stop flag. When `True`, the loop breaks immediately and the `exit_reason` is recorded as `EXITED` <agent_loop.py#L82-L83>.

After all tools in a turn have been dispatched, the loop checks whether any `next_prompt` values were produced. If none exist and there are no pending `_done_hooks`, the loop terminates normally with `CURRENT_TASK_DONE` <agent_loop.py#L91-L93>. This dual-signal system (`should_exit` for hard aborts, `next_prompt=None` for graceful completion) provides tools with fine-grained control over the agent's lifecycle.

Sources: <agent_loop.py#L4-L8>, <agent_loop.py#L82-L97>

## BaseHandler and Tool Dispatch

`BaseHandler` in <agent_loop.py> defines the dispatch contract with four methods <agent_loop.py#L14-L29>:

* **`tool_before_callback`** / **`tool_after_callback`**: Lifecycle hooks called before and after each tool invocation, designed for cross-cutting concerns like logging or state mutation.
* **`turn_end_callback`**: Called after all tools in a turn complete. Receives the full response, all tool calls, all results, the turn number, the assembled `next_prompt`, and the `exit_reason`. Returns the (possibly modified) next prompt string <agent_loop.py#L17>.
* **`dispatch`**: The core router. It looks for a method named `do_{tool_name}` on the handler instance, calls it with `(args, response)`, and wraps the result in a `StepOutcome`. If no matching method exists, it returns a recovery outcome with `next_prompt` set to an error message <agent_loop.py#L18-L29>.

The dispatch method is generator-aware: it uses `try_call_generator` to transparently handle both regular return values and generator functions <agent_loop.py#L9-L12>. This means any `do_*` tool can `yield` intermediate output (visible to the user) and `return` a `StepOutcome` at the end — a pattern used extensively in `GenericAgentHandler` for progress reporting.

The `dispatch` method injects `\_index` into the `args` dict before calling the tool, indicating which tool call in a multi-tool turn this is [agent\_loop.py#L21](agent\_loop.py#L21). Tools use this to decide whether to inject working memory anchors (only on the first call) or skip them (subsequent calls in the same turn).

Sources: <agent_loop.py#L9-L29>

## GeneraticAgent.run(): The Orchestrator Thread

The `run()` method is an infinite loop that blocks on `task_queue.get()`, pulling one task at a time <agentmain.py#L118>. For each task, it:

1. **Processes slash commands** — commands like `/session.temperature=0.7` for live parameter tuning, or `/resume` for context recovery <agentmain.py#L122-L124>.
2. **Creates a fresh `GenericAgentHandler`** — but transfers `key_info` and `passed_sessions` from the previous handler, enabling cross-task working memory persistence <agentmain.py#L131-L137>.
3. **Constructs the system prompt** — loads from `sys_prompt.txt`, appends date, global memory, and any `extra_sys_prompt` from the LLM backend <agentmain.py#L129>.
4. **Invokes `agent_runner_loop`** — consuming the generator in a `for chunk in gen` loop, pushing each chunk to the task's `display_queue` for the frontend <agentmain.py#L143-L154>.
5. **Handles abort and errors** — checks for `_stop` files and `stop_sig` between chunks, catching backend exceptions gracefully <agentmain.py#L148-L161>.

The display queue protocol is simple: items are dicts with either a `'next'` key (incremental progress) or a `'done'` key (final result). The `inc_out` flag on `GeneraticAgent` controls whether incremental output is enabled; when disabled, every `'next'` item contains the *full* accumulated response rather than just the delta <agentmain.py#L152>.

Sources: <agentmain.py#L118-L168>

## GenericAgentHandler: The Concrete Tool Layer

`GenericAgentHandler` in <ga.py> extends `BaseHandler` with the full tool library and agent lifecycle logic <ga.py#L258-L266>. Its constructor initializes a working-memory dict (`self.working`), a history list, a code-stop signal list (for aborting running code), and a `_done_hooks` list for post-completion actions <ga.py#L260-L266>.

Two tool implementations are architecturally significant to the loop itself:

**`do_no_tool`** — This is the most complex "tool" in the system despite not being exposed in `TOOLS_SCHEMA`. It is automatically triggered when the LLM produces a response without any tool calls <agent_loop.py#L61>. Its responsibilities include: detecting blank/truncated responses and requesting regeneration <ga.py#L444-L450>; intercepting premature plan-mode completion claims that lack a `[VERIFY]` step <ga.py#L452-L455>; catching the "large code block with no tool call" anti-pattern where the model dumps code without invoking `code_run` or `file_write` <ga.py#L457-L478>; and finally, when all checks pass, returning `StepOutcome(response, next_prompt=None)` which terminates the loop gracefully <ga.py#L485-L486>.

**`turn_end_callback`** — This is where the handler asserts agent safety and continuity. It extracts a `<summary>` tag from the response (or constructs one from the tool call), appends it to `history_info` <ga.py#L516-L527>. Then it injects escalating warnings: at turn 7, a reminder to avoid futile retries; at turn 10, a global memory refresh; at turn 35 (or 70 in plan mode), a mandatory `ask_user` interrupt <ga.py#L528-L536>. It also checks for external intervention files (`_keyinfo`, `_intervene`) that allow an operator to inject context mid-task <ga.py#L538-L541>.

Sources: <ga.py#L258-L266>, <ga.py#L439-L543>

## Working Memory Injection via Anchors

Before the loop starts, `GeneraticAgent.run()` may inject a "working memory anchor" into the user's input. This happens when the task comes from a channel that supports context recovery (e.g., Feishu) and there is existing history <agentmain.py#L139-L140>. The `_get_anchor_prompt` method in the handler assembles this anchor from the last 20 history entries, the current turn counter, and any `key_info` or `related_sop` stored in `self.working` <ga.py#L504-L514>.

Within the loop, the same anchor is re-injected as the `next_prompt` by `do_update_working_checkpoint` <ga.py#L435-L437>, creating a persistent context thread across tool calls. This is the mechanism that allows the agent to maintain task state without relying on the LLM's native conversation memory.

Working memory survival across tasks is explicitly handled: when a new handler is created, `key\_info` is copied from the old handler with a deprecation notice (`此为 N 个对话前设置的key\_info`) that prompts the LLM to refresh or clear stale context [agentmain.py#L132-L136](agentmain.py#L132-L136). The `passed\_sessions` counter increments with each successive task.

Sources: <ga.py#L504-L514>, <agentmain.py#L132-L140>

## Client Types and Protocol Differences

The runner abstracts over two fundamentally different LLM communication protocols, both accessed through the same `client.chat(messages, tools)` interface:

**`ToolClient`** — Used for LLMs that lack native tool-use support (most OpenAI-compatible APIs). It builds a text-based protocol prompt that embeds tool schemas as instructions and expects tool calls in `<tool_use>` XML tags within the response text <llmcore.py#L747-L762>. The `_parse_mixed_response` method regex-extracts these tags and constructs `MockToolCall` / `MockResponse` objects <llmcore.py#L764-L813>. If the model fails to produce valid JSON inside a tool tag, a `bad_json` synthetic tool call is generated to trigger recovery <llmcore.py#L804-L811>.

**`NativeToolClient`** — Used for Anthropic Claude and OpenAI native tool-use APIs. It sets tools directly on the backend and receives structured `tool_calls` in the response object <llmcore.py#L942-L944>. It maintains a `_pending_tool_ids` list to auto-close any tool calls that don't receive explicit results <llmcore.py#L958-L960>.

| Feature | `ToolClient` | `NativeToolClient` |
| --- | --- | --- |
| Tool schema delivery | Embedded in text prompt | Native API `tools` parameter |
| Tool call format | `<tool_use>` XML in text | Structured `tool_calls` field |
| History management | Built into protocol prompt | Content-block based in session |
| Schema reset trigger | `last_tools = ''` + token threshold | Every 10 turns in runner |
| Response parsing | Regex + `MockResponse` | Direct `MockResponse` from backend |

Sources: <llmcore.py#L683-L704>, <llmcore.py#L930-L970>

## Safety Rails and Loop Termination

The agent loop incorporates multiple independent safety mechanisms that operate at different granularities:

1. **Hard limit**: `max_turns=40` prevents infinite loops regardless of tool behavior <agent_loop.py#L42>.
2. **Tool schema refresh**: Every 10 turns, `client.last_tools` is cleared, forcing the full tool schema to be re-injected into the next prompt <agent_loop.py#L51>.
3. **Escalating turn warnings**: The handler's `turn_end_callback` injects progressively stronger nudges at turns 7, 10, 35, and 70 <ga.py#L528-L536>.
4. **External abort**: The `_stop` file check in `GeneraticAgent.run()` and the `stop_sig` + `code_stop_signal` mechanism allow graceful interruption from outside the loop <agentmain.py#L148-L149>.
5. **Done hooks**: Tools like GPT can register post-completion hooks (`_done_hooks`) that inject an additional prompt after the loop would otherwise terminate, forcing a final verification pass <agentmain.py#L141>.
6. **Plan mode enforcement**: When in plan mode, premature completion claims are intercepted by `do_no_tool`, and a maximum of 70 turns is enforced <ga.py#L452-L455>, <ga.py#L536>.

The loop's final return value is a dict with a `result` key: either `EXITED` (hard stop), `CURRENT_TASK_DONE` (graceful completion), or `MAX_TURNS_EXCEEDED` <agent_loop.py#L96-L97>. This is consumed by `GeneraticAgent.run()` to determine post-task behavior.

Sources: <agent_loop.py#L42-L97>, <ga.py#L528-L536>, <agentmain.py#L141>

## Execution Modes and Entry Points

The `GeneraticAgent` supports three distinct execution modes, all mediated through the same `put_task()` → `run()` pipeline:

* **Interactive REPL** — The default mode when no CLI flags are set. Reads from stdin, pushes to the task queue, and streams output to the console <agentmain.py#L249-L261>.
* **File I/O task mode** (`--task`) — Reads input from `temp/{task}/input.txt`, writes incremental and final output to the same directory, and supports multi-round task chains via a `reply.txt` handshake with a 10-minute timeout <agentmain.py#L198-L217>.
* **Reflect mode** (`--reflect`) — Loads a Python script with a `check()` function that is polled at a configurable interval. When `check()` returns a non-`None` string, it is submitted as a task. Supports hot-reload, `ONCE` mode, and per-script logging <agentmain.py#L218-L248>.

All three modes converge on the same `agent_runner_loop` call with the same handler and client, ensuring consistent execution semantics regardless of origin.

Sources: <agentmain.py#L171-L263>

## Next Steps

Now that you understand how tasks flow from submission through the multi-turn loop to completion, the natural next question is: what happens when the loop dispatches a tool call? The [Tool Dispatch Handler](/10-tool-dispatch-handler)  page details how each `do_*` method is resolved, how generators enable streaming tool output, and how the nine core tools are implemented. For the LLM communication layer beneath the runner, see [Session Classes and Backends](/12-session-classes-and-backends)  and [SSE Stream Parsing](/13-sse-stream-parsing) .---

<!-- Page 8: https://zread.ai/lsdefine/GenericAgent/10-tool-dispatch-handler -->

# Tool Dispatch Handler

Level: Advanced

The Tool Dispatch Handler is the central nervous system of GenericAgent's action execution pipeline. It bridges the LLM's tool-call intentions with concrete side effects—code execution, file I/O, browser control, and user interaction—through a generator-based dispatch architecture that supports real-time streaming while maintaining strict error boundaries and stateful task context.

## Architecture Overview

The dispatch system is split across two files with clear separation of concerns: the abstract dispatch protocol lives in `agent_loop.py`, while all concrete tool implementations reside in `ga.py`. The orchestrator in `agentmain.py` wires them together at runtime.

Sources: [agent\_loop.py](agent_loop.py#L4-L31), [ga.py](ga.py#L258-L260)

## The Dispatch Protocol

### `BaseHandler` — Abstract Contract

`BaseHandler` in `agent_loop.py` defines the four-method contract that all handlers must satisfy. Its most critical method is `dispatch()`, which implements a **name-based dynamic dispatch** pattern: given a tool name string from the LLM response, it resolves the implementation by prepending `do_` and checking for the method via `hasattr`. This is the entire routing layer—no registration table, no decorator-based wiring, just Python's runtime introspection.

Sources: [agent\_loop.py](agent_loop.py#L14-L31)

### `StepOutcome` — Uniform Return Contract

Every tool handler returns a `StepOutcome` dataclass with three fields that control the agent loop's flow. The `data` field carries the tool's result back to the LLM as a tool\_result message. The `next_prompt` field injects context into the following turn; when `None`, it signals task completion. The `should_exit` flag triggers an immediate loop break used exclusively by `ask_user` for human-in-the-loop interrupts.

Sources: [agent\_loop.py](agent_loop.py#L4-L8)

### Generator-Based Streaming

A defining architectural choice: `dispatch()` and every `do_*` handler are **generators**, not plain functions. They `yield` status strings (e.g., `"[Action] Running python..."`) that propagate through `agent_runner_loop` to the display queue in real time. The runner uses a `try/StopIteration` pattern with a `proxy` generator to capture both intermediate yields and the final `StepOutcome` return value from a single dispatch call. The `exhaust()` utility handles non-verbose mode by silently consuming all yielded chunks.

This means every tool execution is observable mid-flight—the frontend sees progress updates before the LLM even receives the result.

Sources: [agent\_loop.py](agent_loop.py#L9-L11), [agent\_loop.py](agent_loop.py#L32-L36), [agent\_loop.py](agent_loop.py#L76-L86)

## The Dispatch Cycle in Detail

Each turn of `agent_runner_loop` follows a precise sequence:

### Multi-Tool Batching

The runner iterates over all tool\_calls in a single LLM response, dispatching each sequentially. Each dispatch receives an `_index` argument injected into `args` at [agent\_loop.py#L22](agent_loop.py#L22-L22). Handlers use this index to suppress anchor prompt injection for secondary calls (`_get_anchor_prompt(skip=index > 0)`), avoiding redundant context injection when the LLM issues multiple tool calls in one turn.

Sources: [agent\_loop.py](agent_loop.py#L68-L89)

### Error Recovery Paths

Three distinct error paths exist within the dispatch loop:

| Trigger | Response | Mechanism |
| --- | --- | --- |
| Unknown tool name | Warning yield + continue | `dispatch()` returns `StepOutcome` with `"未知工具"` next\_prompt; resets `last_tools` to force re-injection of tool schema |
| `bad_json` tool name | Continues with error message | Interpreted as LLM's self-reported parse failure; the `msg` arg becomes the next\_prompt |
| Handler exception | `StopIteration` capture | Wrapped in `try/StopIteration`; outcome extracted from `e.value` |

Sources: [agent\_loop.py](agent_loop.py#L25-L31), [agent\_loop.py](agent_loop.py#L80-L86)

## Callback Hooks

### Per-Tool Callbacks

`tool_before_callback` and `tool_after_callback` in `BaseHandler` are no-ops by default, designed for subclass override. They wrap every dispatched tool call and receive the same arguments plus the result (for `after`). The `try_call_generator` adapter ensures they work whether overridden as plain functions or generators.

Sources: [agent\_loop.py](agent_loop.py#L15-L16)

### `turn_end_callback` — Post-Turn Enrichment

`GenericAgentHandler.turn_end_callback` is the most complex hook, responsible for five post-turn operations executed after all tool calls in a turn complete:

1. **Summary extraction**: Parses `<summary>` from the LLM response; falls back to a tool-name-based summary if missing, appending a `[DANGER]` warning about protocol violation.
2. **Staleness guards**: Injects increasingly urgent warnings at turn 7, 10, 35, and 70—escalating from "switch strategy" to mandatory `ask_user` intervention. Every 10th turn also re-injects global memory.
3. **Plan mode enforcement**: In plan mode, periodically reminds the agent to re-read the plan file; at turn 70, forces a user checkpoint.
4. **External injection**: Reads `_keyinfo` and `_intervene` files from the task directory (consumed once via `consume_file`), injecting master-level overrides into working memory and the next prompt.
5. **Turn-end hooks**: Fires any registered `_turn_end_hooks` from the parent agent with a read-only `locals()` snapshot.

Sources: [ga.py](ga.py#L516-L544)

## `GenericAgentHandler` — Concrete Implementations

### Handler State

The handler maintains four pieces of mutable state that persist across all tool calls within a task:

* **`working` dict**: Holds `key_info` (short-term notepad), `related_sop`, `in_plan_mode`, and `passed_sessions`.
* **`history_info` list**: Append-only log of `[USER]` and `[Agent]` summaries, carrying context across tasks.
* **`code_stop_signal` list**: Thread-safe abort mechanism; `append(1)` triggers subprocess termination in `code_run`.
* **`_done_hooks` list**: Post-completion prompts injected when no more next\_prompts exist but the task isn't explicitly done.

Sources: [ga.py](ga.py#L260-L266)

### The Nine Exposed Tools

These are the tools defined in `tools_schema.json` and presented to the LLM via function calling. Each has a corresponding `do_*` method:

| Tool Name | Method | Category | Key Behavior |
| --- | --- | --- | --- |
| `code_run` | `do_code_run` | Execution | Extracts code from reply block if no `script` arg; supports `inline_eval` mode |
| `file_read` | `do_file_read` | File I/O | Keyword search with context window; fuzzy-match suggestions on `FileNotFoundError` |
| `file_patch` | `do_file_patch` | File I/O | Exact-match replacement with `{{file:...}}` reference expansion |
| `file_write` | `do_file_write` | File I/O | Extracts content from `<file_content>` tags or code blocks in response body |
| `web_scan` | `do_web_scan` | Browser | Simplified HTML via `simphtml`; tab switching support |
| `web_execute_js` | `do_web_execute_js` | Browser | Full JS control; result file persistence via `save_to_file` |
| `update_working_checkpoint` | `do_update_working_checkpoint` | Meta | Persists `key_info` and `related_sop` in handler state |
| `ask_user` | `do_ask_user` | Interaction | Returns `should_exit=True` to halt loop for human response |
| `start_long_term_update` | `do_start_long_term_update` | Memory | Triggers memory distillation; injects SOP and current memory as next\_prompt |

Sources: [assets/tools\_schema.json](assets/tools_schema.json#L1-L73), [ga.py](ga.py#L277-L504)

### The Invisible Tenth Tool: `no_tool`

`do_no_tool` is never included in `TOOLS_SCHEMA`. When the LLM produces a response without any tool calls, the runner synthesizes a `no_tool` call automatically at [agent\_loop.py#L69](agent_loop.py#L69-L69). This handler performs critical quality assurance:

* **Empty response detection**: Yields a warning and forces regeneration.
* **Incomplete response detection**: Catches truncated SSE responses (SSL errors, max\_tokens).
* **Plan mode completion gate**: Intercepts premature "task done" claims in plan mode unless a `[VERIFY]` step with `VERDICT` output exists.
* **Dangling code block detection**: If the response is essentially one large code block with no tool call and minimal prose, requests explicit clarification.
* **Plan completion check**: Auto-exits plan mode when no unchecked `[ ]` items remain in the plan file.

Sources: [ga.py](ga.py#L439-L488)

The `do\_no\_tool` handler's code-block detection logic at [ga.py#L462-L480](ga.py#L462-L480) uses a precise heuristic: exactly one code block ≥50 chars, followed by only whitespace, with ≤30 chars of non-tag residual content after stripping `` and ``. This prevents false positives on responses that legitimately discuss code without executing it.

## Integration with the Agent Runner

`GeneraticAgent.run()` in `agentmain.py` instantiates a fresh `GenericAgentHandler` per task, but carries forward `key_info` from the previous handler to maintain working memory continuity across conversation turns. The handler receives the active `llmclient` as its `parent`, giving it indirect access to the full session history, task directory, and verbose flag.

The system prompt is assembled from a base template file plus `get_global_memory()` injection, and the tool schema is loaded once at startup (or re-loaded when switching to Chinese-preferring LLMs via `load_tool_schema('_cn')`). On non-Windows platforms, `powershell` in the schema is automatically replaced with `bash`.

Sources: [agentmain.py](agentmain.py#L118-L168), [agentmain.py](agentmain.py#L14-L15)

## Schema Loading and Platform Adaptation

Tool schemas are not hardcoded into the handler. Instead, `load_tool_schema()` at module level reads `assets/tools_schema.json` (or `_cn.json`) and stores it in the global `TOOLS_SCHEMA` variable. On Unix systems, a string replacement swaps `powershell` references to `bash`, ensuring the `code_run` tool's enum matches the actual execution environment. This schema is then passed directly to `agent_runner_loop`, which forwards it to the LLM client's `chat()` method as the function-calling specification.

Sources: [agentmain.py](agentmain.py#L14-L16)---

To understand how the dispatched tools are called in the context of the full execution loop, continue to [Agent Loop and Task Runner](/9-agent-loop-and-task-runner) . For a detailed examination of each individual tool's capabilities and parameters, proceed to [Nine Atomic Tools](/11-nine-atomic-tools) .---

<!-- Page 9: https://zread.ai/lsdefine/GenericAgent/11-nine-atomic-tools -->

# Nine Atomic Tools

Level: Advanced

GenericAgent's entire behavioral repertoire reduces to exactly nine tools exposed to the LLM via OpenAI-compatible function-calling schemas. This is not a minimal viable set — it is a *maximally composable* one. Every complex capability the agent demonstrates (browser automation, memory crystallization, multi-step file editing) emerges from sequencing these primitives within the agentic loop. The schemas are declared as static JSON arrays in [tools\_schema.json](assets/tools_schema.json#L1-L73) and their Chinese-localized counterparts in [tools\_schema\_cn.json](assets/tools_schema_cn.json#L1-L73), loaded at startup through `load_tool_schema()` in [agentmain.py](agentmain.py#L14-L18).

The dispatch architecture follows a naming convention enforced by `BaseHandler.dispatch()` in [agent\_loop.py](agent_loop.py#L18-L29): each tool named `X` maps to a method `do_X` on the handler class via `getattr`. The `GenericAgentHandler` in [ga.py](ga.py#L258-L558) implements all nine `do_*` methods, each returning a `StepOutcome` dataclass that carries  (the tool result),  (what to feed back to the LLM), and  (a hard stop flag). A tenth implicit tool —  — handles the case where the LLM produces no explicit tool call, acting as a safety net for edge cases like empty responses, truncated outputs, or "code block without a tool call" anti-patterns.

`data`

`next_prompt`

`should_exit`

`do_no_tool`

## Tool Taxonomy and Relationships

The nine tools fall into three functional clusters, each mapping to a distinct domain of agent capability. Within the agentic loop, these clusters form a natural workflow: **Perceive** the environment → **Manipulate** files and code → **Persist** insights for future turns.

| Cluster | Tool | Domain | Primary Output | Exit Signal |
| --- | --- | --- | --- | --- |
| **Environment Perception** | `web_scan` | Browser DOM | Simplified HTML + tab metadata | No |
|  | `web_execute_js` | Browser runtime | JS return + DOM diff | No |
|  | `file_read` | Local filesystem | Line-addressed text | No |
| **Manipulation** | `code_run` | OS processes | stdout + exit code | No |
|  | `file_patch` | Precise edits | Status confirmation | No |
|  | `file_write` | Bulk file I/O | Byte count | No |
| **Cognitive Persistence** | `update_working_checkpoint` | Turn-scoped memory | Acknowledgment | No |
|  | `ask_user` | Human-in-the-loop | User's answer | **Yes** (`should_exit=True`) |

The `ask_user` tool is the only one that sets `should_exit=True`, which causes the agent loop to break and yield control back to the user. All other tools return `next_prompt` values that feed back into the loop, enabling arbitrary-length task chains.

Sources: [agent\_loop.py](agent_loop.py#L42-L97), [ga.py](ga.py#L302-L307)

## Environment Perception Tools

### `web_scan` — Structured DOM Observation

This tool captures the current browser state as simplified HTML. It delegates to `simphtml.get_html()` in [simphtml.py](simphtml.py#L702-L739), which runs a multi-stage pipeline: (1) an in-browser JavaScript function `optHTML()` removes hidden, floating, and covered elements client-side; (2) `optimize_html_for_tokens()` strips SVG content, inline styles, and long data-attributes server-side; (3) a `cutlist` mechanism identifies repetitive list items and collapses them into `[FAKE ELEMENT]` stubs with sample text; and (4) `smart_truncate()` recursively prunes the DOM tree to fit within a ~35k character budget, protecting `[FAKE ELEMENT]` markers from deletion.

Three parameters control observation granularity: `tabs_only` returns just the tab list (no HTML, minimal tokens), `switch_tab_id` changes the active tab before scanning, and `text_only` strips all HTML tags for plain-text extraction. The handler method at [ga.py](ga.py#L309-L321) injects the working memory anchor prompt into `next_prompt` after each scan, ensuring the LLM retains task context across observations.

Sources: [ga.py](ga.py#L309-L321), [simphtml.py](simphtml.py#L702-L739), [simphtml.py](simphtml.py#L593-L616), [assets/tools\_schema.json](assets/tools_schema.json#L37-L44)

### `web_execute_js` — Full Browser Control

This is the agent's primary browser manipulation tool — the schema description explicitly states "no guessing, act accurately to reduce web\_scan calls." It delegates to `simphtml.execute_js_rich()` in [simphtml.py](simphtml.py#L817-L871), which implements a sophisticated change-detection protocol: before executing the script, it captures a baseline HTML snapshot (unless `no_monitor=True`); after execution, it runs a DOM diff via `find_changed_elements()` and collects transient text elements from a string-monitoring interval timer (`startStrMonitor`) to catch toast notifications, alerts, and other ephemeral UI changes. The result dict includes `js_return`, `diff` (DOM change summary), `transients` (toast/alert text), `newTabs` (if the script opened tabs), `reloaded` (if the page navigated), and `suggestion` (a natural-language hint about what happened).

Like `code_run`, this tool supports dual input modes: either a `script` parameter or a ````javascript`code block extracted from the LLM's response content via`\_extract\_code\_block()`. The` save\_to\_file`parameter allows persisting long JS return values to disk. Multi-call parallelism across tabs is supported by specifying different`switch\_tab\_id` values in concurrent invocations.

The `no\_monitor` parameter saves 2-3 seconds by skipping the before/after HTML snapshot and DOM diff. Use it for read-only JS queries (e.g., reading `localStorage`, counting elements) but never for actions that modify page state (clicks, form submissions, navigation), where you need the diff feedback to confirm the action succeeded.

Sources: [ga.py](ga.py#L323-L349), [simphtml.py](simphtml.py#L817-L871), [assets/tools\_schema.json](assets/tools_schema.json#L45-L53)

### `file_read` — Line-Addressed File Inspection

The standalone implementation at [ga.py](ga.py#L210-L245) uses an `itertools`-based streaming pipeline for memory-efficient reading: `dropwhile` skips to the start line, `islice` limits the count, and a `collections.deque` provides the sliding window for keyword context (returning 1/3 of lines before the match). Each line is individually capped at a dynamic limit (`min(max(100, 256000/count), 8000)` characters) to prevent single megabyte-lines from blowing context. The `keyword` parameter enables fuzzy search — on miss, it falls back to reading from the start line instead of failing. On `FileNotFoundError`, it performs fuzzy file-name matching against previously-read directories using `difflib.SequenceMatcher`, suggesting up to 5 candidates above a 30% similarity threshold.

The handler wrapper at [ga.py](ga.py#L398-L415) adds memory-awareness: reading files containing "memory" or "sop" in their path triggers a system tip reminding the LLM to extract key points and update working memory. All memory-path reads are also logged to `memory/file_access_stats.json` for access-pattern analysis.

Sources: [ga.py](ga.py#L210-L245), [ga.py](ga.py#L398-L415), [assets/tools\_schema.json](assets/tools_schema.json#L12-L21)

## Manipulation Tools

### `code_run` — Sandboxed Process Execution

The core implementation at [ga.py](ga.py#L11-L89) creates temporary `.ai.py` files in a working directory, optionally prepending a header script from <assets/code_run_header.py>. For Python, it spawns `sys.executable -X utf8 -u` as a subprocess with a streaming stdout reader thread, supporting both timeout-based kill and a manual `stop_signal` list for user-initiated aborts. For PowerShell (Windows) or Bash (Unix), it passes the code directly as a `-Command` or `-c` argument. The return value is a dict with `status`, `stdout` (smart-formatted to ~10k chars), and `exit_code`. An `inline_eval` mode (disabled by default) executes Python code in-process via `eval`/`exec` with a namespace exposing `handler` and  — this is intentionally restricted.

The handler at [ga.py](ga.py#L277-L300) implements the dual-input pattern: if no `script` parameter is provided, it extracts the last code block matching the specified `type` from the LLM response via regex. This eliminates JSON-escaping pain for the LLM, since code blocks in natural response text don't need parameter-level escaping.

Sources: [ga.py](ga.py#L11-L89), [ga.py](ga.py#L277-L300), [assets/tools\_schema.json](assets/tools_schema.json#L2-L11)

### `file_patch` — Uniqueness-Guaranteed Edit

The implementation at [ga.py](ga.py#L188-L201) enforces a strict uniqueness constraint: `old_content` must match exactly once in the file. Zero matches return an error suggesting the LLM re-read the file; multiple matches return an error requesting more context to disambiguate. This design deliberately prevents ambiguous edits that could corrupt files. The `new_content` parameter supports `{{file:path:start:end}}` template references, expanded by `expand_file_refs()` at [ga.py](ga.py#L174-L186), which reads the referenced file lines and interpolates them before the replacement occurs.

The handler at [ga.py](ga.py#L351-L363) performs path resolution via `_get_abs_path()` and yields status messages for streaming display. This tool is the preferred mechanism for targeted edits — `file_write` is reserved for bulk operations.

Sources: [ga.py](ga.py#L188-L201), [ga.py](ga.py#L351-L363), [ga.py](ga.py#L174-L186), [assets/tools\_schema.json](assets/tools_schema.json#L22-L29)

### `file_write` — Bulk File Operations

The handler at [ga.py](ga.py#L365-L396) implements three write modes: `overwrite` (default), `append`, and `prepend`. Content is extracted from the LLM response using `extract_robust_content()`, which first looks for `<file_content>` XML tags, then falls back to the last fenced code block in the response. Like `file_patch`, it supports `{{file:...}}` template expansion. The `mode` parameter is a deliberate design choice — forcing the LLM to explicitly specify intent prevents accidental overwrites. The tool returns a byte count on success and an error if no content block is found in the response.

Sources: [ga.py](ga.py#L365-L396), [assets/tools\_schema.json](assets/tools_schema.json#L30-L36)

## Cognitive Persistence Tools

### `update_working_checkpoint` — Turn-Scoped Notepad

This tool implements the agent's short-term memory. The handler at [ga.py](ga.py#L427-L437) stores `key_info` (a <200-token structured note) and `related_sop` in `self.working`, a dict that persists across turns within the same task. Each subsequent turn's `_get_anchor_prompt()` at [ga.py](ga.py#L504-L514) injects the last 20 history lines and the current `key_info` into the LLM's prompt, creating a sliding window of task context that survives context-window pressure. The schema description provides explicit usage guidance: call during early/mid stages (not at task end), store pitfalls and key parameters (not ephemeral info), and incrementally update rather than rewrite.

Across task boundaries, the key\_info survives with a deprecation marker — [agentmain.py](agentmain.py#L132-L136) transfers it to the new handler and appends a system note indicating it came from a previous session, prompting the LLM to evaluate relevance.

Sources: [ga.py](ga.py#L427-L437), [ga.py](ga.py#L504-L514), [agentmain.py](agentmain.py#L132-L136), [assets/tools\_schema.json](assets/tools_schema.json#L54-L60)

### `ask_user` — Human Intervention Gate

The simplest yet most architecturally significant tool. The handler at [ga.py](ga.py#L302-L307) returns `StepOutcome(result, next_prompt="", should_exit=True)`, which causes the agent loop in [agent\_loop.py](agent_loop.py#L82-L83) to break immediately. The `candidates` parameter provides quick-select options to reduce user friction. This is the **only tool** that can halt the agentic loop — all others continue the cycle via their `next_prompt`. The standalone implementation at [ga.py](ga.py#L92-L95) returns a structured dict with `status: "INTERRUPT"` and `intent: "HUMAN_INTERVENTION"`, which the frontend display layers interpret to render an interactive prompt.

Sources: [ga.py](ga.py#L92-L95), [ga.py](ga.py#L302-L307), [agent\_loop.py](agent_loop.py#L82-L83), [assets/tools\_schema.json](assets/tools_schema.json#L61-L67)

### `start_long_term_update` — Memory Crystallization Trigger

This tool does not directly write memory — instead, it prepares a prompt that instructs the LLM to perform a structured memory update following the Memory Management SOP. The handler at [ga.py](ga.py#L488-L502) reads `memory/memory_management_sop.md` and appends `get_global_memory()` output, returning both as the tool result. The LLM then uses `file_patch` and `file_read` in subsequent turns to actually update the layered memory files (L1/L2/L3). This indirection is intentional: it keeps the tool interface minimal (zero parameters) while ensuring memory updates follow the SOP's validation rules. The schema mandates calling this tool after any task exceeding 15 turns.

Sources: [ga.py](ga.py#L488-L502), [ga.py](ga.py#L545-L557), [assets/tools\_schema.json](assets/tools_schema.json#L68-L72)

## Hidden Tool: `do_no_tool` — Implicit Safety Net

Not exposed in `TOOLS_SCHEMA`, `do_no_tool` at [ga.py](ga.py#L439-L486) is auto-triggered by the agent loop when the LLM produces no explicit tool calls. It handles five distinct failure modes: (1) **empty response** — retries with a regeneration prompt; (2) **incomplete response** — detects truncated output markers in the last 100 characters; (3) **max\_tokens overflow** — suggests breaking work into smaller steps; (4) **plan-mode completion claim** — blocks premature task-completion declarations that lack a `[VERIFY]` verification step; and (5) **orphaned code block** — detects when the LLM outputs a large code block without calling any tool, requesting explicit tool invocation.

The orphaned code-block detection (lines [ga.py#L459-L478](ga.py#L459-L478)) uses a specific pattern: exactly one large code block (>50 chars) with no substantive text after it (excluding `` and `` tags). This catches the common failure mode where the LLM generates code but forgets to wrap it in a `code\_run` or `file\_write` call.

Sources: [ga.py](ga.py#L439-L486), [agent\_loop.py](agent_loop.py#L61-L61)

## Cross-Cutting Design Patterns

### Dual-Input Code Injection

Both `code_run` and `web_execute_js` support two mutually exclusive input channels: a `script` parameter (useful for multi-call parallelism since each call needs its own argument) and inline code blocks extracted from the LLM's response content. The extraction logic in `_extract_code_block()` at [ga.py](ga.py#L272-L275) uses regex to find the last fenced code block matching the expected language identifier. The schema descriptions explicitly note: "NEVER use this param when use reply code block." This design eliminates JSON-escaping complexity — a  or  inside a code block parameter requires escaping in JSON but not in natural response text.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | `start_long_term_update` | Long-term memory | Memory SOP content | No |

`parent`

`"`

`\n`

### Template Expansion System

Both `file_patch` and `file_write` support `{{file:path:startLine:endLine}}` syntax, implemented by `expand_file_refs()` at [ga.py](ga.py#L174-L186). This allows the LLM to reference existing file content in patch operations without re-typing it — a significant token savings when modifying large files. The function performs path resolution, file existence checks, and line-boundary validation, raising `ValueError` on any violation.

### Schema Localization Switch

At [agentmain.py](agentmain.py#L82-L83), the `next_llm()` method switches tool schemas between English and Chinese versions based on the active LLM model name. Models like GLM, MiniMax, and Kimi receive `_cn`-suffixed Chinese schemas, while others receive the English default. This ensures tool descriptions match the model's primary language, improving instruction-following accuracy.

### Turn-Cadence Safety Mechanisms

The `turn_end_callback` at [ga.py](ga.py#L516-L543) implements progressive escalation: every 7 turns it warns against ineffective retries; every 10 turns it injects global memory; and at turn 35 (or 70 in plan mode) it forces `ask_user` intervention. This prevents the agent from entering infinite retry loops — a critical safety property for autonomous operation.

Sources: [ga.py](ga.py#L272-L275), [ga.py](ga.py#L174-L186), [agentmain.py](agentmain.py#L82-L83), [ga.py](ga.py#L516-L543)---

**Navigation**: This page covered the complete tool surface area. To understand how these tools are invoked sequentially within the execution loop, proceed to [Agent Loop and Task Runner](/9-agent-loop-and-task-runner) . For the mechanism that maps LLM tool-call JSON to these implementations, see [Tool Dispatch Handler](/10-tool-dispatch-handler) . The browser tools depend on the TMWebDriver bridge — see [TMWebDriver Bridge](/15-tmwebdriver-bridge)  and [HTML Simplification Engine](/16-html-simplification-engine)  for those underlying systems.

Nine Atomic Tools | lsdefine/GenericAgent | Zread---

<!-- Page 10: https://zread.ai/lsdefine/GenericAgent/12-session-classes-and-backends -->

# Session Classes and Backends

Level: Intermediate

GenericAgent's LLM integration lives in a single, densely layered module — `llmcore.py` — that implements a **session/client two-tier architecture**. Sessions own the network protocol and conversation history; clients wrap sessions with tool-handling logic and response parsing. This separation lets the agent switch between Anthropic, OpenAI, and relay providers without touching the tool-dispatch layer above it.

## Session Hierarchy

All session classes inherit from **`BaseSession`**, which provides the shared lifecycle: configuration loading, history management with automatic context trimming, Claude-style thinking-parameter injection, and the `ask()` generator that serialises tool-use blocks back into XML tags for the text-protocol path. The critical design decision is that `BaseSession.ask()` returns a **generator** — it yields streaming text chunks and, via `StopIteration.value`, returns a list of structured `content_block` dicts ([`llmcore.py`](llmcore.py#L500-L517)).

## The Two Protocol Families

### Non-Native Sessions (Text-Protocol)

**`ClaudeSession`** and **`LLMSession`** are the older, text-protocol path. They speak to their respective APIs but return tool calls as inline `<tool_use>` XML inside the text stream — the model never sees a native `tools` parameter. `ClaudeSession` sends the Anthropic Messages API directly with prompt-caching headers on the last two user messages ([`llmcore.py`](llmcore.py#L519-L538)). `LLMSession` delegates to the shared `_openai_stream()` helper, which handles both `chat_completions` and the newer `responses` API mode ([`llmcore.py`](llmcore.py#L540-L546)).

These sessions are now marked as **deprecated** in the template. They still work — and remain the only option for providers that don't support structured tool schemas — but they sacrifice tool-call reliability because the model must emit JSON inside markdown inside text rather than using a dedicated content block.

### Native Sessions (Structured Tool-Calling)

**`NativeClaudeSession`** is the recommended session for Anthropic and Anthropic-compatible providers. It sends tools as a proper `tools` array in the request payload, receives structured `tool_use` content blocks in the SSE response, and returns a **`MockResponse`** object from its overridden `ask()` method ([`llmcore.py`](llmcore.py#L618-L643)). This object carries `.thinking`, `.content`, `.tool_calls`, and `.raw` — a far richer return type than a plain string.

Key features specific to `NativeClaudeSession`:

* **CC-switch compatibility** via `fake_cc_system_prompt=True`, which injects the Claude Code system fingerprint into the first user message for relay providers that validate it ([`llmcore.py`](llmcore.py#L569-L598)).
* **1M context beta** triggered by appending `[1m]` to the model name, which injects the `context-1m-2025-08-07` beta header ([`llmcore.py`](llmcore.py#L579-L580)).
* **Dual auth modes**: keys starting with `sk-ant-` use `x-api-key`; everything else falls back to `Bearer` ([`llmcore.py`](llmcore.py#L584-L585)).
* **Message repair** via `_fix_messages()`, which enforces Claude's strict alternating-role requirement and auto-inserts placeholder `tool_result` blocks for any orphaned `tool_use` IDs ([`llmcore.py`](llmcore.py#L548-L561)).

**`NativeOAISession`** inherits from `NativeClaudeSession` and overrides only `raw_ask()` to route through `_openai_stream()` instead of the Anthropic endpoint ([`llmcore.py`](llmcore.py#L645-L654)). The parent's `ask()`, tool-parsing, and `MockResponse` construction are fully reused.

## Client Wrappers: ToolClient and NativeToolClient

Sessions handle protocol; clients handle **tools**. The two client classes sit at different levels of sophistication:

**`ToolClient`** wraps any non-Native session. Since the model receives tool descriptions as inline text in the prompt (via `_build_protocol_prompt()`), `ToolClient` must construct a "protocol instruction" block that teaches the model the `<tool_use>` XML format, append the full tool schema as JSON, and then parse `<tool_use>` tags out of the response with a multi-strategy regex fallback ([`llmcore.py`](llmcore.py#L683-L813)). It includes a token-saving optimisation: if the tool schema hasn't changed and cumulative context is under 9 000 characters, it substitutes a one-liner reminder instead of re-sending the entire schema ([`llmcore.py`](llmcore.py#L741-L745)).

**`NativeToolClient`** wraps any Native session. Because the session itself handles structured tool calls natively, `NativeToolClient` is dramatically simpler: it passes tool schemas directly to `backend.tools`, merges multi-part message content into a single Claude-format user message, tracks pending tool-result IDs for auto-completion, and appends the thinking/summary action protocol to the system prompt ([`llmcore.py`](llmcore.py#L930-L970)).

| Feature | `ToolClient` | `NativeToolClient` |
| --- | --- | --- |
| Wrapped sessions | `ClaudeSession`, `LLMSession` | `NativeClaudeSession`, `NativeOAISession` |
| Tool delivery | Inline text in prompt | Native API `tools` parameter |
| Tool-call parsing | Regex on response text | Structured content blocks from session |
| Thinking protocol | Embedded in prompt instructions | Appended to `system` prompt |
| Schema caching | Yes — skips re-sending if unchanged | N/A (API handles it) |
| Return type | `MockResponse` (parsed from text) | `MockResponse` (from `session.ask()`) |

The `MockResponse` object returned by Native clients uses a \*\*fabricated stop\_reason\*\*: it's set to `'tool\_use'` whenever `tool\_calls` is non-empty, regardless of what the API actually reported ([`llmcore.py`](llmcore.py#L679)). This lets the agent loop use a single `stop\_reason` check to decide whether to dispatch tools.

## Session Instantiation and Auto-Detection

When `GeneraticAgent.__init__()` runs, it scans every key in `mykey.py` (or `mykey.json`) and classifies it by **substring matching** on the variable name ([`agentmain.py`](agentmain.py#L48-L56)):

| Variable name contains | Session class | Client wrapper |
| --- | --- | --- |
| `native` + `claude` | `NativeClaudeSession` | `NativeToolClient` |
| `native` + `oai` | `NativeOAISession` | `NativeToolClient` |
| `claude` (no `native`) | `ClaudeSession` | `ToolClient` |
| `oai` (no `native`) | `LLMSession` | `ToolClient` |
| `mixin` | — | Stored as dict, resolved in second pass |

Keys containing `api`, `config`, or `cookie` are skipped. Mixin configs are deferred and resolved after all individual sessions are created, because a `MixinSession` needs references to the already-instantiated session objects ([`agentmain.py`](agentmain.py#L57-L63)). The final `llmclients` list is what the agent loop and chat frontends index into.

## Configuration Reference

Every session is driven by a config dict. Below are the universal fields accepted by `BaseSession.__init__()` and the provider-specific additions:

### Universal Fields (All Sessions)

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `apikey` | `str` | *required* | API key for authentication |
| `apibase` | `str` | *required* | Base URL; `auto_make_url()` appends `/v1/{path}` if needed ([`llmcore.py`](llmcore.py#L91-L95)) |
| `model` | `str` | `''` | Model identifier; appended to display name if `name` is unset |
| `name` | `str` | `model` | Human-readable name shown in `/llms` and used for mixin references |
| `context_win` | `int` | `24000` | Character budget before `trim_messages_history()` starts dropping old messages ([`llmcore.py`](llmcore.py#L77-L89)) |
| `temperature` | `float` | `1` | Sampling temperature |
| `max_tokens` | `int` | `8192` | Max output tokens per request |
| `stream` | `bool` | `True` | Enable SSE streaming; `False` for single JSON response |
| `max_retries` | `int` | `1` | Automatic retry count on transient failures |
| `timeout` | `int` | `5` / `10` | Connect timeout in seconds (lower for streaming) |
| `read_timeout` | `int` | `30` / `240` | Read timeout in seconds (higher for non-streaming) |
| `proxy` | `str` | `None` | Per-session HTTP proxy override |
| `api_mode` | `str` | `chat_completions` | `'chat_completions'` or `'responses'` (LLMSession / NativeOAISession only) |
| `reasoning_effort` | `str` | `None` | `none/minimal/low/medium/high/xhigh` — Claude maps to `output_config.effort`, OAI to `reasoning_effort` |
| `thinking_type` | `str` | `None` | `adaptive/enabled/disabled` — Claude extended thinking |
| `thinking_budget_tokens` | `int` | `None` | Required when `thinking_type='enabled'` |

### NativeClaudeSession-Specific Fields

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `fake_cc_system_prompt` | `bool` | `False` | Inject Claude Code system fingerprint into first user message |
| `user_agent` | `str` | `claude-cli/2.1.113` | User-Agent header for CC-switch compatibility |

## MockResponse and MockToolCall: The Unified Return Types

Since the agent loop must handle both text-protocol (XML parsing) and native-protocol (structured blocks) paths through a single interface, `llmcore.py` defines lightweight data objects:

* **`MockToolCall`** wraps a tool invocation with `.function.name`, `.function.arguments` (JSON string), and `.id` ([`llmcore.py`](llmcore.py#L670-L673)).
* **`MockResponse`** bundles `.thinking`, `.content`, `.tool_calls`, `.raw`, and a derived `.stop_reason` ([`llmcore.py`](llmcore.py#L675-L681)).

Both `ToolClient._parse_mixed_response()` and `NativeClaudeSession.ask()` return `MockResponse`, which is what the agent loop receives from `handler.dispatch()` after tool execution. This means the loop code is completely agnostic to which session/client is active underneath.

## What's Next

Understanding sessions and backends is prerequisite for two deeper topics: how the SSE bytes become structured content in [SSE Stream Parsing](/13-sse-stream-parsing) , and how `MixinSession` orchestrates multi-provider failover in [Multi-Session Fallback](/14-multi-session-fallback) . For the broader picture of how the client's `chat()` return feeds into the agent loop, see [Agent Loop and Task Runner](/9-agent-loop-and-task-runner) .---

<!-- Page 11: https://zread.ai/lsdefine/GenericAgent/13-sse-stream-parsing -->

# SSE Stream Parsing

Level: Advanced

GenericAgent's SSE (Server-Sent Events) stream parsing layer forms the critical bridge between raw LLM HTTP responses and the structured content blocks consumed by the agent loop. It implements a **dual-generator pattern** — each parser is both a streaming text emitter and a structured return value — enabling real-time token delivery to chat frontends while simultaneously assembling machine-readable tool call payloads for the dispatch system.

## Architectural Overview

The SSE parsing subsystem lives entirely within [`llmcore.py`](llmcore.py) and follows a clean separation: two format-specific parsers feed a unified `content_block` schema that propagates upward through the session hierarchy. The entire pipeline is generator-based — no intermediate buffering of the full response is required for streaming delivery.

The session classes ([`ClaudeSession`](llmcore.py#L519-L538), [`LLMSession`](llmcore.py#L540-L546), [`NativeClaudeSession`](llmcore.py#L565-L616), [`NativeOAISession`](llmcore.py#L645-L654)) each select and invoke the appropriate parser via their `raw_ask()` methods. Both [`BaseSession.ask()`](llmcore.py#L500-L517) and [`NativeClaudeSession.ask()`](llmcore.py#L618-L643) consume these generators with the same `StopIteration` return-value pattern.

Sources: [llmcore.py](llmcore.py#L97-L158), [llmcore.py](llmcore.py#L176-L260), [llmcore.py](llmcore.py#L500-L517)

## The Dual-Generator Contract

Every SSE parser in GenericAgent adheres to a **single generator, dual output** contract. This is the foundational design pattern that makes real-time streaming and structured extraction coexist without coupling.

The contract works by exploiting Python's generator return mechanism (PEP 380). A parser function `yield`s text chunks as they arrive, and when the stream ends, the accumulated `content_blocks` list is returned via the `return` statement — which surfaces as the `.value` attribute of the raised `StopIteration` exception.

```
gen = self.raw_ask(messages)          # gen is a generator
try:
    while True:
        chunk = next(gen)             # yields text chunks for streaming
        content += chunk
        yield chunk                   # re-yield to caller
except StopIteration as e:
    content_blocks = e.value or []    # structural return value
```

This means every caller receives both: (1) a real-time token stream for UI rendering, and (2) a final structured payload for tool dispatch. The pattern repeats identically in [`NativeToolClient.chat()`](llmcore.py#L942-L970) at lines 964–967, [`MixinSession._raw_ask()`](llmcore.py#L885-L911) at lines 894–898, and [`_openai_stream()`](llmcore.py#L316-L372) at lines 359–362.

The `yield from` delegation in `\_openai\_stream` (line 358) and `ClaudeSession.raw\_ask` (line 529) transparently forwards both yielded chunks \*and\* the return value. Any custom session class that delegates to these parsers must use `yield from` — not manual iteration — to preserve the return value contract.

Sources: [llmcore.py](llmcore.py#L500-L517), [llmcore.py](llmcore.py#L316-L372), [llmcore.py](llmcore.py#L885-L911)

## Anthropic SSE Parser: `_parse_claude_sse`

The Anthropic parser ([`_parse_claude_sse()`](llmcore.py#L97-L158)) implements a state machine that tracks a single `current_block` across the Anthropic SSE event sequence. It processes five distinct event types in a strict lifecycle.

### Event Lifecycle

| Event Type | Purpose | State Mutation |
| --- | --- | --- |
| `message_start` | Session metadata and input token usage | Calls `_record_usage()` with `api_mode="messages"` |
| `content_block_start` | Initialize a new block (text / thinking / tool\_use) | Creates `current_block` dict; resets `tool_json_buf` for tool\_use |
| `content_block_delta` | Incremental content delivery | Appends to `current_block["text"]` / `"thinking"` / `"signature"` / `tool_json_buf` |
| `content_block_stop` |

The parser maintains six local state variables through the stream lifecycle: `content_blocks` (accumulated output), `current_block` (active block being assembled), `tool_json_buf` (raw JSON string for tool arguments), `stop_reason`, `got_message_stop`, and `warn` (error diagnostic) — all initialized at [line 99–100](llmcore.py#L99-L100).

### Thinking Block Handling

Anthropic's extended thinking feature produces two sub-block types within a single thinking block: `thinking_delta` (visible reasoning text) and `signature_delta` (cryptographic proof). The parser accumulates both separately into `current_block["thinking"]` and `current_block["signature"]` ([lines 128–132](llmcore.py#L128-L132)). These thinking blocks are silently accumulated — no text is yielded to the streaming consumer — ensuring chain-of-thought remains hidden from end users.

### Error Detection and Stream Integrity

The parser implements two layers of stream integrity checking. First, if the `error` event type is received, parsing terminates immediately with a descriptive warning ([lines 148–151](llmcore.py#L148-L151)). Second, post-stream validation checks whether both `got_message_stop` and `stop_reason` were received — if neither is present, an abnormal termination warning is injected ([lines 152–154](llmcore.py#L152-L154)). The `max_tokens` truncation case receives its own distinct warning. All warnings are appended as synthetic text blocks and yielded as content, ensuring the downstream session layer can log or surface them.

Sources: [llmcore.py](llmcore.py#L97-L158), [llmcore.py](llmcore.py#L262-L274)

## OpenAI SSE Parser: `_parse_openai_sse`

The OpenAI parser ([`_parse_openai_sse()`](llmcore.py#L176-L260)) handles both the standard `chat_completions` API and the newer `responses` API through a single entry point with mode-specific branching at [line 182](llmcore.py#L182).

### Responses API Mode (`api_mode="responses"`)

The responses API parser tracks function calls by their `output_index`, accumulating argument fragments in `fc_buf` — an `index → {id, name, args}` dictionary initialized at [line 183](llmcore.py#L183).

| Event Type | Action |
| --- | --- |
| `response.output_text.delta` | Yields text delta, appends to `content_text` |
| `response.output_text.done` | Fallback yield for non-streamed text delivery |
| `response.output_item.added` | Creates new `fc_buf` entry when `item.type == "function_call"` |
| `response.function_call_arguments.delta` | Accumulates argument fragments into `fc_buf[idx]["args"]` |
| `response.function_call_arguments.done` | Finalizes arguments with complete string |
| `response.completed` | Records usage; terminates parsing |

The responses API branch handles a subtle edge case: if no delta events were received but `response.output_text.done` fires, the full text is yielded in one shot ([lines 196–198](llmcore.py#L196-L198)). This accommodates providers that batch the entire output text in a single non-streamed chunk.

### Chat Completions Mode (`api_mode="chat_completions"`)

The chat completions parser ([lines 230–260](llmcore.py#L230-L260)) follows the standard OpenAI streaming format, extracting `delta.content` for text and `delta.tool_calls[]` for function invocations. Tool calls are tracked by index in `tc_buf`, with argument strings accumulated across multiple deltas via string concatenation at [line 248](llmcore.py#L248).

### Concatenated JSON Splitting

Both OpenAI modes rely on [`_try_parse_tool_args()`](llmcore.py#L161-L174) for robust argument parsing. This function addresses a common failure mode where models emit concatenated JSON objects without separators (e.g., `{"arg":"val"}{"arg2":"val2"}`). It attempts three strategies in order: (1) direct `json.loads`, (2) regex splitting on `}{` boundaries with individual parsing, (3) fallback to `_raw` key with the unparsed string. This is especially important for multi-tool-call scenarios where argument deltas may arrive without proper delimiters.

When a tool call's arguments split into multiple parsed JSON objects, the parser generates synthetic IDs like `original\_id\_0`, `original\_id\_1` to ensure uniqueness. See lines 225–228 (responses mode) and 256–258 (chat completions mode). Downstream dispatch must handle these compound tool calls by iterating over all content blocks with `type == "tool\_use"`.

Sources: [llmcore.py](llmcore.py#L176-L260), [llmcore.py](llmcore.py#L161-L174)

## Streaming Transport: `_openai_stream`

[`_openai_stream()`](llmcore.py#L316-L372) is the shared HTTP transport for all OpenAI-compatible backends. It wraps the raw `requests.post()` call with retry logic, request construction, and parser invocation — serving as the single entry point for `LLMSession` and `NativeOAISession`.

### Retry Architecture

The retry system ([lines 338–372](llmcore.py#L338-L372)) classifies HTTP status codes into retryable and terminal categories:

| Category | Status Codes | Behavior |
| --- | --- | --- |
| **Retryable** | 408, 409, 425, 429, 500, 502, 503, 504, 529 | Exponential backoff with `Retry-After` header respect |
| **Terminal** | All others (4xx except above) | Immediate error yield and return |
| **Network** | `Timeout`, `ConnectionError` | Retry if no data was streamed; fail if partial data sent |

The backoff strategy is intelligent: it first checks for the standard `Retry-After` header (line 340–341), falling back to exponential delay capped at 30 seconds (`min(30, 1.5 * 2^attempt)` at line 342). Crucially, if any text was already yielded to the consumer before a network failure (`streamed = True` at line 364), no retry is attempted — partial responses are never transparently replaced.

### Model-Specific Temperature Normalization

Before constructing the payload, the function applies model-specific overrides ([lines 321–323](llmcore.py#L321-L323)): Kimi/Moonshot models force `temperature=1`, and MiniMax clamps to `(0, 1]`. These adjustments are invisible to the session configuration layer.

### Cache Control Stamping

For Anthropic models accessed via OpenAI-compatible relays, [`_stamp_oai_cache_markers()`](llmcore.py#L303-L314) injects `cache_control: {"type": "ephemeral"}` on the last two user messages. This enables prompt caching on relay providers (like OpenRouter) that translate Anthropic caching semantics. The function detects Claude models by checking for `'claude'` or `'anthropic'` in the model name ([line 306](llmcore.py#L306)).

Sources: [llmcore.py](llmcore.py#L316-L372), [llmcore.py](llmcore.py#L303-L314)

## Session Hierarchy and Parser Dispatch

The four concrete session classes form two evolutionary generations, each selecting a parser through their `raw_ask()` method.

**Legacy sessions** ([`ClaudeSession`](llmcore.py#L519-L538), [`LLMSession`](llmcore.py#L540-L546)) use the `BaseSession.ask()` contract where `raw_ask` is a pure generator returning `content_blocks` via `StopIteration`, and the base class handles history management and tool call XML tag injection.

**Native sessions** ([`NativeClaudeSession`](llmcore.py#L565-L616), [`NativeOAISession`](llmcore.py#L645-L654)) override `ask()` entirely to produce a `MockResponse` object directly. They leverage native tool\_use blocks instead of XML protocol tags, and the `NativeClaudeSession.ask()` method at [lines 618–643](llmcore.py#L618-L643) performs additional post-processing: extracting thinking from `<thinking>` XML tags as a fallback if the model didn't use native thinking blocks, and delegating to [`_parse_text_tool_calls()`](llmcore.py#L815-L835) if no native tool\_use blocks were found.

### Non-Streaming Fallback

Both parser families support a non-streaming path. When `stream=False`, [`_openai_stream()`](llmcore.py#L316-L372) invokes [`_parse_openai_json()`](llmcore.py#L276-L301) instead of `_parse_openai_sse()` ([line 358](llmcore.py#L358)). Similarly, [`NativeClaudeSession.raw_ask()`](llmcore.py#L575-L616) switches to `resp.json()` parsing at [lines 607–613](llmcore.py#L607-L613) when `self.stream` is `False`. Both non-streaming paths yield text blocks and return `content_blocks` through the same generator interface, maintaining API consistency.

Sources: [llmcore.py](llmcore.py#L461-L654), [llmcore.py](llmcore.py#L815-L835), [llmcore.py](llmcore.py#L276-L301)

## Consumption by the Agent Loop

The agent loop in [`agent_loop.py`](agent_loop.py#L42-L97) consumes SSE streams through one of two paths depending on verbosity mode. In verbose mode, [`agent_runner_loop()`](agent_loop.py#L42-L97) delegates streaming to the caller via `yield from` at [line 54](agent_loop.py#L54):

```
response_gen = client.chat(messages=messages, tools=tools_schema)
if verbose:
    response = yield from response_gen  # real-time token delivery
else:
    response = exhaust(response_gen)     # buffered, cleaned output
```

The [`exhaust()`](agent_loop.py#L32-L35) helper drains the generator silently, collecting only the `StopIteration` return value. The [`ToolClient`](llmcore.py#L683-L813) (legacy protocol-based client) accumulates streamed chunks into `raw_text` at [lines 697–700](llmcore.py#L697-L700), then delegates to [`_parse_mixed_response()`](llmcore.py#L764-L813) for regex-based extraction of thinking blocks and XML-embedded tool calls. The [`NativeToolClient`](llmcore.py#L930-L970) simply yields chunks through and collects the `MockResponse` from `StopIteration`.

Sources: [agent\_loop.py](agent_loop.py#L42-L97), [llmcore.py](llmcore.py#L691-L704), [llmcore.py](llmcore.py#L942-L970)

## MixinSession: Fallback with Stream Awareness

[`MixinSession`](llmcore.py#L856-L911) implements multi-backend failover that is **stream-aware** — it can detect failure from the first yielded chunk before committing to a session. The [`_raw_ask()`](llmcore.py#L885-L911) method wraps each session's generator and inspects the first chunk:

* If the first chunk starts with `Error:` or `[Error:`, it silently discards the chunk and tries the next session ([line 896](llmcore.py#L896))
* Once a non-error chunk is yielded (`yielded = True`), all subsequent chunks pass through — no mid-stream failover is attempted
* On successful failover, the `_cur_idx` is updated with a timestamp, enabling "spring-back" to the primary session after a configurable delay ([line 901](llmcore.py#L901))

This design ensures that chat frontends never see error prefixes from failed backends — they receive clean text from whichever session succeeds first.

Sources: [llmcore.py](llmcore.py#L856-L911)

## Unified `content_block` Schema

All parsers converge on the same `content_block` schema, regardless of the upstream API format:

| Block Type | Shape | Produced By |
| --- | --- | --- |
| `text` | `{"type": "text", "text": str}` | All parsers |
| `tool_use` | `{"type": "tool_use", "id": str, "name": str, "input": dict}` | All parsers |
| `thinking` | `{"type": "thinking", "thinking": str, "signature": str}` | `_parse_claude_sse` only |

The `tool_use` blocks are consumed by [`BaseSession.ask()`](llmcore.py#L500-L517) which re-serializes them as XML tags (`<tool_use>...</tool_use>`) for the legacy protocol-based `ToolClient` path, or extracted directly by `NativeClaudeSession.ask()` into `MockToolCall` objects. The `thinking` blocks are silently consumed by `NativeClaudeSession.ask()` — they never reach the agent loop or the frontend.

Sources: [llmcore.py](llmcore.py#L176-L179), [llmcore.py](llmcore.py#L511-L516)---

**Next in the LLM Integration Layer**: See [Multi-Session Fallback](/14-multi-session-fallback)  for the complete `MixinSession` failover strategy, or return to [Session Classes and Backends](/12-session-classes-and-backends)  for full session configuration. For how parsed content blocks flow into tool dispatch, see [Tool Dispatch Handler](/10-tool-dispatch-handler) .

|  |
| --- |
| Finalize block, parse accumulated JSON |

|  |
| --- |
| `json.loads(tool_json_buf)` → `current_block["input"]`; appends to `content_blocks` |

|  |  |  |
| --- | --- | --- |
| `message_delta` | Output token count and stop reason | Updates `stop_reason`; logs token usage |

|  |  |  |
| --- | --- | --- |
| `message_stop` | Stream termination sentinel | Sets `got_message_stop = True` |

SSE Stream Parsing | lsdefine/GenericAgent | Zread---

<!-- Page 12: https://zread.ai/lsdefine/GenericAgent/14-multi-session-fallback -->

# Multi-Session Fallback

Level: Advanced

The `MixinSession` class implements a **circuit-breaker proxy** that wraps multiple LLM session backends into a single failover unit. When the primary backend returns an error, the system transparently rotates to the next session in priority order—with exponential backoff on full-cycle exhaustion and an automatic spring-back timer to reclaim the preferred backend once it recovers. This mechanism operates entirely within `llmcore.py` and is wired into the agent at startup via `agentmain.py`.

## Architectural Overview

At a structural level, `MixinSession` is not a new session implementation—it is a **proxy decorator** that intercepts the `raw_ask` generator on the primary session. All attribute access (`__getattr__`) and mutations (`__setattr__`) are delegated or broadcast to the underlying sessions, making the composite transparent to the rest of the system.

Sources: [llmcore.py](llmcore.py#L856-L871), [llmcore.py](llmcore.py#L519-L545)

## Two-Layer Retry Architecture

GenericAgent employs **two independent retry mechanisms** that stack multiplicatively. Understanding their interaction is essential for configuring reliable behavior.

| Layer | Scope | Mechanism | Error Types | Config Key |
| --- | --- | --- | --- | --- |
| **Inner (per-session)** | Single backend | `_openai_stream` loop | HTTP 408/429/5xx, timeouts, connection errors | `max_retries` in individual session cfg |
| **Outer (cross-session)** | Full `MixinSession` rotation | `_raw_ask` generator interception | Any `Error:` / `[Error:` prefix in first chunk | `max_retries` in `mixin_config` |

The inner layer handles **transient infrastructural failures**—rate limits, gateway timeouts, server errors—by retrying the *same* endpoint with exponential backoff (capped at 30s). The outer layer handles **semantic or provider-level failures** that the inner layer either exhausts or cannot classify as retryable (e.g., model overload returning a 200 with an error body, or authentication failures on a relay).

Sources: [llmcore.py](llmcore.py#L338-L372), [llmcore.py](llmcore.py#L885-L911)

## Configuration in `mykey.py`

The `mixin_config` dictionary controls failover behavior. It is detected by `agentmain.py` when scanning `mykeys` for variable names containing `mixin` [agentmain.py](agentmain.py#L48-L63).

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `llm_nos` | `list[int | str]` | `[]` | Priority-ordered session references: integers for positional index, strings matching a session's `name` field |
| `max_retries` | `int` | `3` | Total rotation attempts across all sessions before giving up |
| `base_delay` | `float` | `1.5` | Exponential backoff base (seconds) when a full rotation cycle fails |
| `spring_back` | `int` | `300` | Seconds after switching to a backup before attempting to return to the primary session |

A minimal production configuration with two Claude relays and an OpenAI fallback:

```
mixin_config = {
    'llm_nos': ['cc-relay-1', 'cc-relay-2', 'gpt-native'],
    'max_retries': 10,
    'base_delay': 0.5,
    'spring_back': 300,
}
```

Sources: [mykey\_template.py](mykey_template.py#L125-L136), [mykey\_template.py](mykey_template.py#L130-L131)

## Session Resolution and Homogeneity Constraint

During `MixinSession.__init__`, the `llm_nos` list is resolved to actual session objects. Integer indices reference the positional order of sessions in `mykeys` scanning; string values match the `name` field of previously-instantiated sessions [llmcore.py](llmcore.py#L861-L862). A critical **homogeneity assertion** enforces that all referenced sessions belong to the same protocol group:

```
is_native = lambda s: 'Native' in s.__class__.__name__
groups = {is_native(s) for s in self._sessions}
assert len(groups) == 1, "MixinSession: sessions must be in same group (Native or non-Native)"
```

This constraint exists because Native sessions and non-Native sessions use fundamentally different tool-calling protocols (API-native `tool` fields vs. text-embedded `<tool_use>` blocks). Mixing them within a single `MixinSession` would produce inconsistent tool interactions. The outer wrapper (`ToolClient` vs. `NativeToolClient`) is selected accordingly [agentmain.py](agentmain.py#L60-L62):

| Inner Sessions | Outer Wrapper |
| --- | --- |
| All `Native*` | `NativeToolClient(mixin)` |
| All non-Native | `ToolClient(mixin)` |

If you see `BADCONFIG\_MIXIN` in `/llms` output, the mixin initialization failed silently (caught exception at [agentmain.py#L63](agentmain.py#L63)). Check stderr for the full error traceback—the most common cause is violating the homogeneity constraint by mixing a `ClaudeSession` with a `NativeClaudeSession` in the same `llm\_nos` list.

Sources: [llmcore.py](llmcore.py#L863-L866), [agentmain.py](agentmain.py#L57-L63)

## The `_raw_ask` Failover Generator

The core failover logic resides in `MixinSession._raw_ask`, a generator that replaces the primary session's `raw_ask` method via shallow copy [llmcore.py](llmcore.py#L867-L869).

The error detection predicate `test_error` checks whether the *first yielded chunk* starts with `"Error:"` or `"[Error:"` [llmcore.py](llmcore.py#L887-L888). This is a stream-level heuristic: if the backend begins its response with an error string, the entire generator is consumed and discarded, and the rotation advances. Once a non-error chunk is yielded (`yielded = True`), all subsequent chunks from that session pass through regardless of content—partial failures mid-stream are not retried.

Sources: [llmcore.py](llmcore.py#L885-L911)

## Attribute Broadcasting

`MixinSession` overrides `__setattr__` to broadcast critical state changes across all constituent sessions simultaneously [llmcore.py](llmcore.py#L873-L878). The broadcast set is defined by `_BROADCAST_ATTRS`:

| Attribute | Broadcast Behavior |
| --- | --- |
| `system` | Direct broadcast to all sessions |
| `tools` | Converted via `openai_tools_to_claude()` for `NativeClaudeSession` instances, direct for others |
| `temperature` | Direct broadcast |
| `max_tokens` | Direct broadcast |
| `reasoning_effort` | Direct broadcast |
| `history` | Direct broadcast |

This ensures that when the agent loop sets the system prompt, tool schema, or conversation history, all backup sessions remain synchronized and ready to take over without a cold-start penalty. The `history` broadcast is particularly important for continuity—when a failover occurs mid-task, the backup session inherits the full conversation context from the primary.

The `\_\_getattr\_\_` delegation to `self.\_sessions[0]` means all read accesses (model name, context window, etc.) resolve against the primary session. If the primary session's configuration differs from backups (e.g., different `context\_win` values), only the primary's values are visible through the `MixinSession` proxy.

Sources: [llmcore.py](llmcore.py#L872-L879), [llmcore.py](llmcore.py#L656-L665)

## Spring-Back Mechanism

The `_pick` method implements a time-based spring-back to the primary session [llmcore.py](llmcore.py#L882-L884):

```
def _pick(self):
    if self._cur_idx and time.time() - self._switched_at > self._spring_sec:
        self._cur_idx = 0
    return self._cur_idx
```

After a successful failover pins `_cur_idx` to a backup session, the system continues using that backup for all subsequent requests. Once `spring_back` seconds have elapsed (default 300s / 5 minutes), `_pick` resets to index 0, causing the next `_raw_ask` call to attempt the primary session first. If the primary fails, the rotation proceeds through all sessions again starting from the top.

This creates a **two-phase recovery model**: immediate failover to the best available backend, followed by periodic probes back to the preferred backend without requiring manual intervention.

Sources: [llmcore.py](llmcore.py#L882-L884), [llmcore.py](llmcore.py#L900-L901)

## Initialization Sequence in `GeneraticAgent`

The agent's `__init__` method performs session assembly in two passes [agentmain.py](agentmain.py#L47-L64):

The two-pass design is necessary because `MixinSession` references other sessions by name or index, and those sessions must already exist in the registry. The mixin placeholder (a dict with key `mixin_cfg`) is resolved after all individual sessions are instantiated. If mixin initialization fails (e.g., a referenced session name doesn't exist), a warning is printed but the agent continues with the remaining sessions.

Sources: [agentmain.py](agentmain.py#L47-L64), [agentmain.py](agentmain.py#L74-L79)

## Runtime Session Switching

Beyond automatic failover, operators can manually switch the active LLM backend at runtime. The `next_llm` method cycles through all registered `llmclients` (including mixin-wrapped ones) [agentmain.py](agentmain.py#L74-L79). When switching between a mixin composite and a standalone session (or between two mixins), the history is transferred from the outgoing client to the incoming one:

```
def next_llm(self, n=-1):
    self.llm_no = ((self.llm_no + 1) if n < 0 else n) % len(self.llmclients)
    lastc = self.llmclient
    self.llmclient = self.llmclients[self.llm_no]
    try: self.llmclient.backend.history = lastc.backend.history
    except: raise Exception('[ERROR] BAD Mixin config: Check your mykey.py')
```

Additionally, the `/session.<key>=<value>` slash command in the REPL allows live tuning of session parameters (temperature, thinking\_type, reasoning\_effort, etc.) on the current backend without restart [agentmain.py](agentmain.py#L103-L113).

Sources: [agentmain.py](agentmain.py#L74-L83), [agentmain.py](agentmain.py#L103-L113)

## Error Taxonomy and Retry Behavior

Understanding which errors trigger which retry layer is critical for tuning configuration:

| Error Scenario | Inner Retry (per-session) | Outer Retry (MixinSession) | Result |
| --- | --- | --- | --- |
| HTTP 429 (rate limit) | ✅ Exponential backoff up to `max_retries` | Only if all inner retries exhausted | Failover to next session |
| HTTP 502/503 (gateway) | ✅ Same as above | Same | Failover to next session |
| Connection timeout | ✅ Same as above | Same | Failover to next session |
| 200 response with `Error:` body | ❌ Not retryable (HTTP 200) | ✅ Detected by `test_error` | Immediate rotation |
| HTTP 401/403 (auth) | ❌ Not in RETRYABLE set | ✅ Detected by `test_error` | Rotation (but all will likely fail) |
| Partial stream failure | ❌ `yielded=True` blocks re-check | ❌ Chunks already emitted | Partial output delivered |

Sources: [llmcore.py](llmcore.py#L338-L340), [llmcore.py](llmcore.py#L887-L904)

## Relationship to Other Components

The multi-session fallback system touches several architectural boundaries that are detailed in companion pages:

* **[Session Classes and Backends](/12-session-classes-and-backends)**  — covers `BaseSession`, `NativeClaudeSession`, `LLMSession`, and their individual retry/timeout configurations
* **[SSE Stream Parsing](/13-sse-stream-parsing)**  — documents `_parse_claude_sse` and `_parse_openai_sse` which are invoked within each session's `raw_ask`
* **[Agent Loop and Task Runner](/9-agent-loop-and-task-runner)**  — shows how `agent_runner_loop` calls `client.chat()`, which ultimately triggers `MixinSession._raw_ask` through the client chain
* **[Context Compression Strategy](/26-context-compression-strategy)**  — explains `trim_messages_history` which runs inside `BaseSession.ask` before the mixin layer is reached
* **[API Key Configuration](/3-api-key-configuration)**  — full guide to setting up `mykey.py` with mixin and individual session configurations

Multi-Session Fallback | lsdefine/GenericAgent | Zread---

<!-- Page 13: https://zread.ai/lsdefine/GenericAgent/15-tmwebdriver-bridge -->

# TMWebDriver Bridge

Level: Intermediate

TMWebDriver is GenericAgent's browser control backbone — a dual-layer bridge connecting a Python-side session manager to the user's live Chrome browser via a Manifest V3 extension. Unlike Selenium or Playwright, it **preserves the user's existing login state, cookies, and browser context**, enabling the agent to operate on authenticated web applications without separate session management. This page dissects the architecture, transport mechanisms, and CDP command routing that make this possible.

## Architectural Overview

The bridge consists of two tightly coupled halves: a Python server (`TMWebDriver.py`) and a Chrome extension (`tmwd_cdp_bridge/`). The Python server exposes both a WebSocket listener and an HTTP long-polling endpoint, while the extension serves as the browser-side agent that executes JavaScript, manages cookies, and tunnels Chrome DevTools Protocol (CDP) commands through the `chrome.debugger` API.

The architecture is deliberately transport-agnostic at the Python boundary: whether the connection arrives via WebSocket or HTTP long-poll, the same `execute_js` code path produces the result. The extension is the single authority for all browser interaction, ensuring that CSP restrictions, dialog suppression, and cookie isolation are handled in one place.

Sources: [TMWebDriver.py](TMWebDriver.py#L37-L49), [background.js](assets/tmwd_cdp_bridge/background.js#L190-L240), [manifest.json](assets/tmwd_cdp_bridge/manifest.json#L1-L39)

## Session Model and Transport Modes

The `Session` class encapsulates a single browser tab's connection state. Each session tracks its transport type, connection timestamps, and the underlying client handle — either a `WebSocket` object or a `queue.Queue` for HTTP long-polling.

Sources: [TMWebDriver.py](TMWebDriver.py#L8-L34)

### Three Transport Types

| Transport | Type Tag | Client Handle | Use Case |
| --- | --- | --- | --- |
| Userscript WebSocket | `ws` | `WebSocket` instance | Legacy tampermonkey-style tab injection |
| Extension WebSocket | `ext_ws` | Shared `WebSocket` from extension | **Primary path** — CDP bridge extension |
| HTTP Long-poll | `http` | `queue.Queue` | Fallback for restricted environments |

The `ext_ws` transport is the most significant: a single WebSocket connection from the extension's service worker multiplexes commands to **all** open browser tabs. The background.js maintains this connection and routes commands to specific tabs by `tabId`. When the extension connects, it sends an `ext_ready` message containing a snapshot of all scriptable tabs (filtered by `isScriptable()` to exclude `chrome://` and other internal pages), and each tab becomes a separate `Session` with its tab ID as the session ID.

Sources: [TMWebDriver.py](TMWebDriver.py#L14-L16), [background.js](assets/tmwd_cdp_bridge/background.js#L326-L335)

### Session Lifecycle

Sessions are created on first contact (`_register_client`), can reconnect if the same tab ID reappears (`reconnect`), and are marked disconnected when the WebSocket closes or an HTTP session exceeds 60 seconds of inactivity. The `clean_sessions` method garbage-collects sessions that have been disconnected for more than 10 minutes.

A critical detail for session resolution: when `execute_js` is called without an explicit `session_id`, it falls back to `self.default_session_id` (the first session that ever connected). If that session is dead, it scans for any alive session and auto-switches — a resilience pattern that prevents task failures when the user closes a tab mid-operation.

Sources: [TMWebDriver.py](TMWebDriver.py#L165-L178), [TMWebDriver.py](TMWebDriver.py#L193-L204), [TMWebDriver.py](TMWebDriver.py#L114-L119)

## JavaScript Execution Pipeline

The core of the bridge is `execute_js`, which implements a reliable request-response protocol over unreliable transports.

### Request-Response Protocol

The execution flow uses a three-phase reliability model:

1. **Dispatch**: The code payload (with a UUID `exec_id`) is sent to the extension via WebSocket or enqueued for HTTP long-poll pickup.
2. **ACK**: The extension immediately sends back an `{type: "ack"}` message, confirming receipt. The Python side resets its timeout clock upon receiving this ACK.
3. **Result/Error**: The extension sends back `{type: "result", ...}` or `{type: "error", ...}` with the execution outcome and any newly opened tabs.

This design produces nuanced timeout diagnostics. If an ACK was received but no result arrives, the message was delivered but the script may still be running. If no ACK arrived at all, the script was never delivered — pointing to a transport-level failure rather than a script execution issue.

The `execute\_js` method on the Python side also detects \*\*page reloads mid-execution\*\*: if the session was active, then went inactive (reload), then came back active, it returns `{closed: 1}` instead of waiting for a result that will never arrive from the old page context. This prevents the agent from hanging indefinitely on navigated-away tabs.

Sources: [TMWebDriver.py](TMWebDriver.py#L184-L243), [background.js](assets/tmwd_cdp_bridge/background.js#L242-L312)

## Extension Architecture (tmwd\_cdp\_bridge)

The Chrome extension is a Manifest V3 application with four components, each serving a distinct role in the browser control pipeline.

### Component Breakdown

| Component | Injection Context | Role |
| --- | --- | --- |
| `background.js` | Service Worker | WebSocket client to Python, command router, CDP bridge, alarm-based keepalive |
| `content.js` | Content Script (ISOLATED world) | TID-based DOM command bridge, CSP meta-tag removal, connection indicator badge |
| `disable_dialogs.js` | Content Script (MAIN world, `document_start`) | Overrides `alert()`/`confirm()`/`prompt()` to prevent page JS from blocking the agent |
| `popup.html` / `popup.js` | Extension popup | Debug UI for viewing cookies with `[H]` (httpOnly), `[S]` (secure), `[P]` (partitioned) flags |

Sources: [manifest.json](assets/tmwd_cdp_bridge/manifest.json#L1-L39), [content.js](assets/tmwd_cdp_bridge/content.js#L1-L47), [disable\_dialogs.js](assets/tmwd_cdp_bridge/disable_dialogs.js#L1-L24)

### Service Worker Survival Strategy

Manifest V3 service workers are ephemeral — Chrome terminates them after 30 seconds of inactivity. Since the extension needs a persistent WebSocket connection to the Python server, `background.js` implements a sophisticated alarm-based survival strategy:

1. **Keepalive cycle** (while connected): A `chrome.alarms` event fires every ~24 seconds, sending a ping over the WebSocket to keep the service worker alive and detect dead connections.
2. **Probe cycle** (while disconnected): An alarm fires every ~5 seconds, checking if the Python server is alive via an HTTP probe to `http://127.0.0.1:18765`. If the server is detected, it initiates a WebSocket connection.

The transition from keepalive → probe happens automatically when the WebSocket connection drops, and probe → keepalive when a connection is established. This creates a self-healing loop that survives Chrome's aggressive service worker termination.

Sources: [background.js](assets/tmwd_cdp_bridge/background.js#L194-L240)

### CSP Handling: Dual-Strategy Script Execution

Content Security Policy is the primary obstacle to reliable JavaScript execution. The extension employs a two-tier fallback strategy:

**Tier 1 — `chrome.scripting.executeScript` (MAIN world)**: The preferred path. Code is wrapped in `buildPageScript()`, which creates an async IIFE with a `smartProcessResult` function that intelligently serializes DOM elements, jQuery objects, NodeLists, and Window references into JSON-safe representations. If CSP blocks evaluation, the error handler sets a `csp: true` flag.

**Tier 2 — CDP `Runtime.evaluate` (fallback)**: When Tier 1 fails with a CSP error, the extension attaches the Chrome Debugger to the tab and evaluates via `Runtime.evaluate`. CDP execution bypasses CSP restrictions because it operates at the browser engine level. The code is wrapped with `buildCdpScript()` for this context.

On extension installation, `declarativeNetRequest` rules strip `Content-Security-Policy` and `Content-Security-Policy-Report-Only` response headers site-wide, reducing the frequency of Tier 2 fallback. The content script also proactively removes `<meta http-equiv="Content-Security-Policy">` tags from the DOM.

The `buildExecScript` core in `background.js` includes an `\_air()` (auto-insert-return) function: if the last line of user code doesn't start with a statement keyword (`let`, `const`, `if`, `for`, etc.), it prepends `return` to make expression evaluation natural. This means `document.title` works as expected without requiring `return document.title`. If `eval` fails with a SyntaxError mentioning `return` or `await`, it automatically re-wraps the code as an `AsyncFunction`.

Sources: [background.js](assets/tmwd_cdp_bridge/background.js#L2-L16), [background.js](assets/tmwd_cdp_bridge/background.js#L134-L188), [background.js](assets/tmwd_cdp_bridge/background.js#L254-L292)

## CDP Command Routing

Beyond plain JavaScript execution, the extension exposes a structured command protocol that gives the agent direct access to Chrome DevTools Protocol capabilities. Commands are sent as JSON strings with a `cmd` field and routed through `handleExtMessage()`.

### Available Commands

| Command | Parameters | Description |
| --- | --- | --- |
| `cookies` | `url`, `tabId` | Retrieve all cookies for a URL, including partitioned cookies (CHIPS) |
| `cdp` | `tabId`, `method`, `params` | Send a single CDP command via `chrome.debugger.sendCommand` |
| `batch` | `commands[]`, `tabId` | Execute multiple commands in sequence with lazy CDP attach and `$N.path` result referencing |
| `tabs` | `method: "switch"` or none | List all scriptable tabs, or switch focus to a specific tab |
| `management` | `method: "list"/"reload"/"disable"/"enable"`, `extId` | Manage Chrome extensions (list, reload, enable, disable) |

Sources: [background.js](assets/tmwd_cdp_bridge/background.js#L18-L57), [memory/tmwebdriver\_sop.md](memory/tmwebdriver_sop.md#L41-L70)

### Batch Command Engine

The batch command system is the most powerful CDP interaction pattern. It allows chaining multiple operations in a single request, with automatic CDP session reuse and cross-result referencing via the `$N.path` syntax.

The `$N.path` reference syntax (e.g., `"$2.root.nodeId"`) is resolved by `resolve$N()`, which uses a regex to replace `"$N.path"` patterns with the actual value from the Nth result in the batch's results array. This enables complex workflows like file upload in a single request: `getDocument` → `querySelector` → `setFileInputFiles`, where each step references the nodeId produced by the previous one.

A key optimization in the batch engine is **lazy CDP attach**: the debugger is attached only when the first CDP command is encountered and reused for subsequent CDP commands targeting the same tab. The debugger is detached once at the end of the batch, rather than per-command — significantly reducing the overhead of multi-step CDP interactions.

Sources: [background.js](assets/tmwd_cdp_bridge/background.js#L84-L115), [memory/tmwebdriver\_sop.md](memory/tmwebdriver_sop.md#L55-L70)

## Content Script: TID DOM Bridge

The `content.js` file implements a secondary communication channel — a DOM-based command bridge using a hidden element identified by a TID (Transaction ID). While the WebSocket path is preferred for new commands, the TID bridge remains relevant as the underlying mechanism used by `web_scan` and the `execute_js` fallback.

A `MutationObserver` watches for elements matching the TID. When found, the element's `textContent` is parsed as a JSON command (e.g., `{cmd: "cookies"}`), dispatched to the background script via `chrome.runtime.sendMessage`, and the response is written back into the element's `textContent`. This creates a synchronous-looking request-response pattern across the content script / background script boundary.

The content script also injects a small green "ljq\_driver: 已连接" indicator badge in the bottom-right corner of each page (excluding Streamlit apps), providing visual confirmation that the extension is active on the current page.

Sources: [content.js](assets/tmwd_cdp_bridge/content.js#L1-L47)

## Agent Integration: web\_scan and web\_execute\_js

From the agent's perspective, TMWebDriver is accessed through two tools defined in `tools_schema.json`: `web_scan` (for reading page content) and `web_execute_js` (for executing JavaScript). The tool dispatch layer in `agentmain.py` maps these tool calls to TMWebDriver methods, with session selection via `switch_tab_id` parameters.

The `web_execute_js` tool supports a dual invocation mode: either pass a `script` parameter with the code string, or include the JavaScript in a fenced ```` ```javascript ``` ```` code block in the reply — the dispatch layer automatically extracts and executes it. This reduces escaping complexity for the LLM, which can write natural JavaScript without worrying about JSON string escaping.

The `web_scan` tool reads the current page's simplified HTML (processed by the HTML Simplification Engine — see [HTML Simplification Engine](/16-html-simplification-engine) ) and returns it along with a list of all open tabs. The `switch_tab_id` parameter allows the agent to target a specific tab, and `text_only` mode strips all HTML markup for pure text extraction.

Sources: [tools\_schema.json](assets/tools_schema.json#L37-L53), [memory/tmwebdriver\_sop.md](memory/tmwebdriver_sop.md#L1-L6)

## Key Limitations and Design Decisions

Understanding what TMWebDriver **cannot** do is as important as understanding its capabilities. These limitations are architectural consequences of the browser security model, not bugs.

### isTrusted Event Restriction

JavaScript-dispatched events carry `isTrusted: false`, which many web applications check before processing clicks, file uploads, or form submissions. For these scenarios, the CDP batch path is the preferred solution — CDP-dispatched `Input.dispatchMouseEvent` events carry `isTrusted: true` because they originate from the browser's input pipeline.

### Cross-Tab Operation

While the CDP bridge can target any tab by `tabId` (including background tabs), some CDP domains like `Target.getTargets` and `Target.attachToTarget` are restricted by `chrome.debugger` permissions and return "Not allowed" errors. Cross-origin iframe access requires the `Page.getFrameTree` → `Page.createIsolatedWorld` → `Runtime.evaluate` workaround rather than direct target attachment.

### Remote Mode

When a TMWebDriver instance detects that port `18766` is already occupied (indicating a master instance is running), it switches to remote mode. In this mode, all operations are proxied via HTTP POST to the master's `/link` endpoint. This allows multiple agent processes to share a single browser connection.

Sources: [TMWebDriver.py](TMWebDriver.py#L43-L48), [memory/tmwebdriver\_sop.md](memory/tmwebdriver_sop.md#L11-L16), [memory/tmwebdriver\_sop.md](memory/tmwebdriver_sop.md#L71-L101)

## Next Steps

The TMWebDriver bridge is the gateway between the agent's cognitive layer and the browser. To understand how the agent decides *what* to execute, see [Agent Loop and Task Runner](/9-agent-loop-and-task-runner) . For how page content is simplified before the agent reads it, continue to [HTML Simplification Engine](/16-html-simplification-engine) . For the full repertoire of atomic tools available to the agent including `web_scan` and `web_execute_js`, see [Nine Atomic Tools](/11-nine-atomic-tools) .

TMWebDriver Bridge | lsdefine/GenericAgent | Zread---

<!-- Page 14: https://zread.ai/lsdefine/GenericAgent/16-html-simplification-engine -->

# HTML Simplification Engine

Level: Advanced

GenericAgent's browser control pipeline treats raw DOM as an adversarial input: modern web pages routinely ship 5–15 MB of markup for a viewport that an LLM must reason over within a ~35k token budget. The HTML Simplification Engine in <simphtml.py> solves this by executing a **two-phase pipeline**—a JavaScript-side spatial analysis layer runs inside the browser to identify and strip non-essential DOM, then a Python-side token optimization layer post-processes the surviving markup for density. This page dissects the engine's architecture, its marking algorithm, list compression strategy, change detection protocol, and the orchestration glue that binds it to the agent loop.

## Architectural Overview

The engine follows a **browser-native → Python-post-process** split that exploits the asymmetric capabilities of each runtime. The browser has access to `getComputedStyle`, `getBoundingClientRect`, shadow roots, and cross-origin iframe documents—information that cannot be reconstructed from serialized HTML. Python, conversely, has BeautifulSoup's deterministic tree manipulation and token counting. The handoff occurs at serialization: JavaScript returns an optimized HTML string, and Python applies orthogonal compressions that don't require rendering context.

The entry point into this pipeline depends on which agent tool is invoked. The `web_scan` tool calls [get\_html()](simphtml.py#L702-L739) for a single consolidated snapshot, while `web_execute_js` wraps the entire sequence inside [execute\_js\_rich()](simphtml.py#L817-L871) which adds pre/post change detection around arbitrary JavaScript execution.

Sources: [simphtml.py](simphtml.py#L1-L4), [ga.py](ga.py#L112-L116), [ga.py](ga.py#L163-L164)

## Phase 1: JavaScript DOM Analysis (`js_optHTML`)

The browser-side workhorse is the [`optHTML()`](simphtml.py#L4-L324) function, a 320-line JavaScript monolith injected via `driver.execute_js()`. It operates in three sequential stages: **clone → mark → prune**.

### Enhanced DOM Cloning

[`createEnhancedDOMCopy()`](simphtml.py#L5-L124) performs a deep clone of `document.body` while simultaneously computing per-node metadata stored in a `WeakMap`. The cloning logic is deliberately selective:

* **Tag filtering**: `SCRIPT`, `STYLE`, `NOSCRIPT`, `META`, `LINK`, `COLGROUP`, `COL`, `TEMPLATE`, `PARAM`, `SOURCE` are dropped at the gate ([line 7](simphtml.py#L7)).
* **ID filtering**: Elements with `id="ljq-ind"` (the agent's own UI overlay) are excluded ([line 8](simphtml.py#L8)).
* **State preservation**: `INPUT` values, `CHECKBOX` checked states,  selected values, and autofill indicators are copied into attributes so the LLM can infer form state ().

The clone step is the engine's only opportunity to access live rendering data. Any element whose visibility depends on CSS cascade, `z-index` stacking, or JavaScript-applied styles must be resolved here. The `WeakMap` approach avoids mutating the live DOM—a critical safety property since the agent shares the browser tab with user interactions.

Sources: [simphtml.py](simphtml.py#L5-L124)

### Recursive Spatial Marking

After cloning, [`analyzeNode()`](simphtml.py#L140-L182) walks the cloned tree top-down, assigning `data-mark` attributes that classify each node's role in the visual layout. The algorithm treats the DOM as a spatial partitioning problem.

The recursion has a **penetration heuristic**: if a node has exactly one child, it is marked `K:container` and the algorithm recurses into that child ([lines 153-156](simphtml.py#L153-L156)). This skips the ubiquitous wrapper `<div>` patterns that add no structural information. Processing stops at nodes with more than 10 children to avoid expensive O(n²) overlap checks on large flat containers ([line 157](simphtml.py#L157)).

For each multi-child node whose bounding box covers ≥80% of the viewport in both width and height, the algorithm determines whether children **partition** (tile without overlap) or **overlay** (stack on top of each other) using [`hasOverlap()`](simphtml.py#L273-L288). This distinction drives two completely different classification strategies.

**Partition containers** ([`handlePartitionContainer()`](simphtml.py#L185-L217)) rank children by area and identify a dominant element:

| Condition | Mark | Rationale |
| --- | --- | --- |
| Largest child > 50% of total area AND > 2× the second largest | `K:main` | Dominant content region |
| Contains `button`, `input[submit]`, `.btn`, nav-related classes, breadcrumbs, or substantial text (>200 chars) | `K:secondary` | Navigation, toolbars, sidebar with interactive elements |
| None of the above | `K:nonEssential` | Decorative dividers, whitespace containers |

**Overlay containers** ([`handleOverlayContainer()`](simphtml.py#L226-L271)) handle modal dialogs, floating UIs, and layered content. The top-most element by `z-index` is classified by a multi-signal heuristic:

| Signal Combination | Mark | Example |
| --- | --- | --- |
| Contains form elements + centered (<20% offset) + sized 20-98% of viewport | `K:mainInteractive` | Login modal, settings dialog |
| Form elements + near top (`rect.top < 50`) + visible + >40% of viewport in one dimension | `K:topBar` | Fixed navigation header |
| Mostly text (>7 chars) with no links | `K:messageContent` | Toast notification, alert banner |
| Contains button/input/iframe + centered (<30% offset) | `K:messageContent` | Cookie consent, feature tour popup |
| None of the above | `R:floatingAd` | Promotional overlay, watermark |

A critical refinement uses `document.elementFromPoint()` at the viewport center to establish ground-truth z-ordering, boosting the actual topmost element's effective z-index to 9999 ([line 229](simphtml.py#L229)). This corrects for cases where CSS `z-index` doesn't reflect visual stacking due to stacking context isolation.

Sources: [simphtml.py](simphtml.py#L140-L271)

### Dialog Hoisting and Pruning

Before the recursive marking begins, fixed-position dialogs that satisfy coverage criteria (>15% but <100% of viewport area, centered within 30% of viewport midpoint, containing at least one interactive element) are **hoisted** to become direct children of the root cloned element ([lines 291-301](simphtml.py#L291-L301)). This prevents them from being incorrectly classified as children of their original DOM parent, which might be marked for removal.

After marking completes, all elements with `data-mark` prefixed by `R:` are stripped—this includes `R:covered` (elements beneath overlays), `R:floatingAd` (detected ads), and `R:equalmany` (repetitive sibling groups from the disabled equal-many path). A three-pass empty-div cleanup follows ([lines 308-310](simphtml.py#L308-L310)), then all `data-mark` attributes are removed to produce clean output HTML. Finally, iframes that were inlined as `div[data-tag="iframe"]` during cloning are converted back to proper `<iframe>` tags ([lines 313-321](simphtml.py#L313-L321)).

Sources: [simphtml.py](simphtml.py#L290-L324)

## Phase 2: Python Token Optimization

The HTML string returned from the browser undergoes deterministic post-processing in Python that targets token density rather than visual fidelity.

### Attribute and Content Compression

[`optimize_html_for_tokens()`](simphtml.py#L593-L616) applies a series of attrition rules via BeautifulSoup:

| Transformation | Token Savings | Example |
| --- | --- | --- |
| SVG content cleared + attrs stripped | Eliminates entire inline icon libraries | `<svg>…complex paths…</svg>` → `<svg></svg>` |
| All `style` attributes removed | Cuts CSS-in-HTML bloat | `style="color:#fff;font-size:14px;..."` → deleted |
| Data URIs shortened to `__img__` | ~500 chars per inline image | `data:image/png;base64,iVBOR...` → `__img__` |
| Long URLs shortened to `__url__` / `__link__` | ~50-200 chars per URL | `href="https://cdn.example.com/path/to/resource"` → `__url__` |
| Long `value`// truncated to 50 chars |

The whitelist of 28 preserved attributes is deliberately chosen to maintain **LLM actionability**: the agent needs `id`, `class`, `name`, `placeholder`, `role`, `aria-label`, and form state attributes to construct reliable CSS selectors and `document.querySelector()` calls when executing JavaScript actions.

Sources: [simphtml.py](simphtml.py#L593-L616)

### List Detection and Truncation (`cutlist`)

When `cutlist=True` is passed to [`get_html()`](simphtml.py#L702-L739), the engine activates [`js_findMainList()`](simphtml.py#L326-L591)—a 265-line JavaScript function that identifies repetitive list structures in the DOM. This is the engine's most sophisticated analysis, employing a multi-stage scoring pipeline.

**Candidate scanning** ([lines 332-344](simphtml.py#L332-L344)) surveys all DOM elements, computing a composite score of `childCount + grandchildCount × 0.1` for each. Elements scoring ≥ 8 (with at least 5 direct children) become candidates, capped at the top 20 by score.

**Group discovery** ([`findTopGroups()`](simphtml.py#L403-L500)) within each candidate container identifies structural repetition by analyzing tag frequency, class frequency, and their combinations. It generates selector candidates like `li`, `.item`, `div.card`, and `.btn-primary.btn-sm`, scoring each by coverage (fraction of children matched) and selector specificity.

**Container scoring** ([`scoreContainer()`](simphtml.py#L512-L591)) evaluates candidate containers across five dimensions using continuous mathematical functions rather than hard thresholds:

| Dimension | Max Score | Function | What It Measures |
| --- | --- | --- | --- |
| Item count | ~40 | `log₂(n) × 5 + floor(n/5) × 0.25`, modulated by uniformity | Sheer volume of list items |
| Area coverage | 40 | Sigmoid: `40 / (1 + e^(-12(x-0.4)))` where x = totalItemArea/containerArea | How much of the container's space items occupy |
| Size uniformity | 20 | Exponential decay: `20 × e^(-2.5 × CV)` where CV = coefficient of variation | Consistency of item dimensions |
| Container viewport ratio | ~15 | Sigmoid: `2(1 - 1/(1 + e^(-10(x-0.25)}))` | Whether the list occupies meaningful screen real estate |
| Layout efficiency | 20 | Grid coverage: `0.7 × coverage + 0.3 × efficiency` using coordinate-bucketed rows/cols | Whether items form a clean grid or list |

The use of sigmoid functions for area and container-size scoring creates smooth transitions that avoid cliff-edge behaviors where a 1-pixel difference in area ratio causes a dramatic score jump.

**Deduplication** ([lines 365-376](simphtml.py#L365-L376)) removes dominated candidates where a higher-scoring result shares >50% item overlap in an ancestor/descendant relationship, ensuring the agent receives non-redundant list descriptors.

The Python side then **truncates detected lists** ([lines 713-738](simphtml.py#L713-L738)): for each list with average item length > 200 chars (or > 700 chars with < 2500 total), it keeps only 3 items (or up to 6 if they match the agent's current instruction), decomposes the rest, and injects a `[FAKE ELEMENT]` hint tag listing the selector and sample text of hidden items. This preserves the LLM's awareness of the list's existence and structure while cutting token usage by 60-90% for large product grids, search results, or comment threads.

Sources: [simphtml.py](simphtml.py#L326-L591), [simphtml.py](simphtml.py#L702-L739)

### Budget-Aware Recursive Truncation

When the total HTML still exceeds `maxchars` (default 35,000 characters), [`smart_truncate()`](simphtml.py#L741-L815) performs recursive budget carving on the BeautifulSoup tree. This is not a simple character-slice—it's a structural algorithm:

1. **Single-child penetration**: If the root has only one child, recurse into it, preserving the wrapper tag's overhead budget ([lines 776-778](simphtml.py#L776-L778)).
2. **Top-3 assessment**: Rank children by serialized size. If the top 3 largest children can collectively absorb the excess, recurse into them proportionally ([lines 783-814](simphtml.py#L783-L814)).
3. **Proportional allocation**: Each large child's new budget is calculated as `originalSize - excess × (size / topTotal)`, with a minimum-size filter that prevents tiny children from being unfairly penalized ([lines 797-801](simphtml.py#L797-L801)).
4. **Tail-cut fallback**: If the top 3 cannot absorb the excess (they're collectively smaller than the overage), children are removed from the end until the budget is met ([lines 786-794](simphtml.py#L786-L794)).
5. **Leaf truncation**: When recursing bottoms out (budget < 8,000 chars), a direct `innerHTML` truncation inserts a `[TRUNCATED Nk chars]` marker ([lines 746-766](simphtml.py#L746-L766)).

The `smart\_truncate` function is designed to preserve the \*\*beginning\*\* of the page (where navigation and primary content typically live) while aggressively trimming from the end. The `[FAKE ELEMENT]` hint tags injected by `cutlist` are explicitly protected from truncation via extraction-and-reinsertion ([line 752](simphtml.py#L752)), ensuring the LLM always knows truncated lists existed even when the budget is extremely tight.

Sources: [simphtml.py](simphtml.py#L741-L815)

## Change Detection and Transient Capture

The [`execute_js_rich()`](simphtml.py#L817-L871) function wraps arbitrary JavaScript execution with a three-part monitoring protocol that enables the agent to reason about *what changed* without re-scanning the entire page.

### DOM Diffing

[`find_changed_elements()`](simphtml.py#L669-L700) computes a structural diff between two HTML snapshots. It builds **element signatures** from `tag name + attributes (excluding data-track-id) + direct text content`, then compares the before/after signature maps. The algorithm identifies:

* **New elements**: signatures present in `after` but absent in `before`
* **Count increases**: signatures with more occurrences in `after`
* **Positional changes**: when no signature-level changes are found but serialized HTML differs, a positional scan detects the first differing element ([lines 688-691](simphtml.py#L688-L691))

The result includes a `changed` count and a `top_change` field containing the HTML of the most significant changed element (up to 2,000 characters), selected as the deepest changed element whose parent is not itself changed—the **change boundary** ([lines 692-700](simphtml.py#L692-L700)).

### Transient Text Monitoring

[`start_temp_monitor()`](simphtml.py#L633-L635) and [`get_temp_texts()`](simphtml.py#L637-L657) implement a time-based string capture mechanism. A `TreeWalker` extracts all text nodes > 10 characters every 450ms, building a set of "seen strings." After JavaScript execution, [`get_temp_texts()`](simphtml.py#L637-L657) returns strings that appeared during execution but are no longer present in the final DOM—these are **transient UI texts** like toast messages, loading indicators, or ephemeral validation errors that the LLM would otherwise have no visibility into.

The filtering logic has a smart threshold: if fewer than 8 transient strings were observed, all are returned; if more, only strings no longer present in the current DOM are returned ([lines 644-648](simphtml.py#L644-L648)). This prevents flooding the context with persistent notification-bar text that happened to be captured during the monitoring window.

Sources: [simphtml.py](simphtml.py#L619-L700), [simphtml.py](simphtml.py#L817-L871)

## Integration with the Agent Loop

The HTML Simplification Engine is not a standalone service—it is invoked synchronously within two tool dispatch paths of the [`GenericAgentHandler`](ga.py#L258-L260):

### `web_scan` Path

[`do_web_scan()`](ga.py#L309-L322) calls `get_html(driver, cutlist=True, maxchars=35000)` for the default full-scan mode, or returns only the tab list when `tabs_only=True`. The `cutlist=True` default means every `web_scan` invocation activates the expensive `js_findMainList()` analysis. The `text_only=True` variant bypasses all HTML processing and returns plain text from the JavaScript-side [`text_only` branch](simphtml.py#L126-L137) which collapses block elements into newlines and formats form controls as bracketed descriptors.

### `web_execute_js` Path

[`do_web_execute_js()`](ga.py#L323-L350) calls `execute_js_rich(script, driver)` which wraps the user's script with pre-snapshot, transient monitoring, and post-snapshot diffing. This means every JavaScript execution automatically incurs the cost of two `get_html()` calls (baseline + comparison) unless `no_monitor=True` is specified. The returned dict bundles `js_return`, `transients`, `diff`, `reloaded` status, `newTabs`, and an optional `suggestion` string—giving the LLM a rich post-execution summary without needing a separate `web_scan`.

### Orchestration in `get_html`

The master function [`get_html()`](simphtml.py#L702-L739) sequences the full pipeline:

The `instruction` parameter is threaded into list truncation ([line 723](simphtml.py#L723)): if the agent's current task instruction text appears within a list item, those matching items are preserved preferentially (up to 6 instead of the default 3). This creates a feedback loop where the agent's stated intent influences what content the simplification engine prioritizes.

Sources: [ga.py](ga.py#L309-L350), [simphtml.py](simphtml.py#L702-L739)

## Text-Only Mode

When the LLM doesn't need structural HTML (e.g., reading article content), `text_only=True` activates a completely different code path that runs entirely within the browser. The [`text_only` branch](simphtml.py#L126-L137) of `optHTML()`:

1. Collapses all block-level elements (`DIV`, `P`, `H1-H6`, `LI`, `TR`, `SECTION`, etc.) into newline-separated text ([lines 127-130](simphtml.py#L127-L130)).
2. Formats interactive form controls as bracketed descriptors including tag, id, name, type, placeholder, autofill status, and disabled state ([lines 131-133](simphtml.py#L131-L133)).
3. Prefixes disabled buttons with `[DISABLED]` ([line 135](simphtml.py#L135)).
4. Returns `textContent` of the marked clone—no BeautifulSoup processing needed on the Python side.

The Python-side [`get_main_block()`](simphtml.py#L660-L667) then applies regex cleanup: collapsing consecutive spaces, stripping leading whitespace per line, and reducing 3+ consecutive blank lines to a single blank line ([lines 663-666](simphtml.py#L663-L666)). This produces a clean, dense plaintext representation that typically uses 40-60% fewer tokens than the HTML equivalent.

Sources: [simphtml.py](simphtml.py#L126-L137), [simphtml.py](simphtml.py#L660-L667)

## Configuration and Tuning Parameters

| Parameter | Location | Default | Effect |
| --- | --- | --- | --- |
| `maxchars` | `get_html()` | 35,000 | Hard ceiling on returned HTML character count |
| `cutlist` | `get_html()` | `True` (via `web_scan`) | Enables/disables list detection and truncation |
| `instruction` | `get_html()` | `""` | Text matched against list items to prioritize preservation |
| `text_only` | `get_html()`, `get_main_block()` |

Sources: [simphtml.py](simphtml.py#L328-L329), [simphtml.py](simphtml.py#L619-L632), [simphtml.py](simphtml.py#L702-L739), [simphtml.py](simphtml.py#L744)

## Next Steps

This page covered the HTML Simplification Engine in isolation. To understand how the simplified HTML feeds into the agent's decision loop, see [Agent Loop and Task Runner](/9-agent-loop-and-task-runner) . For the browser bridge that delivers JavaScript to the page, see [TMWebDriver Bridge](/15-tmwebdriver-bridge) . To understand how the token budget interacts with the broader context management strategy, see [Context Compression Strategy](/26-context-compression-strategy) .

`SELECT`

[lines 19-22](simphtml.py#L19-L22)

- **Shadow DOM penetration**: `shadowRoot` children are recursively cloned and appended as regular children, breaking encapsulation barriers ([lines 48-53](simphtml.py#L48-L53)).

- **Cross-origin iframe descent**: Accessible iframe `contentDocument` bodies are cloned into wrapper `div` elements with a `data-iframe-content` attribute preserving the source URL ([lines 34-47](simphtml.py#L34-L47)).

- **Visibility computation**: Each node receives a computed `isVisible` flag based on `getBoundingClientRect()` dimensions (must exceed 1×1px), `display`/`visibility`/`opacity` styles, and viewport boundary checks (coordinates must fall within ±5000px) ([lines 55-62](simphtml.py#L55-L62)).

`title`

`alt`

|  |
| --- |
| Prevents hidden data leaks |

|  |
| --- |
| `value="eyJhbGciOiJIUzI1NiIs..."` → first 50 chars + `...` |

|  |  |  |
| --- | --- | --- |
| Non-essential attributes removed | ~5-15 attrs per element average | Only 28 whitelisted attribute names survive ([line 608](simphtml.py#L608-L611)) |

|  |  |  |
| --- | --- | --- |
| Vue scoped `data-v-*` attrs removed | Framework-specific bloat | `data-v-a1b2c3d=""` → deleted |

|  |  |  |
| --- | --- | --- |
| Long generic `data-*` attrs shortened to `__data__` | Analytics/tracking noise | `data-track-id="eyJ...200chars..."` → `__data__` |

|  |
| --- |
| `False` |

|  |
| --- |
| Switches to plaintext extraction mode |

|  |  |  |  |
| --- | --- | --- | --- |
| `MIN_CHILDREN` | `js_findMainList` | 8 | Minimum composite score for list container candidacy |

|  |  |  |  |
| --- | --- | --- | --- |
| `MAX_CONTAINERS` | `js_findMainList` | 20 | Max containers subjected to group analysis |

|  |  |  |  |
| --- | --- | --- | --- |
| Monitor interval | `temp_monitor_js` | 450ms | Polling frequency for transient text capture |

|  |  |  |  |
| --- | --- | --- | --- |
| `CUT_THRESHOLD` | `smart_truncate` | 8,000 | Below this budget, direct string truncation instead of recursive |

HTML Simplification Engine | lsdefine/GenericAgent | Zread---

<!-- Page 15: https://zread.ai/lsdefine/GenericAgent/17-memory-hierarchy-design -->

# Memory Hierarchy Design

Level: Intermediate

GenericAgent treats memory not as passive storage but as a **tiered navigation system** for the LLM's own cognition. The architecture enforces a strict four-layer pyramid — L1 through L4 — where each layer serves a distinct purpose, is bound by explicit size constraints, and is governed by an "existence-encoding" philosophy: the LLM only needs to *know something exists* to retrieve it on demand via tool calls. This design directly addresses the fundamental tension in agentic systems between context-window scarcity and the need for persistent, cross-session knowledge.

## The Four-Layer Architecture

The memory system is a directed acyclic graph where information flows downward (from volatile to persistent) and references flow upward (from index to detail). At the top, L1 is injected into every system prompt; at the bottom, L4 is an archive that the agent never reads unless explicitly instructed.

The initialization sequence in `agentmain.py` establishes this structure at startup: it creates the `memory/` directory, bootstraps  (L2) with a header if absent, and copies the L1 insight template from . This ensures a valid memory pyramid exists before the agent processes its first task.

`global_mem.txt`

`assets/global_mem_insight_template.txt`

Sources: [agentmain.py](agentmain.py#L21-L28)

## L0: The META-SOP — Governance Layer

Before examining the four data layers, it is essential to understand the governance layer that regulates all memory operations. The file `memory/memory_management_sop.md` functions as the **constitution** for the memory system — it is not a storage layer itself, but a set of immutable axioms that the agent must consult before any write operation.

Four core axioms constrain all memory mutations:

| Axiom | Principle | Practical Effect |
| --- | --- | --- |
| **Action-Verified Only** | Only write information derived from successful tool call results | Prevents hallucinated "knowledge" from polluting memory |
| **Sanctity of Verified Data** | Never discard verified configurations or pitfall guides during cleanup | Compression may shrink text, but information accuracy is preserved |
| **No Volatile State** | Never store ephemeral data (timestamps, PIDs, session IDs) | Memory stores durable facts, not runtime state |
| **Minimum Sufficient Pointer** | Upper layers store only the shortest identifier needed to locate lower-layer data | Minimizes token cost per prompt injection |

The agent is explicitly instructed — via the fixed structure injected with every prompt — that it must read the META-SOP before writing to any memory file: *"写任何记忆前读META-SOP核验，memory下文件只能patch修改（除非新建）"*.

Sources: [memory\_management\_sop.md](memory/memory_management_sop.md#L1-L14), [insight\_fixed\_structure.txt](assets/insight_fixed_structure.txt#L9)

## L1: Global Insight Index — The Needle Finder

L1 (`memory/global_mem_insight.txt`) is the only layer injected into the system prompt on every turn. It is therefore the most token-sensitive and the most tightly constrained: **≤ 30 lines** (hard limit) and **< 1,000 tokens** (expectation). Its role is purely navigational — it tells the LLM *what knowledge exists* and *where to find it*, never *what that knowledge contains*.

The layer contains two categories of content:

1. **Scene-keyword → Memory-location mappings**: High-frequency scenarios get a direct pointer (e.g., `tmwebdriver_sop(httponly cookie)`); low-frequency ones get only a keyword for the agent to `file_read` or `ls` on demand.
2. **RULES block**: A compressed collection of red-line rules (actions that kill the process or produce silent wrong results) and high-frequency mistake patterns.

The `get_global_memory()` function assembles the L1 payload each time the system prompt is built. It reads both the insight file and a fixed structural preamble from `assets/insight_fixed_structure.txt`, concatenating them into the prompt. Additionally, every 10 turns during a running task, the agent re-injects this global memory to prevent the LLM from "forgetting" available capabilities deep in a long session.

Sources: [ga.py](ga.py#L545-L558), [ga.py](ga.py#L532), [memory\_management\_sop.md](memory/memory_management_sop.md#L27-L40)

### L1 Cleanup Philosophy: Existence Encoding

The memory cleanup SOP (`memory_cleanup_sop.md`) codifies a striking principle: **the LLM is itself a compressor and decoder**. L1 needs only to make the LLM *aware that a category of knowledge exists* — it can then self-retrieve deeper content via tool calls. The cleanup evaluates every L1 entry by a simple ROI formula:

**ROI = (Probability of error without this entry × Cost of error) / Token cost per turn**

Entries that fail this test — redundant translations, intuitive capabilities that need no reminder, implementation details that belong in the SOP itself — are ruthlessly pruned. The cleanup process is itself constrained: L1 may only be modified via `file_patch` at the word level; overwrites are forbidden.

The L1 → L3 pointer format follows a convention: `scenario\_name(counterintuitive\_trigger\_term)`. Only \*counterintuitive\* trigger terms earn parentheses — if a developer can infer the relevance from the scenario name alone, the parenthetical is waste. This is the "existence encoding" principle in action.

Sources: [memory\_cleanup\_sop.md](memory/memory_cleanup_sop.md#L1-L27)

## L2: Global Fact Store — Environment Truths

L2 (`memory/global_mem.txt`) stores **environment-specific facts** that the LLM cannot generate from its training data: non-standard file paths, credential locations, configuration constants, user preferences, and infrastructure IDs. Unlike L1, L2 is allowed to grow as the deployment environment expands — it has no hard line limit.

Content is organized into `## [SECTION]` blocks for navigability. When L2 is updated, the agent must synchronize the corresponding pointer in L1 (adding a new entry if the scenario is novel, or leaving L1 untouched if only a value changed without affecting discoverability). The sync rules are explicit:

| L2/L3 Operation | L1 Sync Action |
| --- | --- |
| New scenario added | Default to low-frequency → add filename to L3 list |
| Scenario removed | Delete corresponding keyword/mapping |
| Value modified | No L1 change if discoverability unaffected |
| Universal pitfall discovered | Compress to one sentence, add to RULES |

Sources: [memory\_management\_sop.md](memory/memory_management_sop.md#L42-L49), [memory\_management\_sop.md](memory/memory_management_sop.md#L60-L68)

## L3: Task-Level Record Store — SOPs and Scripts

L3 is the `memory/` directory itself, populated with `*_sop.md` files (Standard Operating Procedures) and `*.py` utility scripts. Each file serves a specific task domain and is designed to be the **minimum viable reference** for that domain — recording only information that is costly to re-derive through exploration.

The directory currently contains 15+ SOPs covering domains like browser automation (`tmwebdriver_sop.md`), scheduled tasks (`scheduled_task_sop.md`), vision processing (`vision_sop.md`), and autonomous operations (`autonomous_operation_sop.md`), alongside reusable utility modules like `procmem_scanner.py` and `ocr_utils.py`.

The L3 philosophy is one of *selective persistence*: only record cross-session knowledge that (a) required painful trial-and-error to discover and (b) cannot be reconstructed from a few quick tool calls. Ordinary operational steps and easily re-discoverable state are explicitly excluded.

Sources: [memory\_management\_sop.md](memory/memory_management_sop.md#L50-L58), <memory/>

## L4: Raw Session Archive — The History Vault

L4 (`memory/L4_raw_sessions/`) is the deepest layer, storing compressed logs of past sessions. Unlike L1–L3, the agent **never reads L4 during normal operation** — it is populated by the scheduled reflection system (`reflect/scheduler.py`) and exists for post-hoc analysis or context recovery.

The `compress_session.py` module handles two input formats: JSON-structured logs (kept as-is) and raw text logs (stripped of system prompts and assistant echoes to minimize storage). The scheduler triggers batch processing every 12 hours via its `check()` function, compressing raw model response files from `temp/model_responses/` into dated archives.

Sources: [compress\_session.py](memory/L4_raw_sessions/compress_session.py#L1-L45), [scheduler.py](reflect/scheduler.py#L62-L63)

## Working Memory — The Transient Layer

Beyond the persistent L1–L4 pyramid, GenericAgent maintains a **working memory** that exists only for the duration of a single agent run. This is managed by `GenericAgentHandler` through two mechanisms:

1. **`working` dictionary**: Stores `key_info` (task-critical context set by the agent via `update_working_checkpoint`) and `related_sop` (a pointer to the most relevant SOP for the current task). These are injected into every subsequent turn via `_get_anchor_prompt()`.
2. **`history_info` list**: A rolling log of `[USER]` and `[Agent]` summaries (extracted from `<summary>` tags or inferred from tool calls). The last 20 entries are injected as a `<history>` block with each turn, providing recent conversational context.

Working memory is **not persisted to disk** — it is purely transient. When the agent needs to preserve insights across sessions, it must explicitly invoke `start_long_term_update`, which triggers the META-SOP-guided consolidation process into L1/L2/L3.

Sources: [ga.py](ga.py#L260-L266), [ga.py](ga.py#L504-L514), [ga.py](ga.py#L427-L437)

## The Memory Lifecycle — Write Path

Information enters the memory system through a deliberate, gated process rather than passive accumulation. The `start_long_term_update` tool is the sole entry point for cross-session memory writes. When invoked, it:

1. Injects the full memory SOP into the next prompt turn
2. Instructs the agent to classify information by the decision tree (environment fact → L2, universal rule → L1 RULES, task-specific → L3 SOP, common knowledge → discard)
3. Requires the agent to read existing memory first, then apply minimum-patch updates

Sources: [ga.py](ga.py#L488-L502), [memory\_management\_sop.md](memory/memory_management_sop.md#L71-L89)

## System Prompt Assembly — How Memory Enters Context

The complete flow from filesystem to LLM context window is orchestrated by two functions called at the start of each task in `agentmain.py`:

1. `get_system_prompt()` reads the base system prompt template from `assets/sys_prompt.txt`, appends the current date, and then appends the output of `get_global_memory()`.
2. `get_global_memory()` reads the fixed structure preamble and the L1 insight file, composing them into a `[Memory]` block.

This means **every agent turn begins with L1 content in context**, ensuring the LLM always has its navigational index available. The L2 fact file and L3 SOPs are not pre-loaded — the LLM must decide to `file_read` them based on L1 pointers.

Sources: [agentmain.py](agentmain.py#L36-L40), [ga.py](ga.py#L545-L558)---

**Next Steps**: To understand how L4 session logs are compressed and archived in detail, continue to [L4 Session Archive Compression](/18-l4-session-archive-compression) . For a comprehensive look at the SOPs that govern memory operations, see [Memory Management SOPs](/19-memory-management-sops) . To understand how the system prompt and context window are managed during long conversations, see [Context Compression Strategy](/26-context-compression-strategy) .

Memory Hierarchy Design | lsdefine/GenericAgent | Zread---

<!-- Page 16: https://zread.ai/lsdefine/GenericAgent/18-l4-session-archive-compression -->

# L4 Session Archive Compression

Level: Advanced

L4 represents the deepest layer of GenericAgent's hierarchical memory system — a cold-storage archive of raw conversational sessions. Unlike L1–L3, which serve active decision-making, L4 exists for forensic retrieval and long-term context continuity across restarts. The compression pipeline is a self-contained module that transforms verbose, per-PID log files into deduplicated, time-ranged archives, and it is invoked silently by the scheduler every 12 hours without any user intervention.

## Position Within the Memory Hierarchy

The memory management SOP defines four distinct layers, each governed by strict write policies and size constraints ([memory\_management\_sop.md](/memory/memory_management_sop.md#L16-L24)). L4 sits at the base as the "history session layer":

Copy code

```
L1: global_mem_insight.txt   (≤30 lines, pure navigation index)
    ↓
L2: global_mem.txt           (environment facts, may grow)
    ↓
L3: ../memory/               (task-level SOPs and scripts)
    ↓
L4: ../memory/L4_raw_sessions/ (raw session archives, auto-collected)
```

The defining axiom for all layers is **"No Execution, No Memory"** — nothing enters the hierarchy unless it was action-verified during a tool call ([memory\_management\_sop.md](/memory/memory_management_sop.md#L2-L5)). L4 inherits this principle passively: every session it archives is, by definition, a record of executed tool calls, because the raw logs are emitted by the LLM communication layer during live agent execution.

## Raw Log Generation

Before compression can occur, logs must be written. The function `_write_llm_log` in [llmcore.py](/llmcore.py#L837-L843) appends labeled, timestamped sections to a per-PID file at `temp/model_responses/model_responses_{pid}.txt`. Each section is delimited by markers such as `=== Prompt ===`, `=== Response ===`, `=== USER ===`, and `=== ASSISTANT ===`. This is the sole intake point for L4 — every LLM round-trip flows through it, creating a sequential transcript of the full conversation including system prompts, model responses, and user messages.

## Session Format Detection

The compression module must handle two distinct log formats, which it auto-detects via `_detect_format` ([compress\_session.py](/memory/L4_raw_sessions/compress_session.py#L20-L24)):

| Format | Identifier | Content Structure | Compression Strategy |
| --- | --- | --- | --- |
| **A (JSON)** | Content after `=== Prompt ===` starts with `{` | Structured JSON payloads in prompt bodies | Kept as-is — no stripping needed |
| **B (Raw)** | Content after `=== Prompt ===` is free text | Full system prompts, assistant echo, user input interleaved | Strip system prompts and redundant assistant echoes |

Detection is a simple heuristic: after locating the first `=== Prompt ===` marker, the module checks whether the following 200 characters begin with `{`. If so, format A; otherwise, format B ([compress\_session.py](/memory/L4_raw_sessions/compress_session.py#L20-L24)).

## The Four-Phase Batch Pipeline

`batch_process` is the single entry point for the entire archival workflow ([compress\_session.py](/memory/L4_raw_sessions/compress_session.py#L154-L236)). It accepts a source directory (defaulting to `temp/model_responses/`) and orchestrates four sequential phases, writing intermediate results to a temporary directory to ensure atomicity.

### Phase 1: Compress and Extract

Each raw file matching `model_responses_*.txt` is evaluated against three guard conditions before processing ([compress\_session.py](/memory/L4_raw_sessions/compress_session.py#L162-L185)):

1. **Recency guard** — files modified within the last 2 hours are skipped, as they may still be actively written by a running agent PID.
2. **Deduplication guard** — the module reads `all_histories.txt` to build a set of already-archived session names; any duplicate is skipped and the temp file removed.
3. **Minimum size guard** — after compression, sessions smaller than 4,500 bytes are discarded as too insubstantial to archive ([compress\_session.py](/memory/L4_raw_sessions/compress_session.py#L59-L60)).

For files that pass all guards, `compress_session` performs the core transformation. It extracts the first and last `=== Prompt ===` timestamps, formats them as `MMDD_HHMM`, and constructs a destination filename like `0403_2013-0403_2205.txt` ([compress\_session.py](/memory/L4_raw_sessions/compress_session.py#L48-L58)). For format B files, `_compress_raw` strips sections marked `prompt` (system prompts) and `assistant` (redundant echo), retaining only `user` and `response` content ([compress\_session.py](/memory/L4_raw_sessions/compress_session.py#L70-L85)). The function returns a stats dictionary including original/compressed sizes and the compression ratio.

Simultaneously, `extract_history` is called on each compressed file to pull out conversation history lines prefixed with `[USER]` or `[Agent]` from `<history>` XML blocks embedded in the prompts ([compress\_session.py](/memory/L4_raw_sessions/compress_session.py#L127-L137)).

### Phase 2: History Extraction and Merge

The extracted history lines from all new sessions are appended to `all_histories.txt` in a structured block format ([compress\_session.py](/memory/L4_raw_sessions/compress_session.py#L200-L204)):

Copy code

```
============================================================
SESSION: 0403_2013-0403_2205
============================================================
[USER] Please analyze the stock data...
[Agent] I'll scan the latest reports...
[USER] Focus on tech sector...
```

The history extraction mechanism handles **sliding-window deduplication** — raw sessions often contain overlapping `<history>` blocks because each new prompt re-sends prior conversation context. The `_merge_history_blocks` function ([compress\_session.py](/memory/L4_raw_sessions/compress_session.py#L103-L125)) reconstructs the canonical conversation by finding the longest suffix-prefix overlap between consecutive blocks and merging them. It also handles cases where blocks share a common entry but with misalignment, scanning for the best matching prefix to avoid duplication.

### Phase 3: Monthly ZIP Archival

Compressed session files are grouped by their year-month prefix and packed into monthly ZIP archives using DEFLATE compression ([compress\_session.py](/memory/L4_raw_sessions/compress_session.py#L206-L218)). Each archive is named `YYYY-MM.zip` (e.g., `2026-04.zip`). The module uses append mode `'a'` when a zip already exists, checking `namelist()` to avoid re-adding files that were already archived in a previous run.

### Phase 4: Raw File Cleanup

After successful archival, the original raw files are deleted from `temp/model_responses/` ([compress\_session.py](/memory/L4_raw_sessions/compress_session.py#L220-L230)). Files that were skipped for reasons other than "recent" (i.e., too small, already duplicated, or missing timestamps) are also cleaned up. Only files skipped due to the 2-hour recency guard are preserved, ensuring active sessions are never destroyed.

The `dry\_run=True` default in `batch\_process` is a deliberate safety mechanism. When invoked via CLI without the `--run` flag, the pipeline executes all four phases up to the point of writing — then prints a summary and removes the temporary directory without touching any persistent state ([compress\_session.py](/memory/L4\_raw\_sessions/compress\_session.py#L193-L198)). The scheduler, however, bypasses this safety net by passing `dry\_run=False` directly.

## Automated Scheduling

The L4 archival pipeline is triggered automatically by the reflection scheduler in [scheduler.py](/reflect/scheduler.py#L62-L74). The `check()` function maintains a module-level timestamp `_l4_t` and fires `batch_process` every 43,200 seconds (12 hours):

```
if _time.time() - _l4_t > 43200:
    _l4_t = _time.time()
    from compress_session import batch_process
    raw_dir = os.path.join(_dir, '../temp/model_responses')
    r = batch_process(raw_dir, dry_run=False)
```

This runs as part of the reflection loop — when GenericAgent is launched with `--reflect reflect/scheduler.py`, the main loop polls `mod.check()` at the module's `INTERVAL` of 120 seconds ([scheduler.py](/reflect/scheduler.py#L11-L12), [agentmain.py](/agentmain.py#L228-L231)). The L4 check piggybacks on this polling cycle but uses its own independent 12-hour cooldown. Any exception during archival is caught and logged without disrupting the scheduler's ability to process other scheduled tasks ([scheduler.py](/reflect/scheduler.py#L73-L74)).

## CLI Interface

For manual invocation, the module exposes an argparse-based CLI at the bottom of the file ([compress\_session.py](/memory/L4_raw_sessions/compress_session.py#L238-L247)):

| Flag | Default | Effect |
| --- | --- | --- |
| `src` (positional) | `temp/model_responses/` | Directory containing raw log files |
| `--run` | `False` (dry run) | Actually execute all four phases; without this, only reports what would happen |

```
# Preview what would be archived
python memory/L4_raw_sessions/compress_session.py
 
# Execute archival
python memory/L4_raw_sessions/compress_session.py --run
```

## Architectural Invariants

The L4 compression system enforces several implicit invariants that are worth understanding for anyone extending or debugging it:

* **Atomic writes via temp directory**: All compressed files are first written to `tempfile.mkdtemp()`. They only enter the permanent L4 directory after the full batch succeeds, preventing partial-state corruption ([compress\_session.py](/memory/L4_raw_sessions/compress_session.py#L165)).
* **Idempotent re-runs**: The deduplication guard using `_existing_sessions` ensures that re-running `batch_process` on the same raw files produces no duplicates in `all_histories.txt` and no conflicts in ZIP archives ([compress\_session.py](/memory/L4_raw_sessions/compress_session.py#L162-L163)).
* **Two-hour recency as a liveness contract**: The 2-hour cutoff (`time.time() - 7200`) at [compress\_session.py](/memory/L4_raw_sessions/compress_session.py#L169) is the only protection against archiving an in-progress session. This assumes no single session remains actively written for more than 2 hours — a reasonable assumption given the 40-turn max in the agent loop ([agent\_loop.py](/agent_loop.py#L42)).
* **Graceful format degradation**: The history parser handles both newline-delimited and literal `\\n`-delimited formats within `<history>` blocks, ensuring compatibility across different LLM backends and session serialization styles ([compress\_session.py](/memory/L4_raw_sessions/compress_session.py#L95-L100)).

## Reading Next

* **[Memory Hierarchy Design](/17-memory-hierarchy-design)**  — the full architectural rationale for L1–L4 layering and inter-layer synchronization rules.
* **[Memory Management SOPs](/19-memory-management-sops)**  — the canonical policy document governing what may be written to each layer.
* **[Scheduled Reflection and Cron](/22-scheduled-reflection-and-cron)**  — how the scheduler orchestrates L4 archival alongside other periodic tasks.
* **[Context Compression Strategy](/26-context-compression-strategy)**  — the orthogonal mechanism that compresses *live* conversation context within a running session, as opposed to L4's post-hoc archival compression.

L4 Session Archive Compression | lsdefine/GenericAgent | Zread---

<!-- Page 17: https://zread.ai/lsdefine/GenericAgent/19-memory-management-sops -->

# Memory Management SOPs

Level: Advanced

GenericAgent's memory layer is not a passive database — it is a self-governing knowledge constitution enforced by the agent on itself. The SOPs (Standard Operating Procedures) living under `memory/` form a hierarchical control system that governs how the agent reads, writes, curates, and validates every piece of information it encounters. For advanced developers extending or debugging the agent, understanding this SOP fabric is essential: every tool call, every memory write, and every verification step traces back to one of these procedural contracts.

Sources: [memory\_management\_sop.md](memory/memory_management_sop.md#L1-L90), [memory\_cleanup\_sop.md](memory/memory_cleanup_sop.md#L1-L38)

## The SOP Topology: From Constitution to Tactics

The memory SOPs form a stratified governance structure. At the top sits the **Meta-SOP (L0)** — an inviolable constitution that defines what may be remembered and how. Below it, **L1–L3 SOPs** encode operational knowledge ranging from browser automation to adversarial verification, each serving a distinct cognitive function in the agent's decision loop. The following diagram maps this hierarchy and the bidirectional enforcement flows between layers.

Sources: [memory\_management\_sop.md](memory/memory_management_sop.md#L16-L24), [global\_mem\_insight\_template.txt](assets/global_mem_insight_template.txt#L1-L23), [insight\_fixed\_structure.txt](assets/insight_fixed_structure.txt#L1-L10)

## L0: The Memory Constitution — Core Axioms

The `memory_management_sop.md` file is the **Meta-SOP** — the supreme law that all other SOPs and memory operations must obey. It establishes four inviolable axioms that act as hard constraints on the agent's epistemic behavior. These axioms exist because LLMs naturally hallucinate, conflate inference with fact, and accumulate irrelevant state; the axioms mechanically prevent these failure modes from corrupting persistent memory.

### Axiom 1: Action-Verified Only

Every piece of information written to any memory layer **must originate from a successful tool call result** — a `shell` execution that returned exit code 0, a `file_read` that confirmed content exists, or code that actually ran. The agent is prohibited from storing its own "inherent knowledge," reasoning guesses, unexecuted plans, or unverified hypotheses. The slogan is explicit: **No Execution, No Memory.** This axiom is the single most important guardrail in the system.

### Axiom 2: Sanctity of Verified Data

Once information has passed the action-verification gate, it becomes **sacrosanct during garbage collection**. The agent may compress the text representation, or migrate data between layers (e.g., from L2 to L3), but it must never lose the accuracy or traceability of the information. During memory refactoring, verified configurations, pitfall warnings, and critical paths are explicitly protected from deletion.

### Axiom 3: No Volatile State

The memory system is explicitly forbidden from storing data that changes frequently with time or across sessions: current timestamps, temporary session IDs, running PIDs, specific absolute paths, or connected device information. This prevents the memory from becoming stale and misleading — a form of temporal hallucination.

### Axiom 4: Minimum Sufficient Pointer

Each layer stores only the shortest identifier needed to locate information in the layer below. "One word too many is redundancy." This enforces a pointer-chasing discipline: L1 stores a keyword that points to L2, L2 stores a section reference that points to L3, and L3 contains the actual operational detail.

Sources: [memory\_management\_sop.md](memory/memory_management_sop.md#L1-L15)

## The Four-Layer Memory Architecture

The memory system implements a **progressive disclosure** architecture, where each layer trades precision for brevity. The agent never loads everything into context — it navigates from the sparsest index down to the densest detail only when triggered by task relevance.

| Layer | File | Purpose | Size Constraint | Read Frequency |
| --- | --- | --- | --- | --- |
| **L0** | `memory_management_sop.md` | Constitutional meta-rules | Unbounded (rarely read in full) | Before any memory write |
| **L1** | `global_mem_insight.txt` | Existence pointers + behavioral RULES | ≤ 30 lines, < 1K tokens (hard) | Every agent turn |
| **L2** | `global_mem.txt` | Environment-specific facts | Grows with environment | On demand per scenario |
| **L3** | `memory/*.md`, `memory/*.py` | Task-level SOPs and utility scripts | Per-file, as short as possible | On demand, per-SOP reference |
| **L4** | `L4_raw_sessions/` | Historical session archives | Managed by compression scheduler | Rarely, for context recovery |

The L1 layer is the most critical design artifact. It is loaded into every agent turn's system prompt, so every token counts. Its structure contains two mapping tiers: a **high-frequency tier** with direct `key → SOP/file` mappings, and a **low-frequency tier** that lists only keywords requiring the agent to `read L2` or `ls L3` to self-navigate. Appended to these mappings is a `[RULES]` section encoding compressed behavioral guardrails — red-line rules (fatal violations that kill processes), covert rules (silent wrong-result producers), and high-frequency error points.

Sources: [memory\_management\_sop.md](memory/memory_management_sop.md#L16-L41)

## Information Classification Decision Tree

Every piece of information the agent encounters must pass through a deterministic classification before storage. This prevents knowledge pollution and ensures each layer maintains its designated granularity.

This decision tree is the operational translation of the four axioms. It ensures that only action-verified, environment-specific, or hard-won knowledge persists — and that it lands in the correct layer on first write, avoiding costly migration later.

Sources: [memory\_management\_sop.md](memory/memory_management_sop.md#L71-L90)

## L1 ↔ L2/L3 Synchronization Protocol

When the lower layers change, L1 must be updated — but with extreme caution. The synchronization rules form a state machine that governs what changes propagate upward.

| Lower-Layer Event | L1 Synchronization Action |
| --- | --- |
| L2/L3 **new scenario** added | Default to low-frequency → add filename to L3 list (self-explanatory names get no annotation; only counter-intuitive scenarios get parenthetical trigger words) |
| L2/L3 **scenario deleted** | Remove the corresponding keyword/mapping line from L1 |
| L2/L3 **value modified** | If the modification doesn't affect scenario discoverability → leave L1 untouched |
| **Universal pitfall pattern** discovered | Compress to a single sentence → add to `[RULES]` section |

The synchronization red line is absolute: **L1 stores only keywords and names. Never copy details upward.** Every modification to L1 must be evaluated for both token cost and index utility. The `memory_cleanup_sop.md` provides the operational procedures for performing this curation safely.

Sources: [memory\_management\_sop.md](memory/memory_management_sop.md#L60-L68)

## Memory Cleanup SOP: Existence Encoding and ROI Curation

The `memory_cleanup_sop.md` operationalizes the compression of L1 through a principle called **existence encoding**. The insight is that the LLM itself is a compression engine — L1 only needs to make the agent *aware that a class of knowledge exists*, and it will autonomously retrieve the deep content via tool calls when triggered. L1's essence is: **use the fewest words to express what scenario has what memory available.**

### The ROI Formula

Every entry in L1 consumes tokens on every agent turn. The cleanup SOP defines a strict ROI calculation:

**ROI = (probability of error without these words × cost of error) / tokens per turn**

Only entries where this ratio exceeds the threshold survive curation. This transforms the subjective question "is this worth remembering?" into an evaluable metric.

### The Four Compression Principles

1. **Self-explanatory naming > annotations**: If an SOP filename communicates its purpose, L1 adds no description. Renaming the SOP often has higher ROI than adding L1 annotations.
2. **Minimal set description**: Multiple related entries covered by a single superordinate scenario should be collapsed. E.g., `qq操作/飞书操作/企微操作` → `im操作:*_im_sop`.
3. **Entry = scenario ↔ existence of solution**: Each line encodes a scenario trigger word (left) and a solution existence pointer (right). Parenthetical content is reserved **exclusively** for counter-intuitive trigger words — translations, content descriptions, and implementation details are waste.
4. **Layered placement**: Entries with behavioral rules or high-frequency/high-ROI value go in the upper scenario rows. Pure existence pointers sink to the L2/L3 flat list.

### The Curation Workflow

The cleanup follows a strict four-step process: (1) read L1 line by line, classify each fragment as pointer/RULE/translation/description/detail/redundancy; (2) audit RULES — global high-ROI stays, scenario-specific or low-risk rules demote to L3 or delete; (3) audit pointers — verify each expresses a scenario↔existence mapping, strip non-counter-intuitive annotations; (4) verify L3 filenames are self-explanatory, confirm total lines ≤ 30. The red line is stark: **memory modification is persistent damage, errors compound every turn. L1 permits only word-level patches; overwrites are forbidden.**

Sources: [memory\_cleanup\_sop.md](memory/memory_cleanup_sop.md#L1-L38)

## Plan Mode SOP: Structured Multi-Step Execution

The `plan_sop.md` is the most elaborate SOP in the system — a 263-line procedural framework governing how the agent handles complex tasks requiring 3+ dependent steps, multi-file coordination, conditional branching, or parallel execution. It implements a **four-phase state machine**: Exploration → Planning → Execution → Verification, with explicit gates between each transition.

Key architectural decisions in the plan SOP:

* **Exploration phase** uses subagents exclusively for environment probing. The main agent's context is the scarcest resource — long probe outputs displace planning capacity. The main agent creates directories, reads SOP indexes, launches subagents, and reads conclusions only.
* **Delegation markers** (`[D]`) are assigned during planning: any step requiring >3 files, >100 lines of reading, 3+ repetitive operations, or test/build analysis must be delegated to a subagent.
* **The verification phase** is **mandatory and adversarial**. An independent subagent is spawned with no access to the implementation context — it receives only task description, plan path, and deliverables list. Its job is to *disprove* the deliverables work, following the verify SOP's structured methodology.
* **Fix loops** are bounded: at most 2 FAIL→fix→reverify cycles before escalating to the user.

Sources: [plan\_sop.md](memory/plan_sop.md#L1-L263)

## Verify SOP: Adversarial Quality Assurance

The `verify_sop.md` defines the verification protocol that plan mode's final phase enforces. It is explicitly designed to counter two LLM-specific failure modes: **verification avoidance** (finding excuses not to run things — reading code instead of executing, writing PASS without evidence) and **the 80% illusion** (seeing passing tests and declaring success while half the functionality is hollow stubs).

### The Three Iron Laws

1. **Must execute.** Everything that can run must run; everything that can be screenshotted must be screenshotted.
2. **Must have tool evidence.** A PASS without tool output is a SKIP.
3. **Independent verification.** The implementer is also an LLM — its tests may be entirely mocked happy paths. Test suites are context, not evidence.

### Verification Strategy by Deliverable Type

| Deliverable Type | Required Actions |
| --- | --- |
| Web/Frontend | Open + screenshot → console errors → curl sub-resources for non-hollow confirmation |
| Script/CLI | Execute → check stdout/stderr/exit code → re-run with boundary inputs |
| Data files | Format validation → row count → spot-check first/middle/last 3 entries |
| API/Service | Call endpoint → verify response shape (not just 200) → test error inputs |
| Config/Docs | file\_read full content → format/syntax → verify no destruction of existing content |
| Bug fixes | Reproduce original bug → verify fix → regression test |
| Batch operations | Total count → spot-check first/middle/last → check for duplicates/omissions |

Every verification must include at least one **adversarial probe** (boundary values, idempotency checks, missing dependencies, orphan IDs) — otherwise only the happy path is confirmed. The output is a structured table with columns: `  
Sources: [verify\_sop.md](memory/verify_sop.md#L1-L65)

## Subagent Orchestration SOP

The `subagent.md` SOP defines how the main agent delegates work to child agent processes. Subagents are full agent instances (launched via `python agentmain.py --task {name}`) sharing the filesystem but operating in independent context windows. This isolation is the architectural solution to context pollution.

The file-IO protocol is explicit: subagents communicate through `temp/{task_name}/output.txt` (appended, with `[ROUND END]` as round boundary) and receive instructions via `input.txt`. The main agent can intervene mid-execution using three control files: `_stop` (terminate after current round), `_keyinfo` (inject working memory), and `_intervene` (append instructions).

Two primary orchestration patterns exist:

* **Test Mode**: Launch a subagent with a task goal but no SOP hints, observe whether it autonomously navigates to the correct SOP via L1. This is used for **meta-testing the memory system itself** — validating that the insight index actually enables skill discovery.
* **Map Mode**: Distribute N independent, isomorphic subtasks to N subagents for parallel processing. The key advantage is **context isolation** — processing document A's long context doesn't degrade processing quality for document B.

The Map pattern's constraint is that shared resources (keyboard, mouse, browser tabs) cannot be parallelized. Only independent file-system operations and compute tasks are safe for concurrent subagent execution.

Sources: [subagent.md](memory/subagent.md#L1-L62)

## Autonomous Operation and Scheduled Task SOPs

These two SOPs enable **time-gated, self-directed execution** — the agent operating without real-time user oversight.

The **autonomous operation SOP** (`autonomous_operation_sop.md`) governs how the agent selects, executes, and reports on self-assigned tasks. Task selection follows the value formula: **"Cannot be covered by AI training data" × "Persistent benefit for future collaboration."** Execution is bounded to ≤30 turns with a mandatory three-part closure: (1) re-read the SOP, (2) write a report to `./autonomous_reports/`, (3) call `complete_task()` to archive the report, record history, and mark the TODO. Permission boundaries are clearly delineated: read-only probing and cwd-internal experiments require no approval, while modifying `global_mem`/SOPs, installing software, or external API calls require deferral to a user review report.

The **scheduled task SOP** (`scheduled_task_sop.md`) provides cron-like scheduling through JSON task definitions in `../sche_tasks/`. The `reflect/scheduler.py` module polls every 60 seconds, checking `enabled` status, schedule time, and cooldown (based on the most recent report timestamp in `done/`). Task definitions support `daily`, `weekday`, `weekly`, `monthly`, `once`, `every_Nh`, and `every_Nd` repeat modes, with a configurable `max_delay_hours` (default 6) to suppress stale task execution.

Sources: [autonomous\_operation\_sop.md](memory/autonomous_operation_sop.md#L1-L44), [scheduled\_task\_sop.md](memory/scheduled_task_sop.md#L1-L27)

## Domain-Specific SOPs: Browser, Vision, Input, and Systems

The remaining SOPs encode hard-won operational knowledge for specific domains. Each follows the L3 convention: minimal prose, maximum pitfall density.

### TMWebDriver SOP (`tmwebdriver_sop.md`)

The most extensive domain SOP (122 lines), governing browser control through Chrome DevTools Protocol. It documents the CDP bridge architecture, `isTrusted` event limitations, coordinate transformation formulas (logical → physical pixel conversion with DPI scaling), iframe penetration strategies (including closed Shadow DOM via `DOM.getDocument({depth:-1, pierce:true})`), autofill value extraction, and a prioritized connection troubleshooting sequence. The batch command system (`$N.path` result chaining) and cross-tab operations without foregrounding are particularly noteworthy patterns.

### Vision SOP (`vision_sop.md`)

A strict 24-line SOP with three absolute pre-rules: (1) always enumerate windows via `pygetwindow` before any vision call, (2) **never capture full-screen** — prefer window region, prefer window region over screenshot, vision is last resort, (3) prefer local OCR (`ocr_utils.py`) or window title over vision API. It includes the bootstrap procedure for generating `vision_api.py` from the template, with a ModelScope API fallback.

### ljqCtrl SOP (`ljqCtrl_sop.md`)

Covers physical coordinate conversion for high-DPI environments. The core formula `physical = logical / ljqCtrl.dpi_scale` and the mandatory `activate()` call before any mouse/keyboard operation are the two critical patterns. It documents the subtle trap where `win32gui.GetWindowRect` returns logical coordinates while screenshots are in physical pixels.

### GitHub Contribution SOP (`github_contribution_sop.md`)

A complete PR lifecycle SOP: fork → branch → implement (minimal changes, one logical commit per change point) → test (hard gate: untested PR = unverified PR) → push → CI → review → merge. It includes a state machine for follow-up cycles and a common-mistakes anti-pattern table.

Sources: [tmwebdriver\_sop.md](memory/tmwebdriver_sop.md#L1-L122), [vision\_sop.md](memory/vision_sop.md#L1-L24), [ljqCtrl\_sop.md](memory/ljqCtrl_sop.md#L1-L46), [github\_contribution\_sop.md](memory/github_contribution_sop.md#L1-L118)

## Process Memory Scanner SOP

The `procmem_scanner_sop.md` governs the use of `procmem_scanner.py` — a Windows-specific tool for scanning process virtual memory using both hex pattern matching (Cheat Engine style) and string search, with an LLM-enhanced mode that returns structured JSON with surrounding byte context.

The SOP documents the **CE-style differential scanning** technique for locating dynamic memory fields in self-drawn UI applications (e.g., WeChat session titles). The workflow uses three contacts A/B/C to converge: full scan on A → switch to B → read original addresses to filter → switch back to A → read remaining candidates → confirm. Critical pitfall: **never re-scan after switching** — only read the original address set, because dynamic addresses change and a new scan will find only static residue.

Sources: [procmem\_scanner\_sop.md](memory/procmem_scanner_sop.md#L1-L82), [procmem\_scanner.py](memory/procmem_scanner.py#L1-L120)

## The Keychain Utility: Secure Secret Storage

The `keychain.py` module provides a file-based secret storage mechanism that the memory system references but never reads into LLM context. Secrets are stored in `~/ga_keychain.enc`, XOR-encrypted with a user-specific key derived from `sha256(os.getlogin() + "@ga_keychain")`. The `SecretStr` class ensures that printing a secret always shows a masked preview (e.g., `SecretStr(api_key=sk-1a2···x9z len=40)`) with the explicit directive `# .use() to get raw, do not print raw value`. This aligns with the constitutional axiom: **key files are referenced, never read or moved**.

Sources: [keychain.py](memory/keychain.py#L1-L47), [insight\_fixed\_structure.txt](assets/insight_fixed_structure.txt#L4-L9)

## SOP Inventory and Scope Reference

The following table provides a complete inventory of all SOPs in the memory system, their trigger conditions, and their primary function — serving as a quick-reference map for developers navigating the system.

| SOP File | Trigger Condition | Primary Function | Lines |
| --- | --- | --- | --- |
| `memory_management_sop.md` | Before any memory write | Constitutional axioms + layer architecture | 90 |
| `memory_cleanup_sop.md` | L1 curation cycles | Existence encoding + ROI-based compression | 38 |
| `plan_sop.md` | 3+ step tasks with dependencies | Four-phase structured execution (Explore→Plan→Execute→Verify) | 263 |
| `verify_sop.md` | Plan mode verification phase | Adversarial deliverable validation | 65 |
| `subagent.md` | Any delegation scenario | Subagent launch, communication, and intervention protocol | 62 |
| `autonomous_operation_sop.md` | Self-directed task execution | Task selection, bounded execution, and report archival | 44 |
| `scheduled_task_sop.md` | Cron-triggered tasks | JSON task definition + scheduler integration | 27 |
| `tmwebdriver_sop.md` | Browser interaction | CDP bridge, coordinate transforms, DOM penetration | 122 |

When extending the system with a new domain capability, the correct pattern is: (1) write a minimal L3 SOP, (2) index the filename in L1 only if the trigger scenario is counter-intuitive, (3) run a Test Mode subagent to validate the insight index enables autonomous discovery, (4) only then mark the capability as operational.---

For the architectural context of how these SOPs integrate into the broader agent loop, see [Memory Hierarchy Design](/17-memory-hierarchy-design) . To understand how L4 session archives are compressed and queried, see [L4 Session Archive Compression](/18-l4-session-archive-compression) . For the skill crystallization process that creates new SOPs from operational experience, see [Skill Crystallization Process](/20-skill-crystallization-process) .

|  |  |  |  |
| --- | --- | --- | --- |
| `vision_sop.md` | Visual information needed | Window enumeration, screenshot discipline, API bootstrap | 24 |

|  |  |  |  |
| --- | --- | --- | --- |
| `web_setup_sop.md` | Initial web toolchain setup | Chrome extension installation and connectivity verification | 25 |

|  |  |  |  |
| --- | --- | --- | --- |
| `ljqCtrl_sop.md` | Physical mouse/keyboard input | DPI coordinate conversion and window activation | 46 |

|  |  |  |  |
| --- | --- | --- | --- |
| `github_contribution_sop.md` | Open-source PR submission | Fork-to-merge lifecycle with CI integration | 118 |

|  |  |  |  |
| --- | --- | --- | --- |
| `procmem_scanner_sop.md` | Process memory inspection | Hex/string scanning + CE differential technique | 82 |

|  |  |  |  |
| --- | --- | --- | --- |
| `skill_search/SKILL.md` | Skill discovery from 105K+ cards | Semantic search API with scoring and filtering | 64 |

Memory Management SOPs | lsdefine/GenericAgent | Zread---

<!-- Page 18: https://zread.ai/lsdefine/GenericAgent/20-skill-crystallization-process -->

# Skill Crystallization Process

Level: Intermediate

How GenericAgent converts raw operational experience into structured, reusable knowledge — transforming ad-hoc problem-solving into permanent capability. This page traces the full pipeline from experience capture through autonomous reflection to persistent memory formation, explaining the self-evolution mechanism that makes the agent progressively more competent over time.

## The Crystallization Pipeline — From Chaos to Structure

Skill crystallization in GenericAgent is not a single mechanism but a **multi-stage pipeline** that converts ephemeral conversational traces into durable, queryable knowledge. The process follows a strict hierarchy: raw experience is archived, reflected upon autonomously, distilled into actionable artifacts, and finally indexed for future retrieval. Each stage has explicit quality gates — nothing becomes "memory" without passing through tool-verified execution and adversarial review.

The core value proposition is captured by the formula embedded in the task planning SOP: **"AI training data cannot cover × persistent value for future collaboration"**. This formula acts as a filter — only discoveries that are both non-obvious (not in the model's training set) and durably useful survive the crystallization process <memory/autonomous_operation_sop/task_planning.md#L4-L5>.

## Stage 1 — Experience Capture via L4 Session Archiving

Every conversational session generates a `model_responses_*.txt` file in `temp/`. These raw traces are the crude ore from which skills are eventually refined. The `compress_session.py` module in `memory/L4_raw_sessions/` processes these files on a 12-hour cron cycle triggered by the scheduler <reflect/scheduler.py#L63-L74>.

The compression pipeline handles two session formats. **Format A (JSON)** is kept as-is since it already carries structured metadata. **Format B (Raw)** undergoes aggressive stripping: system prompts between `=== Prompt ===` and `=== USER ===` markers are removed, and `=== ASSISTANT ===` echo blocks are discarded entirely, since they duplicate information already in `=== Response ===` sections <memory/L4_raw_sessions/compress_session.py#L70-L85>. Sessions under 4.5 KB after compression are discarded as too small to contain useful signal, and files modified within the last 2 hours are skipped to avoid processing in-progress sessions <memory/L4_raw_sessions/compress_session.py#L59-L60>, <memory/L4_raw_sessions/compress_session.py#L169>.

Each compressed session is named by timestamp range (e.g., `0403_2013-0403_2215.txt`) and stored in the L4 archive. A parallel extraction process pulls `[USER]`/`[Agent]` dialogue pairs from `<history>` blocks, deduplicates them via suffix-overlap merging, and appends them to `all_histories.txt` — creating a searchable cross-session dialogue corpus <memory/L4_raw_sessions/compress_session.py#L127-L142>.

| Phase | Operation | Filter/Threshold | Output |
| --- | --- | --- | --- |
| Detect format | JSON vs Raw by first Prompt marker content | — | Format label |
| Compress | Strip system prompts (Format B) or keep (Format A) | Min 4.5 KB post-compress | `MMDD_HHMM-MMDD_HHMM.txt` |
| Extract history | Parse `<history>` blocks, merge sliding windows | Dedup via suffix overlap | `all_histories.txt` entries |
| Archive | Move to L4 directory, skip recent/duplicate files | 2-hour freshness, duplicate session names | Permanent archive |

## Stage 2 — Autonomous Reflection Trigger

The reflection mechanism is deliberately minimal. `reflect/autonomous.py` contains just three lines of runtime logic: a 30-minute interval check (`INTERVAL = 1800`) and a trigger function that injects a prompt instructing the agent to read the autonomous SOP and execute pending tasks <reflect/autonomous.py#L1-L6>. This trigger is consumed by the main `agentmain.py` reflect loop, which loads the script module dynamically, polls `check()` at the configured interval, and enqueues any non-None return value as a task <agentmain.py#L218-L234>.

The design philosophy is significant: **the reflect script is a thin trigger, not a controller**. All decision-making about what to do, how to prioritize, and how to execute resides in the SOP documents read by the agent itself. This keeps the reflection infrastructure stateless and hot-reloadable — if the SOP files change on disk, the agent's next reflective cycle automatically picks up the updated procedures.

The reflect loop in `agentmain.py` watches the script file's `mtime` and reloads the module on change, enabling live updates to reflection behavior without restarting the agent process. This is visible in the `while True` loop at [agentmain.py#L225-L227](agentmain.py#L225-L227).

## Stage 3 — Task Planning and Value Filtering

When no pending TODOs exist, the agent enters **planning mode** rather than executing blindly. This is a critical quality gate that prevents low-value busywork. The planning SOP mandates a deeply self-critical process <memory/autonomous_operation_sop/task_planning.md#L10-L19>:

1. **Critique history**: Read `history.txt` to identify failure *patterns*, not to replicate past tasks. The SOP explicitly warns that 90% of historical tasks are low-value — the purpose is anti-pattern recognition.
2. **Reflect on causes**: Why were past tasks low-value? Common anti-patterns include shallow validation, assumption-free inspection tours, repetitive exploration, and generic tool documentation.
3. **Inventory existing assets**: Review reports and memory files to identify underutilized knowledge or improvement opportunities.
4. **Generate 5-7 TODOs** following the format: `[ ] type(produce/explore/env) | one-line goal | acceptance criteria`.
5. **Subagent review**: A subagent independently scores each TODO 1-10 with justification. Low-scored items are deleted or replaced.

The value hierarchy — from highest to lowest — prioritizes **practical capability expansion** (writing tools that unlock new ability nodes in the capability tree), followed by environment discovery (finding unused tools/libraries), niche tool evaluation, user preference analysis, self-improvement proposals, and finally memory auditing <memory/autonomous_operation_sop/task_planning.md#L21-L27>. A critical rule: **planning mode ends immediately after writing TODOs** — execution must wait for the next autonomous cycle, preventing impulsive task selection <memory/autonomous_operation_sop/task_planning.md#L19>.

## Stage 4 — Structured Execution with Verification

Task execution operates under strict constraints designed to maximize signal-to-noise in the output. The autonomous SOP enforces a **30-turn limit** per task with "small steps, fast iteration" methodology <memory/autonomous_operation_sop.md#L27-L30>. Hypotheses must be validated with temporary scripts before writing conclusions — read-only inspection is explicitly forbidden as a basis for claims. Even failed experiments produce valuable reports documenting what was tried and why it failed.

The execution lifecycle is managed by four functions in `helper.py` <memory/autonomous_operation_sop/helper.py#L7-L10>:

| Function | Purpose | Key Behavior |
| --- | --- | --- |
| `get_todo()` | Read pending tasks from `TODO.txt` | Returns content or hint if file missing |
| `get_history(n)` | Retrieve last *n* history entries | Newest first, default 20 |
| `set_todo()` | Return absolute path to `TODO.txt` | Agent reads/writes TODO independently |
| `complete_task(taskname, historyline, report_path)` | Finalize task with 3 side-effects | Auto-number report, move to archive, prepend history, return TODO-update instruction |

The `complete_task()` function is the crystallization checkpoint. It performs three atomic operations: (1) scans `history.txt` for the maximum `RXX` report number and increments it, (2) moves the completed report from the working directory into `temp/autonomous_reports/` with the new number prefix, and (3) prepends a one-line history entry in the format `type | topic | conclusion` <memory/autonomous_operation_sop/helper.py#L64-L135>.

**Permission boundaries** are explicitly tiered. Read-only exploration and working-directory writes require no approval. Writing proposals for global memory or SOP changes, installing software, calling external APIs, or deleting non-temporary files must be documented in reports awaiting user review. Reading key files or modifying core code is absolutely forbidden <memory/autonomous_operation_sop.md#L38-L42>.

## Stage 5 — Adversarial Verification

Before any completed task's output is accepted, GenericAgent can invoke an **independent verification subagent** — a separate LLM instance with no access to the execution context, whose sole job is to prove the deliverables *don't* work. This addresses a fundamental problem identified in `verify_sop.md`: the agent has two failure modes — **verification avoidance** (finding excuses not to run tests) and **being fooled by the first 80%** (assuming passing initial tests means everything works) <memory/verify_sop.md#L1-L4>.

The verification SOP enforces three iron rules: must execute (reading code is not verification), must produce tool output evidence (no tool output = no PASS), and must verify independently (the implementer's tests are considered potentially biased since both are LLMs) <memory/verify_sop.md#L10-L15>. Verification actions are calibrated by artifact type — web artifacts require screenshots and console error checks, scripts require boundary input testing, data files require format validation and sampling, and API services require response shape verification beyond HTTP 200 <memory/verify_sop.md#L29-L39>.

The verdict is one of three literal strings: `VERDICT: PASS`, `VERDICT: FAIL`, or `VERDICT: PARTIAL` (the last only when environmental constraints prevent full verification) <memory/verify_sop.md#L62-L65>.

## Stage 6 — Memory Integration and the L1↔L3 Sync Protocol

Approved insights flow into the **layered memory system** governed by `memory_management_sop.md`, which acts as the constitutional document (META-SOP, L0) for all memory operations <memory/memory_management_sop.md#L1-L9>.

The system enforces a strict **Action-Verified Only** axiom: nothing enters memory unless it was confirmed by a successful tool call. Model priors, unverified hypotheses, and unexecuted plans are categorically excluded <memory/memory_management_sop.md#L2-L5>. A second axiom — **Sanctity of Verified Data** — ensures that once information survives the verification gate, it can be compressed or moved between layers but never deleted for accuracy loss <memory/memory_management_sop.md#L6-L9>.

The four-layer hierarchy determines where crystallized knowledge lands:

| Layer | Location | Token Budget | Content Type | Update Trigger |
| --- | --- | --- | --- | --- |
| L0 | `memory/memory_management_sop.md` | N/A (governance) | Meta-rules for memory ops | Manual / user review |
| L1 | `global_mem_insight.txt` | ≤30 lines, <1K tokens | Scene keywords → memory pointers; RULES | On L2/L3 add/delete |
| L2 | `memory/global_mem.txt` | Elastic | Environment facts, paths, credentials | On environment change |
| L3 | `memory/*.md, *.py` | Per-file minimal | Task-specific SOPs, utility scripts | On verified discovery |

The decision tree for placing new information is deterministic: environment-specific facts → L2, universal operating principles → L1 RULES section, task-specific techniques that required painful discovery → L3, and anything a competent model could already reason about → discarded entirely <memory/memory_management_sop.md#L71-L89>.

The `start\_long\_term\_update` tool in the schema serves as the explicit crystallization trigger. It is designed to be called when the agent discovers information "worth remembering" — environment facts, user preferences, or lessons learned — and is mandatory after any task exceeding 15 conversation turns [assets/tools\_schema.json#L68-L72](assets/tools\_schema.json#L68-L72).

## Skill Search — Querying the Crystallized Knowledge Base

Once skills are crystallized into SOPs and scripts, they need to be **discoverable**. The `skill_search` module provides semantic search over 105K+ pre-indexed skill cards via a remote API, allowing the agent to find relevant procedural knowledge on demand <memory/skill_search/SKILL.md#L1-L3>.

The search engine (`engine.py`) is a zero-dependency API client that automatically detects the local environment — OS, shell, available runtimes (Python, Node, Go, Rust, etc.), and installed tools (git, docker, kubectl, etc.) — and sends this context alongside the query to improve relevance ranking <memory/skill_search/skill_search/engine.py#L105-L109>. Each `SkillIndex` result carries rich metadata including safety attributes (`autonomous_safe`, `blast_radius`, `data_exposure`), quality scores (`clarity`, `completeness`, `actionability`), and platform compatibility data <memory/skill_search/skill_search/engine.py#L8-L39>.

The composite quality score is weighted toward actionability: `clarity × 0.3 + completeness × 0.3 + actionability × 0.4` <memory/skill_search/skill_search/engine.py#L42-L43>. This bias ensures that theoretically complete but impractical skills rank below concise, immediately executable ones — a design choice that reinforces the system's preference for actionable knowledge over encyclopedic documentation.

## The Scheduled Reflection Layer

Beyond user-inactivity triggers, GenericAgent supports **cron-based scheduled tasks** through `reflect/scheduler.py`. This module scans `sche_tasks/` for JSON task definitions and triggers them based on schedule time, repeat interval, and cooldown windows <reflect/scheduler.py#L62-L129>.

The scheduler implements several protective mechanisms: a **max delay window** (default 6 hours) prevents stale tasks from firing if the system was offline at the scheduled time [reflect/scheduler.py#L29](reflect/scheduler.py#L29-L29), weekday-only tasks automatically skip weekends, and cooldown tracking via done-file timestamps prevents duplicate execution. A port lock on `127.0.0.1:45762` prevents multiple scheduler instances from running simultaneously <reflect/scheduler.py#L6-L9>. The L4 archive compression runs as a silent background cron every 12 hours, independent of the task scheduling system <reflect/scheduler.py#L64-L74>.

## Putting It All Together

The skill crystallization process embodies a core architectural insight: **an agent's long-term capability is proportional to the quality of its distilled experience, not the quantity of its raw interactions**. Every mechanism in this pipeline — from the 4.5 KB minimum archive size to the adversarial verification subagent to the Action-Verified Only axiom — exists to prevent noise from diluting the knowledge base.

For developers extending GenericAgent, the key integration points are: writing new SOPs for `memory/` (L3), proposing updates to `memory_management_sop.md` (L0) for new memory categories, and contributing skill cards to the 105K+ search index. To understand how tasks flow through the agent loop during autonomous execution, see [Agent Loop and Task Runner](/9-agent-loop-and-task-runner) . For the broader memory architecture, see [Memory Hierarchy Design](/17-memory-hierarchy-design) . For the scheduled task infrastructure, continue to [Autonomous Task Management](/21-autonomous-task-management) .---

<!-- Page 19: https://zread.ai/lsdefine/GenericAgent/21-autonomous-task-management -->

# Autonomous Task Management

Level: Advanced

GenericAgent's autonomous task management is a multi-layered system that enables the agent to perform unsupervised work during user absence, execute cron-scheduled tasks, and self-manage a TODO backlog with full audit trails. The architecture separates **trigger mechanisms** (when to act) from **behavioral protocols** (how to act), connected through a generic reflection loop that any polling script can plug into.

## Reflect Loop: The Universal Trigger Engine

All autonomous behavior originates from a single polling mechanism in `agentmain.py`. When launched with `--reflect <script_path>`, the agent enters a dedicated mode that repeatedly invokes the script's `check()` function at a configurable `INTERVAL`, injecting any non-`None` return value as a task prompt into the agent loop ([agentmain.py](agentmain.py#L218-L248)).

The reflection loop implements three critical safeguards: **hot-reload** (detecting file modification timestamps and re-executing the module on change), **sequential execution** (blocking until the current task's `'done'` signal arrives before polling again), and  (appending results to ). The  module attribute, when set to , causes the loop to terminate after a single trigger — useful for one-shot scripts ().

**persistent logging**

`temp/reflect_logs/{script}_{date}.log`

`ONCE`

`True`

[agentmain.py](agentmain.py#L224-L248)

The `launch.pyw` entry point wires two reflect-capable subsystems: the **idle monitor** (an in-process thread that injects the autonomous prompt after 30 minutes of user inactivity) and the **scheduler** (a separate `agentmain.py --reflect reflect/scheduler.py` process, gated by a TCP port lock on `127.0.0.1:45762` to prevent duplicate instances) ([launch.pyw](launch.pyw#L50-L114)).

## Two Autonomous Trigger Modes

GenericAgent supports two complementary autonomous activation strategies, each implemented as a reflect-compatible script with the `check()` → `str | None` interface.

### Idle Detection

The simplest trigger monitors user absence. `reflect/autonomous.py` is a 6-line module that returns a fixed prompt instructing the agent to read the autonomous SOP and execute pending tasks ([reflect/autonomous.py](reflect/autonomous.py#L1-L6)). In practice, this is consumed by `launch.pyw`'s `idle_monitor()` thread, which polls the Streamlit frontend's `#last-reply-time` element every 5 seconds and, once the gap exceeds 1800 seconds (30 minutes), injects the autonomous prompt directly into the chat input via DOM manipulation — bypassing the reflect loop entirely for lower latency ([launch.pyw](launch.pyw#L50-L63)).

The idle monitor enforces a 120-second cooldown between triggers (`last_trigger_time`), preventing the agent from re-entering autonomous mode while still processing the previous session ([launch.pyw](launch.pyw#L56-L57)).

### Cron Scheduler

`reflect/scheduler.py` implements a full-featured cron engine that polls `sche_tasks/*.json` every 120 seconds ([reflect/scheduler.py](reflect/scheduler.py#L11-L12)). Each JSON task definition supports six fields:

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| `schedule` | `HH:MM` | required | Target execution time |
| `repeat` | string | `"daily"` | Frequency policy: `daily`, `weekday`, `weekly`, `monthly`, `once`, `every_Nh`, `every_Nm`, `every_Nd` |
| `enabled` |

The scheduler evaluates five conditions before triggering: enabled flag, current time ≥ schedule, weekday filter (for `weekday` repeat), execution window (`max_delay_hours`), and cooldown (derived from repeat policy with a slight undershoot to prevent drift — e.g., `daily` uses a 20-hour cooldown rather than 24) ([reflect/scheduler.py](reflect/scheduler.py#L32-L49), [reflect/scheduler.py](reflect/scheduler.py#L76-L129)).

Upon trigger, the scheduler generates a prompt that references the `scheduled_task_sop.md`, includes the task prompt, and specifies a deterministic report path in `sche_tasks/done/YYYY-MM-DD_{tid}.md`. The existence of this done-file is how the scheduler determines last-run time for cooldown calculations ([reflect/scheduler.py](reflect/scheduler.py#L119-L129)).

The scheduler silently triggers L4 session archive compression every 12 hours via `compress\_session.batch\_process()` — this is not a user-facing task but a maintenance cron baked into the `check()` function ([reflect/scheduler.py](reflect/scheduler.py#L63-L74)).

A TCP port lock on `127.0.0.1:45762` provides singleton guarantee for the scheduler process. If the port is already bound, `agentmain.py` crashes immediately rather than running a duplicate scheduler — a fail-fast design choice documented explicitly in the source ([reflect/scheduler.py](reflect/scheduler.py#L4-L9)).

## The Autonomous Operation SOP: Behavioral Protocol

When the autonomous trigger fires, the agent receives a prompt directing it to read `memory/autonomous_operation_sop.md` — a structured behavioral protocol that governs every aspect of unsupervised execution ([memory/autonomous\_operation\_sop.md](memory/autonomous_operation_sop.md#L1-L44)).

The SOP defines a three-tier permission model that the agent must follow without user oversight:

|  |
| --- |
| bool |

|  |
| --- |
| `false` |

|  |
| --- |
| Master toggle |

|  |  |  |  |
| --- | --- | --- | --- |
| `prompt` | string | `""` | Task instructions injected into agent |

|  |  |  |  |
| --- | --- | --- | --- |
| `max_delay_hours` | float | `6` | Execution window after schedule time; tasks beyond this are skipped |

|  |  |  |  |
| --- | --- | --- | --- |
| *(implied)* `tid` | string | filename stem | Derived from JSON filename (e.g., `morning_digest.json` → `morning_digest`) |

| Permission Level | Examples | Agent Action |
| --- | --- | --- |

|  |  |  |
| --- | --- | --- |
| **No approval needed** | Read-only exploration, writes in cwd, script experiments | Execute freely |
| **Write report, await review** | Modifying `global_mem` or memory SOPs, installing software, external API calls, deleting non-temp files | Log in report, do not block |
| **Absolutely forbidden** | Reading API keys, modifying core codebase, irreversible destructive operations | Never attempt |

The SOP mandates a strict startup sequence: first, record a working checkpoint with the helper API's import path; second, call `get_history(40)` to avoid repeating past work; third, call `get_todo()` to find pending tasks ([memory/autonomous\_operation\_sop.md](memory/autonomous_operation_sop.md#L8-L21)). Task selection follows a value formula: **"what AI training data cannot cover" × "persistent value for future collaboration"**. The agent must never select the same sub-task twice consecutively ([memory/autonomous\_operation\_sop.md](memory/autonomous_operation_sop.md#L18-L21)).

Execution is bounded to ≤30 agent-turns per session. The SOP mandates "small steps, fast iterations" — hypothesis-driven experimentation with temporary scripts, never concluding from read-only observation alone. Even failed experiments must be documented in the report ([memory/autonomous\_operation\_sop.md](memory/autonomous_operation_sop.md#L24-L31)).

The three-step completion protocol is atomic and non-negotiable: (1) re-read the SOP, (2) write a report file, (3) call `complete_task()` to archive the report and update history, then manually mark the TODO item as `[x]` ([memory/autonomous\_operation\_sop.md](memory/autonomous_operation_sop.md#L32-L36)).

## Task Planning: From Exploration to TODO Backlog

When `TODO.txt` has no pending items, the agent enters **planning mode** rather than executing immediately — a separation that prevents the agent from inventing low-value tasks on the fly ([memory/autonomous\_operation\_sop/task\_planning.md](memory/autonomous_operation_sop/task_planning.md#L7-L19)).

The planning protocol is deliberately skeptical: the agent must critically read `history.txt` first, recognizing that "90% of historical tasks are low-value" — the purpose is to **identify failure patterns and avoid them**, not to imitate past behavior. Low-value patterns include shallow validations, aimless inspections, repetitive exploration, generic collections, and basic usage of well-known tools ([memory/autonomous\_operation\_sop/task\_planning.md](memory/autonomous_operation_sop/task_planning.md#L10-L14)).

The agent must produce 5–7 TODO items in the format `[ ] type | one-line goal | acceptance criteria`, then invoke a subagent to score each item 1–10 with minimal prior context (to avoid bias). Low-scoring items are deleted or replaced. The planning session ends immediately — execution is deferred to the next autonomous activation ([memory/autonomous\_operation\_sop/task\_planning.md](memory/autonomous_operation_sop/task_planning.md#L15-L19)).

Task priorities are explicitly ranked by value:

1. **Practical output & capability expansion** — tools that solve pain points or unlock new capability nodes
2. **Environment discovery** — scanning for underutilized tools, libraries, or data sources on the host
3. **Niche tool mining** — finding cold but practical tools from forums and communities
4. **User understanding & recommendations** — analyzing bookmarks, old code, and files for personalization (low frequency)
5. **Self-evolution** — reflecting on framework shortcomings and proposing improvements
6. **Memory audit** — correcting outdated or incorrect records ([memory/autonomous\_operation\_sop/task\_planning.md](memory/autonomous_operation_sop/task_planning.md#L21-L28))

Explicit exclusion zones include Hacker News, news headline scanning, and exploring frameworks inferior to GenericAgent's own stack ([memory/autonomous\_operation\_sop/task\_planning.md](memory/autonomous_operation_sop/task_planning.md#L39)).

## Helper API: The Task Lifecycle Contract

`memory/autonomous_operation_sop/helper.py` exposes a minimal four-function API that serves as the agent's interface to the task management filesystem ([memory/autonomous\_operation\_sop/helper.py](memory/autonomous_operation_sop/helper.py#L1-L11)):

| Function | Returns | Purpose |
| --- | --- | --- |
| `get_todo()` | `str` (TODO content) | Read current TODO backlog |
| `get_history(n=20)` | `str` (first n lines) | Read recent task history, newest first |
| `set_todo()` | `str` (absolute path) | Get TODO.txt path for direct read/write |
| `complete_task(taskname, historyline, report_path)` | `str` (result + instruction) | Atomic: move report → numbered archive, prepend history, return TODO update instruction |

The `complete_task()` function is the most critical — it performs an atomic three-step operation with rollback semantics ([memory/autonomous\_operation\_sop/helper.py](memory/autonomous_operation_sop/helper.py#L64-L132)):

1. **Archive the report**: moves the agent-written report file to `temp/autonomous_reports/R{XX}_{sanitized_name}.md`, where `XX` is auto-incremented by scanning `history.txt` for the highest existing `R`-prefixed number ([memory/autonomous\_operation\_sop/helper.py](memory/autonomous_operation_sop/helper.py#L93-L97))
2. **Prepend history**: strips any existing `R`-number or date prefix from the `historyline` (idempotent), then prepends `R{XX} | YYYY-MM-DD | {line}` to `history.txt` ([memory/autonomous\_operation\_sop/helper.py](memory/autonomous_operation_sop/helper.py#L106-L118))
3. **Return TODO instruction**: tells the agent which TODO entry to mark `[x] R{XX}` ([memory/autonomous\_operation\_sop/helper.py](memory/autonomous_operation_sop/helper.py#L128-L132))

If the history write fails, the function rolls back the report move — preserving filesystem consistency ([memory/autonomous\_operation\_sop/helper.py](memory/autonomous_operation_sop/helper.py#L120-L125)).

All file paths in the helper API are computed relative to the module's own `\_\_file\_\_` location via `Path(\_\_file\_\_).resolve().parent`, making the module portable regardless of the agent's current working directory. The canonical paths are: `temp/autonomous\_reports/` for archived reports, `temp/autonomous\_reports/history.txt` for history, and `temp/TODO.txt` for the task backlog ([memory/autonomous\_operation\_sop/helper.py](memory/autonomous\_operation\_sop/helper.py#L20-L26)).

## Scheduled Task SOP: The Cron Execution Protocol

Scheduled tasks follow a separate SOP (`memory/scheduled_task_sop.md`) distinct from the autonomous operation SOP. The critical difference is that scheduled task report paths are **determined by the scheduler** and injected into the prompt, whereas autonomous tasks generate their own temporary report files that `complete_task()` then archives ([memory/scheduled\_task\_sop.md](memory/scheduled_task_sop.md#L1-L27)).

The scheduled task SOP mandates that the agent's first action upon receiving a cron-triggered prompt is to call `update_working_checkpoint` with the report destination path — a safeguard against the agent forgetting the target file during long-running tasks ([memory/scheduled\_task\_sop.md](memory/scheduled_task_sop.md#L16-L17)).

## Integration Map

The autonomous task management system connects to several other subsystems documented elsewhere in this guide:

* The **Reflect Loop** feeds tasks into the same `put_task()` / `agent_runner_loop()` pipeline described in [Agent Loop and Task Runner](/9-agent-loop-and-task-runner)
* The L4 archive cron within the scheduler invokes `compress_session.batch_process()` from the [L4 Session Archive Compression](/18-l4-session-archive-compression)  system
* The `start_long_term_update` tool, available during autonomous sessions, triggers the [Skill Crystallization Process](/20-skill-crystallization-process)  for persisting discoveries
* The `update_working_checkpoint` tool used at task boundaries is part of the [Context Compression Strategy](/26-context-compression-strategy)
* The full scheduler capabilities including `health_check()` are covered in [Scheduled Reflection and Cron](/22-scheduled-reflection-and-cron)---

**Next**: To understand how scheduled tasks integrate with reflection and health monitoring, continue to [Scheduled Reflection and Cron](/22-scheduled-reflection-and-cron) . For the broader execution pipeline that autonomous tasks enter, revisit [Agent Loop and Task Runner](/9-agent-loop-and-task-runner) .

Autonomous Task Management | lsdefine/GenericAgent | Zread---

<!-- Page 20: https://zread.ai/lsdefine/GenericAgent/22-scheduled-reflection-and-cron -->

# Scheduled Reflection and Cron

Level: Advanced

GenericAgent implements a **plugin-based reflection architecture** that enables the agent to self-trigger tasks on a timed basis — either through cron-style scheduled tasks defined as JSON files, or through idle-detection mechanisms that activate when the user goes inactive. This system transforms the agent from a purely reactive tool into a semi-autonomous entity capable of periodic self-maintenance, memory archival, and proactive task execution. The architecture cleanly separates the *polling infrastructure* (in `agentmain.py`), the *trigger logic* (in `reflect/` modules), and the *task definitions* (as JSON files), allowing new reflection behaviors to be added as single-file Python modules with a prescribed interface.

## Reflection Runtime Architecture

The entire reflection subsystem is orchestrated through `agentmain.py`'s `--reflect` mode, which dynamically loads a Python script and polls its `check()` function at a configurable interval. The launch orchestrator in `launch.pyw` wires this together with a `--sched` flag, while a separate idle-monitor thread runs concurrently to detect user absence.

The critical architectural insight is that `agentmain.py` treats reflection scripts as **first-class plugin modules**. Any Python file exposing `INTERVAL` and `check()` can be loaded via `--reflect`, making the system extensible beyond the two built-in modules. The runtime polls `mod.INTERVAL` seconds between calls, hot-reloads the module when its file modification time changes, and supports both persistent (`ONCE=False`) and one-shot (`ONCE=True`) execution modes ([agentmain.py](reflect/../agentmain.py#L218-L248)).

Sources: [agentmain.py](agentmain.py#L218-L248), [launch.pyw](launch.pyw#L111-L114)

## The Reflect Plugin Interface

Every reflection module must conform to a minimal contract. The runtime expects two module-level attributes and one function:

| Attribute / Function | Type | Default | Description |
| --- | --- | --- | --- |
| `INTERVAL` | `int` | (required) | Seconds between successive `check()` polls |
| `ONCE` | `bool` | `False` | If `True`, the runtime exits after the first successful trigger |
| `check()` | `callable → str | None` | (required) | Called each cycle; returns a prompt string to inject as a task, or `None` to skip |
| `on_done(result)` | `callable → None` | (optional) | Callback invoked after the agent finishes processing the triggered task |

The runtime loads the module via `importlib.util.spec_from_file_location`, polls every `INTERVAL` seconds, and on each cycle detects file modifications to trigger a hot-reload without restarting the process ([agentmain.py](agentmain.py#L219-L227)). When `check()` returns a non-`None` string, the runtime calls `agent.put_task(task, source='reflect')` which enqueues the task into the agent loop's internal queue. The result is drained from a display queue with a 120-second timeout per turn, then written to `temp/reflect_logs/<script_name>_YYYY-MM-DD.log` ([agentmain.py](agentmain.py#L224-L244)).

Sources: [agentmain.py](agentmain.py#L219-L244)

## Cron Scheduler (`reflect/scheduler.py`)

The scheduler is the most feature-rich built-in reflection module, combining two distinct trigger mechanisms within a single `check()` function: a **hardcoded L4 archive cron** that runs silently every 12 hours, and a **file-based task scheduler** that evaluates JSON-defined tasks against schedule conditions.

### Singleton Enforcement via Port Lock

The scheduler employs a TCP port-binding technique to guarantee at most one instance runs at a time. On module load, it attempts to bind `127.0.0.1:45762` — if the bind fails (port already in use), `agentmain.py` crashes immediately, preventing duplicate schedulers from corrupting task state ([reflect/scheduler.py](reflect/scheduler.py#L4-L9)). The `try: _lock / except NameError:` guard ensures that on module hot-reload the existing `_lock` object in `mod.__dict__` is reused rather than attempting a second bind.

### L4 Archive Cron (Hardcoded)

Before scanning user-defined tasks, the scheduler checks whether 43200 seconds (12 hours) have elapsed since the last L4 archive run. If so, it dynamically imports `compress_session.batch_process` and executes it against the raw session directory at `temp/model_responses/`, with `dry_run=False` to perform actual compression, history extraction, and archiving ([reflect/scheduler.py](reflect/scheduler.py#L63-L74)). This serves as the [L4 Session Archive Compression](/18-l4-session-archive-compression)  layer's automated trigger — see that page for details on the four-phase batch process.

### User-Defined Task Evaluation

The file-based scheduler scans `sche_tasks/*.json` in the project root, evaluating each task against a five-condition gate:

**Condition 1 — Enabled gate**: Tasks must have `"enabled": true` in their JSON definition. Disabled tasks are silently skipped ([reflect/scheduler.py](reflect/scheduler.py#L89)).

**Condition 2 — Weekday filter**: If `repeat` is set to `"weekday"` and `now.weekday() >= 5` (Saturday or Sunday), the task is skipped for that cycle ([reflect/scheduler.py](reflect/scheduler.py#L100)).

**Condition 3 — Schedule time**: The task must have a `"schedule"` field in `HH:MM` format. The current time must be at or past the scheduled hour and minute ([reflect/scheduler.py](reflect/scheduler.py#L92-L103)).

**Condition 4 — Max delay window**: To prevent stale tasks from firing after a long system downtime (e.g., booting hours after a scheduled time), the scheduler computes how many minutes have elapsed since the scheduled time and compares it against `max_delay_hours` (defaulting to 6 hours). Tasks exceeding this window are logged and skipped ([reflect/scheduler.py](reflect/scheduler.py#L106-L112)).

**Condition 5 — Cooldown guard**: The scheduler looks in the `sche_tasks/done/` directory for previous execution reports matching the pattern `YYYY-MM-DD_HHMM_<task_id>.md`. It parses the most recent timestamp and compares it against a cooldown duration derived from the `repeat` field. This cooldown is intentionally set **shorter** than the actual repeat period to prevent timing drift — for example, a daily task uses a 20-hour cooldown rather than 24, allowing the task to trigger as soon as the next day's schedule time arrives ([reflect/scheduler.py](reflect/scheduler.py#L32-L49)).

Sources: [reflect/scheduler.py](reflect/scheduler.py#L62-L129)

### Task JSON Schema and Repeat Modes

Task definitions are placed as `*.json` files in the `sche_tasks/` directory at the project root. The schema follows this structure:

```
{
  "schedule": "08:00",
  "repeat": "daily",
  "enabled": true,
  "prompt": "Perform daily memory review and update global_mem_insight.txt",
  "max_delay_hours": 6
}
```

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `schedule` | `string` | Yes | Trigger time in `HH:MM` 24-hour format |
| `repeat` | `string` | Yes | Repeat cadence (see table below) |
| `enabled` | `bool` | Yes | Master toggle; `false` disables the task entirely |
| `prompt` | `string` | Yes | The task prompt injected into the agent when triggered |
| `max_delay_hours` | `int` | No | Maximum delay window in hours (default: 6) |

The `repeat` field supports the following cadences, each with an associated cooldown period calculated by `_parse_cooldown()`:

| Repeat Value | Cooldown Duration | Behavior |
| --- | --- | --- |
| `daily` | 20 hours | Triggers once per day, every day |
| `weekday` | 20 hours | Same as daily, but skips Saturday/Sunday |
| `weekly` | 6 days | Triggers once per week |
| `monthly` | 27 days | Triggers once per month |
| `once` | ~999999 days | Executes once, then effectively permanently disabled |
| `every_Nh` | N hours (e.g., `every_3h`) | Custom interval in hours |
| `every_Nm` | N minutes | Custom interval in minutes |
| `every_Nd` | N days | Custom interval in days |

Unknown repeat values fall back to a 20-hour cooldown with a warning logged to `scheduler.log` ([reflect/scheduler.py](reflect/scheduler.py#L48)).

Sources: [reflect/scheduler.py](reflect/scheduler.py#L32-L49), [memory/scheduled\_task\_sop.md](memory/scheduled_task_sop.md#L5-L10)

### Deduplication via Done Files

When a task triggers, the scheduler generates a report path in the format `sche_tasks/done/YYYY-MM-DD_HHMM_<task_id>.md` and injects this path directly into the prompt string returned to the agent ([reflect/scheduler.py](reflect/scheduler.py#L122-L129)). The agent is expected to write its execution report to this exact path. On subsequent evaluation cycles, `_last_run()` scans the `done/` directory for files matching `<task_id>.md` and extracts the most recent timestamp to determine whether the cooldown has elapsed ([reflect/scheduler.py](reflect/scheduler.py#L51-L60)).

This design creates a **file-based idempotency mechanism**: the scheduler never directly writes done markers — it relies entirely on the agent's successful report creation as proof of completion. If the agent fails mid-task, no done file is produced, and the task remains eligible for re-trigger on the next cycle.

\*\*Critical invariant\*\*: The done file naming convention uses the trigger timestamp (`YYYY-MM-DD\_HHMM`) rather than the schedule time. This means a task scheduled for `08:00` that actually triggers at `08:02` will produce `2026-06-15\_0802\_taskname.md`. The `\_last\_run()` parser extracts timestamps via `strptime(df[:15], '%Y-%m-%d\_%H%M')`, so the filename must strictly follow this 15-character prefix format for deduplication to work correctly.

Sources: [reflect/scheduler.py](reflect/scheduler.py#L51-L60), [reflect/scheduler.py](reflect/scheduler.py#L119-L129)

### Triggered Prompt Composition

When all five conditions are satisfied, the scheduler returns a formatted string to `agentmain.py`, which injects it as a task into the agent loop. The prompt includes a directive to read the SOP, the user-defined task prompt, and the report output path ([reflect/scheduler.py](reflect/scheduler.py#L125-L129)):

Copy code

```
[定时任务] {task_id}
[报告路径] {report_path}

先读 scheduled_task_sop 了解执行流程，然后执行以下任务：

{user_prompt}

完成后将执行报告写入 {report_path}。
```

This composition ensures the agent understands the execution protocol before beginning work. The SOP instructs the agent to immediately call `update_working_checkpoint` with the report path to prevent forgetting it during long-running tasks ([memory/scheduled\_task\_sop.md](memory/scheduled_task_sop.md#L12-L17)).

Sources: [reflect/scheduler.py](reflect/scheduler.py#L125-L129), [memory/scheduled\_task\_sop.md](memory/scheduled_task_sop.md#L12-L17)

## Idle-Detection Autonomous Trigger

Alongside the file-based scheduler, GenericAgent implements a complementary **idle-detection mechanism** that activates the agent when the user has been inactive for 30 minutes. This operates through two distinct channels depending on the deployment mode.

### Streamlit Web UI Mode (`launch.pyw`)

When launched via `launch.pyw`, a dedicated `idle_monitor()` thread runs in the background, polling every 5 seconds. It evaluates a JavaScript expression through the webview window to retrieve `last-reply-time` — a DOM element that records the timestamp of the agent's last response ([launch.pyw](launch.pyw#L43-L48)). If more than 1800 seconds (30 minutes) have elapsed since the last reply, the monitor injects an autonomous task prompt directly into the Streamlit chat input via JavaScript, programmatically setting the textarea value and clicking the submit button ([launch.pyw](launch.pyw#L50-L63)). A 120-second throttle (`last_trigger_time`) prevents rapid re-injection.

### Reflect Mode (`reflect/autonomous.py`)

The `autonomous.py` module provides the equivalent behavior for `--reflect` mode deployments. With `INTERVAL = 1800` and `ONCE = False`, it returns the autonomous task prompt on each check cycle ([reflect/autonomous.py](reflect/autonomous.py#L1-L6)):

Copy code

```
[AUTO]🤖 用户已经离开超过30分钟，作为自主智能体，请阅读自动化sop，执行自动任务。
```

Note that in reflect mode, the 30-minute idle detection is **implicit** — the module itself does not check idle state. Instead, the runtime's 1800-second polling interval serves as the de facto idle threshold. The agent is expected to follow the [Autonomous Task Management](/21-autonomous-task-management)  SOP, which directs it to read `TODO.txt`, check history, select a task, execute it within 30 agent turns, and write a report.

Sources: [reflect/autonomous.py](reflect/autonomous.py#L1-L6), [launch.pyw](launch.pyw#L50-L63)

## Logging and Observability

The scheduler maintains a dedicated log file at `sche_tasks/scheduler.log` with entries formatted as `YYYY-MM-DD HH:MM LEVEL message`. Three categories of events are recorded:

| Log Level | Trigger Condition | Example Message |
| --- | --- | --- |
| `INFO` | Task triggered | `TRIGGER daily_review (repeat=daily, schedule=08:00, last_run=2026-06-14 08:01)` |
| `INFO` | Task skipped (max delay) | `SKIP daily_review: 420min past schedule, exceeds max_delay=6h` |
| `WARNING` | Unknown repeat type | `Unknown repeat type: biweekly, fallback to 20h cooldown` |
| `ERROR` | JSON parse failure | `JSON parse error for review.json: Expecting value: line 1 column 1` |
| `ERROR` | L4 archive failure | `L4 archive failed: [Errno 2] No such file` |

Additionally, completed task results from the agent loop are written to `temp/reflect_logs/<script_name>_YYYY-MM-DD.log` by the reflect runtime in `agentmain.py` ([agentmain.py](agentmain.py#L242-L244)). The SOP document also references a `scheduler.health_check()` method that returns task status lists (`HEALTHY/OVERDUE/DISABLED/NEVER_RUN/ERROR`), though this function is not yet implemented in the current codebase ([memory/scheduled\_task\_sop.md](memory/scheduled_task_sop.md#L21)).

Sources: [reflect/scheduler.py](reflect/scheduler.py#L19-L26), [memory/scheduled\_task\_sop.md](memory/scheduled_task_sop.md#L19-L23)

## Putting It All Together: Component Relationship Map

Sources: [launch.pyw](launch.pyw#L111-L118), [reflect/scheduler.py](reflect/scheduler.py#L1-L132), [memory/autonomous\_operation\_sop.md](memory/autonomous_operation_sop.md#L1-L44)

## Next Steps

The scheduled reflection system is one axis of the agent's self-evolution capabilities. To complete your understanding of the autonomous loop:

* **[Autonomous Task Management](/21-autonomous-task-management)**  — How the agent selects, executes, and reports on tasks once the idle trigger fires, including the TODO/history lifecycle and the `helper.py` API.
* **[L4 Session Archive Compression](/18-l4-session-archive-compression)**  — Deep dive into the four-phase `batch_process` pipeline triggered by the scheduler's 12-hour L4 cron.
* **[Skill Crystallization Process](/20-skill-crystallization-process)**  — How completed task reports evolve into reusable knowledge patterns within the memory hierarchy.
* **[Agent Loop and Task Runner](/9-agent-loop-and-task-runner)**  — How `agent.put_task()` and `put_task(task, source='reflect')` enqueue tasks into the core execution loop.

Scheduled Reflection and Cron | lsdefine/GenericAgent | Zread---

<!-- Page 21: https://zread.ai/lsdefine/GenericAgent/26-context-compression-strategy -->

# Context Compression Strategy

Level: Intermediate

GenericAgent operates as a long-running autonomous agent that accumulates context across dozens of tool-call turns within a single task, and across multiple conversational sessions over its lifetime. Without aggressive compression, context windows overflow rapidly—each tool call can inject thousands of characters of HTML, file content, or execution output. The system therefore implements a **multi-layered compression pipeline** that operates at different granularities and lifecycle stages, balancing token economy against the agent's ability to reason over its own history.

## The Compression Problem Space

Before examining the solutions, it's worth understanding why this problem is acute in GenericAgent's architecture. The agent loop supports up to 40 turns per task ([agent\_loop.py#L42](agent_loop.py#L42-L47)), and each turn appends both an assistant message (potentially containing `<thinking>`, `<summary>`, and `<tool_use>` blocks) and a user message carrying tool results. A single `code_run` tool result can easily exceed 4,000 characters; a `browser_screenshot` injects OCR text from an entire web page; `file_read` dumps raw file content. Over a multi-session deployment, the  list grows unboundedly unless constrained. The  configuration parameter (defaulting to 24,000 characters for  and 28,000 for ) defines the budget ceiling (, ).

`BaseSession.history`

`context_win`

`BaseSession`

`NativeClaudeSession`

[llmcore.py#L466](llmcore.py#L466-L467)

<llmcore.py#L568>

The following diagram shows where each compression mechanism activates within a single request cycle:

## Tag-Level Compression: `compress_history_tags`

The first and most frequently invoked mechanism is `compress_history_tags()`, a module-level function in <llmcore.py#L26-L57>. Rather than running on every turn, it uses a **throttled execution pattern**: a call counter on the function object itself (`compress_history_tags._cd`) ensures it only executes every 5th invocation, skipping the other 4 calls entirely. This is a deliberate trade-off—compression is destructive, and running it too often would degrade context quality, while running it too rarely wastes tokens.

The function targets four specific XML-like tag types in older messages: `<thinking>`, `<think`, `<tool_use>`, and `<tool_result>`. It also collapses `<history>` and `<key_info>` blocks. The compression strategy is **head-and-tail preservation**: for any tagged content exceeding `max_len` (default 800) characters, it keeps the first `max_len//2` and last `max_len//2` characters, replacing the middle with `...[Truncated]...`. This retains the *intent* of a thinking block (the initial reasoning) and the *conclusion* (final output), while discarding the verbose intermediate chain-of-thought.

The function handles both message formats that flow through the system: **string content** (used by `ToolClient`/`ClaudeSession` via the protocol-prompt path) and **list-of-blocks content** (used by `NativeClaudeSession`/`NativeOAISession` via the native tool-use path). For block-format content, it additionally truncates `tool_result.content` and `tool_use.input` field values, ensuring even structured tool artifacts don't bloat the context. Only the `keep_recent` most recent messages are left untouched (default 10), preserving the agent's immediate working memory intact.

Sources: <llmcore.py#L26-L57>

## History Trimming: `trim_messages_history`

While tag compression is a soft compression that preserves message structure, `trim_messages_history()` at <llmcore.py#L77-L89> is a **hard eviction** mechanism. It is called at the top of both `BaseSession.ask()` (<llmcore.py#L504>) and `NativeClaudeSession.ask()` (<llmcore.py#L622>)—the two entry points for all LLM requests.

The function first calls `compress_history_tags()` for soft compression, then measures total context cost by serializing all messages to JSON and summing character lengths. The eviction threshold is set at `context_win * 3`, a deliberately high multiplier that accounts for the difference between raw character count and actual token count (roughly 1 token ≈ 3-4 characters for English, less for CJK). When this threshold is breached, the system enters a two-phase emergency protocol:

1. **Force-compress**: calls `compress_history_tags()` again with `keep_recent=4` (reduced from the normal 10) and `force=True` to bypass the throttle, extracting maximum savings from tag truncation before any message removal.
2. **Pop-and-sanitize**: enters a loop that removes the oldest message pair (assistant then user, maintaining conversational alternation), with a hard floor of 5 messages. The critical detail is that when a new user message becomes the list head, `_sanitize_leading_user_msg()` (<llmcore.py#L59-L75>) is called on it to rewrite any orphaned `tool_result` content blocks as plain text. This prevents dangling tool-use ID references that would cause API errors.

The target after eviction is 60% of the `context_win * 3` threshold, providing headroom so the next few turns don't immediately trigger another eviction cycle.

Sources: <llmcore.py#L77-L89>, <llmcore.py#L59-L75>, <llmcore.py#L504>, <llmcore.py#L622>

## Tool Schema Caching: Adaptive Instruction Compression

A less obvious but equally important compression mechanism lives in `ToolClient._prepare_tool_instruction()` at <llmcore.py#L719-L745>. The full tool schema (all 9 atomic tools with their JSON parameter definitions) constitutes a substantial fixed token cost in every prompt. GenericAgent avoids re-emitting this schema when it determines the model still "remembers" the tools.

The mechanism works by comparing the current `tools_json` string against `self.last_tools`. If they match and `auto_save_tokens` is enabled, instead of emitting the full schema, it outputs a one-line reminder: *"Tools: still active, ready to call. Protocol unchanged."* This collapses roughly 2,000+ characters of tool definitions into a ~60 character placeholder. The cache is invalidated when the schema actually changes (e.g., switching between English and Chinese tool descriptions), when `total_cd_tokens` exceeds 9,000 characters (<llmcore.py#L760>), when a `bad_json` parse error occurs (<llmcore.py#L805>), or when an unknown tool is encountered (<agent_loop.py#L86>)—all signals that the model may have lost track of the tool protocol and needs a full reminder.

Complementarily, the agent loop itself resets `client.last_tools = ''` every 10 turns (<agent_loop.py#L51>), ensuring the full schema is periodically re-injected to combat gradual context drift in very long tasks.

Sources: <llmcore.py#L719-L745>, <llmcore.py#L760>, <llmcore.py#L805>, <agent_loop.py#L51>, <agent_loop.py#L86>

## Output-Side Compression: `_clean_content` and `_compact_tool_args`

Compression is not limited to the input context. The agent loop applies output-side compression to control what gets displayed to users and, more importantly, what gets fed back into the context on subsequent turns.

`_clean_content()` at <agent_loop.py#L99-L111> strips verbose content blocks from assistant responses in non-verbose mode: code blocks longer than 6 lines are truncated to show the first 5 lines with a line count summary, `<file_content>`, `<tool_use>`, and `<tool_call` blocks are entirely removed from display, and excessive blank lines are collapsed.

`_compact_tool_args()` at <agent_loop.py#L113-L118> shortens tool argument representations in non-verbose logging: file paths are reduced to basenames, `update_working_checkpoint` key\_info is capped at 60 characters, and all other tool arguments are JSON-serialized and capped at 120 characters.

Sources: <agent_loop.py#L99-L118>

## Prompt Caching: Semantic Compression via API-Level Hints

GenericAgent leverages Anthropic's **prompt caching** API to achieve a different kind of compression—not reducing token count, but reducing *cost and latency* for repeated token sequences. Three distinct caching strategies are employed:

For the `ClaudeSession` path, `make_messages()` adds `cache_control: ephemeral` to the last content block of the last 2 user messages (<llmcore.py#L536-L537>). For the `NativeClaudeSession` path, the same pattern is applied in `raw_ask()` (<llmcore.py#L600-L602>), and additionally the system prompt and tool schema are marked with `cache_control` (<llmcore.py#L592>, <llmcore.py#L595>). For OpenAI-compatible relay sessions, `_stamp_oai_cache_markers()` handles the equivalent annotation (<llmcore.py#L303-L314>).

This is a *semantic* compression in the economic sense: cached tokens are billed at 10% of the base rate and have significantly lower time-to-first-token, effectively making the system's fixed context overhead (system prompt, tool schema, recent history) 90% cheaper after the first request.

Prompt caching effectiveness depends on **exact prefix matching**. Because `trim_messages_history()` removes old messages from the head of the list, the cached prefix (system prompt + recent messages) shifts over time. The dual-marking strategy on the last 2 user messages maximizes cache hits even as the conversation window slides forward.

Sources: <llmcore.py#L536-L537>, <llmcore.py#L592>, <llmcore.py#L600-L602>, <llmcore.py#L303-L314>

## Compression Mechanism Summary

| Mechanism | Layer | Trigger | What It Targets | Invasiveness |
| --- | --- | --- | --- | --- |
| `compress_history_tags` | Soft | Every 5th LLM call | `<thinking>`, `<tool_use>`, `<tool_result>`, `<history>` in older messages | Low — preserves structure, truncates content |
| `trim_messages_history` | Hard | Cost exceeds `context_win × 3` | Entire oldest message pairs | High — removes messages entirely |
| Tool schema caching | Instruction | Schema unchanged since last call | Full tool JSON definitions (~2KB) | None — replaces with one-line reminder |
| 10-turn schema reset | Instruction | `turn % 10 == 0` | Same as above (inverse) | None — restores full schema |
| `_clean_content` | Output | Non-verbose mode | Code blocks, file content, tool XML in display | Low — display only |
| Prompt caching markers | API | Every native Claude call | System prompt, tools, recent user messages | None — API hint, no content change |

## Cross-Task Persistence and the `/session` Interface

Context compression is not solely automatic. Users can dynamically tune compression behavior at runtime via the `/session.<param>=<value>` slash command (<agentmain.py#L105-L113>), which sets arbitrary attributes on the backend session object—including `context_win` itself. This allows live adjustment of the compression threshold without restarting the agent. The `/resume` command (<agentmain.py#L114-L115>) triggers a cross-session context recovery flow, scanning recent model response logs to reconstruct a `<history>` summary of prior sessions, effectively compressing entire past sessions into a single injected prompt.

## Relationship to the Layered Memory System

Context compression operates at a different level than the [Memory Hierarchy Design](/17-memory-hierarchy-design) . While the memory system manages *long-term* knowledge persistence (global memory, insights, SOPs), context compression manages the *short-term* working context that the LLM sees in each request. They interact at one critical junction: when `_sanitize_leading_user_msg()` strips tool results from a message that becomes the new history head, the agent's `<summary>` mechanism (part of the interaction protocol) has already captured the essential information from those tool results into the `<summary>` tags, which survive the sanitization. This is why the interaction protocol's summary requirement is not merely a logging nicety—it is a **compression survival mechanism** ensuring critical information outlives the raw data that produced it.

For deeper exploration of how compressed sessions are archived and later recovered, see [L4 Session Archive Compression](/18-l4-session-archive-compression) . To understand the tool protocol that generates the content being compressed, refer to [Tool Dispatch Handler](/10-tool-dispatch-handler) .

Context Compression Strategy | lsdefine/GenericAgent | Zread
