# filename: download_and_plot_stocks.py
from functions import get_stock_prices, plot_stock_prices
import matplotlib.pyplot as plt

# Set the desired symbols and date range
symbols = ['NVDA', 'TSLA']
start_date = '2025-01-01'  # Start of the year
end_date = '2025-01-15'   # Today's date

# Retrieve stock prices
stock_prices = get_stock_prices(symbols, start_date, end_date)

# Plotting the stock prices
plot_stock_prices(stock_prices, "stock_prices_YTD_plot.png")