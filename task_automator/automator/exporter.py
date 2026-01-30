import pandas as pd
from pathlib import Path

def export_data(df: pd.DataFrame, output_path: Path):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if output_path.suffix == ".csv":
        df.to_csv(output_path, index=False)
    elif output_path.suffix in [".xls", ".xlsx"]:
        df.to_excel(output_path, index=False)
    else:
        raise ValueError("Unsupported export format. Use CSV or Excel.")
