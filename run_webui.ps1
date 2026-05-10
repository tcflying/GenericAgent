Set-Location -Path $PSScriptRoot

$TempDir = Join-Path $PSScriptRoot "temp"
New-Item -ItemType Directory -Force -Path $TempDir | Out-Null

$LogFile = Join-Path $TempDir "webui.log"
$ErrFile = Join-Path $TempDir "webui.err.log"

"[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] Starting GenericAgent Streamlit chat UI" |
    Set-Content -Path $LogFile -Encoding UTF8

Start-Process -FilePath "$PSScriptRoot\.venv\Scripts\python.exe" `
    -ArgumentList @("-m", "streamlit", "run", "$PSScriptRoot\frontends\stapp2.py", "--server.headless", "true") `
    -WorkingDirectory $PSScriptRoot `
    -WindowStyle Hidden `
    -RedirectStandardOutput $LogFile `
    -RedirectStandardError $ErrFile

Write-Host "GenericAgent Streamlit chat UI started."
Write-Host "Log: $LogFile"
Write-Host "Error log: $ErrFile"
