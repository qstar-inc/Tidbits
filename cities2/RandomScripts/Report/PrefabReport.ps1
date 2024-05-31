param(
    [switch]$outside
)

function Search-PrefabFiles {
    param (
        [string]$basePath
    )

    $results = @()
    $nameRegex = '"name":\s*"([^"]+)"'
    $filesProcessed = 0

    Get-ChildItem -Path $basePath -Recurse -Filter '*.Prefab' | ForEach-Object {
        $file = $_.FullName
        $relativePath = $file.Substring($basePath.Length + 1)
        $nameFound = $null

        Get-Content -Path $file | ForEach-Object {
            if ($_ -match $nameRegex) {
                $nameFound = $matches[1]
                return
            }
        }

        $cidFilePath = "$file.cid"
        if (Test-Path -Path $cidFilePath) {
            $cid = Get-Content -Path $cidFilePath -Raw
            $cid = $cid.Trim()
        } else {
            $cid = "CID file missing"
        }

        if ($nameFound) {
            $results += "${relativePath}: ${nameFound} : ${cid}"
        } else {
            $results += "${relativePath}: name not found : ${cid}"
        }
        $filesProcessed++
    }

    return $results, $filesProcessed
}

function Write-Report {
    param (
        [array]$results,
        [string]$reportPath
    )

    $results | Out-File -FilePath $reportPath
}

$startTime = Get-Date
$basePath = Get-Location
$cs2UserPath = [System.Environment]::GetFolderPath('LocalApplicationData') + "\Low\Colossal Order\Cities Skylines II"

if ($basePath.Path -like "$cs2UserPath*") {
    $go = $true
} else {
    Write-Host "Hello from the other side!"
    Write-Host "This script is running from outside the Cities Skylines II user data folder."
    if ($outside) {
        $go = $true
    } else {
        Write-Host "To use this script outside the Cities Skylines II user data folder, use the -outside parameter. Like this:"
        Write-Host ".\PrefabReport.ps1 -outside"
        $go = $false
    }
}

if ($go) {
    Write-Host "Creating report... This might take a while..."
    $reportPath = 'PrefabReport.txt'
    $results, $filesProcessed = Search-PrefabFiles -basePath $basePath.Path
    $endTime = Get-Date
    $executionTime = New-TimeSpan -Start $startTime -End $endTime
    Write-Report -results $results -reportPath $reportPath
    Write-Host "Report written to $reportPath for $filesProcessed files in $($executionTime.TotalSeconds) seconds."
} else {
    Write-Host "Cancelling script execution"
}
