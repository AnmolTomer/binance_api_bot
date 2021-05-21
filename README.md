# binance_api_bot

> :warning: **WORK IN PROGRESS** :warning:

- Collection of multiple mini projects made while experimenting with Binance API, trying technical analysis libraries, backtrader package and following binance academy guides and so on.

## [01_cosmic_view](01_cosmic_view)

- Flask webapp which displays all the coins currently a user holds both in spot as well as savings wallet with an ability to buy coins from a dropdown window to select from. Could have a better UI, functionally tested, working as intended.

## [02_trading_bot](./02_trading_bot) 

-Simple CLI based Trading Bot that is connected to TA-Lib and looks for a certain threshold of RSI value and when the share is overbought i.e. RSI > 70 it closes off the position automatically, and at oversold i.e. RSI < 30 opens the position by purchasing the specified quantity of a given token.

- Strategy could be made better by taking in Bollinger Bands, MACD instead of only using RSI but the proof of concept is implemented, strategy for trading needs to be made better. Programatically the solution is end to end.

- Receives the data in web socket streams from binance in JSON form, converts the json objects into python list using `json.loads()`, check if the data belongs to final candle of 1 minute time frame, because for RSI we only need closing position of a candle.

- Check the RSI threshold, do buy, sell order by hitting the binance-python order end point value as per RSI threshold.
