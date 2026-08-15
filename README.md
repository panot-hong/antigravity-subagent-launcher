# Antigravity Sub-Agent Launcher (`antigravity-subagent-launcher`)

A lightweight, cross-platform bridge allowing external AI agents (**OpenAI Codex**, **Claude Code**, **Cursor**, or custom LLM scripts) to spawn **Google Antigravity (`agy`)** as a sub-agent.

It uses your existing **Google Antigravity Subscription** credentials (via local OAuth token sharing) so you can delegate tasks without requiring per-token API keys.

---

## Key Features

- **Subscription-Based Authentication**: Shares your machine's logged-in Antigravity account (`~/.gemini/`) — no `OPENAI_API_KEY` or `GEMINI_API_KEY` required.
- **Model Selection**: Switch dynamically between `gemini-3.6-pro` (high-reasoning, deep planning) and `gemini-3.6-flash` (fast, lightweight execution).
- **Dual Execution Engine**:
  - **Python SDK (`google-antigravity`)**: Primary high-performance programmatic interface with real-time token streaming.
  - **CLI Fallback (`agy -p ...`)**: Automatic fallback to subprocess execution if SDK package is not installed.
- **Agent Skill Ready**: Comes with a ready-to-use `SKILL.md` for instant integration into Codex, Claude Code, and Antigravity custom skill registries.

---

## Prerequisites

1. **Python 3.9+**
2. **Google Antigravity SDK** (or `agy` CLI):
   ```bash
   pip install google-antigravity
   ```
3. **Active Antigravity Login**:
   Make sure you have logged in once on your machine:
   ```bash
   agy login
   # OR open the Antigravity Desktop App / IDE
   ```

---

## Quickstart

### 1. Direct Command Line Usage

Run a fast task using **Gemini 3.6 Flash**:
```bash
python agy_subagent.py --prompt "Fix failing unit tests in ./tests"
```

Run a complex refactoring task using **Gemini 3.6 Pro**:
```bash
python agy_subagent.py --prompt "Refactor database access layer to async" --model gemini-3.6-pro
```

Run in a specific project directory in **read-only mode**:
```bash
python agy_subagent.py --prompt "Analyze security vulnerabilities" --workdir "/path/to/project" --read-only
```

---

## Integration with Codex & Claude Code

### Adding as a Codex / Claude Code Skill

1. Copy `SKILL.md` into your agent's skill directory:
   - **Codex / Antigravity Skills**: `.agents/skills/spawn-antigravity/SKILL.md` or `~/.gemini/config/skills/spawn-antigravity/SKILL.md`
   - **Claude Code Skills**: `.claude/skills/spawn-antigravity.md` or `~/.claude/skills/spawn-antigravity.md`

2. When Codex or Claude Code is running, it will automatically discover `spawn-antigravity` and can execute:
   ```bash
   python D:/Projects/antigravity-subagent-launcher/agy_subagent.py --prompt "<TASK>" --model gemini-3.6-pro
   ```

---

## Project Structure

```
antigravity-subagent-launcher/
├── agy_subagent.py      # Core Python launcher script (SDK + CLI fallback)
├── SKILL.md             # Standard Agent Skill specification for Codex / Claude Code
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignore settings
└── README.md            # Documentation & setup guide
```

---

## GitHub Setup & Syncing Across Computers

To commit and push this repository to your private GitHub account so you can pull it on other machines:

```bash
# 1. Initialize git repository
git init

# 2. Add files and commit
git add .
git commit -m "Initial commit: Antigravity Sub-Agent launcher script & skill definition"

# 3. Create private repo on GitHub (e.g. via GitHub CLI or web UI)
gh repo create antigravity-subagent-launcher --private --source=. --remote=origin --push

# 4. On your other computer, simply pull:
git clone https://github.com/YOUR_USERNAME/antigravity-subagent-launcher.git
pip install -r requirements.txt
```

---

## License

MIT License. Free for personal and commercial integration with Google Antigravity.
