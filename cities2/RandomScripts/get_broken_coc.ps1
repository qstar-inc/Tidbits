function Is-BinaryFile {
    param (
        [string]$FilePath
    )
    
    $chunkSize = 1024
    $fileStream = [System.IO.File]::OpenRead($FilePath)
    $buffer = New-Object byte[] $chunkSize
    $bytesRead = $fileStream.Read($buffer, 0, $chunkSize)
    $fileStream.Close()

    if ($bytesRead -eq 0) {
        return $false
    }

    $nonPrintableCount = 0
    $totalChecked = 0

    foreach ($byte in $buffer) {
        if ($totalChecked -ge $bytesRead) {
            break
        }

        if ($byte -lt 32 -and $byte -notin (9, 10, 13)) {
            $nonPrintableCount++
        }

        $totalChecked++
    }

    $threshold = 0.1
    if (($nonPrintableCount / $totalChecked) -gt $threshold) {
        return $true
    }
    else {
        return $false
    }
}

$directoryPath = Get-Location

$cocFiles = Get-ChildItem -Path $directoryPath -Filter "*.coc" -Recurse

foreach ($cocFile in $cocFiles) {
    if (Is-BinaryFile $cocFile.FullName) {
        Write-Output "$($cocFile.FullName): Binary"
    }
}
