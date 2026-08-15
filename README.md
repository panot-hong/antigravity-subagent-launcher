# Antigravity Sub-Agent Launcher (`antigravity-subagent-launcher`)

A lightweight, cross-platform bridge and agent tool interface that allows **any coding agent** (such as **OpenAI Codex**, **Claude Code**, **Cursor**, **Windsurf**, **Aider**, or custom AI agent loops) to spawn **Google Antigravity (`agy`)** as an autonomous sub-agent.

It leverages your existing **Google Antigravity Subscription** credentials (via local OAuth session sharing), allowing external AI agents to delegate tasks to Gemini 3.6 Pro / Gemini 3.6 Flash without requiring pay-per-token API keys.

---

## 🤖 Supported Coding Agents & Frameworks

This launcher is designed out-of-the-box to work with any tool or agent capable of running terminal commands or loading skill files:

| Agent / Tool | Supported Integration Method | How It Works |
| :--- | :--- | :--- |
| **OpenAI Codex** | Skill file (`SKILL.md`) or Shell Execution | Codex invokes `python agy_subagent.py --prompt "..."` |
| **Claude Code** | Custom Skill (`.claude/skills/`) or Tool Call | Claude Code delegates tasks to `agy` as a sub-agent |
| **Cursor / Windsurf** | Terminal Tool Execution / MCP | Agent runs `agy_subagent.py` in workspace terminal |
| **Aider / Custom LLMs** | Subprocess / Shell Command | Invokes `agy` script as a sub-command |

---

## 🌟 Why Delegate to Antigravity as a Sub-Agent?

1. **Subscription-Based Auth**: Uses your existing logged-in Antigravity account (`~/.gemini/`) rather than pay-per-token API keys.
2. **Model Switching**: Easily switch between high-reasoning **Gemini 3.6 Pro** (for architecture, planning, deep refactoring) and fast **Gemini 3.6 Flash** (for quick edits, test fixes, searches).
3. **Cross-Model Validation**: Let OpenAI Codex or Claude Code delegate specific sub-tasks to Gemini 3.6 to get a second opinion or cross-verify solution approaches.
4. **Dual Execution Engine**:
   - **Python SDK (`google-antigravity`)**: Fast programmatic execution with streaming output.
   - **CLI Fallback (`agy -p ...`)**: Automatic fallback to standard `agy` CLI subprocess if Python SDK is missing.

---

## 📋 Prerequisites

1. **Python 3.9+**
2. **Google Antigravity SDK** (or `agy` CLI):
   ```bash
   pip install google-antigravity
   ```
3. **Active Antigravity Account Login**:
   Make sure `agy` is logged in on your machine once:
   ```bash
   agy login
   # OR open the Antigravity Desktop App / IDE
   ```

---

## 🚀 Quickstart

### Direct Command Line Usage

**Fast execution with Gemini 3.6 Flash:**
```bash
python agy_subagent.py --prompt "Fix failing unit tests in ./tests"
```

**Complex refactoring with Gemini 3.6 Pro:**
```bash
python agy_subagent.py --prompt "Refactor database access layer to async" --model gemini-3.6-pro
```

**Read-only analysis on a specific project directory:**
```bash
python agy_subagent.py --prompt "Analyze security vulnerabilities" --workdir "/path/to/project" --read-only
```

---

## 🛠️ Step-by-Step Integration for Specific Agents

### 1. Integrating with Claude Code

To let **Claude Code** spawn Antigravity as a skill:

1. Copy `SKILL.md` to Claude Code's skill directory:
   ```bash
   # User-level (global across all projects):
   mkdir -p ~/.claude/skills/
   cp SKILL.md ~/.claude/skills/spawn-antigravity.md

   # Project-level (repo specific):
   mkdir -p .claude/skills/
   cp SKILL.md .claude/skills/spawn-antigravity.md
   ```
2. In Claude Code, tell it:
   > *"Use the spawn-antigravity skill to refactor the module using Gemini 3.6 Pro."*

---

### 2. Integrating with OpenAI Codex / Custom Agents

To let **Codex** or custom agentic scripts use Antigravity:

1. Copy `SKILL.md` to your workspace skills directory:
   ```bash
   mkdir -p .agents/skills/spawn-antigravity/
   cp SKILL.md .agents/skills/spawn-antigravity/SKILL.md
   ```
2. Codex can run the tool via command line execution:
   ```bash
   python /path/to/antigravity-subagent-launcher/agy_subagent.py --prompt "<TASK_DESCRIPTION>" --model gemini-3.6-pro
   ```

---

## ⚙️ CLI Flags & Parameters

```text
usage: agy_subagent.py [-h] --prompt PROMPT [--model MODEL]
                       [--system-instructions SYSTEM_INSTRUCTIONS]
                       [--workdir WORKDIR] [--read-only] [--force-cli]

options:
  --prompt, -p        Task prompt/instruction for AGY (Required)
  --model, -m         Model: gemini-3.6-pro, gemini-3.6-flash, pro, flash (Default: gemini-3.6-flash)
  --system-instructions Custom instructions for the sub-agent
  --workdir, -w       Target working directory path
  --read-only         Restrict sub-agent to read-only actions
  --force-cli         Force CLI subprocess instead of Python SDK
```

---

## 📁 Project Structure

```
antigravity-subagent-launcher/
├── agy_subagent.py      # Core Python launcher (SDK + CLI fallback)
├── SKILL.md             # Standard Agent Skill specification (Codex, Claude Code, AGY)
├── requirements.txt     # Python dependencies (google-antigravity)
├── .gitignore           # Git ignore patterns
└── README.md            # Complete multi-agent setup & usage guide
```

---

## 🔄 Syncing Across Computers via GitHub

```bash
# Clone on a new machine:
git clone https://github.com/panot-hong/antigravity-subagent-launcher.git
cd antigravity-subagent-launcher

# Install dependencies:
pip install -r requirements.txt
```

---

## 📄 License

MIT License. Free for personal and commercial integration.
