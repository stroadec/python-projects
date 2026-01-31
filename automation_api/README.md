# Automation API (FastAPI)

## Description
A REST API built with FastAPI to automate CSV and Excel data processing.

The API loads, cleans, and exports structured data automatically.
Designed for integration into internal tools, websites, or scripts.

## Features
- REST API
- CSV / Excel support
- Configurable cleaning rules
- Automatic export
- Swagger documentation

## How to Run
```bash
pip install -r requirements.txt
uvicorn api:app --reload
