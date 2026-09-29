# DataDoctor

DataDoctor is a beginner-friendly CSV data-quality analysis tool built with Python, Pandas, and Streamlit. Users can upload a CSV file and inspect common data-quality indicators through a simple web interface.

The project is intentionally small and was created to practise CSV analysis, DataFrame operations, error handling, modular code, Git, and basic application development.

## Features

DataDoctor currently provides:

- CSV file upload through a Streamlit interface
- Total row and column counts
- Column names and detected data types
- Missing-value count for each column
- Duplicate-row count
- Descriptive statistics generated with Pandas
- Preview of the uploaded dataset
- User-friendly messages for empty or malformed CSV files

## Tech Stack

- **Python 3.11** — application language
- **Pandas** — CSV loading and DataFrame analysis
- **Streamlit** — web interface
- **Git and GitHub** — version control and repository hosting

## Project Structure

```text
DataDoctor/
├── data/
│   └── sample.csv       # Deliberately imperfect sample dataset
├── app.py               # Streamlit interface and upload handling
├── analyzer.py          # Reusable DataFrame analysis logic
├── requirements.txt     # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Files excluded from version control
```

The analysis logic is kept in `analyzer.py`, while `app.py` handles CSV uploads and displays the results. This separation keeps the data-processing logic independent from the user interface.

## Setup and Installation

The following instructions are for Windows PowerShell.

### 1. Clone the repository

```powershell
git clone https://github.com/bishnoimohit015-dotcom/DataDoctor.git
cd DataDoctor
```

This downloads the repository and moves the terminal into the project directory.

### 2. Create a virtual environment

```powershell
py -m venv .venv
```

The virtual environment keeps this project's packages separate from other Python projects.

### 3. Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

After activation, `(.venv)` should appear at the beginning of the terminal prompt.

### 4. Install the dependencies

```powershell
python -m pip install -r requirements.txt
```

This installs the required versions of Pandas and Streamlit.

## How to Run

With the virtual environment active, start the application:

```powershell
python -m streamlit run app.py
```

Streamlit will start a local development server and open DataDoctor in a web browser.

## How to Use

1. Start the application using the command above.
2. Select **Browse files** in the Streamlit interface.
3. Upload a file with a `.csv` extension.
4. Review the dataset overview, column information, missing values, duplicate count, statistics, and uploaded-data preview.

A deliberately imperfect file is available at `data/sample.csv` for testing the analysis.

## Error Handling

DataDoctor currently handles two common CSV problems:

- **Empty CSV files:** displays a message explaining that the uploaded file is empty.
- **Malformed CSV data:** displays a message explaining that the file could not be parsed as a valid CSV.

These errors are shown inside the Streamlit interface instead of allowing the application to fail with an unhandled traceback.

## Current Limitations

DataDoctor is currently an analysis-only learning project. It does not:

- Clean, modify, or export uploaded data
- Detect outliers or calculate a data-quality score
- Produce charts or other visualizations
- Generate downloadable reports
- Include automated tests
- Use machine learning or AI
- Provide authentication or database storage

Error handling currently focuses on empty and malformed CSV files. Other file problems, including unsupported encodings, may not yet have custom error messages.

## Future Improvements

Possible future additions include:

- Outlier detection for numerical columns
- A transparent data-quality score
- Missing-value and distribution visualizations
- Downloadable analysis reports
- Additional file-validation messages
- Automated tests for the reusable analysis function

## Learning Goals

This project was created to practise:

- Reading and inspecting CSV files with Pandas
- Working with DataFrames, missing values, duplicates, and descriptive statistics
- Separating reusable analysis logic from interface code
- Building a simple interactive application with Streamlit
- Handling predictable input errors gracefully
- Managing dependencies with a virtual environment and `requirements.txt`
- Using Git commits and GitHub to track project development
- Writing clear and accurate project documentation
