import pandas as pd
import yfinance as yf
import plotly.express as px

df = yf.download('AAPL', start='2020-01-01', end='2020-01-10')
if isinstance(df.columns, pd.MultiIndex):
    df.columns = [col[0] for col in df.columns]
df.reset_index(inplace=True)
df['Date'] = pd.to_datetime(df['Date']).dt.date
df.dropna(inplace=True)

try:
    fig = px.line(df, x='Date', y='Close', title='Test')
    print("Plotly build successful!")
except Exception as e:
    print(f"Error building plot: {e}")
