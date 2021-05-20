# Plotting Oversold Conditions with TA-Lib RSI, Backtrader and Python

- Now we will be using TA-Lib and look at technical indicators in conjunction with Backtrader and backtest the strategy, use RSI to find over sold and overbought coins.

- RSI is a relative strength index indicator, commonly when RSI is above 70 it means that particular coin/stock/commodity is overbought and in regions where RSI is above 70 you should ideally look at closing your position and when RSI is below 30 or close to it, it means that it is oversold right now and this is a good time to buy the asset.

- We use get_data to get 1 day candlestick data for BTCUSDT.

- You might encounter an issue when you run backtest.py that has something to do with dates, for that make sure you install backtrader patch and then installing v3.2.2 of matplotlib. Simply run these 2 commands:

```
pip install git+https://github.com/mementum/backtrader.git@0fa63ef4a35dc53cc7320813f8b15480c8f85517#egg=backtrader

pip uninstall matplotlib

pip install matplotlib==3.2.2
```

- More details on the issues mentioned above, Matplotlib dates issue fix backtrader [Link](https://github.com/mementum/backtrader/pull/418), Link to same issue on StackOverFlow: [Link](https://stackoverflow.com/questions/63471764/importerror-cannot-import-name-warnings-from-matplotlib-dates)

- Now when you have fixed the date related issues and you run backtest.py you will get a plot which will look similar to this:

![](https://i.imgur.com/ir5uoAE.png)

- Next we create a strategy based off of RSI, for that we create a new class in backtest.py named `RSIStrategy()`. We make use of talib in backtrader as both of them have a well documented integration. You can read the docs [here](https://www.backtrader.com/docu/talib/talib/)

- Strategy to do sell at RSI > 70, buy at RSI < 30 on 5 minute scale from Jan 2020 to Jul 2020 gives us following set of trades:

![](https://i.imgur.com/Qac5DKe.png)
