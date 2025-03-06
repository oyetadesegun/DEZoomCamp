import sqlite3
import pandas as pd

def create_connection(db_file):
    """Create a database connection."""
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    """Create a table for student performance data."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS student_performance (
        student_id TEXT PRIMARY KEY,
        gender TEXT,
        study_hours_per_week INTEGER,
        attendance_rate REAL,
        past_exam_scores INTEGER,
        parental_education_level TEXT,
        internet_access_at_home TEXT,
        extracurricular_activities TEXT,
        final_exam_score INTEGER,
        pass_fail TEXT,
        pass_fail_binary INTEGER
    );
    """
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()

def load_data_to_db(conn, csv_file):
    """Load data from CSV into the database."""
    df = pd.read_csv(csv_file)
    df.to_sql("student_performance", conn, if_exists="replace", index=False)
    print("Data loaded into the database.")

if __name__ == "__main__":
    database = "student_performance.db"
    csv_file = "data/clean_student_performance.csv"
    
    conn = create_connection(database)
    create_table(conn)
    load_data_to_db(conn, csv_file)
    conn.close()
