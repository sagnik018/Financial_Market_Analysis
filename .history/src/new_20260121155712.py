import yfinance as yfinance
stock =yf.Ticker("AAPL")
df = stock.history(period="2")