# Portfolio Optimization and Efficient Frontier Analysis

This project analyzes portfolio construction using historical market data from Yahoo Finance. 
It evaluates multiple asset allocations and simulates 10,000 random portfolios to study the tradeoff between return and risk.

The goal is to identify optimal portfolios using the Sharpe ratio and visualize the efficient frontier.

---

## Assets Analyzed
- AAPL
- MSFT
- SPY

---

## Methods

- Retrieved historical price data using `yfinance`
- Computed daily returns for each asset
- Constructed multiple portfolios with predefined weights
- Simulated 10,000 random portfolios with normalized weights
- Calculated annualized return and volatility
- Evaluated performance using the Sharpe ratio

---

## Results

- The S&P 500 ETF (SPY) achieved the highest Sharpe ratio among manually constructed portfolios
- Higher-return assets (e.g., AAPL) exhibited significantly higher volatility, reducing risk-adjusted performance
- Simulated portfolios identified allocations with improved Sharpe ratios compared to naive weightings
- These results highlight that optimal portfolio construction requires balancing return and volatility, not simply maximizing returns

---

## Visualizations

### Manual Portfolio Growth
Shows cumulative returns of different portfolio allocations over time.

### Efficient Frontier
Displays the distribution of 10,000 simulated portfolios in return-volatility space, with color representing Sharpe ratio.  
The maximum Sharpe portfolio is highlighted.

---

## How to Run

```bash
pip install -r requirements.txt
python portfolio_optimization.py
