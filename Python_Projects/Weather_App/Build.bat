#!/bin/bash

echo "========================================"
echo "Weather App - EXE Builder (Git Bash)"
echo "========================================"
echo ""

echo "Step 1: Installing PyInstaller..."
pip install pyinstaller
echo ""

echo "Step 2: Cleaning previous builds..."
rm -rf build dist *.spec
echo ""

echo "Step 3: Building WeatherApp.exe..."
pyinstaller --onefile --windowed --add-data ".env;." --name "WeatherApp" --clean weatherUI.py
echo ""

echo "========================================"
echo "Build Complete!"
echo "========================================"
echo ""
echo "Your WeatherApp.exe is located in the 'dist' folder"
echo ""
echo "IMPORTANT: When distributing your app:"
echo "1. Copy WeatherApp.exe from the 'dist' folder"
echo "2. Keep the .env file in the same directory as the .exe"
echo "3. DO NOT share your .env file with your API key publicly!"
echo ""
read -p "Press Enter to exit..."