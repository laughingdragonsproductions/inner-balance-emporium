# InnerBalancEmporium — Google Flow image generation (Chrome Profile 8 CDP).
param(
    [switch]$LiveFlow,
    [string]$Priority = "",
    [int]$Max = 3,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$Scripts = Join-Path $Root "scripts"
$DesktopScripts = "G:\LocalAIagent\desktop-agent\scripts"
$Config = Join-Path $Root "flow\ibe-flow-pipeline.config.json"

Write-Host "1/4 Mock crops from Eyvette reference PNGs..."
python (Join-Path $Scripts "prepare_mock_crops.py")

Write-Host "2/4 Build Flow job JSON..."
$buildArgs = @("--config", $Config, "--max", $Max)
if ($Priority) { $buildArgs += @("--priority", $Priority) }
if ($DryRun) { $buildArgs += "--dry-run" }
python (Join-Path $Scripts "build_ibe_flow_jobs.py") @buildArgs

if ($DryRun) { exit 0 }

if ($LiveFlow) {
    Write-Host "3/4 Submit to Google Flow (Chrome CDP on :9334)..."
    if (-not (Test-NetConnection 127.0.0.1 -Port 9334 -WarningAction SilentlyContinue).TcpTestSucceeded) {
        Write-Host "Starting Chrome Flow debug profile..."
        & (Join-Path $DesktopScripts "start-chrome-flow-debug.ps1")
        Start-Sleep -Seconds 4
    }
    py -3 (Join-Path $DesktopScripts "submit_google_flow_images.py") --config $Config --max $Max --no-apply --no-rebuild
    Write-Host "4/4 Convert Flow PNGs to JPG for site..."
    python (Join-Path $Scripts "sync_flow_images.py")
} else {
    Write-Host "3/4 Skipping live Flow (use -LiveFlow). Mock crops are in assets/images/."
    Write-Host "4/4 Regenerate HTML..."
}

python (Join-Path $Root "generate_pages.py")
Write-Host "Done. Redeploy: npx wrangler pages deploy . --project-name=inner-balance-emporium --branch=main"
