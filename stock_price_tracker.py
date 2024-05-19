import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

def fetch_real_time_stock_price(ticker):
    # Fetch the real-time stock data
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d", interval="1m")

    return data

def plot_stock_data(data, ticker):
    fig = go.Figure()

    # Adding trace for the closing prices
    fig.add_trace(go.Scatter(
        x=data.index, y=data['Close'],
        mode='lines', name='Close'
    ))

    # Adding layout details
    fig.update_layout(
        title=f"Real-Time Stock Price for {ticker}",
        xaxis_title="Time",
        yaxis_title="Price (USD)",
        xaxis_rangeslider_visible=True
    )

    fig.show()

if __name__ == "__main__":
    ticker = "AAPL"  # Example: Apple Inc.
    data = fetch_real_time_stock_price(ticker)
    plot_stock_data(data, ticker)
