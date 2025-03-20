import os
import pandas as pd
import scipy.stats as stats
import seaborn as sns
import matplotlib.pyplot as plt

# Numeric file path
file_path = "data_no_outliers.csv"

# Load the file
df = pd.read_csv(file_path, sep=None, engine="python")

# Exclude the first three columns
data_columns = df.columns[3:]

# Calculate Spearman's correlation
spearman_corr = df[data_columns].corr(method="spearman")

# Save correlation results in a CSV
corr_output_file = "spearman_correlation.csv"
spearman_corr.to_csv(corr_output_file)

# Creating a heatmap to visualise correlations
plt.figure(figsize=(12, 8))
sns.heatmap(spearman_corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Spearman Correlation Matrix")
plt.savefig("spearman_correlation_heatmap.png")
plt.close()

print(f"Spearman correlation analysis completed. Results saved in '{corr_output_file}'.")