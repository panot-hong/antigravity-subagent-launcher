#!/usr/bin/env python3
"""
Antigravity (AGY) Sub-Agent Launcher
------------------------------------
Allows external AI agents (OpenAI Codex, Claude Code, Cursor, custom scripts)
to spawn Google Antigravity as a sub-agent to execute complex coding, refactoring,
or research tasks using your existing Antigravity subscription.

Usage:
    python agy_subagent.py --prompt "Fix all broken unit tests in ./tests"
    python agy_subagent.py --prompt "Refactor db layer" --model gemini-3.6-pro
    python agy_subagent.py --prompt "Analyze codebase" --read-only
"""

import sys
import os
import argparse
import asyncio
import subprocess
import shutil

# Try importing the official google-antigravity Python SDK
try:
    from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig
    HAS_SDK = True
except ImportError:
    HAS_SDK = False


async def run_via_sdk(prompt: str, model: str, system_instructions: str, read_only: bool, workdir: str):
    """Executes the sub-agent via the official Python SDK."""
    if workdir:
        os.chdir(workdir)

    capabilities = CapabilitiesConfig() if not read_only else None
    
    config = LocalAgentConfig(
        model=model,
        system_instructions=system_instructions or "You are an Antigravity (AGY) sub-agent spawned by an external AI supervisor.",
        capabilities=capabilities,
    )

    async with Agent(config) as agent:
        response = await agent.chat(prompt)
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print()


def run_via_cli(prompt: str, model: str, read_only: bool, workdir: str):
    """Fallback execution via agy CLI subprocess if Python SDK is not installed."""
    agy_bin = shutil.which("agy")
    if not agy_bin:
        print("[Error] Neither 'google-antigravity' Python SDK nor 'agy' CLI was found in PATH.", file=sys.stderr)
        print("Please install the SDK via `pip install google-antigravity` or install the Antigravity CLI.", file=sys.stderr)
        sys.exit(1)

    cmd = [agy_bin, "-p", prompt]
    if model:
        cmd.extend(["--model", model])
    if read_only:
        cmd.append("--read-only")

    cwd = workdir if workdir else os.getcwd()
    
    print(f"[AGY Sub-Agent Launcher] Invoking CLI: {' '.join(cmd)} (cwd: {cwd})")
    subprocess.run(cmd, cwd=cwd)


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
        help="Model to use (e.g. gemini-3.6-pro, gemini-3.6-flash, pro, flash). Default: gemini-3.6-flash."
    )
    parser.add_argument(
        "--system-instructions", "-s",
        default="You are an Antigravity (AGY) sub-agent spawned to complete a specific task for an external AI agent.",
        help="Custom system instructions for the sub-agent."
    )
    parser.add_argument(
        "--workdir", "-w",
        default="",
        help="Working directory path for the sub-agent task."
    )
    parser.add_argument(
        "--read-only",
        action="store_true",
        help="Run the agent in read-only mode (prevents file writes and system execution)."
    )
    parser.add_argument(
        "--force-cli",
        action="store_true",
        help="Force CLI execution instead of Python SDK."
    )

    args = parser.parse_args()

    if HAS_SDK and not args.force_cli:
        try:
            asyncio.run(run_via_sdk(
                prompt=args.prompt,
                model=args.model,
                system_instructions=args.system_instructions,
                read_only=args.read_only,
                workdir=args.workdir
            ))
        except Exception as e:
            print(f"[Warning] SDK execution encountered error: {e}. Falling back to CLI...", file=sys.stderr)
            run_via_cli(args.prompt, args.model, args.read_only, args.workdir)
    else:
        run_via_cli(args.prompt, args.model, args.read_only, args.workdir)


if __name__ == "__main__":
    main()
