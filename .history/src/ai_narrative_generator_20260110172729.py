import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Step 1: Load EDA results

df = pd.read_excel(r"D:/Financial_Market_Analysis/reports/investment_analysis.xlsx")

stats_text = ""
for _, row in df.iterrows():
    stats_text += (
        f"{row['symbol']} has an average daily return of "
        f"{row['avg_return']:.4f} and a risk value of "
        f"{row['risk']:.4f}. "
    )


# Step 2: Prompt for LLaMA-style model
prompt = f"""
You are a financial data analyst.

Here is investment performance data:
{stats_text}

Write a clear and simple summary that:
- Explains which assets provide better returns
- Explains which assets are safer for long-term investment
- Uses eco-friendly, non-technical language
- Encourages sustainable investing habits
- Avoids complex financial jargon

Write in short paragraphs.
"""

# Step 3: Load LLaMA-style model

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,
    device_map="auto"
)

generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=300,
    temperature=0.4
)

# Step 4: Generate AI summary
output = generator(prompt)
generated_text = output[0]["generated_text"]

# Step 5: Save summary
with open("../reports/ai_summary.txt", "w", encoding="utf-8") as f:
    f.write(generated_text)

print("🦙 LLaMA-based AI summary generated and saved")
