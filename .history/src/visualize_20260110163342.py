import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

sns.set(style="whitegrid")

engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

df = pd.read_sql("SELECT * FROM asset_prices", engine)
df["daily_return"] = df.groupby("symbol")["close_price"].pct_change()

# Price trends
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x="trade_date", y="close_price", hue="symbol")
plt.title("Price Trends of Assets")
plt.savefig("../reports/price_trends.png")
plt.close()

# Risk vs Return
summary = df.groupby("symbol").agg(
    avg_return=("daily_return", "mean"),
    risk=("daily_return", "std")
).reset_index()

plt.figure(figsize=(8,6))
sns.scatterplot(data=summary, x="risk", y="avg_return", hue="symbol", s=100)
plt.title("Risk vs Return Comparison")
plt.savefig("../reports/risk_return.png")
plt.close()

print("📈 Visualizations saved in reports/")
