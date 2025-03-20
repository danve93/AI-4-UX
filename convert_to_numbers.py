# CONVERT_TO_NUMBERS.PY


import pandas as pd
import scale_mappings  # Import the dictionary we just created


# File path
file_path = "cleaned_data.csv"


# Load the file
print("Loading the file...")
df = pd.read_csv(file_path, sep=None, engine="python")


# Converts text columns to numbers
for col in df.columns:
   if df[col].dtype == "object":  # Check whether the column is textual
       df[col] = df[col].map(scale_mappings.likert_mapping).fillna(df[col])  
# Apply Likert Mapping
       df[col] = df[col].map(scale_mappings.likert_mapping).fillna(df[col])
# Apply Ordinal Mapping
       df[col] = df[col].map(scale_mappings.ordinal_mapping).fillna(df[col])  


# Save the new file with numerical answers
output_file = "numeric_likert.csv"
df.to_csv(output_file, index=False, sep=",")
print(f"File saved: {output_file}")