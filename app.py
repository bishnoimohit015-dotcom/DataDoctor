import pandas as pd
import streamlit as st
from analyzer import analyze_dataframe

st.set_page_config(
    page_title="DataDoctor",
    page_icon="🔬",
    layout="wide"
)

st.title("DataDoctor")
st.caption("A beginner-friendly CSV data quality analyzer")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    try:
      df = pd.read_csv(uploaded_file)
      results = analyze_dataframe(df)
    except pd.errors.EmptyDataError:
        st.error("The uploaded CSV file is empty.")
        st.stop()
    except pd.errors.ParserError:
        st.error("The uploaded file could not be parsed as a valid CSV.")
        st.stop()
    duplicate_count = results["duplicate_count"]

    st.divider()
    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    rows, columns = results["shape"]
    col1.metric("Rows", rows)
    col2.metric("Columns", columns)
    col3.metric("Duplicate Rows", duplicate_count)

    st.subheader("Column Information")
    column_info = results["dtypes"].reset_index()
    column_info.columns = ["Column", "Data Type"]

    st.dataframe(column_info)

    st.subheader("Missing Values")
    missing_values = results["missing_values"]
    st.dataframe(
        missing_values.reset_index().rename(
            columns={"index": "Column", 0: "Missing Values"}
        )
    )

    st.subheader("Numerical Statistics")
    numeric_stats = results["numerical_statistics"]
    st.dataframe(numeric_stats)

    st.subheader("Uploaded Data")
    st.dataframe(df)