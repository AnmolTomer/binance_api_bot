# Import Flask from flask package
from flask import Flask, render_template, request, flash, redirect
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
