import pandas as pd

def load_data(file_path):
    """Extract: Load data from CSV."""
    df = pd.read_csv(file_path)
    return df

def transform_data(df):
    """Transform: Clean and prepare data."""
    # Example: Ensure column names are lower case and spaces replaced with underscores
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    
    # Optionally, you can create new columns or filter data.
    # For instance, convert 'pass_fail' to binary (Pass: 1, Fail: 0)
    df['pass_fail_binary'] = df['pass_fail'].apply(lambda x: 1 if x.lower() == 'pass' else 0)
    
    return df

def save_to_csv(df, output_path):
    """Load: Save the cleaned data to a new CSV file."""
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")

if __name__ == "__main__":
    # File paths
    input_file = "data/student_performance_dataset.csv"
    output_file = "data/clean_student_performance.csv"
    
    # Run ETL process
    data = load_data(input_file)
    data_clean = transform_data(data)
    save_to_csv(data_clean, output_file)
