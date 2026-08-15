---
name: spawn-antigravity
description: Delegate sub-tasks, refactoring, research, or execution to Google Antigravity (agy) powered by Gemini 3.6 Pro / Gemini 3.6 Flash from OpenAI Codex or Claude Code.
---

# Spawn Google Antigravity (AGY) Sub-Agent

Use this skill when you (**OpenAI Codex** / **Claude Code** / external AI model) need to delegate a complex task, broad codebase analysis, multi-file refactoring, or specialized code generation to Google Antigravity as a sub-agent.

## When to Use
- **Deep Refactoring / Planning**: Use `gemini-3.6-pro` model to delegate heavy multi-file edits or architectural reviews.
- **Fast Search / Isolated Execution**: Use `gemini-3.6-flash` model for targeted search, unit test fixes, or script generation.
- **Offloading Execution**: Delegate long-running or autonomous coding tasks without consuming Codex / Claude token limits directly, leveraging your local Antigravity subscription credentials.

## Execution Command

Invoke the python launcher script from the terminal:

### Standard Task (Fast - Gemini 3.6 Flash)
```bash
python /path/to/antigravity-subagent-launcher/agy_subagent.py --prompt "<TASK_DESCRIPTION>"
```

### Complex Task (High Reasoning - Gemini 3.6 Pro)
```bash
python /path/to/antigravity-subagent-launcher/agy_subagent.py --prompt "<COMPLEX_TASK_DESCRIPTION>" --model gemini-3.6-pro
```

### Read-Only Research / Inspection
```bash
python /path/to/antigravity-subagent-launcher/agy_subagent.py --prompt "<RESEARCH_QUESTION>" --read-only
```

### Specifying Target Directory
```bash
python /path/to/antigravity-subagent-launcher/agy_subagent.py --prompt "<TASK>" --workdir "<TARGET_PROJECT_PATH>"
```

## Parameters

| Parameter | Short | Default | Description |
| :--- | :--- | :--- | :--- |
| `--prompt` | `-p` | *Required* | High-level instructions for the Antigravity sub-agent. |
| `--model` | `-m` | `gemini-3.6-flash` | Model choice: `gemini-3.6-pro`, `gemini-3.6-flash`, `pro`, `flash`. |
| `--workdir` | `-w` | `.` | Target project directory to execute in. |
| `--read-only` | | `false` | Restricts Antigravity to read-only tools (no file edits or command runs). |
| `--force-cli` | | `false` | Forces subprocess execution of `agy` CLI instead of Python SDK. |

## Notes & Environment Requirements
- Ensure `google-antigravity` is installed (`pip install google-antigravity`) or `agy` CLI is accessible in PATH.
- Uses existing local Antigravity subscription credentials (`~/.gemini/`) — no API key needed.
