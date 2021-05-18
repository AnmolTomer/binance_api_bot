## 02. Real Time Crypto Price Data over Websockets

- We will obtain crypto data using binance websockets. We can connect with websockets either using CLI tool such as wscat, we can use js, python websocket client can be used as well to connect and respond to the messages that we receive from websocket streams.

- Base endpoint is: `wss://stream.binance.com:9443`
- Raw streams are accessed at `/ws/<streamName>`
- Complete details on websockets stream [here](https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md)

## Installing and working with wscat

- `npm install -g wscat` to install wscat. Connect to a websocket server by doing `wscat -c <url>`. We will be connecting to `wss://stream.binance.com:9443/ws/btcusdt@trade`. This will give you following stream of data in your terminal:

![](https://i.imgur.com/ebX3dX2.png)

- So the response you see in the image above looks like this `{"e":"trade","E":1621307691228,"s":"BTCUSDT","t":842121829,"p":"44852.05000000","q":"0.03034500","b":5978224874,"a":5978225053,"T":1621307691226,"m":true,"M":true}`. What we really do in a websocket stream is we subscribe to a stream and it sends us data in json format, here `"s"` is for symbol, `"T"` is for unix time-stamp, if I put `1621307691226` in [unixtimestamp.com](http://unixtimestamp.com/) we will get the date, time along with timezone. Similarly `p` tells us the price at which `BTCUSDT` pair was trading at that time.

![](https://i.imgur.com/AgdQjJH.png)

- The entire payload of what we are receiving is as follows:

```json
{
  "e": "trade", // Event type
  "E": 123456789, // Event time
  "s": "BNBBTC", // Symbol
  "t": 12345, // Trade ID
  "p": "0.001", // Price
  "q": "100", // Quantity
  "b": 88, // Buyer order ID
  "a": 50, // Seller order ID
  "T": 123456785, // Trade time
  "m": true, // Is the buyer the market maker?
  "M": true // Ignore
}
```

- We aren't really interested in getting every single trade happening for a particular cryptocurrency. Next, we will be looking at `Kline/Candlestick Streams` and how they can be used, as per defined timeframe. We just do `<symbol>@kline_<interval>` for this. `wss://stream.binance.com:9443/ws/btcusdt@kline_1m` and we connect to this stream using `wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_1m`.

![](https://i.imgur.com/wTheQHi.png)

- In the above kline stream we are getting data at a slower rate as well as responses have a timestamp as follows: `1621308419999`, `1621308419999`. Candlestick data looks as follows:

```json
{
  "e": "kline", // Event type
  "E": 123456789, // Event time
  "s": "BNBBTC", // Symbol
  "k": {
    "t": 123400000, // Kline start time
    "T": 123460000, // Kline close time
    "s": "BNBBTC", // Symbol
    "i": "1m", // Interval
    "f": 100, // First trade ID
    "L": 200, // Last trade ID
    "o": "0.0010", // Open price
    "c": "0.0020", // Close price
    "h": "0.0025", // High price
    "l": "0.0015", // Low price
    "v": "1000", // Base asset volume
    "n": 100, // Number of trades
    "x": false, // Is this kline closed?
    "q": "1.0000", // Quote asset volume
    "V": "500", // Taker buy base asset volume
    "Q": "0.500", // Taker buy quote asset volume
    "B": "123456" // Ignore
  }
}
```

- So far, so good. So maybe we don't want to just stream the data in our console, say we want to capture this data into a file so that it can be used for analysis. We can do `wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m | tee datasaet.txt`

![](https://i.imgur.com/Cfv8SW5.png)

- You can use something like the command we are running above to create your own historical data as well, instead of paying 3rd-party providers for historical data.

- Now we have connected to websocket using `wscat`, next we will be moving towards connecting to websocket through programming language of our choice. We will do it first using js. Ref: [01_coinview](./01_cosmicview)

- We want to connect a websocket, for that open developer tools on your preferred browser. We will be using websocket object that JavaScript has built in, we instantiate it and connect to it. More on WebSockets on MDN Docs [here](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications)

- On including the call to web stream we get the following response when we console log it:

![](https://i.imgur.com/5kPbn06.png)

- To receive the message and interpreting the JSON objects we will use `onmessage` function. More on this [here](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications#receiving_messages_from_the_server)

- Logging to console the values coming from websocket stream.

![](https://i.imgur.com/LIVAKkG.png)

- Now we display those values on the webpage instead of console. Result is as follows:

![](https://i.imgur.com/c0RjL5v.png)
