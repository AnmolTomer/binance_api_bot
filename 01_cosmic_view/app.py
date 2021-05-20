# Import Flask from flask package
from flask import Flask, render_template, request, flash, redirect, jsonify
import config
import csv
from binance.enums import *

from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)
# Create new app from flask object
app = Flask(__name__)

app.secret_key = 'A0Zr98jyXXHHjmN]LWX'
# Define routes and the function that will run when that route is called.


@app.route('/')
def index():
    title = 'CosmicView'
    # Display html template using render_template and send it to the page, and we can place the title value
    info = client.get_account()

    # print(info)
    """ for inf in info:
        print(inf) """
    balances = info['balances']
    # print(balances)  # Returns list of assets with balance
    exchange_info = client.get_exchange_info()
    symbols = exchange_info['symbols']
    return render_template('index.html', title=title, my_balances=balances, symbols=symbols)


@app.route('/buy', methods=['POST'])
def buy():
    print(request.form)
    try:
        order = client.create_test_order(symbol=request.form['symbol'],
                                         side=SIDE_BUY,
                                         type=ORDER_TYPE_MARKET,
                                         quantity=request.form['quantity'])
    except Exception as e:
        flash(e.message, "error")

    return redirect('/')


@app.route('/sell')
def sell():
    return 'Sell'


@app.route('/settings')
def settings():
    return 'Settings'


@app.route('/history')
def history():
    candlesticks = client.get_historical_klines(
        "BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 May, 2021", "20 May, 2021")
# Processed candlesticks where the format is same as what's required by lightweight-charts
    processed_candlesticks = []
 # format we want to append to processed_candlesticks => {'time': '2020-05-01',open: 180.34,high: 180.99, low: 178.57, close: 179.85}
    for data in candlesticks:
        data[0] /= 1000
        candlestick = {'time': data[0],
                       "open": data[1],
                       "high": data[2],
                       "low": data[3],
                       "close": data[4]
                       }

        processed_candlesticks.append(candlestick)

    if(candlesticks):
        print("Successfully retrieved klines.✅")
    return jsonify(processed_candlesticks)
# Import jsonify and this will allow us to take data and return python list as json
