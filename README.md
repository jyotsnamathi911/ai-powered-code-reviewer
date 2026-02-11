# AI-Powered Code Reviewer & Quality Assistant

A modular tool that analyzes Python code for quality, maintainability, and best practices using static analysis and configurable rules.

---

## 🚀 Features

- AST-based Python code parsing
- Detection of code smells (long functions, missing docstrings, etc.)
- Quality scoring and validation metrics
- Command Line Interface (CLI)
- Configurable rules via `pyproject.toml`

---

## 🛠 CLI Usage

Run commands as a module:

```bash
python -m ai_code_reviewer.cli.main scan <path>
python -m ai_code_reviewer.cli.main review <file>
python -m ai_code_reviewer.cli.main apply
python -m ai_code_reviewer.cli.main report
python -m ai_code_reviewer.cli.main diff
