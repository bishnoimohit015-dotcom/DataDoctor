import pandas as pd

df = pd.read_csv("data/sample.csv")

print(df)
print(df.shape)
print(df.columns)
print(df.dtypes)
print("\nMissing values:")
print(df.isna().sum())
print("\nDuplicate rows:")
print(df.duplicated().sum())
print("\nNumerical statistics:")
print(df.describe())