# Crypto Trading Bot

- Trying to build an automated trading bot using Python, TA-Lib, Binance and websockets to get real time price data and apply TA to the price data and execute trades automatically.

- Install the requirements by doing `pip install -r requirements.txt`.

- Use the `TA-Lib*.whl` provided to install TA-Lib. Refer [01_cosmic_view/05_Notes.md](../01_cosmic_view/Notes/05_Notes.md) for instructions on installing TA-Lib.

- Enter your API and Secret key in [config.py](config.py) file.

- We receive the price data through WSS, we get the candle data, apply technical indicator using TA-Lib to that data, whenever RSI is above overbought_threshold we execute an order and when it is below OVERSOLD_THRESHOLD we execute a sell.

- First we have binance (our broker and data provider), we use web socket to get data. Binance has these bunch of different streams one for candlestick data, another for prices of currencies and so on, we can connect a client to the wss while maintaining a persistent connection rather than always requesting data with HTTP request. Binance has different streams for different coins, BTCUSDT, ETHUSDT, LTCUSDT, VETUSDT etc. All these streams are pushed out continuously.

- In candlestick data we get OHLC (Open, High, Low, Close) which keeps coming in, we need a client to connect with stream of data. We will use python websocket client to read data from the stream. We then process the data, we are interested in closing prices, we apply RSI to the closing prices data and then TA-Lib gives us an RSI score telling us if the coin is overbought or oversold.

- If RSI value > 70 then we hit the Sell endpoint to sell the coin, if RSI < 30 then we hit the Buy Endpoint to buy the oversold coin. Logging WSS to terminal:

![](https://i.imgur.com/Nc8rHXR.png)

- Pretty print the data after converting it into python data object from JSON using `json.loads()`

![](https://i.imgur.com/frG4DTi.png)

- As per documentation [here](https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md#klinecandlestick-streams) if a kline is closed or not is indicated by boolean value `"x"` if it is true it means that the values sent are the final values of that candlestick and that candlestick is closed.

- Since we are using RSI indicator, we care about closing final value of each candle stick and due to this reason we need to capture the closing value. We create an is_candle_closed var to keep a track of this. Then we store in `closes[]` list the last closed values of candlestick after checking which will be sent to TA-Lib for RSI calculation.

![](https://i.imgur.com/8JlFm2M.png)

- RSI Indicator when a coin is overbought RSI value goes above 70 and value goes below 30 when coin is oversold. RSI Calculation on realtime 1minute candlestick data

![](https://i.imgur.com/B0aVZFE.png)

![](https://i.imgur.com/hhKvIki.png)

![](https://i.imgur.com/L8rFw3D.png)

---

## References

- [Python Binance Package](https://python-binance.readthedocs.io/en/latest/index.html)
- [Binance Spot API WSS](https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md)
