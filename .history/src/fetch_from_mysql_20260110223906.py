import pandas as pd
from sqlalchemy import create_engine
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

# -----------------------------
# MYSQL CONNECTION
# -----------------------------
engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

# -----------------------------
# SQL QUERY (UPDATED)
# -----------------------------
query = """
SELECT
    trade_date,
    open-price,
    close_price,
    volume
FROM stock_prices
WHERE ticker = 'AAPL'
ORDER BY trade_date;
"""

# -----------------------------
# FETCH DATA
# -----------------------------
df = pd.read_sql(query, engine)

print(df.head())
