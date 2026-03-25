import yfinance as yf
import pandas as pd
import numpy as np

# Download price data
data = yf.download(["AAPL", "MSFT", "SPY"], start="2022-01-01")
prices = data["Close"]

# Compute daily returns
returns = prices.pct_change().dropna()

# Portfolio weights
weights = np.array([0.5, 0.3, 0.2])

# Portfolio daily returns
portfolio_returns = returns.dot(weights)

# Metrics
mean_daily_return = portfolio_returns.mean()
daily_volatility = portfolio_returns.std()

annual_return = mean_daily_return * 252
annual_volatility = daily_volatility * np.sqrt(252)
sharpe_ratio = annual_return / annual_volatility

print("Annual return:", annual_return)
print("Annual volatility:", annual_volatility)
print("Sharpe ratio:", sharpe_ratio)