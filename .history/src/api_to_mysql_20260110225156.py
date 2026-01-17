import yfi as yf
import pandas as pd
from sqlalchemy import create_engine
from config import ASSETS, PERIOD, INTERVAL, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

# MYSQL CONNECTION
engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

all_data = []

# FETCH & STORE DATA
for ticker, asset_type in ASSETS.items():
    print(f"📥 Fetching data for {ticker}")

    df = yf.Ticker(ticker).history(
        period=PERIOD,
        interval=INTERVAL,
        auto_adjust=False
    )

    if df.empty:
        print(f"⚠️ No data for {ticker}, skipping")
        continue

    df.reset_index(inplace=True)

    # Rename columns to match MySQL schema EXACTLY
    df = df.rename(columns={
        "Date": "trade_date",
        "Open": "open_price",
        "Close": "close_price",
        "High": "high",
        "Low": "low",
        "Adj Close": "adjusted_close",
        "Volume": "volume"
    })

    df["ticker"] = ticker

    # Reorder columns (important)
    df = df[
        [
            "ticker",
            "trade_date",
            "open_price",
            "close_price",
            "high",
            "low",
            "adjusted_close",
            "volume"
        ]
    ]

    # Insert into MySQL
    df.to_sql(
        "stock_prices",
        engine,
        if_exists="append",
        index=False
    )

    all_data.append(df)
    print(f"✅ {ticker} inserted")

# SAVE RAW DATA (OPTIONAL)

if all_data:
    pd.concat(all_data).to_json(
        "D:/Financial_Market_Analysis/data/raw_yahoo_data.json",
        orient="records",
        indent=2,
        date_format="iso"
    )

print("🚀 ALL ASSETS INGESTED SUCCESSFULLY")
