import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# get stock data from yahoofinance
df = yf.download("NVDA", start="2024-01-01", end="2024-12-01")

# get the first 5 rows
print(df.head())
# get the information on each column
print(df.info())
# get the statistical information of each column
print(df.describe())

# Plot the closing price of the stock data
df["Close"].plot(title="NVIDIA Stock Closing price")
plt.show()