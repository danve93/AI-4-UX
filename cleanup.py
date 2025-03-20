# CLEANUP.PY

# pandas is an open source data analysis and manipulation tool based on python
import pandas as pd


# we will now load the csv, ignoring other separators other than “,”, as it may cause errors in reading the file
file_path = "your_data.csv" # replace your_data.csv with you file name
df = pd.read_csv(file_path, sep=None, engine="python")


# Let’s now remove any comma from the column titles (headers)
df.columns = [col.replace(",", "") for col in df.columns]


# Check if the number of columns is correct before proceeding
print(f"Number of columns in the original file: {len(df.columns)}")


# Find the correct columns to check, in our case is the first column after the Status column
col_name = [col for col in df.columns if "Je trouve que la gestion simultanée de deux ou plusieurs courriels (suppression marquage comme lu etc.) est un véritable jeu d'enfant:" in col] #Replace the text between the “” with the column title that we need to check to be filled with data and not empty


if col_name:
   col_name = col_name[0]  # Get the first column
  
# Filter the rows in which "Status" is "SUCCESS" or "DROP_OFF" and the next column is empty
   df = df[~((df["Status"].isin(["SUCCESS", "DROP_OFF"])) & (df[col_name].isna() | (df[col_name].str.strip() == '')))]
  
# Save the new file using “,” as delimiter
   df.to_csv("cleaned_data.csv", index=False, sep=",")
  
   print(f"Number of columns after the saving of the new file: {len(df.columns)}")
else:
   print("Error: Column not found in the dataset.")
