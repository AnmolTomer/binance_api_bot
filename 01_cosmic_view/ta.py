import numpy as np
import talib
from numpy import genfromtxt

""" 
# numpy array is faster for scientific computation
close = np.random.random(100)

# print(type(close))
# print(close)

# Simple Moving average
moving_average = talib.SMA(close, timeperiod=10)
# By default we have 30 day SMA, so first 29 are nan, we change it using timeperiod=10
print(moving_average)

# RSI to see overbought above 70 or oversold below 30
rsi = talib.RSI(close)
print(rsi)
 """

# Import 01_cosmicview\kline_15min.csv

kline_data = genfromtxt('01_cosmicview\kline_15min.csv', delimiter=',')

# print(kline_data)

# Import only the close value i.e. 4th column
close = kline_data[:, 4]
# print(close)

# Apply rsi indicator to BTCUSDT closing price on 15min candlestick
rsi = talib.RSI(close)
print(rsi)
