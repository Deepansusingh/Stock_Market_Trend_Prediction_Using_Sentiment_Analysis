import yfinance as yf
ticker = "AAPL"
data = yf.download(ticker, start="2020-01-01", end="2020-01-10")
print("Columns:", data.columns)
try:
    close = data['Close']
    print("Can access 'Close'")
except Exception as e:
    print(f"Error accessing 'Close': {e}")
try:
    close_attr = data.Close
    print("Can access data.Close")
except Exception as e:
    print(f"Error accessing data.Close: {e}")
