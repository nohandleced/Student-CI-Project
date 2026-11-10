# Student-CI-Project

Small Python project used for CMSC 426 In-Class Activity #3 (Jenkins + GitHub CI).

## Structure
- `app.py` - application (add / subtract functions)
- `tests/test_app.py` - unit tests (`unittest`)
- `build.bat` - Windows batch script run by the Jenkins job

## Run locally
```
python app.py
python -m unittest discover -s tests -v
```

## Jenkins
Freestyle job `Student-CI-Project`:
- Source: this repo (Git), branch `main`
- Trigger: GitHub hook trigger for GITScm polling
- Build step: Execute Windows batch command -> `build.bat`

A failing test makes `build.bat` exit with code 1, so Jenkins marks the build FAILED.

Requirements: Python 3.8+, Git. No third-party packages.
