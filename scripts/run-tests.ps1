# ========================================
# Dashboard Test Runner Script
# ========================================
# Purpose: Automate running Jest tests with coverage and reporting
# Usage: powershell -ExecutionPolicy Bypass -File scripts/run-tests.ps1
# Platform: Windows, Mac (with PowerShell Core), Linux (with PowerShell Core)

param(
    [switch]$Coverage = $false,
    [switch]$Watch = $false,
    [switch]$Verbose = $false,
    [switch]$UpdateSnapshots = $false,
    [string]$TestName = "",
    [switch]$ShowBrowser = $false
)

$ErrorActionPreference = "Continue"

# Colors for output
$colors = @{
    Success = "Green"
    Error = "Red"
    Warning = "Yellow"
    Info = "Cyan"
    Header = "Magenta"
    Progress = "Blue"
}

function Write-Status {
    param(
        [string]$Status,
        [string]$Message = "",
        [ValidateSet("Success", "Error", "Warning", "Info", "Header", "Progress")]
        [string]$Type = "Info"
    )
    
    $icon = @{
        Success = "✓"
        Error = "✗"
        Warning = "⚠"
        Info = "ℹ"
        Header = "═"
        Progress = "→"
    }[$Type]
    
    Write-Host "$icon $Status" -ForegroundColor $colors[$Type] -NoNewline
    if ($Message) {
        Write-Host " - $Message" -ForegroundColor White
    } else {
        Write-Host
    }
}

function Test-Prerequisites {
    Write-Status "Checking" "Prerequisites..." "Progress"
    Write-Host "─────────────────────────────────────────────────────────" -ForegroundColor Gray
    
    # Check npm
    try {
        $npmVersion = npm --version 2>&1
        Write-Status "npm" "$npmVersion" "Success"
    } catch {
        Write-Status "npm" "Not found - Install Node.js" "Error"
        exit 1
    }
    
    # Check jest
    try {
        $jestVersion = npx jest --version 2>&1
        Write-Status "Jest" "$jestVersion" "Success"
    } catch {
        Write-Status "Jest" "Not installed" "Warning"
        Write-Host
        Write-Status "Installing" "Jest and dependencies..."
        npm install
    }
    
    # Check test files
    $testCount = (Get-ChildItem -Path "tests/" -Filter "*.test.js" -Recurse -ErrorAction SilentlyContinue).Count
    if ($testCount -gt 0) {
        Write-Status "Test Files" "Found $testCount test files" "Success"
    } else {
        Write-Status "Test Files" "No tests found in tests/ directory" "Warning"
    }
}

function Build-TestCommand {
    $cmd = "npm test"
    
    if ($Coverage) {
        $cmd += " -- --coverage"
    }
    
    if ($Watch) {
        $cmd += " -- --watch"
    }
    
    if ($UpdateSnapshots) {
        $cmd += " -- --updateSnapshot"
    }
    
    if ($TestName) {
        $cmd += " -- --testNamePattern=$TestName"
    }
    
    if ($Verbose) {
        $cmd += " -- --verbose"
    }
    
    return $cmd
}

function Run-Tests {
    param(
        [string]$Command
    )
    
    Write-Host
    Write-Status "Running" "Tests..." "Progress"
    Write-Host "─────────────────────────────────────────────────────────" -ForegroundColor Gray
    Write-Host "Command: $Command" -ForegroundColor Gray
    Write-Host
    
    $startTime = Get-Date
    
    try {
        # Run the tests
        Invoke-Expression $Command
        $exitCode = $LASTEXITCODE
        
        $endTime = Get-Date
        $duration = ($endTime - $startTime).TotalSeconds
        
        Write-Host
        Write-Host "─────────────────────────────────────────────────────────" -ForegroundColor Gray
        Write-Status "Duration" "$('{0:F2}' -f $duration) seconds" "Info"
        
        return $exitCode
    } catch {
        Write-Status "Test Execution" "Exception: $_" "Error"
        return 1
    }
}

function Show-CoverageReport {
    if (Test-Path "coverage/index.html") {
        Write-Host
        Write-Status "Coverage Report" "Generated at coverage/index.html" "Success"
        
        if ($ShowBrowser) {
            Write-Status "Opening" "Coverage report in browser..."
            $coverageFile = (Resolve-Path "coverage/index.html").Path
            try {
                Start-Process $coverageFile
                Write-Status "Browser" "Opened" "Success"
            } catch {
                Write-Status "Browser" "Could not open: $_" "Warning"
            }
        }
    }
}

function Show-Summary {
    param(
        [int]$ExitCode
    )
    
    Write-Host
    Write-Host "╔════════════════════════════════════════════════════════╗" -ForegroundColor $colors.Header
    
    if ($ExitCode -eq 0) {
        Write-Host "║           ✓ ALL TESTS PASSED                          ║" -ForegroundColor $colors.Header
        Write-Host "╚════════════════════════════════════════════════════════╝" -ForegroundColor $colors.Header
        Write-Host
        Write-Status "Status" "Tests are passing - Good to commit!" "Success"
    } else {
        Write-Host "║           ✗ TESTS FAILED                              ║" -ForegroundColor $colors.Header
        Write-Host "╚════════════════════════════════════════════════════════╝" -ForegroundColor $colors.Header
        Write-Host
        Write-Status "Status" "Fix failing tests before committing" "Error"
    }
    
    Write-Host
    Write-Status "Next Steps" "1. Review test output above"
    if ($Coverage) {
        Write-Status "Next Steps" "2. Check coverage report"
    }
    Write-Status "Next Steps" "3. Run: powershell scripts/build-dashboard.ps1"
    Write-Status "Next Steps" "4. Test in browser"
    Write-Host
}

# ========================================
# MAIN EXECUTION
# ========================================

Write-Host
Write-Host "╔════════════════════════════════════════════════════════╗" -ForegroundColor $colors.Header
Write-Host "║        Dashboard Test Runner                          ║" -ForegroundColor $colors.Header
Write-Host "║        $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')                           ║" -ForegroundColor $colors.Header
Write-Host "╚════════════════════════════════════════════════════════╝" -ForegroundColor $colors.Header

Write-Host
Write-Status "Configuration" ""
Write-Host "─────────────────────────────────────────────────────────" -ForegroundColor Gray
Write-Status "Coverage" if($Coverage) { "Enabled" } else { "Disabled" }
Write-Status "Watch Mode" if($Watch) { "Enabled" } else { "Disabled" }
Write-Status "Verbose" if($Verbose) { "Enabled" } else { "Disabled" }

if ($TestName) {
    Write-Status "Filter" "Running tests matching: $TestName"
}

# Test prerequisites
Write-Host
Test-Prerequisites

# Build command
$testCommand = Build-TestCommand

# Run tests
$result = Run-Tests -Command $testCommand

# Show coverage report if generated
if ($Coverage) {
    Show-CoverageReport
}

# Show summary
Show-Summary -ExitCode $result

exit $result
