# Real Time Candlestick Charts using Websockets and JS

- Chart using static values created with ability to buy the coins and retrieve the account balances using our widget.

- Settings form created for RSI indicator which takes the value of overbought and oversold. We send this to python script that reads price data and sends it to a technical analysis library and executes buy/sell based on conditions.

- We start updating the candlesticks in real time now. We have python code `get_data.py` that can retrieve kline information and store it in csv format which contains date, open, high, low, close data. We define a route `/history` which gives the data in a list for BTC let's say.

- List of objects containing close, high, low, open and time for candlestick generation sent to `/history` route.

![](https://i.imgur.com/XlHsTcs.png)

- We have the response in the format we want. Now we set the data using `candleSeries.setData(response)`

![](https://i.imgur.com/LVU3e2B.png)

- Real time data added to chart and console

![](https://i.imgur.com/goE4rBC.png)

- Next, we stream and add data in real time to the chart. Connect to the binance websocket stream and instead of logging to the console, add the WSS stream to the chart.

- Real Time Demo Video: [Here](https://i.imgur.com/3ZurzD3.mp4)
