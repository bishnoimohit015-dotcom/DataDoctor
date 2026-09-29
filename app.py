import pandas as pd
import streamlit as st

st.title("DataDoctor")
st.write("CSV Data Quality Analyzer")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)

  st.metric("Rows", df.shape[0])
  st.metric("Columns", df.shape[1])

  st.subheader("Column Information")

  column_info = df.dtypes.reset_index()
  column_info.columns = ["Column", "Data Type"]

  st.dataframe(column_info)

  st.subheader("Missing Values")
  missing_values = df.isna().sum()
  st.dataframe(
      missing_values.reset_index().rename(
          columns={"index": "Column", 0: "Missing Values"}
      )
  )

  st.subheader("Duplicate Rows")
  duplicate_count = df.duplicated().sum()
  st.metric("Duplicate Rows", duplicate_count)

  st.subheader("Numerical Statistics")
  numeric_stats = df.describe()
  st.dataframe(numeric_stats)

  st.write(df)