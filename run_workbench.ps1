Set-Location -Path $PSScriptRoot
& "$PSScriptRoot\.venv\Scripts\streamlit.exe" run "$PSScriptRoot\frontends\workbench.py" --server.port 8502
