from fastapi import FastAPI, HTTPException
from pathlib import Path
from automator.loader import load_data
from automator.cleaner import clean_data
from automator.exporter import export_data
from automator.config import load_config

app = FastAPI(
    title="Automation API",
    description="API to automate CSV and Excel data processing",
    version="1.0.0"
)

@app.post("/run")
def run_automation():
    try:
        config = load_config()

        df = load_data(Path(config["input_file"]))
        df_clean = clean_data(
            df,
            fill_text=config["cleaning"]["fill_text"],
            fill_number=config["cleaning"]["fill_number"]
        )
        export_data(df_clean, Path(config["output_file"]))

        return {
            "status": "success",
            "output_file": config["output_file"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
