
import yfinance as yf
import plotly.graph_objects as go

ticker = "TSLA"
userTicker = input("Write ticker name: ")
if userTicker:
    ticker = userTicker

data = yf.download(tickers=ticker, period="6mo", interval="1d", rounding=True)
print(data)