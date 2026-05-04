# Codex Handoff: GenericAgent Workbench

This note is for continuing the setup on another Windows machine or in another Codex session.

## Repository

Fork/branch expected after push:

```powershell
git clone https://github.com/tcflying/GenericAgent.git
cd GenericAgent
git switch codex/workbench-token-e2e
```

If the branch is not checked out automatically:

```powershell
git fetch origin codex/workbench-token-e2e
git switch codex/workbench-token-e2e
```

## Python Environment

Use Python 3.11 if available.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\pip.exe install requests streamlit pywebview beautifulsoup4 bottle pyperclip
```

Optional project install:

```powershell
.\.venv\Scripts\pip.exe install -e ".[ui]"
```

## LLM Configuration

Create `mykey.py` from the template:

```powershell
Copy-Item mykey_template.py mykey.py
```

Configure MiniMax Token Plan without committing secrets:

```python
mixin_config = {
    "llm_nos": ["minimax-token-plan"],
}

native_claude_config_minimax = {
    "name": "minimax-token-plan",
    "apikey": "YOUR_MINIMAX_TOKEN_PLAN_KEY",
    "apibase": "https://api.minimaxi.com/anthropic",
    "model": "MiniMax-M2.7-highspeed",
    "stream": True,
    "fake_cc_system_prompt": False,
    "timeout": 120,
    "connect_timeout": 30,
}
```

Never commit `mykey.py`.

## Start Workbench

```powershell
.\run_workbench.ps1
```

Or directly:

```powershell
.\.venv\Scripts\streamlit.exe run .\frontends\workbench.py --server.port 8502
```

Open:

```text
http://localhost:8502/
```

## What This Branch Adds

- Independent Streamlit Workbench at `frontends/workbench.py`.
- Dashboard pages for runtime readiness, MiniMax Token Plan config, token-efficiency indicators, memory/docs/files, and multiple frontends.
- `file_write` now accepts `file_content` and `content` arguments.
- `code_run` default working directory is the project root, so `temp/foo.md` writes to project `temp/foo.md`.
- Tool schema descriptions were updated to teach the model the corrected behavior.
- Archived Zread documentation is stored under `docs/`.

## Smoke Tests

```powershell
.\.venv\Scripts\python.exe -m py_compile ga.py frontends\workbench.py
.\.venv\Scripts\python.exe -m json.tool assets\tools_schema.json > $null
.\.venv\Scripts\python.exe -m json.tool assets\tools_schema_cn.json > $null
```

Workbench E2E task:

```text
请使用 file_write 工具把文本 PATH_FIX_OK 写入 temp/path_fix_e2e.md，然后用 file_read 回读确认。最终回复路径、内容、状态。
```

Expected file:

```text
temp/path_fix_e2e.md
```

It must not write to:

```text
temp/temp/path_fix_e2e.md
```

Complex E2E report from the previous session:

```text
temp/complex_e2e_report.md
```

That report is generated output and is not required for a fresh install.
