#!/usr/bin/env python3
"""
Antigravity (AGY) Sub-Agent Launcher
------------------------------------
Allows external AI agents (OpenAI Codex, Claude Code, Cursor, custom scripts)
to spawn Google Antigravity as a sub-agent to execute complex coding, refactoring,
or research tasks using your existing Antigravity subscription credentials.

Usage:
    python agy_subagent.py --prompt "Fix all broken unit tests in ./tests"
    python agy_subagent.py --prompt "Refactor db layer" --model gemini-3.6-pro --effort high
    python agy_subagent.py --prompt "Analyze codebase" --workdir "/path/to/project"
"""

import sys
import os
import argparse
import subprocess
import shutil


def run_agy(prompt: str, model: str, effort: str, workdir: str, skip_permissions: bool, mode: str, output_format: str):
    """Executes agy CLI with correct subscription credentials and flags."""
    agy_bin = shutil.which("agy")
    if not agy_bin:
        print("[Error] 'agy' CLI binary was not found in PATH.", file=sys.stderr)
        print("Please install Antigravity CLI and ensure 'agy' is accessible.", file=sys.stderr)
        sys.exit(1)

    cmd = [agy_bin, "-p", prompt]
    
    if model:
        cmd.extend(["--model", model])
    
    if effort:
        cmd.extend(["--effort", effort])
        
    if skip_permissions:
        cmd.append("--dangerously-skip-permissions")
        
    if mode:
        cmd.extend(["--mode", mode])
        
    if output_format and output_format != "text":
        cmd.extend(["--output-format", output_format])

    cwd = os.path.abspath(workdir) if workdir else os.getcwd()
    cmd.extend(["--add-dir", cwd])
    
    print(f"[AGY Sub-Agent Launcher] Invoking CLI: {' '.join(cmd)}", file=sys.stderr)
    result = subprocess.run(cmd, cwd=cwd)
    sys.exit(result.returncode)


def main():
    parser = argparse.ArgumentParser(
        description="Spawn Google Antigravity (AGY) as a sub-agent from Codex / Claude Code / external tools."
    )
    parser.add_argument(
        "--prompt", "-p",
        required=True,
        help="The instruction/task prompt to pass to the AGY sub-agent."
    )
    parser.add_argument(
        "--model", "-m",
        default="gemini-3.6-flash",
        help="Model to use (e.g. gemini-3.6-pro, gemini-3.6-flash). Default: gemini-3.6-flash."
    )
    parser.add_argument(
        "--effort", "-e",
        default="high",
        choices=["low", "medium", "high"],
        help="Reasoning effort level for the model (low, medium, high). Default: high."
    )
    parser.add_argument(
        "--workdir", "-w",
        default="",
        help="Working directory path for the sub-agent task (passed via --add-dir)."
    )
    parser.add_argument(
        "--mode",
        default="",
        choices=["", "accept-edits", "plan"],
        help="Execution mode for the sub-agent (accept-edits, plan)."
    )
    parser.add_argument(
        "--no-skip-permissions",
        action="store_true",
        help="Do not pass --dangerously-skip-permissions (defaults to auto-approving tool permissions)."
    )
    parser.add_argument(
        "--output-format",
        default="text",
        choices=["text", "json", "stream-json"],
        help="Output format (text, json, stream-json). Default: text."
    )

    args = parser.parse_args()

    run_agy(
        prompt=args.prompt,
        model=args.model,
        effort=args.effort,
        workdir=args.workdir,
        skip_permissions=not args.no_skip_permissions,
        mode=args.mode,
        output_format=args.output_format
    )


if __name__ == "__main__":
    main()
