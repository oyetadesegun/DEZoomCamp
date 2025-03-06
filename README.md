# Student Performance Analysis

## Project Objective
This project analyzes student performance data to understand the factors influencing exam outcomes. By examining variables like study hours, attendance, parental education level, and extracurricular activities, we aim to determine how these factors correlate with final exam scores and pass/fail status.

## Installation Instructions

### Prerequisites
- Python 3.8 or higher
- Pip package manager

### Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/oyetadesegun/DEZoomCamp.git
   cd data_engineering_project
   ```
2. **Install Dependencies:**
   ```bash
   pip install pandas matplotlib seaborn streamlit
   ```

## ETL Pipeline
The ETL process for this project is split into three main stages:

### Extract:
Read the raw data from `data/student_performance_dataset.csv` using Pandas.

### Transform:
Clean and preprocess the data by:
- Renaming columns for consistency.
- Converting categorical variables if needed.
- Creating new features (e.g., a binary column for pass/fail status).

### Load:
Save the cleaned data to `data/clean_student_performance.csv` and load it into a SQLite database (`student_performance.db`).

## Running the ETL Pipeline
Execute the following commands in your terminal:
```bash
python scripts/etl_pipeline.py
python scripts/load_to_db.py
```

## Dashboard Instructions
The interactive dashboard, built with Streamlit, provides two key visualizations:

### Pass/Fail Distribution:
A bar chart displaying the number of students who passed or failed.

### Study Hours vs Final Exam Score:
A scatter plot that shows the relationship between study hours per week and final exam scores, with a distinction between pass and fail.

### Launching the Dashboard
Run the following command:
```bash
streamlit run scripts/dashboard.py
```
This will open a browser window where you can interact with the dashboard.

## Project Structure
```
data_engineering_project/
├── data/
│   ├── student_performance_dataset.csv   # Raw dataset
│   └── clean_student_performance.csv      # Cleaned dataset after ETL
├── notebooks/
│   └── eda.ipynb                          # Exploratory Data Analysis notebook
├── scripts/
│   ├── etl_pipeline.py                    # ETL pipeline script
│   ├── load_to_db.py                      # Script to load data into SQLite database
│   └── dashboard.py                       # Streamlit dashboard script
└── README.md                              # Project documentation
```

## Usage
- **Explore the Data:**
  Open the `notebooks/eda.ipynb` notebook to conduct exploratory analysis.
- **Run the ETL Pipeline:**
  Execute the ETL scripts to clean and transform the data, and then load it into the database.
- **Visualize Insights:**
  Launch the dashboard with Streamlit to interactively explore key insights from the data.

## GitHub Link & Commit Details
- **Repository:** [DEZoomCamp](https://github.com/oyetadesegun/DEZoomCamp)


