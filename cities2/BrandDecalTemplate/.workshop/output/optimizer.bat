@echo off
:: Check if ImageMagick's magick.exe exists in PATH
where magick >nul 2>nul
if %errorlevel% neq 0 (
  echo Error: magick.exe not found in your PATH. Please check your ImageMagick installation.
  echo Press any key to exit...
  pause >nul
  exit /b
)

:: Enable delayed expansion
setlocal enabledelayedexpansion
set "files_found=false"

:: Process only `image.png` files in valid directories
for /d /r %%d in (*) do (
  set "folder=%%~nxd"

  :: Skip hidden folders (starting with ".")
  if /i not "!folder:~0,1!"=="." (
    if exist "%%d\image.png" (
      set "files_found=true"
      set "input_file=%%d\image.png"
      set "output_file=%%d\_BaseColorMap.png"

      echo Processing "!input_file!"...
      magick "!input_file!" -modulate 70,70 -colors 256 "!output_file!"
      if not errorlevel 1 (
        echo Created: "!output_file!"
      ) else (
        echo Failed to process "!input_file!"
        del "!output_file!" 2>nul
      )
    )
  )
)

:: Handle case when no valid `image.png` files exist
if "%files_found%"=="false" (
  echo No valid `image.png` files found in the current directory or subdirectories.
)

echo Conversion completed. Press any key to exit...
pause >nul
