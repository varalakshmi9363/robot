# AI Robot CLI 🤖

A powerful, local CLI tool that uses Google Gemini (via OpenRouter) to execute system tasks using natural language.

## Features

- **Natural Language Control**: Just tell it what to do.
- **System Operations**: Find, move, delete, or organize files.
- **Web Generation**: Create scaffolding for websites.
- **Git Integration**: Can automate git commands (add, commit, push).
- **Safe Execution**: Prompts for confirmation before running generated Python code.

## Installation

### From Source
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your API Key:
   ```powershell
   $env:OPENROUTER_API_KEY = "your_key_here"
   ```
4. Run:
   ```powershell
   python -m src.main "Your command here"
   ```

### Using the Executable
1. Locate `ai-robot.exe` (built using `build_tool.py`).
2. Run in terminal:
   ```powershell
   .\ai-robot.exe "Create a generic index.html file"
   ```

## Requirements
- Windows (tested)
- Python 3.10+
- OpenRouter API Key (uses free models by default)

## License
MIT
