import pprint
import websocket
import json
import numpy
import talib
import config

from binance.enums import *
from binance.client import Client

# CONSTANTS
RSI_PERIOD = 14
OVERSOLD_THRESHOLD = 30
OVERBOUGHT_THRESHOLD = 70
TRADE_QUANTITY = 0.05

# Symbol that we will be trading
TRADE_SYMBOL = 'ETHUSD'

# Data will be received through websocket stream, link https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md
SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

# List to keep track of at what value candle closed
closes = []

in_position = False  # Tracking if we have purchased / in the position or not.
# client = Client.config(config.API_KEY, config.API_SECRET)


# Connect to a websocket and create WebSocketApp

def on_open(ws):
    print('Opened Connection.')


def on_close(ws):
    print('Closed connection.')


r = 0


def on_message(ws, message):
    global closes, r

    if(r == 0):
        print('Received Message')
        r += 1
    # As we are getting json data, we use json.loads() takes a json string and convert it into Python data object
    json_message = json.loads(message)
    # Pretty print to display data in console properly
    # pprint.pprint(json_message)

# "k" in the message holds the info we need for candlesticks https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md#klinecandlestick-streams
    candle = json_message['k']
    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        print(f"Candle closed at {close}")
        closes.append(close)
        print(f"Closes: {closes}")


# WebSocketApp requires some callbacks so we need functions for, when function is opened, closed and when message comes
ws = websocket.WebSocketApp(SOCKET, on_open=on_open,
                            on_message=on_message, on_close=on_close)

ws.run_forever()  # Run forever
