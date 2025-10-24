# ========================================
# Dashboard Environment Verification Script
# ========================================
# Purpose: Verify all dependencies are installed and configured correctly
# Usage: powershell -ExecutionPolicy Bypass -File scripts/verify-environment.ps1
# Platform: Windows, Mac (with PowerShell Core), Linux (with PowerShell Core)

param(
    [switch]$Verbose = $false,
    [switch]$FixMissing = $false,
    [switch]$SkipPip = $false
)

$ErrorActionPreference = "Continue"
$WarningPreference = "Continue"

# Colors for output
$colors = @{
    Success = "Green"
    Error = "Red"
    Warning = "Yellow"
    Info = "Cyan"
    Header = "Magenta"
}

function Write-Status {
    param(
        [string]$Status,
        [string]$Message,
        [ValidateSet("Success", "Error", "Warning", "Info", "Header")]
        [string]$Type = "Info"
    )
    
    $icon = @{
        Success = "✓"
        Error = "✗"
        Warning = "⚠"
        Info = "ℹ"
        Header = "═"
    }[$Type]
    
    Write-Host "$icon $Status" -ForegroundColor $colors[$Type] -NoNewline
    if ($Message) {
        Write-Host " - $Message" -ForegroundColor White
    } else {
        Write-Host
    }
}

function Check-Command {
    param(
        [string]$Command,
        [string]$DisplayName,
        [string]$MinVersion = $null,
        [string]$CheckArgs = "--version"
    )
    
    try {
        $result = & $Command $CheckArgs 2>&1 | Select-Object -First 1
        
        if ($result) {
            Write-Status "$DisplayName" "$result" "Success"
            return $true
        } else {
            Write-Status "$DisplayName" "Not found" "Error"
            return $false
        }
    } catch {
        Write-Status "$DisplayName" "Not found or inaccessible" "Error"
        return $false
    }
}

# ========================================
# MAIN VERIFICATION
# ========================================

Write-Host
Write-Host "╔════════════════════════════════════════════════════════╗" -ForegroundColor $colors.Header
Write-Host "║   Dashboard Environment Verification                  ║" -ForegroundColor $colors.Header
Write-Host "║   $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')                           ║" -ForegroundColor $colors.Header
Write-Host "╚════════════════════════════════════════════════════════╝" -ForegroundColor $colors.Header
Write-Host

# Track results
$checklist = @{
    Git = $false
    Python = $false
    Node = $false
    Npm = $false
    BuildScript = $false
    TestScript = $false
    SourceFiles = $false
}

# ========================================
# 1. Check Git
# ========================================
Write-Host "1️⃣  Git Installation" -ForegroundColor $colors.Header
Write-Host "─────────────────────────────────────────────────────────" -ForegroundColor Gray

$checklist.Git = Check-Command "git" "Git"

# ========================================
# 2. Check Python
# ========================================
Write-Host
Write-Host "2️⃣  Python Installation" -ForegroundColor $colors.Header
Write-Host "─────────────────────────────────────────────────────────" -ForegroundColor Gray

$checklist.Python = Check-Command "python" "Python"

if ($checklist.Python) {
    try {
        $pythonVersion = python --version 2>&1
        if ($pythonVersion -match "3\.1[1-9]|3\.[2-9]") {
            Write-Status "Python Version" "Compatible ($pythonVersion)" "Success"
        } elseif ($pythonVersion -match "3\.[9]") {
            Write-Status "Python Version" "OK ($pythonVersion)" "Success"
        } else {
            Write-Status "Python Version" "Older than 3.9 ($pythonVersion) - Consider upgrading" "Warning"
        }
    } catch {
        Write-Status "Python Version Check" "Could not determine version" "Warning"
    }
    
    # Check pip
    try {
        $pipVersion = pip --version 2>&1
        Write-Status "pip" "$pipVersion" "Success"
    } catch {
        Write-Status "pip" "Could not verify" "Error"
    }
}

# ========================================
# 3. Check Node.js & npm
# ========================================
Write-Host
Write-Host "3️⃣  Node.js & npm Installation (for testing)" -ForegroundColor $colors.Header
Write-Host "─────────────────────────────────────────────────────────" -ForegroundColor Gray

$checklist.Node = Check-Command "node" "Node.js"
$checklist.Npm = Check-Command "npm" "npm"

if ($checklist.Npm) {
    try {
        $npmVersion = npm --version 2>&1
        Write-Status "npm Version" "$npmVersion" "Success"
    } catch {
        Write-Status "npm Version" "Could not determine" "Warning"
    }
}

# ========================================
# 4. Check Build Script
# ========================================
Write-Host
Write-Host "4️⃣  Build Configuration" -ForegroundColor $colors.Header
Write-Host "─────────────────────────────────────────────────────────" -ForegroundColor Gray

$buildScript = "build/build_enhanced_dashboard.py"
if (Test-Path $buildScript) {
    Write-Status "Build Script" "Found at $buildScript" "Success"
    $checklist.BuildScript = $true
} else {
    Write-Status "Build Script" "Not found at $buildScript" "Error"
}

# ========================================
# 5. Check Source Files
# ========================================
Write-Host
Write-Host "5️⃣  Source Files" -ForegroundColor $colors.Header
Write-Host "─────────────────────────────────────────────────────────" -ForegroundColor Gray

$sourceDir = "src/modules"
if (Test-Path $sourceDir) {
    $moduleCount = (Get-ChildItem -Path $sourceDir -Filter "*.js").Count
    Write-Status "Source Modules" "Found $moduleCount .js files" "Success"
    $checklist.SourceFiles = $true
} else {
    Write-Status "Source Modules" "Directory not found" "Error"
}

# ========================================
# 6. Check Distribution
# ========================================
Write-Host
Write-Host "6️⃣  Distribution Files" -ForegroundColor $colors.Header
Write-Host "─────────────────────────────────────────────────────────" -ForegroundColor Gray

$distFile = "dist/dashboard_enhanced.html"
if (Test-Path $distFile) {
    $size = (Get-Item $distFile).Length / 1MB
    Write-Status "Distribution" "Found ($('{0:F2}' -f $size) MB)" "Success"
} else {
    Write-Status "Distribution" "Not found - run build script" "Warning"
}

# ========================================
# 7. Check Test Configuration
# ========================================
Write-Host
Write-Host "7️⃣  Test Configuration" -ForegroundColor $colors.Header
Write-Host "─────────────────────────────────────────────────────────" -ForegroundColor Gray

if ((Test-Path "jest.config.js") -and (Test-Path "tests/")) {
    Write-Status "Jest Configuration" "Found" "Success"
    $testCount = (Get-ChildItem -Path "tests/" -Filter "*.test.js" -Recurse).Count
    Write-Status "Test Files" "Found $testCount test files" "Success"
    $checklist.TestScript = $true
} else {
    Write-Status "Jest Configuration" "Not properly configured" "Warning"
}

# ========================================
# 8. Check Repository Status
# ========================================
Write-Host
Write-Host "8️⃣  Repository Status" -ForegroundColor $colors.Header
Write-Host "─────────────────────────────────────────────────────────" -ForegroundColor Gray

try {
    $gitStatus = git status --porcelain 2>&1 | Measure-Object -Line
    if ($gitStatus.Lines -eq 0) {
        Write-Status "Git Status" "Clean (no uncommitted changes)" "Success"
    } else {
        Write-Status "Git Status" "$($gitStatus.Lines) files with changes" "Warning"
    }
} catch {
    Write-Status "Git Status" "Could not check" "Warning"
}

# ========================================
# SUMMARY
# ========================================
Write-Host
Write-Host "╔════════════════════════════════════════════════════════╗" -ForegroundColor $colors.Header
Write-Host "║                    SUMMARY                             ║" -ForegroundColor $colors.Header
Write-Host "╚════════════════════════════════════════════════════════╝" -ForegroundColor $colors.Header
Write-Host

$passedChecks = ($checklist.Values | Where-Object { $_ -eq $true }).Count
$totalChecks = $checklist.Count

Write-Host "Passed: " -NoNewline
Write-Host "$passedChecks/$totalChecks" -ForegroundColor Green

if ($passedChecks -eq $totalChecks) {
    Write-Host
    Write-Status "Environment" "ALL CHECKS PASSED ✓ Ready to work!" "Success"
    exit 0
} elseif ($passedChecks -ge ($totalChecks - 2)) {
    Write-Host
    Write-Status "Environment" "MOSTLY READY - Some optional components missing" "Warning"
    exit 0
} else {
    Write-Host
    Write-Status "Environment" "MISSING CRITICAL COMPONENTS - See above for details" "Error"
    exit 1
}
