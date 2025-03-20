import os
import pandas as pd
import scipy.stats as stats

# Numeric file path
file_path = "data_no_outliers.csv"

# Load the file
df = pd.read_csv(file_path, sep=None, engine="python")

# Exclude the first three columns
data_columns = df.columns[3:]

# Calculate skewness and kurtosis
skew_kurtosis = {}
for col in data_columns:
   skewness = stats.skew(df[col].dropna())
   kurtosis = stats.kurtosis(df[col].dropna())
   skew_kurtosis[col] = {"Skewness": skewness, "Kurtosis": kurtosis}

# Save results in a CSV file
output_file = "skewness_kurtosis_results.csv"
skew_kurtosis_df = pd.DataFrame.from_dict(skew_kurtosis, orient="index")
skew_kurtosis_df.to_csv(output_file)

print(f"Skewness and Kurtosis analysis completed. Results saved in '{output_file}'.")