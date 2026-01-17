import pandas as pd
import requests
from config import DEEPAI_API_KEY

# -------------------------------
# Step 1: Load EDA results
# -------------------------------
df = pd.read_excel("")

# Prepare structured insight text
stats_text = ""
for _, row in df.iterrows():
    stats_text += (
        f"{row['symbol']} has an average daily return of "
        f"{row['avg_return']:.4f} and a risk level of "
        f"{row['risk']:.4f}. "
    )

# -------------------------------
# Step 2: Create AI prompt
# -------------------------------
prompt = f"""
You are a financial data analyst.

Using the following investment analysis results:
{stats_text}

Write a clear and simple investment summary that:
- Explains which assets give better returns
- Explains which assets are safer for long-term investment
- Uses very easy, eco-friendly, and non-technical language
- Avoids complex financial jargon
- Encourages sustainable and long-term investing
- Sounds calm, helpful, and human

Do NOT include warnings or disclaimers.
"""

# -------------------------------
# Step 3: Call DeepAI API
# -------------------------------
response = requests.post(
    "https://api.deepai.org/api/text-generator",
    headers={"api-key": DEEPAI_API_KEY},
    data={"text": prompt}
)

result = response.json()

# Extract generated text safely
summary_text = result.get("output", "")
if isinstance(summary_text, list):
    summary_text = summary_text[0].get("generated_text", "")

# -------------------------------
# Step 4: Save AI summary
# -------------------------------
with open("../reports/ai_summary.txt", "w", encoding="utf-8") as f:
    f.write(summary_text)

print("🤖 AI-generated investment summary saved to reports/ai_summary.txt")
