def validate_data(df):
    errors = []

    for col in ["name", "email", "age"]:
        if col not in df.columns:
            errors.append(f"Missing column: {col}")

    if "age" in df.columns:
        if df["age"].min() < 18 or df["age"].max() > 99:
            errors.append("Age out of allowed range")

    return errors
