import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Drop completely empty rows
    df.dropna(how="all", inplace=True)

    # Fill missing values
    for column in df.columns:
        if df[column].dtype == "object":
            df[column].fillna("Unknown", inplace=True)
        else:
            df[column].fillna(0, inplace=True)

    # Normalize text columns
    for column in df.select_dtypes(include="object"):
        df[column] = df[column].str.strip().str.title()

    return df
