import pandas as pd
from config import OPENAI_API_KEY
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)

# Load analysis results
df = pd.read_excel("../reports/investment_analysis.xlsx")

# Prepare structured insight for AI
stats_text = ""
for _, row in df.iterrows():
    stats_text += (
        f"Asset {row['symbol']} has an average daily return of "
        f"{row['avg_return']:.4f} with a risk (volatility) of "
        f"{row['risk']:.4f}.\n"
    )

prompt = f"""
You are a financial data analyst.

Based on the following investment analysis data:
{stats_text}

Tasks:
1. Suggest which assets are suitable for high returns.
2. Suggest safer long-term investment options.
3. Explain in very simple, eco-friendly, non-technical language.
4. Avoid giving financial advice disclaimers.
5. Write a clean summary that a normal person can understand.

Tone:
- Clear
- Calm
- Sustainable investment mindset
- Short paragraphs
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You generate financial insights from data."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.4
)

summary = response.choices[0].message.content

# Save AI-generated summary
with open("../reports/ai_summary.txt", "w") as f:
    f.write(summary)

print("🤖 AI-generated investment summary saved")
