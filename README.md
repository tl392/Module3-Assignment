# Module 3 - Assignment - Command-Line Calculator (Python, OOP)

## Overview

This project is a command-line calculator application written in Python
using Object-Oriented Programming (OOP) principles.

The application provides an interactive Read--Eval--Print Loop (REPL)
that allows users to perform arithmetic operations repeatedly until they
choose to quit. It also includes comprehensive unit tests with full test
coverage.

This project is suitable for beginners who want to understand: - How to
structure a Python project - How to apply OOP concepts - How to write
and test interactive programs

## Features

-   Interactive REPL interface
-   Addition, subtraction, multiplication, and division
-   Input validation with helpful error messages
-   Graceful handling of division by zero
-   Ability to quit at any prompt
-   Fully unit tested with pytest
-   100% test coverage for all reachable code paths

## Project Structure

    calculator/
    │
    ├── app/
    │   ├── __init__.py
    │   ├── calculator/__init__.py
    │   ├── parser/__init__.py
    │   ├── repl/__init__.py
    │   ├── runner/__init__.py
    │   └── operations/__init__.py
    │
    ├── tests/
    │   ├── __init__.py
    │   ├── test_operations.py
    │   ├── test_calculator.py
    │   ├── test_parser.py
    │   ├── test_repl.py
    │   └── test_runner.py
    │
    ├── main.py
    └── README.md

## Design Overview

This application is divided into small, focused modules. Each module has
a single responsibility.

### Why Object-Oriented Programming

Object-Oriented Programming helps: - Organize code logically - Separate
responsibilities - Make the application easier to extend and maintain

## Module Responsibilities

### operations

Defines all supported arithmetic operations.

-   `Operation` is an abstract base class that defines a common
    interface.
-   `Add`, `Sub`, `Mul`, and `Div` are concrete implementations.
-   Each operation class contains only its own calculation logic.

### calculator.py

Contains the core calculation logic.

Responsibilities: - Store available operations - Validate operator
symbols - Execute calculations

### parser.py

Handles all user input validation.

Responsibilities: - Detect quit commands (`q`, `quit`, `exit`) -
Validate operator input - Validate numeric input

### repl.py

Implements the Read--Eval--Print Loop.

Responsibilities: - Prompt the user for input - Retry on invalid input -
Call the calculator logic - Display results and errors - Exit cleanly
when the user quits

### runner.py

Acts as a wiring layer.

Responsibilities: - Create the calculator with supported operations -
Start the REPL

### main.py

The entry point of the application.

Run the program using:

    python main.py

## How to Run the Application

From the project root directory:

    python main.py

Example interaction:

    Allowed ops: *, +, -, /
              1. Type any operations which mentiond above and hit enter 
              2. Type any number and hit enter
              3. Type any number again hit enter
              
              Type q to quit the calculator
    Operation: +
    First number: 10
    Second number: 5
    Result: 15.0

    Operation: q
    Goodbye!

## Testing

This project uses pytest for unit testing.

### Run Tests

    pytest

### Run Tests With Coverage

    pytest --cov=app --cov-report=term-missing --cov-fail-under=100


## Git and GitHub Workflow (Beginner Guide)

This section explains how to push this project to GitHub step by step.

### Initialize a Git Repository

From the project root directory:

    git init

This creates a local Git repository.

------------------------------------------------------------------------

### Create a .gitignore File

Create a file named `.gitignore` and add:

    __pycache__/
    .pytest_cache/
    .coverage
    .env

This prevents unnecessary files from being committed.

------------------------------------------------------------------------

### Check Repository Status

    git status

You should see all project files listed as untracked.

------------------------------------------------------------------------

### Add Files to Git

    git add .

This stages all files for commit.

------------------------------------------------------------------------

### Commit Changes

    git commit -m "Initial commit: OOP calculator with tests"

------------------------------------------------------------------------

### Create a GitHub Repository

1.  Go to https://github.com
2.  Click **New Repository**
3.  Give it a name (for example: `oop-calculator`)
4.  Do NOT initialize with README (you already have one)
5.  Click **Create Repository**

------------------------------------------------------------------------

### Connect Local Project to GitHub

Copy the repository URL from GitHub, then run:

    git remote add origin git@github.com:USERNAME/REPOSITORYNAME.git

Replace `USERNAME` with your GitHub username.
Replace `REPOSITORYNAME` with your GitHub Repository name.
------------------------------------------------------------------------

### Push Code to GitHub

    git branch -M main
    git push -u origin main

Your project is now available on GitHub.

------------------------------------------------------------------------

### Making Future Changes

Typical workflow for updates:

    git status
    git add .
    git commit -m "Describe your change here"
    git push

------------------------------------------------------------------------

## Adding a New Operation

To add a new operation (for example, modulo):

1.  Create a new class in `app/operations/__init__.py`:

```{=html}
<!-- -->
```
    class Mod(Operation):
        symbol = "%"

        def execute(self, a: float, b: float) -> float:
            return a % b

2.  Register it in `runner.py`.

No other changes are required.

## Key Learning Outcomes

-   Object-Oriented Programming in Python
-   Abstract base classes and polymorphism
-   Clean separation of concerns
-   REPL design patterns
-   Input validation strategies
-   Unit testing with pytest
-   Achieving full test coverage

## Notes

-   Abstract base methods that are intentionally unreachable are
    excluded from coverage using `# pragma: no cover`.
-   The project avoids global state and side effects.
-   All logic is structured to be readable and beginner-friendly.
