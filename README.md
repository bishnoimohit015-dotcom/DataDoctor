# DataDoctor

DataDoctor is a beginner-friendly CSV data-quality analysis tool built with Python, Pandas, and Streamlit. It allows users to upload a CSV file and inspect common quality indicators through a simple web interface.

This is an intentionally small learning project focused on understanding DataFrames, CSV analysis, error handling, Git, and basic application development.

## Features

DataDoctor currently provides:

- CSV file upload through a Streamlit interface
- Total row and column counts
- Column names and detected data types
- Missing-value count for each column
- Duplicate-row count
- Basic statistics for numerical columns
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
│   └── sample.csv       # Sample CSV for local analysis
├── app.py               # Streamlit application
├── analyzer.py          # Command-line analysis of the sample CSV
├── requirements.txt     # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Files excluded from version control
```

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

A virtual environment keeps this project's packages separate from other Python projects.

### 3. Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

After activation, `(.venv)` should appear at the beginning of the terminal prompt.

### 4. Install the dependencies

```powershell
python -m pip install -r requirements.txt
```

This installs the versions of Pandas and Streamlit specified by the project.

## How to Run

With the virtual environment active, start the Streamlit application:

```powershell
python -m streamlit run app.py
```

Streamlit will start a local development server and open the application in a web browser.

## How to Use

1. Start the application using the command above.
2. Select **Browse files** in the Streamlit interface.
3. Upload a file with a `.csv` extension.
4. Review the dataset overview, column information, missing values, duplicate count, numerical statistics, and data preview.

A deliberately imperfect example is available at `data/sample.csv` for testing.

## Error Handling

DataDoctor currently handles two common CSV problems:

- **Empty files:** displays a message explaining that the uploaded CSV is empty.
- **Malformed CSV data:** displays a message explaining that the file could not be parsed as a valid CSV.

These errors are shown in the interface instead of allowing the application to crash with a traceback.

## Current Limitations

DataDoctor is currently an analysis-only learning project. It does not:

- Clean, modify, or export uploaded data
- Detect outliers or calculate a data-quality score
- Produce charts or other visualizations
- Generate downloadable reports
- Include automated tests
- Use machine learning or AI
- Provide authentication or database storage

Error handling currently focuses on empty and malformed CSV files; other file or encoding problems may not yet have custom messages.

## Future Improvements

Possible future additions include:

- Outlier detection for numerical columns
- A transparent data-quality score
- Missing-value and distribution visualizations
- Downloadable analysis reports
- Additional file-validation messages
- Automated tests for the analysis logic

## Learning Goals

This project was created to practise:

- Reading and inspecting CSV files with Pandas
- Working with DataFrames, missing values, duplicates, and summary statistics
- Building a simple interactive interface with Streamlit
- Handling predictable input errors gracefully
- Managing dependencies with a virtual environment and `requirements.txt`
- Using Git commits and GitHub to track project development
- Documenting a software project clearly
