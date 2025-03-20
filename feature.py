# FEATURE.PY


import pandas as pd
from collections import defaultdict
import re


# Load the dataset
file_path = 'open_ended_translated.csv'
df = pd.read_csv(file_path)


# Define keywords to search for, handling singular/plural variations
keywords = {
    "Admin": ["admin", "admins"],
    "Calendar": ["calendar", "calendars"],
    "Contacts": ["contact", "contacts"],
    "Files": ["file", "files"],
    "Generic": ["generic"],
    "Login": ["login", "logins"],
    "Mails": ["mail", "mails", "email", "emails"],
    "Mobile": ["mobile", "mobiles"],
    "Search": ["search", "searches", "searching"],
    "Settings": ["setting", "settings"],
    "UX": ["ux", "user experience"],
    "Messages": ["message", "messages", "messaging"]
}


# Initialize dictionary to count occurrences
keyword_counts = defaultdict(int)


# Ensure 'Translated_Response' column exists
df = df.dropna(subset=['Translated_Response'])


# Count keyword occurrences
for response in df['Translated_Response']:
    found_keywords = set()
    for category, words in keywords.items():
        if any(re.search(rf'\b{word}\b', response, re.IGNORECASE) for word in words):
            found_keywords.add(category)
    
    for keyword in found_keywords:
        keyword_counts[keyword] += 1


# Convert result to DataFrame
keyword_summary = pd.DataFrame(list(keyword_counts.items()), columns=["Keyword", "Response Count"])


# Save results to CSV
output_file = "features.csv"
keyword_summary.to_csv(output_file, index=False)
print(f"Keyword counts saved to {output_file}")
