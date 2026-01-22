
import yfinance as yf
stock =yf.Ticker("AAPL")
df = stock.history(period="2y")
print(df.head())