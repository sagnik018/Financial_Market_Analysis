# src/ai_summary.py

import pandas as pd
import subprocess
import os
import requests

# -------------------------------
# Rule-Based Financial Analysis
# -------------------------------

def classify_risk(volatility):
    if 0.05 <= volatility < 0.10:
        return "low-risk"
    elif 0.10 <= volatility < 0.15:
        return "moderate-risk"
    elif volatility >= 0.15:
        return "high-risk"
    else:
        return "very-low-risk"


def classify_growth(cagr):
    if cagr >= 0.15:
        return "high-growth"
    elif 0.07 <= cagr < 0.12:
        return "moderate-growth"
    elif 0.03 <= cagr < 0.07:
        return "low-growth"
    else:
        return "sub-inflation-growth"


# -------------------------------
# Base Summary (Deterministic)
# -------------------------------

def generate_base_summary(row):
    risk = classify_risk(row["volatility"])
    growth = classify_growth(row["cagr"])

    if risk in ["low-risk", "very-low-risk"]:
        investor_type = "conservative investors seeking stability"
    elif risk == "moderate-risk":
        investor_type = "balanced investors aiming for steady growth"
    else:
        investor_type = "aggressive investors with high risk tolerance"

    summary = (
        f"{row['ticker']} demonstrates {growth.replace('-', ' ')} potential "
        f"with annualized volatility placing it in the {risk.replace('-', ' ')} category. "
        f"The asset exhibits a prevailing trend of '{row['trend']}', "
        f"making it suitable for {investor_type}."
    )

    return summary


# -------------------------------
# LLM ENHANCEMENT (OPTIONAL)
# -------------------------------

def enhance_with_ollama(text):
    """
    Uses local LLaMA via Ollama (FREE, offline)
    """
    try:
        prompt = (
            "Rewrite the following investment analysis in a professional, "
            "clear, and investor-friendly tone:\n\n"
            f"{text}"
        )

        result = subprocess.run(
            ["ollama", "run", "llama3", prompt],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()

    except Exception:
        pass

    return text  # fallback


def enhance_with_deepai(text):
    """
    Uses DeepAI Text Generation API (FREE tier)
    Requires: DEEPAI_API_KEY env variable
    """
    try:
        api_key = os.getenv("DEEPAI_API_KEY")
        if not api_key:
            return text

        response = requests.post(
            "https://api.deepai.org/api/text-generator",
            data={"text": text},
            headers={"api-key": api_key},
            timeout=20
        )

        if response.status_code == 200:
            output = response.json()
            return output.get("output", text)

    except Exception:
        pass

    return text  # fallback


# -------------------------------
# MASTER SUMMARY GENERATOR
# -------------------------------

def generate_final_summary(row, use_llm=True):
    base_text = generate_base_summary(row)

    if not use_llm:
        return base_text

    # Priority: Ollama → DeepAI → Base
    enhanced = enhance_with_ollama(base_text)
    if enhanced != base_text:
        return enhanced

    return enhance_with_deepai(base_text)


# -------------------------------
# Main Pipeline
# -------------------------------

def run_ai_summary(
    input_csv="",
    output_csv="reports/investment_summary.csv",
    use_llm=True
):
    df = pd.read_csv(input_csv)

    summaries = []
    for _, row in df.iterrows():
        summaries.append(generate_final_summary(row, use_llm))

    df["investment_summary"] = summaries
    df.to_csv(output_csv, index=False)

    print("✅ AI Investment Summary generated successfully!")
    print(f"📄 Saved to {output_csv}")
    print(f"🤖 LLM Enhancement: {'ON' if use_llm else 'OFF'}")


if __name__ == "__main__":
    run_ai_summary()
