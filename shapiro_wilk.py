# SHAPIRO_WILK.PY

import os
import pandas as pd
import scipy.stats as stats

# File path
file_path = "data_no_outliers.csv"

# Load the CSV file
df = pd.read_csv(file_path, sep=None, engine="python")

# Exclude the first three columns
data_columns = df.columns[3:]

# Open a file to write results directly
output_file = "shapiro_wilk.csv"
with open(output_file, "w") as f:
    f.write("Column,W Statistic,p-value\n")  # Write header
    
    # Perform Shapiro-Wilk test and write results directly
    for col in data_columns:
        if df[col].dtype in ['int64', 'float64']:  # Ensure column is numeric
            w_stat, p_value = stats.shapiro(df[col].dropna())  # Drop NaNs before testing
            f.write(f"{col},{w_stat},{p_value}\n")  # Write results

print(f"Analysis of distributions completed. Results saved in '{output_file}'.")