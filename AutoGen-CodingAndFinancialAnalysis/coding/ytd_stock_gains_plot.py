# filename: ytd_stock_gains_plot.py
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Function to fetch and compute gain
def fetch_and_plot(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    data['Gain'] = (data['Close'] / data['Close'].iloc[0] - 1) * 100
    return data['Gain']

# Specifying the start of the year and the current date.
start_ytd = "2025-01-01"
current_date = "2025-01-15"

# Fetching data for NVDA and TSLA
nvda_gains = fetch_and_plot('NVDA', start_ytd, current_date)
tsla_gains = fetch_and_plot('TSLA', start_ytd, current_date)

# Plotting the data
plt.figure(figsize=(10, 5))
plt.plot(nvda_gains.index, nvda_gains, label='NVDA YTD Gain %')
plt.plot(tsla_gains.index, tsla_gains, label='TSLA YTD Gain %')
plt.title('NVIDIA and Tesla YTD Stock Gains as of 2025-01-15')
plt.xlabel('Date')
plt.ylabel('Gain (%)')
plt.legend()
plt.grid(True)

# Save the plot to a file
plt.savefig('ytd_stock_gains.png')
plt.show()