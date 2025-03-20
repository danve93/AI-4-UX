import pandas as pd
import re
from deep_translator import GoogleTranslator

# File paths
file_path = "open_ended.csv"
cleaned_output_file = "open_ended_cleaned.csv"
translated_output_file = "open_ended_translated.csv"

# Load the file, handling potential multi-line issues
print("Loading the file...")
df = pd.read_csv(file_path, sep=",", engine="python", quoting=3, on_bad_lines="skip")

# Replace string "None" with actual NaN values
df.replace("None", pd.NA, inplace=True)

# Drop columns and rows that contain only NaN values
df.dropna(axis=1, how="all", inplace=True)
df.dropna(axis=0, how="all", inplace=True)

# Merge all columns into a single column to fix multi-line breaks
df["Merged_Responses"] = df.astype(str).agg(" ".join, axis=1)

# Remove unintended newlines, excessive spaces, and empty values
df["Merged_Responses"] = df["Merged_Responses"].replace(r"\n", " ", regex=True)\
                                                .replace(r"\s+", " ", regex=True)\
                                                .replace(r'"', '', regex=True)\
                                                .str.strip()

# **NEW: Completely Remove "None" From Responses**
df["Merged_Responses"] = df["Merged_Responses"].replace(r"\bNone\b", "", regex=True).str.strip()

# Remove any row where the merged response is still empty after cleaning
df_cleaned = df[df["Merged_Responses"].str.len() > 0]

# Define a list of unwanted responses (case-insensitive)
unwanted_responses = [
  "rien à ajouter", "sans commentaire", "Ràs", "oui","aucun", "Rien de plus", "RAS pour moi", ".", "nc", "non", "pas de commentaire", "NO", "no.", "non", "Néant", "ras", "RAS", "Non"
]

# Convert the list into a regex pattern to match entire rows (case insensitive)
pattern = r"^(" + "|".join(map(re.escape, unwanted_responses)) + r")$"

# Remove rows that contain only these unwanted responses (ignoring case)
df_cleaned = df_cleaned[~df_cleaned["Merged_Responses"].str.fullmatch(pattern, case=False, na=False)]

# **NEW: Final Cleanup to Remove Empty or Meaningless Rows**
df_cleaned = df_cleaned[df_cleaned["Merged_Responses"].str.strip() != ""]

# Keep only the cleaned responses
df_cleaned = df_cleaned[["Merged_Responses"]].rename(columns={"Merged_Responses": "Open-Ended Responses"})

# Save the cleaned file
df_cleaned.to_csv(cleaned_output_file, index=False)
print(f"Cleaned file saved: {cleaned_output_file}")

# ---- Translation ----

# Load cleaned dataset
df = pd.read_csv(cleaned_output_file)

# Automatically get the first column name
text_column = df.columns[0]

# Initialize the translator
translator = GoogleTranslator(source='fr', target='en')

# Translate responses
def translate_response(text):
    try:
        return translator.translate(text)
    except Exception as e:
        print(f"Translation failed for: {text}, Error: {e}")
        return text

df_translated = pd.DataFrame()
df_translated["Original_Response"] = df[text_column]
df_translated["Translated_Response"] = df[text_column].apply(translate_response)

# Save translated responses
df_translated.to_csv(translated_output_file, index=False)
print(f"Translated file saved: {translated_output_file}")