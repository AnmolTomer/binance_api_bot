import pprint
import websocket
import json
import numpy
import talib
import config

from binance.enums import *
# enums holds the constant values needed to sent to Binance API
from binance.client import Client

# CONSTANTS
RSI_PERIOD = 14
OVERSOLD_THRESHOLD = 30
OVERBOUGHT_THRESHOLD = 70
TRADE_QUANTITY = 0.05

# Symbol that we will be trading
TRADE_SYMBOL = 'ETHUSD'


def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print("Sending Order ✅📩")
        order = client.create_test_order(
            symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(order)

    except Exception as e:
        return False
    return True

    # Data will be received through websocket stream, link https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md
SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

# List to keep track of at what value candle closed
closes = []

in_position = False  # Tracking if we have purchased / in the position or not.
client = Client(config.API_KEY, config.API_SECRET)


# Connect to a websocket and create WebSocketApp

def on_open(ws):
    print('Opened Connection.')


def on_close(ws):
    print('Closed connection.')


r = 0


def on_message(ws, message):
    global closes, r, in_position

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
        print("-------------------------------------------------")
        print(f"Candle closed at {close}")
        closes.append(float(close))
        print(f"Closes: {closes}")

# For talib convert closes into a numpy array
        if(len(closes) > RSI_PERIOD):
            np_closes = numpy.array(closes)
            # Calculate series of RSI values
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("All RSIs calculated so far: ")
            print(rsi)
            last_rsi = rsi[-1]
            print(f"The current RSI is: {last_rsi}")
            print("-------------------------------------------------")

        if(last_rsi > OVERBOUGHT_THRESHOLD):
            if in_position:
                print("SELL ! SELL ! SELL !")
                order_succeeded = order(
                    SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)
                # if order_succeeded then get out of position
                if order_succeeded:
                    in_position = False
            # put binance sell logic here
            else:
                print("It is overbought, We don't own any, nothing to do.")

        if(last_rsi < OVERSOLD_THRESHOLD):
            if in_position:
                print("It is oversold, but you already own it, nothing to do.")
            else:
                print("Buy! Buy! Buy!")

                # put binance buy logic here https://python-binance.readthedocs.io/en/latest/account.html#id3
                order_succeeded = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)
                if order_succeeded:
                    in_position = True


# WebSocketApp requires some callbacks so we need functions for, when function is opened, closed and when message comes
ws = websocket.WebSocketApp(SOCKET, on_open=on_open,
                            on_message=on_message, on_close=on_close)

ws.run_forever()  # Run forever
