# Historical Data Retrieval Using Binance Python Package

- We retrieve historical candle data, then we see how to authenticate and retrieve candlesticks data and show them on lightweight charts.

- Running ta-lib indicators on the historical data and test ta-lib results with backtrader.

- Search for `python binance` and install the package. Have your API_KEY and API_SECRET. We use `get_data.py` to get the prices using `get_all_tickers()` method.

![](https://i.imgur.com/0Y7iJRu.png)

- binance-python package has lots of endpoints available such as General Endpoints, Market Data Endpoints, Account Endpoints, Margin Trading Endpoints, Websockets, Withdraw Endpoints etc.

- We will be looking at market data, specifically candlestick data and historical data to do backtesting and use with ta-lib. For that we will look into `Market Data Endpoints > Get Kline/Candlesticks`. Binance docs can be found [here](https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data).

- Data returned from KLine endpoint is as follows:

```json
[
  [
    1499040000000, // Open time
    "0.01634790", // Open
    "0.80000000", // High
    "0.01575800", // Low
    "0.01577100", // Close
    "148976.11427815", // Volume
    1499644799999, // Close time
    "2434.19055334", // Quote asset volume
    308, // Number of trades
    "1756.87402397", // Taker buy base asset volume
    "28.46694368", // Taker buy quote asset volume
    "17928899.62484339" // Ignore.
  ]
]
```

- Get historical kline data [documentation](https://python-binance.readthedocs.io/en/latest/market_data.html#id7)
