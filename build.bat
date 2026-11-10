@echo off
REM Name: Cedric Johnson | CMSC 426 - Software as a Service | Dr. Gyeera
REM Build script run by the Jenkins job Student-CI-Project

echo === CI Build Started ===
echo Checking source files...
dir

echo === Running Application ===
python app.py

echo === Running Application Tests ===
python -m unittest discover -s tests -v

REM If any test fails, exit with code 1 so Jenkins marks the build FAILED
if errorlevel 1 (
    echo TESTS FAILED
    exit /b 1
)
echo === CI Build Completed Successfully ===
exit /b 0
