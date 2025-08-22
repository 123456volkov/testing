# Web Testing Framework

A minimal framework for UI and backend testing of web applications using Python.

## Features

- API testing via `requests` (with a fallback to the standard library)
- UI testing via `selenium` (optional, headless by default)
- Simple configuration via environment variables
- Centralized logging
- Pytest examples for API and UI

## Installation

```bash
pip install -r requirements.txt
```

Optional packages for extended functionality:

```bash
pip install requests selenium
```

## Running tests

```bash
pytest
```

To run UI tests, set `ENABLE_UI_TESTS=1` and ensure Chrome and chromedriver are installed:

```bash
ENABLE_UI_TESTS=1 pytest examples/test_example_ui.py
```
