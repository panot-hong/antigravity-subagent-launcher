#!/usr/bin/env python3
"""
Antigravity Sub-Agent Launcher - Automated Installer
---------------------------------------------------
Automates the installation of dependencies and registers the `spawn-antigravity` skill
for OpenAI Codex, Claude Code, and external agentic environments across Windows, macOS, and Linux.

Usage:
    python install.py
"""

import os
import sys
import shutil
import subprocess
import pathlib

# Force UTF-8 output encoding if possible on Windows legacy terminals
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


def print_step(msg):
    print(f"\n==> {msg}")


def print_success(msg):
    print(f"  [OK] {msg}")


def print_warning(msg):
    print(f"  [!] {msg}")


def install_dependencies():
    print_step("Installing Python SDK dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print_success("Installed 'google-antigravity' SDK.")
    except Exception as e:
        print_warning(f"Could not install dependencies automatically: {e}")
        print_warning("You can manually run: pip install google-antigravity")


def prepare_skill_content(script_abs_path: str, skill_template_path: str) -> str:
    """Reads SKILL.md and injects the actual absolute path to agy_subagent.py."""
    with open(skill_template_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Normalize Windows slashes to forward slashes for cross-platform terminal compatibility
    clean_script_path = script_abs_path.replace("\\", "/")
    
    # Replace placeholder paths
    content = content.replace("/path/to/antigravity-subagent-launcher/agy_subagent.py", clean_script_path)
    return content


def register_skills(script_abs_path: str):
    print_step("Registering skills for OpenAI Codex and Claude Code...")
    
    home_dir = pathlib.Path.home()
    repo_dir = pathlib.Path(__file__).parent.resolve()
    skill_template = repo_dir / "SKILL.md"

    if not skill_template.exists():
        print_warning(f"SKILL.md template not found at {skill_template}")
        return

    skill_content = prepare_skill_content(str(script_abs_path), str(skill_template))

    targets = [
        ("OpenAI Codex (Directory Skill)", home_dir / ".codex" / "skills" / "spawn-antigravity" / "SKILL.md"),
        ("OpenAI Codex (Flat Skill)", home_dir / ".codex" / "skills" / "spawn-antigravity.md"),
        ("Claude Code Skill", home_dir / ".claude" / "skills" / "spawn-antigravity.md"),
        ("Global .agents Skill Registry", home_dir / ".agents" / "skills" / "spawn-antigravity" / "SKILL.md"),
    ]

    for name, skill_path in targets:
        try:
            skill_path.parent.mkdir(parents=True, exist_ok=True)
            with open(skill_path, "w", encoding="utf-8") as f:
                f.write(skill_content)
            print_success(f"Registered {name}: {skill_path}")
        except Exception as e:
            print_warning(f"Could not write {name} skill to {skill_path}: {e}")


def check_auth_status():
    print_step("Checking Antigravity authentication status...")
    agy_bin = shutil.which("agy")
    if agy_bin:
        print_success(f"Found 'agy' CLI binary at {agy_bin}")
    else:
        print_warning("'agy' CLI binary not found in PATH.")

    home_dir = pathlib.Path.home()
    creds_file = home_dir / ".gemini" / "oauth_creds.json"
    if creds_file.exists():
        print_success(f"Found Antigravity local credentials at {creds_file}")
    else:
        print_warning(f"Local credentials file not found at {creds_file}.")
        print_warning("Please run 'agy login' or open Antigravity Desktop App to log in.")


def main():
    print("==========================================================")
    print("  Antigravity Sub-Agent Launcher - Automated Setup")
    print("==========================================================")

    repo_dir = pathlib.Path(__file__).parent.resolve()
    script_abs_path = repo_dir / "agy_subagent.py"

    if not script_abs_path.exists():
        print(f"[Error] agy_subagent.py not found in {repo_dir}", file=sys.stderr)
        sys.exit(1)

    install_dependencies()
    register_skills(str(script_abs_path))
    check_auth_status()

    print("\n==========================================================")
    print("  Setup Complete!")
    print("==========================================================")
    print("You can test the launcher right now by running:")
    print(f'  python "{script_abs_path}" --prompt "Hello from Antigravity sub-agent!"\n')


if __name__ == "__main__":
    main()
