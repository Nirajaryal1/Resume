# Resume Web Application

A Flask web application for hosting and serving a professional resume in PDF format.

## Features

- **Resume PDF Generation**: Dynamically generates a professional resume using Python and FPDF
- **Web Interface**: Clean, modern HTML interface for viewing and downloading the resume
- **Auto-generation**: Automatically generates resume PDF if it doesn't exist when requested
- **Regeneration**: Endpoint to regenerate the resume PDF on demand

## Getting Started

Previews should run automatically when starting a workspace.

## Running Locally

1. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask dev server:
   ```bash
   ./devserver.sh
   ```

The app will be available at `http://localhost:8080`

## Structure

- `main.py` - Flask application with routes for home page and resume serving
- `generate_resume.py` - Resume PDF generation logic
- `templates/index.html` - Home page template
- `requirements.txt` - Python dependencies