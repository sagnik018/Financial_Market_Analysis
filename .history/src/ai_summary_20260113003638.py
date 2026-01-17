import pandas as pd

# Rule-Based Financial Analysis

def classify_risk(volatility):
    """
    volatility: Annualized standard deviation of returns (decimal)
    Example: 0.12 = 12%
    """
    if 0.05 <= volatility < 0.10:
        return "low-risk"
    elif 0.10 <= volatility < 0.15:
        return "moderate-risk"
    elif volatility >= 0.15:
        return "high-risk"
    else:
        return "very-low-risk"


def classify_growth(cagr):
    """
    cagr: Compound Annual Growth Rate (decimal)
    """
    if 0.15 <= cagr:
        return "high-growth"
    elif 0.07 <= cagr < 0.12:
        return "moderate-growth"
    elif 0.03 <= cagr < 0.07:
        return "low-growth"
    else:
        return "sub-inflation-growth"


def generate_summary(row):
    risk = classify_risk(row["volatility"])
    growth = classify_growth(row["cagr"])

    if risk in ["low-risk", "very-low-risk"]:
        investor_type = "conservative investors seeking capital preservation and stability"
    elif risk == "moderate-risk":
        investor_type = "balanced investors aiming for steady long-term growth"
    else:
        investor_type = "aggressive investors with high risk tolerance"

    summary = (
        f"{row['ticker']} demonstrates {growth.replace('-', ' ')} potential "
        f"with annualized volatility placing it in the {risk.replace('-', ' ')} category. "
        f"The stock exhibits a prevailing trend of '{row['trend']}', "
        f"making it suitable for {investor_type}."
    )

    return summary


# Main Pipeline


def run_ai_summary(
    input_csv=r"D:\Financial_Market_Analysis\reports\analysis_summary.csv",
    output_csv="r"D:/Financial_Market_Analysis/reports/analysis_summary.csv""
):
    df = pd.read_csv(input_csv)

    summaries = []
    for _, row in df.iterrows():
        summaries.append(generate_summary(row))

    df["investment_summary"] = summaries
    df.to_csv(output_csv, index=False)

    print("✅ AI Investment Summary generated successfully!")
    print(f"📄 Saved to {output_csv}")


if __name__ == "__main__":
    run_ai_summary()
