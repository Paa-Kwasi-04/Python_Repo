@echo off
REM ============================================
REM Build Script for Number Guessing Game
REM ============================================
REM This script creates a standalone .exe file
REM using PyInstaller
REM ============================================

echo ========================================
echo  Number Guessing Game - Build Script
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

REM Check if pandas is installed (required dependency)
pip show pandas >nul 2>&1
if errorlevel 1 (
    echo [WARNING] pandas not found
    echo [INFO] Installing pandas...
    pip install pandas
    if errorlevel 1 (
        echo [ERROR] Failed to install pandas
        pause
        exit /b 1
    )
    echo [SUCCESS] pandas installed
    echo.
) else (
    echo [INFO] pandas already installed
    echo.
)

REM Clean previous builds
echo [INFO] Cleaning previous builds...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "*.spec" del /q "*.spec"
echo [SUCCESS] Cleanup complete
echo.

REM Create Number_guessing directory if it doesn't exist
if not exist "Number_guessing" (
    echo [INFO] Creating Number_guessing directory...
    mkdir Number_guessing
    echo [SUCCESS] Directory created
    echo.
)

REM Build the executable
echo [INFO] Building executable...
echo [INFO] This may take a few minutes...
echo.

pyinstaller --onefile ^
    --windowed ^
    --name "NumberGuessingGame" ^
    --icon=NONE ^
    --add-data "main.py;." ^
    --hidden-import=pandas ^
    --hidden-import=numpy ^
    number_game_gui.py

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
echo   dist\NumberGuessingGame.exe
echo.
echo IMPORTANT: The Records.csv file will be created in the
echo            Number_guessing folder when you run the game.
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
echo You can now run the game by double-clicking:
echo   dist\NumberGuessingGame.exe
echo.
echo Press any key to exit...
pause >nul