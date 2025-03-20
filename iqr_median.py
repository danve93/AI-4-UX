import pandas as pd
import os

# File path
file_path = "data_no_outliers.csv"

# Load the file
df = pd.read_csv(file_path, sep=None, engine="python")

# Exclude the first three columns
data_columns = df.columns[3:]

# Calculate median and IQR
statistics = {}
for col in data_columns:
   median = df[col].median()
   Q1 = df[col].quantile(0.25)
   Q3 = df[col].quantile(0.75)
   IQR = Q3 - Q1
   statistics[col] = {"Median": median, "Q1": Q1, "Q3": Q3, "IQR": IQR}

# Save results in a CSV file
statistics_df = pd.DataFrame.from_dict(statistics, orient="index")
output_file = "median_iqr_results.csv"
statistics_df.to_csv(output_file)

print(f"Analysis completed. Results saved in '{output_file}'.")