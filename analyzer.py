def analyze_dataframe(df):
    return {
        "shape": df.shape,
        "columns": df.columns,
        "dtypes": df.dtypes,
        "missing_values": df.isna().sum(),
        "duplicate_count": df.duplicated().sum(),
        "numerical_statistics": df.describe()
    }