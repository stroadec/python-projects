import pandas as pd
from pathlib import Path

def load_data(file_path: Path) -> pd.DataFrame:
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    if file_path.suffix == ".csv":
        return pd.read_csv(file_path)
    elif file_path.suffix in [".xls", ".xlsx"]:
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Use CSV or Excel.")
