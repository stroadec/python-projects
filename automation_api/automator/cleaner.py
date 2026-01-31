def clean_data(df, fill_text="Unknown", fill_number=0):
    df = df.copy()
    df.dropna(how="all", inplace=True)

    for col in df.columns:
        if df[col].dtype == "object":
            df[col].fillna(fill_text, inplace=True)
            df[col] = df[col].str.strip().str.title()
        else:
            df[col].fillna(fill_number, inplace=True)

    return df
