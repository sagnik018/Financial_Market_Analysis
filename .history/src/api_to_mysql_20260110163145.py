import yfinance as yf
import pandas as pd
import json
from sqlalchemy import create_engine
from config import ASSETS, PERIOD, INTERVAL, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

all_data = []

for symbol, asset_type in ASSETS.items():
    df = yf.Ticker(symbol).history(period=PERIOD, interval=INTERVAL)
    df.reset_index(inplace=True)

    df = df[["Date", "Close", "Volume"]]
    df.columns = ["trade_date", "close_price", "volume"]

    df["symbol"] = symbol
    df["asset_type"] = asset_type

    df.to_sql("asset_prices", engine, if_exists="append", index=False)
    all_data.append(df)

pd.concat(all_data).to_json("../data/raw_yahoo_data.json", orient="records", indent=2)

print("✅ All assets ingested into MySQL")
