# filename: fetch_nvidia_stock_data.py

import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data[['Close', 'Volume']]

# Set the ticker, start date, and end date for Nvidia
ticker = 'NVDA'
start_date = '2024-03-23'
end_date = '2024-04-22'

# Fetching the data
nvidia_stock_data = fetch_stock_data(ticker, start_date, end_date)

# Output results
print(nvidia_stock_data)