import yfinance as yf
import pandas as pd
import json
from sqlalchemy import create_engine
from config import SYMBOL, PERIOD, INTERVAL, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

# Fetch data from Yahoo Finance
ticker = yf.Ticker(SYMBOL)
df = ticker.history(period=PERIOD, interval=INTERVAL)

# Save raw response
df.reset_index(inplace=True)
df.to_json("../data/raw_api_response.json", orient="records", indent=4)

# Prepare dataframe for SQL
df = df[["Date", "Open", "High", "Low", "Close", "Volume"]]
df.columns = [
    "trade_date",
    "open_price",
    "high_price",
    "low_price",
    "close_price",
    "volume"
]

df["symbol"] = SYMBOL

# MySQL connection
engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

# Store in MySQL
df.to_sql("stock_prices", engine, if_exists="append", index=False)

print("✅ Yahoo Finance data ingested into MySQL")
