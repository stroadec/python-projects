import pandas as pd
from checker.validator import validate_data

def main():
    df = pd.read_csv("data.csv")
    errors = validate_data(df)

    if errors:
        print("❌ Data validation errors:")
        for error in errors:
            print("-", error)
    else:
        print("✅ Data is valid")

if __name__ == "__main__":
    main()
