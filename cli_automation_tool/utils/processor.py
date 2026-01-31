import pandas as pd

def process_file(input_path, output_path):
    df = pd.read_csv(input_path)
    df.dropna(how="all", inplace=True)
    df.columns = [c.lower().strip() for c in df.columns]
    df.to_csv(output_path, index=False)
