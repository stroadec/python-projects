from automator.loader import load_data
from automator.cleaner import clean_data
from automator.exporter import export_data
from pathlib import Path

INPUT_FILE = Path("data/input.csv")
OUTPUT_FILE = Path("data/output.csv")

def main():
    print("🔄 Loading data...")
    df = load_data(INPUT_FILE)

    print("🧹 Cleaning data...")
    df_clean = clean_data(df)

    print("📤 Exporting data...")
    export_data(df_clean, OUTPUT_FILE)

    print("✅ Done! File exported to data/output.csv")

if __name__ == "__main__":
    main()
