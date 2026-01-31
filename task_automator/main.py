from pathlib import Path
from automator.loader import load_data
from automator.cleaner import clean_data
from automator.exporter import export_data
from automator.config import load_config
from automator.logger import setup_logger
import logging
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = Path(".").absolute()
    return Path(base_path) / relative_path

def main():
    config = load_config(resource_path("config.yaml"))

    setup_logger(
        level=config["logging"]["level"],
        log_file=config["logging"]["file"]
    )

    logging.info("Starting automation")

    df = load_data(resource_path(config["input_file"]))
    df_clean = clean_data(
        df,
        fill_text=config["cleaning"]["fill_text"],
        fill_number=config["cleaning"]["fill_number"]
    )
    export_data(df_clean, resource_path(config["output_file"]))

    logging.info("Automation finished successfully")

if __name__ == "__main__":
    main()
