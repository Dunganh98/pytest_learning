[![Python application test with Github Actions](https://github.com/Dunganh98/pytest_learning/actions/workflows/test-ci.yml/badge.svg)](https://github.com/Dunganh98/pytest_learning/actions/workflows/test-ci.yml)

# pytest_learning

Small demo project for learning pytest basics. It includes two simple functions in [hello.py](hello.py) and matching tests in [test_hello.py](test_hello.py).

## Setup
- Python 3.11+ recommended.
- Install dependencies:
	- `make install`
	- or `pip install -r requirements.txt`

## Available commands
- Run tests: `make test` (runs `pytest -vv`)
- Lint: `make lint` (runs pylint on hello.py)
- Format: `make format` (runs black)
- Do everything: `make all`

## Running pytest manually
- `python -m pytest -vv` to run the suite.
- Add `--cov=. --cov-report=term-missing` if you want quick coverage info.

## Project structure
- [hello.py](hello.py): functions `sayHi()` and `sayHello()`.
- [test_hello.py](test_hello.py): pytest tests for both functions.
- [Makefile](Makefile): handy shortcuts for install/test/format/lint.
- [requirements.txt](requirements.txt): dev and test dependencies.
