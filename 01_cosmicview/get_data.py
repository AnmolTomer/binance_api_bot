# Import config containing api keys

# Docs for binance-python https://python-binance.readthedocs.io/en/latest/

import config
import csv

from binance.client import Client

# Instantiate Client and pass in API_KEY and API_SECRET
client = Client(config.API_KEY, config.API_SECRET)
# ---------------------------------------------------------------------

"""
# get_all_tickers() method gives us a list of coins and their price
prices = client.get_all_tickers()
# Print first 25 coins
for price in prices[:25]:
    print(price)

# Prints tickers of all the coins returned

for price in prices:
    print(price)
"""


# Refer https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data to understand what does the returned data contains.
# Write the information to a csv file https://docs.python.org/3/library/csv.html

# Check length of candles
# Gives 500 15 Minute candlesticks
# -----------------------------------------------------------------------------
# print(f"Number of candles data returned = {len(candles)}")

# Insert Headings - Just the format, do not uncomment the below block

"""
kline_writer.writerow([
    "Open Time", "Open", "High", "Low", "Close", "Volume", "Close time", "Quote asset volume", "Number of trades", "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"
])
"""
# -----------------------------------------------------------------------------

csvfile = open(
    './data/BTCUSDT_Jan_Jul_2020_15min.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

candles = client.get_historical_klines(
    "BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2020", "12 Jul, 2020")

# Pass in a list to write a row while iterating over candles
for candlestick in candles:
    candlestick[0] = candlestick[0]/1000
    print(candlestick[0])
    print(candlestick)
    candlestick_writer.writerow(candlestick)
