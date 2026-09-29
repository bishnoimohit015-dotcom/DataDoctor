Create a professional but concise README.md for my GitHub project called "DataDoctor".

Project context:
- DataDoctor is a beginner-friendly CSV data quality analysis tool.
- It is built with Python, Pandas, and Streamlit.
- The project is intentionally simple because it is a learning project.
- Users upload a CSV file through the Streamlit interface.
- The application analyzes the uploaded DataFrame and displays:
  1. Number of rows
  2. Number of columns
  3. Column names
  4. Detected data types
  5. Missing-value count for each column
  6. Duplicate-row count
  7. Basic statistics for numerical columns
  8. A preview of the uploaded data
- The application handles empty CSV files and malformed CSV files with user-friendly error messages instead of crashing.
- It does NOT currently perform data cleaning, machine learning, authentication, database operations, or AI analysis.
- Future improvements may include outlier detection, a data-quality score, visualizations, downloadable reports, and automated tests.

Tech stack:
- Python 3.11
- Pandas
- Streamlit
- Git
- GitHub

Repository:
https://github.com/bishnoimohit015-dotcom/DataDoctor

Current project structure:

DataDoctor/
├── data/
│   └── sample.csv
├── app.py
├── analyzer.py
├── requirements.txt
├── README.md
└── .gitignore

The README must contain these sections:

1. Project title and short description
2. Features
3. Tech Stack
4. Project Structure
5. Setup and Installation
6. How to Run
7. How to Use
8. Error Handling
9. Current Limitations
10. Future Improvements
11. Learning Goals

Use these exact setup commands:

git clone https://github.com/bishnoimohit015-dotcom/DataDoctor.git
cd DataDoctor

Windows PowerShell:
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py

Explain briefly what each setup step does.

Keep the README accurate to the current implementation. Do not claim that features such as outlier detection, data visualization, automated tests, downloadable reports, or data cleaning are already implemented.

Make the README suitable for a third-year B.Tech CSE student's beginner portfolio project. Keep it professional and clear without excessive marketing language.

Make sure every Markdown code block is correctly opened and closed.