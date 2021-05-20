# Candlestick Chart UI with Lightweight Charts

- Now we use lightweight charts library to add a candlestick chart to our UI and make some design changes to UI. Last time we connected to the websocket stream and appended the price of BTCUSDT on the webpage.

- [Lightweight-Charts](https://github.com/tradingview/lightweight-charts)

- Create a div for the charts and pass in the id of div to the chart.js using `getElementById`, we get a chart as follows:

![](https://i.imgur.com/SoQiA2R.gif)

- We place some placeholders so that user can enter some input and they can give in input. We have RSI indicators and input sections for over sold and over bought in place along with chart from lightweight-charts by TradingView. Ref: [index.html](./01_cosmicview/index.html) and [chart.js](01_cosmicview/chart.js)

- Next we will use Python for backend, connect to the websockets and also look into REST-API, download some historical data, use RSI and some other indicators from `TALib`, put those to test against historical data and then integrate Python with front-end

![](https://i.imgur.com/iULdT7C.png)
