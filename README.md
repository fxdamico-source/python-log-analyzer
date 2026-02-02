# Python Log Analyzer

A simple command-line tool that analyzes log files and summarizes log levels.

## Features
- Parses plain-text `.log` files
- Counts log levels (INFO, WARNING, ERROR)
- Designed as a Python refresher project
- Includes pytest-based unit tests

## Usage

Activate the virtual environment and run:

```bash
python main.py data/sample.log
Example output:

makefile
Copy code
INFO: 3
ERROR: 2
WARNING: 1
Development Setup
Create and activate a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Run tests:

bash
Copy code
pytest
Project Structure
css
Copy code
.
├── analyzer.py
├── main.py
├── tests/
├── data/
└── README.md