# Pre-Sales Analyzer

AI-powered tool for analyzing software project requests during the pre-sales process.

## Overview

Pre-Sales Analyzer transforms unstructured customer requests into a structured project analysis.

Given a natural-language request, the system extracts:

* Project type
* Project summary
* Functional requirements
* Missing information
* Clarifying questions
* Project complexity
* Estimated effort
* Assumptions
* Confidence level

The goal is to help sales and technical teams understand a potential project before preparing a proposal or quotation.

## Example

### Input

> We are a company of 80 employees and want to develop an internal web application to manage vacations and leave requests. Employees should be able to log in, submit requests and view a calendar. Managers should be able to approve or reject requests. We would also like email notifications.

### Output

```text
Project type:
Internal Web Application

Complexity:
Medium

Requirements:
- Employee authentication
- Leave request submission
- Calendar view
- Manager approval workflow
- Email notifications

Missing information:
- Authentication provider
- Detailed approval workflow
- Integration requirements

Estimated effort:
120–180 hours

Confidence:
Medium
```

## Architecture

The current version uses a local Large Language Model to transform the customer request into a validated structured representation.

```text
Customer Request
       │
       ▼
   Gemma 3
       │
       ▼
Structured JSON
       │
       ▼
   Pydantic
       │
       ▼
 ProjectAnalysis
```

The system is designed to evolve towards a more complete pre-sales analysis pipeline, including historical project data and data-driven effort estimation.

## Tech Stack

* Python 3.12+
* Pydantic
* Ollama
* Gemma 3
* Pytest
* Git / GitHub

## Getting Started

### Requirements

* Python 3.12+
* Ollama
* Gemma 3

Install Ollama and make sure the `gemma3` model is available locally.

### Installation

Clone the repository:

```bash
git clone <repository-url>
cd pre-sales-analyzer
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project and development dependencies:

```bash
pip install -e ".[dev]"
```

### Running the analyzer

Make sure Ollama is running and that the Gemma 3 model is available.

Then run:

```bash
python tests/evaluate_llm.py
```

The script runs the analyzer against a collection of example customer requests and prints the resulting structured analyses.

### Running tests

```bash
pytest
```

## Project Structure

```text
pre-sales-analyzer/
├── src/
│   └── analyzer/
│       ├── __init__.py
│       ├── models.py
│       ├── analyzer.py
│       └── main.py
├── tests/
│   ├── test_models.py
│   └── evaluate_llm.py
├── README.md
├── .gitignore
└── pyproject.toml
```

## Roadmap

### V0 — Structured requirement analysis

* [x] Local LLM integration
* [x] Structured output
* [x] Pydantic validation
* [x] Requirement extraction
* [x] Missing information detection
* [x] Clarifying questions
* [x] Complexity estimation
* [x] Assumption extraction

### V1 — API and reliability

* [ ] FastAPI endpoint
* [ ] Automated LLM evaluation
* [ ] Improved validation and error handling
* [ ] Better effort estimation
* [ ] Provider abstraction

### V2 — Historical project analysis

* [ ] Historical project dataset
* [ ] Similar project retrieval
* [ ] Embeddings / vector search
* [ ] Data-driven effort estimation
* [ ] Explainable estimates based on similar projects

### V3 — User interface

* [ ] Web dashboard
* [ ] Project analysis visualization
* [ ] Exportable reports

## Privacy

The current implementation uses a locally running LLM through Ollama.

Customer requests therefore do not need to be sent to a third-party API, making local execution suitable for experimenting with potentially sensitive pre-sales data.

## Status

Early development.

The current version focuses on validating the core analysis pipeline before introducing historical project data, automated effort estimation and a user interface.

## License

This project is licensed under the MIT License.
