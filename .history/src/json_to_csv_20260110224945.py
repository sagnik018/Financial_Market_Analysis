import json
import pandas as pd
import os

# Input JSON file
json_file = r"D:\Financial_Market_Analysis\data\raw-yahoodata.json"

# Output CSV file (SAVED HERE 👇)
csv_file = r"D:\Financial_Market_Analysis\data\output.csv"

# Load JSON
with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save CSV
df.to_csv(csv_file, index=False)

print(f"✅ CSV saved successfully at: {csv_file}")
