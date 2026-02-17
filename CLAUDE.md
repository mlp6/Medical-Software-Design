# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the Duke University BME 547 Medical Software Design course repository. It contains lecture materials, assignments, and resources for teaching professional software engineering practices in biomedical contexts. Python 3.5+ is required (Python 2.7 is not supported).

## Common Commands

### Testing
```bash
pytest -v --pep8           # Run tests with PEP8 linting
pytest -v --cov            # Run tests with coverage
pytest path/to/test.py -v  # Run specific test file
```

### Virtual Environment Setup
```bash
python -m venv env
source env/bin/activate    # Linux/Mac
pip install -r requirements.txt
```

### Documentation Generation (Sphinx)
```bash
sphinx-quickstart docs
sphinx-apidoc -f -o docs .
cd docs && make html
```

## Code Architecture

- **Lectures/** - Teaching materials with markdown docs and runnable Python examples demonstrating concepts (Flask web services, OOP, testing patterns, exception handling)
- **Assignments/** - Sequential assignments building from Git fundamentals through unit testing, CI, documentation, and culminating in the HeartRateMonitor ECG analysis project
- **Resources/** - Developer setup guides and reference materials
- **bme590_grading/** - Instructor tools for batch-cloning student repos and Sakai grade integration

## Course Coding Conventions

### Git Workflow
- Feature branch naming: `$USER/$FEATURE`
- Master branch should only contain functional code
- Use annotated tags for versioning: `git tag -a 'v0.0.1' -m 'description'`
- Small, logical commits with descriptive messages

### Testing (pytest)
- Test-Driven Development: write tests before code
- Use `@pytest.mark.parametrize` for multiple input/output combinations
- Test edge cases and bad inputs, not just happy paths
- Use `pytest.approx` for floating point comparisons

### Documentation
- Docstrings required: one-liner summary, `:param:`, `:return:`, `:raises:`
- Supported styles: reStructuredText (default), NumPy, Google (with Napoleon)

### Exception Handling
- Raise exceptions early for conditions the function cannot handle
- Use specific exception types (ValueError, TypeError, etc.)
- Integrate logging with exception handling

## Travis CI Configuration Pattern
```yaml
language: python
python:
  - "3.6"
cache:
  - pip
install:
  - pip install -r requirements.txt
script:
  - pytest -v --pep8
```
