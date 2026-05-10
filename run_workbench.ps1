Set-Location -Path $PSScriptRoot

$TempDir = Join-Path $PSScriptRoot "temp"
New-Item -ItemType Directory -Force -Path $TempDir | Out-Null

$LogFile = Join-Path $TempDir "workbench.log"
$ErrFile = Join-Path $TempDir "workbench.err.log"
$PidFile = Join-Path $TempDir "workbench.pid"

Get-CimInstance Win32_Process |
    Where-Object { $_.CommandLine -like "*frontends*workbench.py*" -or $_.CommandLine -like "*--server.port 8502*" } |
    ForEach-Object {
        try { Stop-Process -Id $_.ProcessId -Force -ErrorAction Stop } catch {}
    }

"[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] Starting GenericAgent Workbench on http://localhost:8502/" |
    Set-Content -Path $LogFile -Encoding UTF8

$Python = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
$Args = @(
    "-m", "streamlit", "run", "$PSScriptRoot\frontends\workbench.py",
    "--server.port", "8502",
    "--server.headless", "true"
)

$Process = Start-Process -FilePath $Python `
    -ArgumentList $Args `
    -WorkingDirectory $PSScriptRoot `
    -WindowStyle Hidden `
    -RedirectStandardOutput $LogFile `
    -RedirectStandardError $ErrFile `
    -PassThru

$Process.Id | Set-Content -Path $PidFile -Encoding ASCII
Write-Host "GenericAgent Workbench started: http://localhost:8502/"
Write-Host "PID: $($Process.Id)"
Write-Host "Log: $LogFile"
Write-Host "Error log: $ErrFile"
