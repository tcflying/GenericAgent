import ast
import glob
import html
import importlib.util
import json
import os
import queue
import re
import requests
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

import streamlit as st

if sys.stdout is None:
    sys.stdout = open(os.devnull, "w")
if sys.stderr is None:
    sys.stderr = open(os.devnull, "w")

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))
sys.path.append(str(ROOT / "frontends"))

from agentmain import GeneraticAgent
from frontends.chatapp_common import build_done_text, format_restore


st.set_page_config(page_title="GenericAgent Workbench", page_icon="GA", layout="wide")

SENSITIVE_KEYS = {"apikey", "api_key", "token", "secret", "password", "cookie"}
PLACEHOLDER_PAT = re.compile(r"<your|your-|YOUR_|YOUR|xxx|sk-your|your_", re.I)

ATOMIC_TOOLS = [
    ("code_run", "Run Python and shell code for dynamic capability growth."),
    ("file_read", "Read local files and project context."),
    ("file_write", "Create files, notes, scripts, and generated outputs."),
    ("file_patch", "Patch existing files while preserving surrounding content."),
    ("web_scan", "Read browser/web state through the bridge."),
    ("web_execute_js", "Drive browser behavior with JavaScript."),
    ("ask_user", "Pause for human confirmation or missing information."),
    ("update_working_checkpoint", "Persist the current working state."),
    ("start_long_term_update", "Promote useful experience into memory."),
]

FRONTENDS = [
    ("Desktop Launcher", "launch.pyw", "python launch.pyw", ["pywebview", "streamlit"], []),
    ("Workbench", "frontends/workbench.py", "streamlit run frontends/workbench.py", ["streamlit"], []),
    ("Streamlit Chat", "frontends/stapp2.py", "streamlit run frontends/stapp2.py", ["streamlit"], []),
    ("Qt Desktop", "frontends/qtapp.py", "python frontends/qtapp.py", [], []),
    ("Telegram", "frontends/tgapp.py", "python frontends/tgapp.py", ["telegram"], ["tg_bot_token", "tg_allowed_users"]),
    ("QQ Bot", "frontends/qqapp.py", "python frontends/qqapp.py", ["botpy"], ["qq_app_id", "qq_app_secret", "qq_allowed_users"]),
    ("WeChat", "frontends/wechatapp.py", "python frontends/wechatapp.py", ["Crypto", "qrcode"], []),
    ("Feishu", "frontends/fsapp.py", "python frontends/fsapp.py", ["lark_oapi"], ["fs_app_id", "fs_app_secret", "fs_allowed_users"]),
    ("WeCom", "frontends/wecomapp.py", "python frontends/wecomapp.py", ["wecom_aibot_sdk"], ["wecom_bot_id", "wecom_secret"]),
    ("DingTalk", "frontends/dingtalkapp.py", "python frontends/dingtalkapp.py", ["dingtalk_stream"], ["dingtalk_client_id", "dingtalk_client_secret"]),
]

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap');
:root {
    --bg: #080d10;
    --ink: #eef7f2;
    --muted: #8ea39a;
    --line: rgba(210, 236, 225, .16);
    --panel: rgba(13, 22, 25, .78);
    --panel-strong: rgba(18, 31, 35, .92);
    --glass: rgba(235, 255, 247, .075);
    --cyan: #45f0ce;
    --amber: #ffb35c;
    --blue: #72a8ff;
    --red: #ff6b5c;
    --green: #50d890;
    --shadow: 0 28px 90px rgba(0, 0, 0, .38);
    --radius: 18px;
    --font-display: "Bricolage Grotesque", "Segoe UI", sans-serif;
    --font-mono: "IBM Plex Mono", Consolas, monospace;
}
.stApp {
    background:
        radial-gradient(circle at 18% 10%, rgba(69, 240, 206, .18), transparent 30rem),
        radial-gradient(circle at 92% 18%, rgba(255, 179, 92, .16), transparent 28rem),
        radial-gradient(circle at 50% 110%, rgba(114, 168, 255, .14), transparent 32rem),
        linear-gradient(90deg, rgba(238,247,242,.04) 1px, transparent 1px),
        linear-gradient(0deg, rgba(238,247,242,.035) 1px, transparent 1px),
        var(--bg);
    background-size: auto, auto, auto, 42px 42px, 42px 42px, auto;
    color: var(--ink);
}
[data-testid="stHeader"] {
    background: linear-gradient(180deg, rgba(8, 13, 16, .96), rgba(8, 13, 16, .68));
    border-bottom: 1px solid var(--line);
    backdrop-filter: blur(18px);
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(9,15,18,.98), rgba(10,20,22,.98));
    border-right: 1px solid var(--line);
}
[data-testid="stSidebar"] * { color: var(--ink) !important; }
[data-testid="stSidebar"] button {
    min-height:44px !important;
    border-radius: 14px !important;
    border: 1px solid var(--line) !important;
    background: rgba(238,247,242,.055) !important;
}
#MainMenu, footer, [data-testid="stToolbar"] { visibility: hidden; }
.block-container { padding-top: 2.6rem; max-width: 1440px; }
h1, h2, h3 {
    letter-spacing: 0;
    color: var(--ink);
    font-family: var(--font-display);
}
.stMarkdown, .stText, .stCaption, p, label, div {
    font-family: var(--font-display);
}
.ga-topline {
    display:grid;
    grid-template-columns: minmax(0, 1fr) 360px;
    gap:1rem;
    align-items:stretch;
    margin-bottom:1rem;
    padding:1rem;
    border:1px solid var(--line);
    border-radius:var(--radius);
    background:
        linear-gradient(135deg, rgba(238,247,242,.10), rgba(238,247,242,.035)),
        radial-gradient(circle at 82% 20%, rgba(69,240,206,.14), transparent 18rem),
        var(--panel);
    backdrop-filter: blur(20px);
    box-shadow: var(--shadow);
    position:relative;
    overflow:hidden;
    animation: ga-enter .42s ease-out both;
}
.ga-topline:before {
    content:"";
    position:absolute;
    left:1rem;
    right:1rem;
    top:0;
    height:1px;
    background:linear-gradient(90deg, transparent, var(--cyan), var(--amber), transparent);
}
.ga-topline:after {
    content:"";
    position:absolute;
    right:-140px;
    top:-180px;
    width:420px;
    height:420px;
    border-radius:999px;
    background:
        radial-gradient(circle, transparent 45%, rgba(69,240,206,.22) 46%, transparent 47%),
        radial-gradient(circle, transparent 62%, rgba(255,179,92,.18) 63%, transparent 64%);
    pointer-events:none;
}
.ga-title-row { display:flex; align-items:center; gap:1rem; min-width:0; padding:.2rem 0 0; position:relative; z-index:1; }
.ga-mark {
    width:58px; height:58px; border-radius:18px;
    display:flex; align-items:center; justify-content:center;
    color:#06100e;
    background:
        radial-gradient(circle at 30% 22%, rgba(255,255,255,.80), transparent 18%),
        linear-gradient(135deg, var(--cyan), var(--amber));
    border:1px solid rgba(238,247,242,.22);
    box-shadow:0 18px 42px rgba(69,240,206,.16);
    font-family:var(--font-mono);
    font-weight:700; font-size:.92rem;
    flex:0 0 auto;
}
.ga-title {
    font-size: clamp(1.75rem, 3.2vw, 2.95rem);
    font-weight: 800;
    line-height: .95;
    color:var(--ink);
    letter-spacing:-.02em;
}
.ga-subtitle { color:var(--muted); margin-top:.45rem; font-size:1rem; }
.ga-path {
    color:rgba(238,247,242,.56);
    font-family:var(--font-mono);
    font-size:.76rem;
    margin:.9rem 0 .1rem;
    word-break:break-all;
    padding-left:.25rem;
}
.ga-chipbox {
    display:flex;
    flex-direction:column;
    align-content:center;
    justify-content:center;
    gap:.6rem;
    padding:.55rem;
    border:1px solid var(--line);
    border-radius:16px;
    background:rgba(8,13,16,.42);
    max-width:360px;
    z-index:1;
}
.ga-chip {
    display:flex; align-items:center; justify-content:space-between; gap:.7rem; min-height:38px; padding:.42rem .65rem;
    border:1px solid var(--line);
    background:rgba(238,247,242,.055);
    border-radius:12px;
    color:var(--ink);
    font-family:var(--font-mono);
    font-size:.76rem;
    white-space:nowrap;
    box-shadow:none;
    backdrop-filter: blur(10px);
}
.ga-dot {
    width:.48rem; height:.48rem; border-radius:999px; background:var(--good);
    box-shadow:0 0 0 3px rgba(39,122,79,.22);
}
.ga-grid { display:grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap:.75rem; margin:.8rem 0 .9rem; }
.ga-stat, .ga-panel {
    border:1px solid var(--line);
    background:
        linear-gradient(180deg, rgba(238,247,242,.095), rgba(238,247,242,.045)),
        var(--panel);
    border-radius:var(--radius);
    backdrop-filter: blur(18px);
    box-shadow: var(--shadow);
}
.ga-stat {
    min-height:122px;
    padding:1rem 1rem .9rem 1rem;
    position:relative;
    overflow:hidden;
    animation: ga-rise .45s ease-out both;
}
.ga-stat:nth-child(2) { animation-delay: .05s; }
.ga-stat:nth-child(3) { animation-delay: .10s; }
.ga-stat:nth-child(4) { animation-delay: .15s; }
.ga-stat:after {
    content:"";
    position:absolute;
    right:-24px;
    top:-38px;
    width:118px;
    height:118px;
    border-radius:999px;
    background:radial-gradient(circle, rgba(255,179,92,.20), transparent 62%);
}
.ga-stat:before {
    content:"";
    position:absolute;
    inset:0 auto 0 0;
    width:3px;
    background:linear-gradient(180deg, var(--cyan), var(--amber));
}
.ga-panel { padding:.85rem .95rem; }
.ga-stat b {
    display:block;
    font-family:var(--font-display);
    font-size:clamp(1.75rem, 3vw, 2.45rem);
    line-height:1.0;
    margin-bottom:.55rem;
    letter-spacing:0;
    position:relative;
    z-index:1;
}
.ga-stat span, .ga-muted { color:var(--muted); font-size:.88rem; position:relative; z-index:1; }
.ga-section-title {
    font-weight:760;
    margin:.1rem 0 .5rem;
    display:flex;
    align-items:center;
    gap:.45rem;
}
.ga-section-title:before {
    content:"";
    width:.55rem;
    height:.55rem;
    border-radius:999px;
    background:var(--amber);
}
.ga-row {
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:.8rem;
    border-top:1px solid var(--line);
    padding:.62rem 0;
}
.ga-row:first-child { border-top:0; }
.ga-pill-ok, .ga-pill-warn, .ga-pill-bad, .ga-pill-idle {
    display:inline-flex;
    border-radius:999px;
    padding:.22rem .55rem;
    font-size:.74rem;
    font-weight:720;
    white-space:nowrap;
    letter-spacing:0;
    font-family:var(--font-mono);
}
.ga-pill-ok { color:#f6fff8; background:var(--green); }
.ga-pill-warn { color:#211b0e; background:#efc56f; }
.ga-pill-bad { color:#fff8f6; background:var(--red); }
.ga-pill-idle { color:#21302c; background:#d9e4dc; }
.ga-code {
    font-family: var(--font-mono); font-size:.84rem;
    background:rgba(8,13,16,.72); color:var(--ink); border-radius:14px; padding:.8rem .85rem; overflow:auto;
    border:1px solid rgba(255,255,255,.08);
}
.ga-file-list { max-height: 560px; overflow:auto; padding-right:.35rem; }
.ga-small { font-size:.82rem; color:var(--muted); }
.stTabs [data-baseweb="tab-list"] {
    gap:.25rem;
    background:rgba(13,22,25,.68);
    border:1px solid var(--line);
    border-radius:18px;
    padding:.42rem;
    overflow-x:auto;
    box-shadow: var(--shadow);
}
.stTabs [data-baseweb="tab"] {
    border:1px solid transparent;
    background:transparent;
    border-radius:14px;
    padding:.52rem .85rem;
    min-height:42px;
    color:var(--muted);
    font-family:var(--font-display);
    font-weight:650;
}
.stTabs [aria-selected="true"] {
    background:linear-gradient(135deg, rgba(69,240,206,.20), rgba(255,179,92,.14)) !important;
    color:var(--ink) !important;
    border-color:rgba(69,240,206,.38) !important;
    box-shadow:0 12px 36px rgba(69,240,206,.08);
}
div[data-testid="stMetric"] {
    background:var(--panel);
    border:1px solid var(--line);
    border-radius:var(--radius);
    padding:.75rem .85rem;
    box-shadow: var(--shadow);
}
div[data-testid="stExpander"] {
    border:1px solid var(--line);
    border-radius:var(--radius);
    background:var(--panel);
}
.stButton button, .stDownloadButton button {
    min-height:44px !important;
    border-radius:14px !important;
    border:1px solid var(--line) !important;
    box-shadow:none !important;
    font-weight:650 !important;
}
.stTextInput input, textarea, [data-baseweb="select"] > div {
    min-height:44px !important;
    border-radius:14px !important;
    border-color:var(--line) !important;
}
pre {
    border-radius:var(--radius) !important;
    border:1px solid var(--line) !important;
}
[data-testid="stChatMessage"] {
    background:var(--panel);
    border:1px solid var(--line);
    border-radius:var(--radius);
    padding:.65rem .75rem;
}
@keyframes ga-enter {
    from { opacity:0; transform:translateY(10px); }
    to { opacity:1; transform:translateY(0); }
}
@keyframes ga-rise {
    from { opacity:0; transform:translateY(14px); }
    to { opacity:1; transform:translateY(0); }
}
@media (max-width: 900px) {
    .ga-grid { grid-template-columns: repeat(2, minmax(0,1fr)); }
    .ga-topline { grid-template-columns:1fr; padding:.75rem; }
    .ga-chipbox { justify-content:flex-start; max-width:100%; }
    .ga-stat { min-height:84px; }
}
@media (max-width: 560px) {
    .block-container { padding-top: 3.2rem; padding-left:.75rem; padding-right:.75rem; }
    .ga-grid { grid-template-columns: 1fr; }
    .ga-title-row { align-items:flex-start; }
    .ga-mark { width:38px; height:38px; }
    .ga-chip { width:100%; justify-content:space-between; }
}
</style>
"""


def project_path(*parts):
    return ROOT.joinpath(*parts)


def mask_value(key, value):
    if any(part in key.lower() for part in SENSITIVE_KEYS):
        text = str(value)
        if not text:
            return ""
        return text[:4] + "..." + text[-4:] if len(text) > 10 else "***"
    return value


def is_placeholder(value):
    if isinstance(value, str):
        return bool(PLACEHOLDER_PAT.search(value))
    if isinstance(value, dict):
        return any(is_placeholder(v) for v in value.values())
    if isinstance(value, (list, tuple)):
        return any(is_placeholder(v) for v in value)
    return False


@st.cache_data(show_spinner=False)
def parse_mykey():
    path = project_path("mykey.py")
    if not path.exists():
        return [], "missing"
    tree = ast.parse(path.read_text(encoding="utf-8"))
    items = []
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name):
                try:
                    value = ast.literal_eval(node.value)
                except Exception:
                    value = "<dynamic>"
                items.append({"name": target.id, "value": value, "line": node.lineno})
    return items, "ok"


def config_kind(name):
    low = name.lower()
    if "mixin" in low:
        return "Fallback"
    if "native" in low and "claude" in low:
        return "Native Claude"
    if "native" in low and "oai" in low:
        return "Native OpenAI"
    if "claude" in low:
        return "Claude Text"
    if "oai" in low:
        return "OpenAI Text"
    if any(k in low for k in ("tg_", "qq_", "fs_", "wecom", "dingtalk")):
        return "Bot"
    return "Runtime"


def active_llm_configs(configs):
    return [c for c in configs if any(x in c["name"].lower() for x in ("config", "cookie", "api"))]


def minimax_token_plan_config(configs):
    for cfg in configs:
        value = cfg.get("value")
        if not isinstance(value, dict):
            continue
        apibase = str(value.get("apibase", ""))
        model = str(value.get("model", ""))
        if "minimaxi.com" in apibase or "minimax.io" in apibase or model.lower().startswith("minimax-"):
            if value.get("apikey"):
                return cfg
    return None


def query_minimax_token_plan(api_key):
    url = "https://www.minimax.io/v1/token_plan/remains"
    response = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        timeout=20,
    )
    try:
        payload = response.json()
    except Exception:
        payload = {"raw": response.text[:2000]}
    return {
        "ok": response.ok,
        "status_code": response.status_code,
        "endpoint": url,
        "data": payload,
        "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def clean_workbench_reply(text):
    text = build_done_text(text)
    text = re.sub(r"\*\*LLM Running \(Turn \d+\) \.\.\.\*\*\s*", "", text)
    text = re.sub(r"```(?:\w+)?\s*\[Info\] Final response to user\.\s*```", "", text, flags=re.DOTALL)
    text = re.sub(r"\[Info\] Final response to user\.", "", text)
    text = re.sub(r"```[a-zA-Z0-9_-]*\s*```", "", text, flags=re.DOTALL)
    text = re.sub(r"```\s*```", "", text, flags=re.DOTALL)
    return re.sub(r"\n{3,}", "\n\n", text).strip() or "..."


def module_available(name):
    return importlib.util.find_spec(name) is not None


@st.cache_data(show_spinner=False)
def scan_files(rel_dir, patterns=("*",), limit=300):
    base = project_path(rel_dir)
    rows = []
    if not base.exists():
        return rows
    files = []
    for pattern in patterns:
        files.extend(base.rglob(pattern))
    for path in sorted({p for p in files if p.is_file()}, key=lambda p: p.stat().st_mtime, reverse=True)[:limit]:
        stat = path.stat()
        rows.append({
            "path": str(path.relative_to(ROOT)),
            "size": stat.st_size,
            "mtime": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
            "suffix": path.suffix.lower(),
        })
    return rows


@st.cache_data(show_spinner=False)
def read_text_file(rel_path, max_chars=50000):
    path = project_path(rel_path)
    if not path.exists() or not path.is_file():
        return ""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:
        return f"Unable to read file: {exc}"
    return text[:max_chars]


def estimate_tokens(chars):
    return max(1, int(chars / 3.2)) if chars else 0


def token_efficiency_snapshot(agent, mem_files, docs):
    source_files = [
        project_path("assets", "tools_schema.json"),
        project_path("assets", "sys_prompt_en.txt"),
        project_path("memory", "global_mem_insight.txt"),
        project_path("memory", "global_mem.txt"),
    ]
    chars = 0
    for path in source_files:
        if path.exists() and path.is_file():
            chars += path.stat().st_size
    l3_chars = sum(row["size"] for row in mem_files[:8])
    doc_chars = sum(len(page.get("body", "")) for page in docs[:4])
    working_tokens = estimate_tokens(chars + l3_chars + doc_chars)
    official_ceiling = 30000
    heavyweight_baseline = 200000
    saved_vs_baseline = max(0, 100 - round(working_tokens * 100 / heavyweight_baseline, 1))
    context_load = min(100, round(working_tokens * 100 / official_ceiling, 1))
    tool_cache_tokens = 0
    llmclient = getattr(agent, "llmclient", None) if agent else None
    if llmclient is not None:
        tool_cache_tokens = int(getattr(llmclient, "total_cd_tokens", 0) or 0)
    return {
        "working_tokens": working_tokens,
        "official_ceiling": official_ceiling,
        "baseline": heavyweight_baseline,
        "saved_vs_baseline": saved_vs_baseline,
        "context_load": context_load,
        "tool_cache_tokens": tool_cache_tokens,
    }


@st.cache_data(show_spinner=False)
def docs_index():
    path = project_path("docs", "zread-genericagent-documentation.md")
    if not path.exists():
        return []
    text = path.read_text(encoding="utf-8", errors="replace")
    matches = list(re.finditer(r"<!-- Page \d+: ([^>]+) -->\s*", text))
    pages = []
    for i, match in enumerate(matches):
        url = match.group(1)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = re.sub(r"\n---\s*$", "", text[match.end():end]).strip()
        title = next((line.lstrip("# ").strip() for line in body.splitlines() if line.startswith("# ")), url)
        pages.append({"title": title, "url": url, "body": body.strip()})
    return pages


@st.cache_resource(show_spinner=False)
def init_agent():
    try:
        agent = GeneraticAgent()
        if getattr(agent, "llmclient", None) is not None:
            threading.Thread(target=agent.run, daemon=True).start()
        return agent, None
    except Exception as exc:
        return None, str(exc)


def status_pill(ok, good="Ready", bad="Needs setup"):
    cls = "ga-pill-ok" if ok else "ga-pill-warn"
    return f'<span class="{cls}">{html.escape(good if ok else bad)}</span>'


def render_topline(agent, configs):
    llms = active_llm_configs(configs)
    current = "No LLM"
    runtime_ok = False
    if agent and getattr(agent, "llmclient", None) is not None:
        try:
            current = agent.get_llm_name(model=True)
            runtime_ok = True
        except Exception:
            current = "Configured"
            runtime_ok = True
    root_name = ROOT.name
    st.markdown(
        f"""
<div class="ga-topline">
  <div>
    <div class="ga-title-row">
      <div class="ga-mark">GA</div>
      <div>
        <div class="ga-title">GenericAgent Workbench</div>
        <div class="ga-subtitle">Local control plane for runtime, memory, docs, and frontends.</div>
      </div>
    </div>
    <div class="ga-path">{html.escape(str(ROOT))}</div>
  </div>
  <div class="ga-chipbox">
    <span class="ga-chip">Project: {html.escape(root_name)}</span>
    <span class="ga-chip">LLM configs: {len(llms)}</span>
    <span class="ga-chip"><span class="ga-dot" style="background:{'#24734b' if runtime_ok else '#b7791f'}"></span>{html.escape(current)}</span>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )


def render_dashboard(agent, agent_error, configs):
    mem_files = scan_files("memory", ("*.md", "*.py", "*.txt"))
    docs = docs_index()
    temp_logs = scan_files("temp", ("*.txt", "*.log", "*.json"), limit=50)
    deps = ["requests", "bs4", "bottle", "streamlit", "webview"]
    dep_ok = sum(1 for d in deps if module_available(d))
    llm_configs = active_llm_configs(configs)
    ready_configs = [c for c in llm_configs if not is_placeholder(c["value"])]
    agent_ok = agent is not None and getattr(agent, "llmclient", None) is not None
    token_eff = token_efficiency_snapshot(agent, mem_files, docs)

    st.markdown(
        f"""
<div class="ga-grid">
  <div class="ga-stat"><b>{'Online' if agent_ok else 'Setup'}</b><span>Runtime state</span></div>
  <div class="ga-stat"><b>{len(ready_configs)}/{len(llm_configs)}</b><span>Model routes ready</span></div>
  <div class="ga-stat"><b>{len(mem_files)}</b><span>Memory files indexed</span></div>
  <div class="ga-stat"><b>{len(docs)}</b><span>Docs pages archived</span></div>
</div>
""",
        unsafe_allow_html=True,
    )

    left, mid, right = st.columns([1.05, 1, 1.15])
    with left:
        st.markdown('<div class="ga-panel"><div class="ga-section-title">System Readiness</div>', unsafe_allow_html=True)
        rows = [
            ("Python", f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}", True),
            ("Core dependencies", f"{dep_ok}/{len(deps)} installed", dep_ok == len(deps)),
            ("mykey.py", "present" if project_path("mykey.py").exists() else "missing", project_path("mykey.py").exists()),
            ("Agent runtime", agent_error or ("ready" if agent_ok else "no usable LLM yet"), agent_ok),
        ]
        for label, value, ok in rows:
            st.markdown(
                f'<div class="ga-row"><div><b>{html.escape(label)}</b><div class="ga-small">{html.escape(str(value))}</div></div>{status_pill(ok)}</div>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)
    with mid:
        st.markdown('<div class="ga-panel"><div class="ga-section-title">Memory Layers</div>', unsafe_allow_html=True)
        memory_rows = [
            ("L1 insight", project_path("memory", "global_mem_insight.txt").exists()),
            ("L2 global memory", project_path("memory", "global_mem.txt").exists()),
            ("L3 SOPs", bool(scan_files("memory", ("*_sop.md", "*.md"), 100))),
            ("L4 archive", project_path("memory", "L4_raw_sessions").exists()),
        ]
        for label, ok in memory_rows:
            st.markdown(f'<div class="ga-row"><b>{label}</b>{status_pill(ok, "Found", "Missing")}</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with right:
        st.markdown('<div class="ga-panel"><div class="ga-section-title">Recent Activity</div>', unsafe_allow_html=True)
        recent = (temp_logs + mem_files)[:6]
        if not recent:
            st.caption("No runtime logs yet.")
        for row in recent:
            st.markdown(
                f'<div class="ga-row"><div><b>{html.escape(Path(row["path"]).name)}</b><div class="ga-small">{html.escape(row["path"])} · {row["mtime"]}</div></div></div>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

    render_token_efficiency(token_eff)
    render_minimax_quota(configs)


def render_token_efficiency(token_eff):
    st.markdown("### Token Efficiency")
    left, right = st.columns([1.1, 1.2])
    with left:
        st.markdown('<div class="ga-panel"><div class="ga-section-title">Official Claim Tracker</div>', unsafe_allow_html=True)
        rows = [
            ("Estimated active context", f'{token_eff["working_tokens"]:,} tokens'),
            ("Official target", f'< {token_eff["official_ceiling"]:,} tokens'),
            ("Context load", f'{token_eff["context_load"]}% of target'),
            ("Saved vs 200K baseline", f'~{token_eff["saved_vs_baseline"]}%'),
        ]
        for label, value in rows:
            st.markdown(
                f'<div class="ga-row"><b>{html.escape(label)}</b><span class="ga-small">{html.escape(value)}</span></div>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)
    with right:
        st.markdown('<div class="ga-panel"><div class="ga-section-title">Why It Saves Tokens</div>', unsafe_allow_html=True)
        mechanisms = [
            ("9 atomic tools", "Small tool schema keeps every turn lighter."),
            ("Layered memory", "L1/L2/L3/L4 load pointers first, details only when needed."),
            ("Compressed history", "Older thinking/tool blocks are compacted in llmcore.py."),
            ("Simplified browser HTML", "simphtml.py trims noisy DOM before web_scan returns it."),
        ]
        for label, value in mechanisms:
            st.markdown(
                f'<div class="ga-row"><div><b>{html.escape(label)}</b><div class="ga-small">{html.escape(value)}</div></div></div>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)


def render_minimax_quota(configs):
    cfg = minimax_token_plan_config(configs)
    st.markdown("### MiniMax Token Plan")
    if not cfg:
        st.info("No MiniMax Token Plan configuration was found in mykey.py.")
        return
    value = cfg["value"]
    left, right = st.columns([1, 1.4])
    with left:
        st.markdown('<div class="ga-panel"><div class="ga-section-title">Plan Route</div>', unsafe_allow_html=True)
        rows = [
            ("Config", cfg["name"]),
            ("Name", value.get("name", "")),
            ("Model", value.get("model", "")),
            ("Base URL", value.get("apibase", "")),
            ("API Key", mask_value("apikey", value.get("apikey", ""))),
        ]
        for label, row_value in rows:
            st.markdown(
                f'<div class="ga-row"><b>{html.escape(label)}</b><span class="ga-small">{html.escape(str(row_value))}</span></div>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)
    with right:
        if st.button("Query Token Plan Quota", use_container_width=True):
            with st.spinner("Querying MiniMax Token Plan quota..."):
                st.session_state.minimax_quota_result = query_minimax_token_plan(value["apikey"])
        result = st.session_state.get("minimax_quota_result")
        if result:
            status = "OK" if result.get("ok") else "Error"
            st.caption(f'{status} · HTTP {result.get("status_code")} · {result.get("checked_at")}')
            st.json(result.get("data", {}), expanded=True)
        else:
            st.caption("Click the button to query remaining Token Plan quota. This sends the configured key to MiniMax's official quota endpoint.")


def render_config(configs):
    llm_configs = active_llm_configs(configs)
    st.subheader("Configuration Center")
    st.caption("Sensitive values are masked. This page reads configuration only, so credentials do not get rewritten accidentally.")
    if not configs:
        st.warning("No mykey.py configuration values were found.")
        return
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Total values", len(configs))
    col_b.metric("LLM-related", len(llm_configs))
    col_c.metric("Placeholders", sum(1 for c in configs if is_placeholder(c["value"])))
    for cfg in configs:
        status = "Template" if is_placeholder(cfg["value"]) else "Configured"
        with st.expander(f'{cfg["name"]} · {config_kind(cfg["name"])} · line {cfg["line"]}', expanded=cfg in llm_configs):
            st.markdown(f'`Status:` **{status}**')
            value = cfg["value"]
            if isinstance(value, dict):
                masked = {k: mask_value(k, v) for k, v in value.items()}
                st.json(masked, expanded=True)
            else:
                st.code(str(mask_value(cfg["name"], value)))


def render_agent(agent, agent_error):
    st.subheader("Agent Workbench")
    if agent_error:
        st.error(f"Agent could not initialize: {agent_error}")
        return
    if agent is None or getattr(agent, "llmclient", None) is None:
        st.warning("No usable LLM session is active yet. Fill mykey.py, then restart the workbench.")
        return

    if "wb_messages" not in st.session_state:
        st.session_state.wb_messages = []
    st.session_state.setdefault("wb_streaming", False)
    st.session_state.setdefault("wb_queue", None)
    st.session_state.setdefault("wb_partial", "")
    st.session_state.setdefault("wb_reply_ts", "")

    side, main = st.columns([0.85, 2.15])
    with side:
        st.markdown("**Runtime**")
        st.write(f"Current LLM: `{agent.get_llm_name(model=True)}`")
        state_label = "Running" if agent.is_running or st.session_state.wb_streaming else "Ready"
        st.markdown(f"State: `{state_label}`")
        options = agent.list_llms()
        if options:
            labels = {idx: f"{idx}: {name}" for idx, name, _ in options}
            selected = st.selectbox("LLM route", [idx for idx, _, _ in options], index=next((i for i, (idx, _, _) in enumerate(options) if idx == agent.llm_no), 0), format_func=labels.get)
            if selected != agent.llm_no:
                agent.next_llm(selected)
                st.rerun()
        c1, c2 = st.columns(2)
        if c1.button("/new", use_container_width=True):
            st.session_state.wb_messages.clear()
            agent.history = []
            st.rerun()
        if c2.button("/status", use_container_width=True):
            st.session_state.wb_messages.append({"role": "user", "content": "/status", "time": datetime.now().strftime("%H:%M:%S")})
            st.session_state.wb_queue = agent.put_task("/status", source="user")
            st.session_state.wb_streaming = True
            st.session_state.wb_reply_ts = datetime.now().strftime("%H:%M:%S")
            st.rerun()
        if st.button("Stop current task", use_container_width=True):
            agent.abort()
            st.toast("Stop signal sent.")
        restore, err = format_restore()
        if err:
            st.caption(err)
        else:
            _, filename, count = restore
            st.caption(f"Recoverable: {filename}, {count} turns")

    with main:
        for msg in st.session_state.wb_messages:
            with st.chat_message(msg["role"]):
                st.caption(msg.get("time", ""))
                st.markdown(msg["content"])
        if st.session_state.wb_streaming and st.session_state.wb_queue is not None:
            q = st.session_state.wb_queue
            done = False
            for _ in range(24):
                try:
                    item = q.get_nowait()
                except queue.Empty:
                    break
                if "next" in item:
                    st.session_state.wb_partial = item["next"]
                if "done" in item:
                    st.session_state.wb_partial = clean_workbench_reply(item["done"])
                    done = True
                    break
            if done:
                st.session_state.wb_partial = clean_workbench_reply(st.session_state.wb_partial)
            if not done and not agent.is_running and q.empty() and st.session_state.wb_partial:
                st.session_state.wb_partial = clean_workbench_reply(st.session_state.wb_partial)
                done = True
            with st.chat_message("assistant"):
                st.caption(st.session_state.wb_reply_ts)
                st.markdown(st.session_state.wb_partial + ("" if done else "\n\n`running...`"))
            if done:
                st.session_state.wb_messages.append({"role": "assistant", "content": st.session_state.wb_partial, "time": st.session_state.wb_reply_ts})
                st.session_state.wb_streaming = False
                st.session_state.wb_queue = None
                st.session_state.wb_partial = ""
                st.rerun()
            else:
                time.sleep(0.25)
                st.rerun()

        prompt = st.chat_input("Send a task or command", disabled=st.session_state.wb_streaming)
        if prompt:
            st.session_state.wb_messages.append({"role": "user", "content": prompt, "time": datetime.now().strftime("%H:%M:%S")})
            st.session_state.wb_queue = agent.put_task(prompt, source="user")
            st.session_state.wb_streaming = True
            st.session_state.wb_reply_ts = datetime.now().strftime("%H:%M:%S")
            st.session_state.wb_partial = ""
            st.rerun()


def render_capability_map():
    st.subheader("Capability Map")
    left, right = st.columns([1.2, 1])
    with left:
        st.markdown('<div class="ga-panel"><div class="ga-section-title">Atomic Tool Surface</div>', unsafe_allow_html=True)
        for name, desc in ATOMIC_TOOLS:
            st.markdown(f'<div class="ga-row"><div><b><code>{name}</code></b><div class="ga-small">{html.escape(desc)}</div></div></div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with right:
        st.markdown('<div class="ga-panel"><div class="ga-section-title">Execution Pattern</div>', unsafe_allow_html=True)
        st.markdown(
            """
<div class="ga-code">Perceive environment<br>Reason over task<br>Call atomic tools<br>Verify result<br>Crystallize useful path into memory</div>
""",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("**System reach**")
        st.write("Browser session, terminal, filesystem, keyboard/mouse, screen vision, ADB, bot channels, scheduled reflection.")


def render_memory():
    st.subheader("Memory and Skill Browser")
    files = scan_files("memory", ("*.md", "*.py", "*.txt"), limit=500)
    query = st.text_input("Filter memory files", placeholder="sop, tmwebdriver, global, skill...")
    filtered = [f for f in files if query.lower() in f["path"].lower()] if query else files
    left, right = st.columns([0.9, 1.6])
    with left:
        st.markdown('<div class="ga-file-list">', unsafe_allow_html=True)
        selected = st.radio("Files", [f["path"] for f in filtered] or ["No files"], label_visibility="collapsed")
        st.markdown("</div>", unsafe_allow_html=True)
    with right:
        if selected != "No files":
            st.caption(selected)
            text = read_text_file(selected)
            st.code(text, language="markdown" if selected.endswith(".md") else "python" if selected.endswith(".py") else "text")


def render_frontends(configs):
    st.subheader("Frontend and Channel Manager")
    cfg_names = {c["name"] for c in configs}
    for name, rel, cmd, deps, required_cfg in FRONTENDS:
        exists = project_path(rel).exists()
        deps_ok = [d for d in deps if module_available(d)]
        cfg_ok = [c for c in required_cfg if c in cfg_names]
        with st.expander(name, expanded=name in {"Desktop Launcher", "Workbench", "Streamlit Chat"}):
            a, b, c = st.columns(3)
            a.markdown(status_pill(exists, "Entry found", "Missing"), unsafe_allow_html=True)
            b.markdown(status_pill(len(deps_ok) == len(deps), f"Deps {len(deps_ok)}/{len(deps)}", f"Deps {len(deps_ok)}/{len(deps)}"), unsafe_allow_html=True)
            c.markdown(status_pill(len(cfg_ok) == len(required_cfg), f"Config {len(cfg_ok)}/{len(required_cfg)}", f"Config {len(cfg_ok)}/{len(required_cfg)}"), unsafe_allow_html=True)
            st.code(cmd, language="powershell")
            if required_cfg:
                st.caption("Required config: " + ", ".join(required_cfg))


def render_docs():
    st.subheader("Documentation Center")
    pages = docs_index()
    if not pages:
        st.warning("Zread documentation archive was not found in docs/.")
        return
    titles = [f'{i + 1}. {p["title"]}' for i, p in enumerate(pages)]
    selected = st.selectbox("Page", titles)
    page = pages[titles.index(selected)]
    st.caption(page["url"])
    st.markdown(page["body"])


def render_logs():
    st.subheader("Logs and Sessions")
    files = scan_files("temp", ("*.txt", "*.log", "*.json"), limit=300)
    if not files:
        st.info("No temp logs yet. Agent runtime logs will appear here after tasks run.")
        return
    selected = st.selectbox("Runtime file", [f["path"] for f in files])
    st.caption(selected)
    st.code(read_text_file(selected), language="text")


def main():
    st.markdown(CSS, unsafe_allow_html=True)
    configs, _ = parse_mykey()
    agent, agent_error = init_agent()
    render_topline(agent, configs)

    with st.sidebar:
        st.markdown("### Workbench")
        st.caption("GenericAgent local control plane")
        st.divider()
        if st.button("Refresh scans", use_container_width=True):
            st.cache_data.clear()
            st.rerun()

    tabs = st.tabs(["Dashboard", "Agent", "Config", "Capabilities", "Memory", "Frontends", "Docs", "Logs"])
    with tabs[0]:
        render_dashboard(agent, agent_error, configs)
    with tabs[1]:
        render_agent(agent, agent_error)
    with tabs[2]:
        render_config(configs)
    with tabs[3]:
        render_capability_map()
    with tabs[4]:
        render_memory()
    with tabs[5]:
        render_frontends(configs)
    with tabs[6]:
        render_docs()
    with tabs[7]:
        render_logs()


if __name__ == "__main__":
    main()
