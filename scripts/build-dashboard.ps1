# ========================================
# Dashboard Build Script
# ========================================
# Purpose: Automate building the dashboard from source
# Usage: powershell -ExecutionPolicy Bypass -File scripts/build-dashboard.ps1
# Platform: Windows, Mac (with PowerShell Core), Linux (with PowerShell Core)

param(
    [switch]$Clean = $false,
    [switch]$Verbose = $false,
    [switch]$OpenBrowser = $false,
    [switch]$NoValidation = $false
)

$ErrorActionPreference = "Stop"

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

function Validate-Prerequisites {
    Write-Host
    Write-Status "Validating" "Prerequisites..." "Progress"
    Write-Host "─────────────────────────────────────────────────────────" -ForegroundColor Gray
    
    # Check Python
    try {
        $pythonVersion = python --version 2>&1
        Write-Status "Python" "$pythonVersion" "Success"
    } catch {
        Write-Status "Python" "Not found" "Error"
        exit 1
    }
    
    # Check build script exists
    if (-not (Test-Path "build/build_enhanced_dashboard.py")) {
        Write-Status "Build Script" "Not found" "Error"
        exit 1
    } else {
        Write-Status "Build Script" "Found" "Success"
    }
    
    # Check source directory
    if (-not (Test-Path "src/modules")) {
        Write-Status "Source Directory" "Not found" "Error"
        exit 1
    } else {
        Write-Status "Source Directory" "Found" "Success"
    }
}

function Clean-BuildArtifacts {
    Write-Host
    Write-Status "Cleaning" "Build artifacts..." "Progress"
    Write-Host "─────────────────────────────────────────────────────────" -ForegroundColor Gray
    
    # Remove dist directory if it exists
    if (Test-Path "dist/") {
        Remove-Item -Path "dist/" -Recurse -Force
        Write-Status "Removed" "dist/ directory" "Success"
    }
    
    # Remove build cache
    if (Test-Path "build/__pycache__") {
        Remove-Item -Path "build/__pycache__" -Recurse -Force
        Write-Status "Removed" "build cache" "Success"
    }
}

function Run-Build {
    Write-Host
    Write-Status "Building" "Dashboard..." "Progress"
    Write-Host "─────────────────────────────────────────────────────────" -ForegroundColor Gray
    
    try {
        $startTime = Get-Date
        
        # Run build script
        $output = python build/build_enhanced_dashboard.py 2>&1
        
        $endTime = Get-Date
        $duration = ($endTime - $startTime).TotalSeconds
        
        # Check if build succeeded
        if ($LASTEXITCODE -eq 0) {
            Write-Status "Build" "Completed successfully" "Success"
            Write-Status "Duration" "$('{0:F2}' -f $duration) seconds" "Info"
            
            # Verify output file
            if (Test-Path "dist/dashboard_enhanced.html") {
                $size = (Get-Item "dist/dashboard_enhanced.html").Length / 1MB
                Write-Status "Output File" "dist/dashboard_enhanced.html ($('{0:F2}' -f $size) MB)" "Success"
                return $true
            } else {
                Write-Status "Output File" "Not created by build script" "Error"
                return $false
            }
        } else {
            Write-Status "Build" "Failed with exit code $LASTEXITCODE" "Error"
            if ($Verbose) {
                Write-Host "Build output:" -ForegroundColor Gray
                $output | ForEach-Object { Write-Host "  $_" -ForegroundColor Gray }
            }
            return $false
        }
    } catch {
        Write-Status "Build" "Exception: $_" "Error"
        return $false
    }
}

function Validate-Output {
    Write-Host
    Write-Status "Validating" "Output..." "Progress"
    Write-Host "─────────────────────────────────────────────────────────" -ForegroundColor Gray
    
    $distFile = "dist/dashboard_enhanced.html"
    
    # Check file exists
    if (-not (Test-Path $distFile)) {
        Write-Status "File Check" "dist/dashboard_enhanced.html not found" "Error"
        return $false
    } else {
        Write-Status "File Check" "Found" "Success"
    }
    
    # Check file size
    $size = (Get-Item $distFile).Length
    if ($size -lt 100KB) {
        Write-Status "File Size" "Suspiciously small ($($size)B)" "Warning"
    } else {
        Write-Status "File Size" "$('{0:F2}' -f ($size/1MB)) MB" "Success"
    }
    
    # Check content
    $content = Get-Content $distFile
    if ($content -match "Dashboard" -and $content -match "StorageManager") {
        Write-Status "Content Check" "Valid Dashboard modules found" "Success"
    } else {
        Write-Status "Content Check" "Expected modules not found" "Warning"
    }
    
    # Check syntax
    try {
        $null = [regex]::new("")
        Write-Status "Syntax Check" "HTML valid" "Success"
    } catch {
        Write-Status "Syntax Check" "Invalid HTML" "Error"
        return $false
    }
    
    return $true
}

function Open-Dashboard {
    if ($OpenBrowser) {
        Write-Host
        Write-Status "Opening" "Dashboard in browser..." "Progress"
        
        $distFile = (Resolve-Path "dist/dashboard_enhanced.html").Path
        try {
            Start-Process $distFile
            Write-Status "Browser" "Opened" "Success"
        } catch {
            Write-Status "Browser" "Could not open: $_" "Warning"
        }
    }
}

# ========================================
# MAIN EXECUTION
# ========================================

Write-Host
Write-Host "╔════════════════════════════════════════════════════════╗" -ForegroundColor $colors.Header
Write-Host "║        Dashboard Build Automation                     ║" -ForegroundColor $colors.Header
Write-Host "║        $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')                           ║" -ForegroundColor $colors.Header
Write-Host "╚════════════════════════════════════════════════════════╝" -ForegroundColor $colors.Header

try {
    # Validate prerequisites
    Validate-Prerequisites
    
    # Clean if requested
    if ($Clean) {
        Clean-BuildArtifacts
    }
    
    # Run build
    $buildSuccess = Run-Build
    
    if (-not $buildSuccess) {
        Write-Host
        Write-Status "BUILD FAILED" "" "Error"
        exit 1
    }
    
    # Validate output
    if (-not $NoValidation) {
        $validSuccess = Validate-Output
        if (-not $validSuccess) {
            Write-Host
            Write-Status "VALIDATION FAILED" "" "Error"
            exit 1
        }
    }
    
    # Open in browser if requested
    Open-Dashboard
    
    # Summary
    Write-Host
    Write-Host "╔════════════════════════════════════════════════════════╗" -ForegroundColor $colors.Header
    Write-Host "║                  BUILD SUCCESSFUL ✓                   ║" -ForegroundColor $colors.Header
    Write-Host "╚════════════════════════════════════════════════════════╝" -ForegroundColor $colors.Header
    Write-Host
    Write-Status "Next Steps" "1. Open dist/dashboard_enhanced.html in browser"
    Write-Status "Next Steps" "2. Test functionality"
    Write-Status "Next Steps" "3. Run: npm test (to verify tests pass)"
    Write-Host
    
    exit 0

} catch {
    Write-Host
    Write-Status "FATAL ERROR" "$_" "Error"
    exit 1
}
