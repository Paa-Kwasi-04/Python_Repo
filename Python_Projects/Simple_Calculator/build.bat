@echo off
REM ============================================
REM Build Script for Shunting Yard Calculator
REM ============================================
REM This script creates a standalone .exe file
REM using PyInstaller
REM ============================================

echo ========================================
echo  Shunting Yard Calculator - Build Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo [INFO] Python found
echo.

REM Check if PyInstaller is installed
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo [WARNING] PyInstaller not found
    echo [INFO] Installing PyInstaller...
    pip install pyinstaller
    if errorlevel 1 (
        echo [ERROR] Failed to install PyInstaller
        pause
        exit /b 1
    )
    echo [SUCCESS] PyInstaller installed
    echo.
) else (
    echo [INFO] PyInstaller already installed
    echo.
)

REM Clean previous builds
echo [INFO] Cleaning previous builds...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "*.spec" del /q "*.spec"
echo [SUCCESS] Cleanup complete
echo.

REM Build the executable
echo [INFO] Building executable...
echo [INFO] This may take a few minutes...
echo.

pyinstaller --onefile ^
    --windowed ^
    --name "ShuntingYardCalculator" ^
    --icon=NONE ^
    --add-data "ShuntingYardAlgorithm.py;." ^
    --add-data "postfixEval.py;." ^
    calculator_gui.py

if errorlevel 1 (
    echo.
    echo [ERROR] Build failed
    echo Please check the error messages above
    pause
    exit /b 1
)

echo.
echo ========================================
echo [SUCCESS] Build completed successfully!
echo ========================================
echo.
echo The executable file is located at:
echo   dist\ShuntingYardCalculator.exe
echo.
echo You can now run the calculator by double-clicking the .exe file
echo.

REM Optional: Clean up build artifacts
choice /C YN /M "Do you want to clean up build files (keep only the .exe)?"
if errorlevel 2 goto :skip_cleanup
if errorlevel 1 (
    echo.
    echo [INFO] Cleaning up build files...
    if exist "build" rmdir /s /q "build"
    if exist "*.spec" del /q "*.spec"
    echo [SUCCESS] Cleanup complete
)

:skip_cleanup
echo.
echo Press any key to exit...
pause >nul