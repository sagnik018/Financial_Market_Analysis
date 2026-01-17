import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

df = pd.read_sql(
    "SELECT trade_date, close_price FROM stock_prices",
    engine
)

plt.figure(figsize=(10, 5))
plt.plot(df["trade_date"], df["close_price"])
plt.title("Yahoo Finance Stock Price Trend")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.grid(True)
plt.show()
