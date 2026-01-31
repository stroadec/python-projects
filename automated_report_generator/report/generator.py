import pandas as pd

def generate_report(df, config):
    results = []

    for metric in config["metrics"]:
        column = metric["column"]
        metric_type = metric["type"]

        if metric_type == "sum":
            value = df[column].sum()
        elif metric_type == "mean":
            value = df[column].mean()
        else:
            continue

        results.append({
            "column": column,
            "metric": metric_type,
            "value": round(value, 2)
        })

    return pd.DataFrame(results)
