import pandas as pd
from deep_translator import GoogleTranslator

# Load your CSV
file_path = 'open_ended_cleaned.csv'
output_file = 'open_ended_translated.csv'

# Load dataset
df = pd.read_csv(file_path)

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
df_translated.to_csv(output_file, index=False)
