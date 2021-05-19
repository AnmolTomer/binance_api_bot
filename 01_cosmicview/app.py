# Import Flask from flask package
from flask import Flask, render_template
import config
import csv

from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)
# Create new app from flask object
app = Flask(__name__)


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
    print(balances)  # Returns list of assets with balance

    return render_template('index.html', title=title)


@app.route('/buy')
def buy():
    return 'Buy'


@app.route('/sell')
def sell():
    return 'Sell'


@app.route('/settings')
def settings():
    return 'Settings'
