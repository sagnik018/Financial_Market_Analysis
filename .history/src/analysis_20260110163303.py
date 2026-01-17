import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

df = pd.read_sql("SELECT * FROM asset_prices", engine)

df["daily_return"] = df.groupby("symbol")["close_price"].pct_change()

summary = df.groupby("symbol").agg(
    avg_return=("daily_return", "mean"),
    risk=("daily_return", "std")
).reset_index()

summary.to_excel("../reports/investment_analysis.xlsx", index=False)

print("📊 EDA & return analysis completed")
