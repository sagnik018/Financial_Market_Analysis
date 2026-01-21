import yfinance as yf
stock =yf.Ticker("AAPL")
df = stock.history(period="2yr")
print(df.head())