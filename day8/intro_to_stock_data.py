import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("NVDA", start="2024-01-01", end="2024-12-01")

print(df.head())
print(df.info())
print(df.describe())

df["Close"].plot(title="Apple Stock Closing price")
plt.show()