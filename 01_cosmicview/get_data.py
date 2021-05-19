# Import config containing api keys

# Docs for binance-python https://python-binance.readthedocs.io/en/latest/

import config
import csv

from binance.client import Client

# Instantiate Client and pass in API_KEY and API_SECRET
client = Client(config.API_KEY, config.API_SECRET)


# ---------------------------------------------------------------------
# get_all_tickers() method gives us a list of coins and their price
prices = client.get_all_tickers()

""" 
# Print first 25 coins
for price in prices[:25]:
    print(price)

# Prints tickers of all the coins returned

for price in prices:
    print(price)
"""
# ---------------------------------------------------------------------
# GET 15 MINUTE KLINES and write to CSV

""" candles = client.get_klines(
    symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

# Print candlestick data present
for candlestick in candles:
    print(candlestick)
"""

# Refer https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data to understand what does the returned data contains.

# Check length of candles
# Gives 500 15 Minute candlesticks

""" print(f"Number of candles data returned = {len(candles)}")

# Write the information to a csv file https://docs.python.org/3/library/csv.html

csv_file = open('kline_15min.csv', 'w', newline='')
# Write the rows to csv
kline_writer = csv.writer(csv_file, delimiter=',')"""

# Insert Headings

""" kline_writer.writerow([
    "Open Time", "Open", "High", "Low", "Close", "Volume", "Close time", "Quote asset volume", "Number of trades", "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"
]) """

# Pass in a list to write a row while iterating over candles

""" for candlestick in candles:
    print(candlestick)
    kline_writer.writerow(candlestick) """

# ---------------------------------------------------------------------
# Get Historical Kline Data: get_historical_klines()

# 5 minute interval klines from 2012 to 2021. A lot of data!
""" historical_klines = client.get_historical_klines(
    'BTCUSDT', Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2018", "18 May, 2021")

# https: // python-binance.readthedocs.io/en/latest/market_data.html  # id7
hist_csv_file = open('hist_kline_5min_2018_2021.csv', 'w', newline='')
hist_kline_writer = csv.writer(hist_csv_file, delimiter=',')

for candlestick in historical_klines:
    print(candlestick)
    hist_kline_writer.writerow(candlestick)
 """
