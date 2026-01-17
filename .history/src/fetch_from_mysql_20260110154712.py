import pandas as pd
from sqlalchemy import create_engine
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

query = """
SELECT trade_date, close_price, volume
FROM stock_prices
ORDER BY trade_date;
"""

df = pd.read_sql(query, engine)
print(df.head())
