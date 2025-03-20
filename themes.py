# THEMES.PY


import pandas as pd
import re
from collections import defaultdict


# Load dataset
file_path = 'open_ended_translated.csv'
df = pd.read_csv(file_path)


# Expanded categorization rules with additional keywords and context-based mapping
theme_keywords = {
   "Bad Experience": ["difficult", "confusing", "frustrating", "complicated", "ineffective", "unreliable", "inconsistent", "unresponsive", "cumbersome", "broken", "failed", "issues", "malfunctions"],
   "Bad Experience Mobile": ["mobile", "phone", "tablet"],
   "Bad Performance": ["slow", "lagging", "freezing", "crashes", "unresponsive", "sluggish", "laggy", "delays", "unoptimized"],
   "Bug": ["error", "glitch", "bug", "crash", "freezes", "corruption", "bugged", "malfunction"],
   "Generic Negative Feedback": ["bad", "terrible", "hate", "annoying", "useless", "awful", "horrible", "disappointing", "unpleasant"],
   "Generic Positive Feedback": ["good", "great", "excellent", "happy", "useful", "helpful", "nice", "satisfied", "decent", "okay", "acceptable"],
   "Good Experience": ["smooth", "intuitive", "efficient", "easy", "productive", "user-friendly"],
   "RFE": ["feature", "request", "add", "missing"],
   "Software Nostalgia": ["previous", "old", "miss"],
   "Unclear Experience": ["unclear", "confusing", "documentation", "vague", "unknown"],
}


# Function to categorize responses
def categorize_response(response):
   response_lower = str(response).lower()
   assigned_categories = set()
  
   for theme, keywords in theme_keywords.items():
       if any(re.search(rf'\b{kw}\b', response_lower) for kw in keywords):
           assigned_categories.add(theme)
  
   return ", ".join(assigned_categories) if assigned_categories else "Other / Needs Review"


# Apply categorization
df['Category'] = df['Translated_Response'].fillna('').apply(categorize_response)


# Save results to CSV
output_file = "themes.csv"
df[['Translated_Response', 'Category']].to_csv(output_file, index=False)
print(f"Categorized responses saved to {output_file}")