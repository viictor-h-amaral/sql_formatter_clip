# SQL Formatter Clip

A lightweight background application that watches the system clipboard, detects SQL snippets, and formats them automatically while preserving intended SQL behavior.

## Overview

This project was designed as a small desktop utility for SQL formatting. It runs in the background and listens to clipboard changes. When a SQL query is detected, it formats the query and writes the formatted version back to the clipboard.

## Architecture

The project follows a small layered structure to keep responsibilities clear:

- `app/`: entry point and app composition
- `core/`: domain state and interfaces
- `services/`: business orchestration logic
- `adapters/`: external integrations such as clipboard and tray
- `helpers/`: SQL formatting utilities
- `tests/`: automated validations

## Requirements

- Python 3.10+
- `pyperclip`
- `pystray`
- `Pillow`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the app

Start the application from the project root:

```bash
python main.py
```

The app creates a tray icon and remains active in the background.

## How it works

1. The clipboard is monitored continuously.
2. New clipboard content is compared with the previous value.
3. If the text looks like a SQL query, it is formatted.
4. The formatted SQL is written back to the clipboard.
5. The tray menu allows pausing or exiting the app.

## Development notes

- The formatting algorithms remain under the `helpers/` layer and are not rewritten during structural refactors.
- External libraries are isolated behind adapters to minimize coupling.
- The application state is separated from the tray and clipboard integration logic.

## Testing

Run the automated tests:

```bash
python -m unittest discover -s tests -v
```

## Project status

This project is intentionally small and focused. The current architecture favors maintainability and testability without introducing unnecessary complexity.
