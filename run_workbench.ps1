Set-Location -Path $PSScriptRoot

$TempDir = Join-Path $PSScriptRoot "temp"
New-Item -ItemType Directory -Force -Path $TempDir | Out-Null

$LogFile = Join-Path $TempDir "workbench.log"
$ErrFile = Join-Path $TempDir "workbench.err.log"
$PidFile = Join-Path $TempDir "workbench.pid"
$PortFile = Join-Path $TempDir "workbench.port"
$RequestedPort = if ($args.Count -gt 0) { [int]$args[0] } elseif ($env:GA_WORKBENCH_PORT) { [int]$env:GA_WORKBENCH_PORT } else { 8502 }

Get-CimInstance Win32_Process |
    Where-Object { $_.CommandLine -like "*frontends*workbench.py*" } |
    ForEach-Object {
        try { Stop-Process -Id $_.ProcessId -Force -ErrorAction Stop } catch {}
    }

$Port = $RequestedPort
while (Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue) {
    $Port += 1
    if ($Port -gt ($RequestedPort + 20)) {
        throw "No available port found from $RequestedPort to $Port."
    }
}

"[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] Starting GenericAgent Workbench on http://localhost:$Port/" |
    Set-Content -Path $LogFile -Encoding UTF8
$Port | Set-Content -Path $PortFile -Encoding ASCII

$Python = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"
$Args = @(
    "-m", "streamlit", "run", "$PSScriptRoot\frontends\workbench.py",
    "--server.port", "$Port",
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
Write-Host "GenericAgent Workbench started: http://localhost:$Port/"
Write-Host "PID: $($Process.Id)"
Write-Host "Port: $Port"
Write-Host "Log: $LogFile"
Write-Host "Error log: $ErrFile"
