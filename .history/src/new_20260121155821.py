import yfinance as y
stock =yf.Ticker("AAPL")
df = stock.history(period="2yr")
print(df.head())