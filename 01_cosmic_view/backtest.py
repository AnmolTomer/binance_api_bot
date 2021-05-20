from itertools import compress
import backtrader as bt
import datetime


class RSIStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=14)

    def next(self):
        if self.rsi <= 30 and not self.position:
            self.buy(size=1)
        if self.rsi > 70 and self.position:
            self.close()


cerebro = bt.Cerebro()

# https://www.backtrader.com/docu/
# Matplotlib dates issue fix backtrader https://github.com/mementum/backtrader/pull/418

# Specify dates when you are doing for a range in a dataset having larger range

fromdate = datetime.datetime.strptime('2020-07-01', '%Y-%m-%d')
todate = datetime.datetime.strptime('2020-07-12', '%Y-%m-%d')
data = bt.feeds.GenericCSVData(dataname='./data/BTCUSDT_Jan_Jul_2020_15min.csv',
                               dtformat=2, compression=15, timeframe=bt.TimeFrame.Minutes, fromdate=fromdate, todate=todate)

# We have float in date format and for that we use 2 as dtformat
# dataname='./data/BTCUSDT_Jan_Jul_2020_15min.csv', dtformat=2)  # For data when candlesticks are for 1 day

# dataname='./data/BTCUSDT_Jan_Jul_2020_15min.csv', dtformat=2, compression=15, timeframe=bt.TimeFrame.Minutes)
# When data is in minutes as the case is here we use compression and specify minutes using timeframe.


cerebro.adddata(data)

cerebro.addstrategy(RSIStrategy)
cerebro.run()

# BTC Price data from Jan 1 2021 to 20 May 2021
cerebro.plot()
