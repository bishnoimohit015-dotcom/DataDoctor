import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="DataDoctor",
    page_icon="🔬",
    layout="wide"
)

st.title("DataDoctor")
st.caption("A beginner-friendly CSV data quality analyzer")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  duplicate_count = df.duplicated().sum()
  
  st.divider()
  st.subheader("Dataset Overview")

  col1, col2, col3 = st.columns(3)

  col1.metric("Rows", df.shape[0])
  col2.metric("Columns", df.shape[1])
  col3.metric("Duplicate Rows", duplicate_count)

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
  
  st.metric("Duplicate Rows", duplicate_count)

  st.subheader("Numerical Statistics")
  numeric_stats = df.describe()
  st.dataframe(numeric_stats)

  st.write(df)