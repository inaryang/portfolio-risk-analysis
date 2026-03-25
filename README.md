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

- Retrieved historical adjusted closing prices using `yfinance`
- Computed daily simple returns for each asset
- Constructed baseline portfolios with predefined weight allocations
- Implemented a Monte Carlo simulation of 10,000 randomly generated portfolios (weights normalized to sum to 1)
- Calculated annualized return and volatility (assuming 252 trading days)
- Evaluated portfolio performance using the Sharpe ratio
- Visualized the efficient frontier and identified the maximum Sharpe ratio portfolio

---

## Results and Analysis

- The S&P 500 ETF (SPY) achieved the highest Sharpe ratio among manually constructed portfolios
- Individual equities (e.g., AAPL) generated higher raw returns but exhibited substantially higher volatility, reducing risk-adjusted performance
- Diversified portfolios reduced volatility but did not outperform SPY under naive weighting schemes
- Simulation identified portfolios with superior Sharpe ratios, demonstrating that optimal allocation requires systematic optimization rather than heuristic diversification

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
