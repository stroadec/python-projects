import pandas as pd
import yaml
from report.generator import generate_report

def main():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    df = pd.read_csv("data/input.csv")
    report_df = generate_report(df, config)

    report_df.to_csv("data/report.csv", index=False)
    print("✅ Report generated: data/report.csv")

if __name__ == "__main__":
    main()
