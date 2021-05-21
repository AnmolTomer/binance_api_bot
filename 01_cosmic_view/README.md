- Create `config.py` file with following contents before running `get_data.py`

```py
API_KEY='your_api_key'
API_SECRET='your_api_secret'
```

# 01_cosmicview

- Flask WebApp that fetches all the coins held as well as ability to place an order for the coin user wants to buy.

- Different topics covered gradually in the course

## Part1 - Websockets and Real-Time Lightweight Charts

- What is binance and how does it compare to other exchanges?
- Why crypto? Open on nights and weekends, learn new things by doing.
- wscat - connect to websocket from the command line
- Capture output to a file
- Connect to websocket from the Web/JavaScript
- Lightweight Charts - Create real-time candle stick chart similar to trading view
- UI to check for Indicators e.g. RSI, MACD, configure values, configure alerts/notifications.

---

## Part 2 - Technical Analysis with Python and TALib

- Connect to websockets from Python, write candlestick data to CSV
- Download some historical data using a REST API
- Install TALib, try out some indicators on a dataset.

---

## Part 3 - Backtesting with Backtrader and TALib Indicators

- Test some indicators against a historical
- Plot some pretty charts with buy and sell points, results

---

## Part 4 - Executing a buy order through webapp

- API endpoint for executing a buy order

## References

- [Binance Spot API Docs](https://github.com/binance/binance-spot-api-docs)
- [Python Wrapper for Binance REST API v3](https://python-binance.readthedocs.io/en/latest/binance.html)
- [Hacking The Markets](https://discuss.hackingthemarkets.com/)
- [Lightweight Charts](http://tradingview.com/lightweight-charts)
