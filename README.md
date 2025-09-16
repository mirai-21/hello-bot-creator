# Project Setup Guide

## Installation

Follow these steps to set up and run the project on Windows, macOS, or Linux:

### 1. Create a Virtual Environment
Run the following command to create a virtual environment:
- **Windows**:
  ```sh
  py -m venv .venv
  ```
- **macOS/Linux**:
  ```sh
  python -m venv .venv
  ```

### 2. Activate Virtual Environment and Install Dependencies
- **Windows** (Command Prompt):
  ```sh
  .venv\Scripts\activate
  ```
  **Windows** (PowerShell):
  ```sh
  .venv\Scripts\Activate.ps1
  ```
- **macOS/Linux**:
  ```sh
  source .venv/bin/activate
  ```

Install dependencies:
```sh
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create and configure a `.env` file with the necessary environment variables.
(An example of the contents of an `.env` file can be found in `.env.example`)

### 4. Run the Project
- **Windows**:
  ```sh
  py run.py
  ```
- **macOS/Linux**:
  ```sh
  python run.py
  ```

## Additional Notes
- Ensure you have Python installed on your system.
- The `.env` file should contain all required environment variables.
- If you encounter issues, check that all dependencies are installed correctly and that the virtual environment is activated.

