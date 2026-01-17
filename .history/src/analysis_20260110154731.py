import pandas as pd
from sqlalchemy import create_engine
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

df = pd.read_sql(
    "SELECT trade_date, close_price, volume FROM stock_prices",
    engine
)

# Time-series indicators
df["moving_avg_20"] = df["close_price"].rolling(20).mean()
df["daily_return"] = df["close_price"].pct_change()

# Save report
df.to_excel("../reports/financial_analysis.xlsx", index=False)

print("📈 Analysis completed and report generated")
