# Account Balances, Exchange Info and Buy Execution

- We installed Flask and wrote some routes with functions.

- Check [Account Endpoints](https://python-binance.readthedocs.io/en/latest/account.html) in python-binance package.

![](https://i.imgur.com/VavwmvW.png)

- Result after including `info = client.get_account() print(info)` on index page. Shows all the currencies and amount held.

![](https://i.imgur.com/PJP369Z.png)

- In flask we want all of our logic stuff like access to APIs, databases etc. we want on Python. In templates we want to display all of our calculations and information.

- Refer [account endpoints](https://python-binance.readthedocs.io/en/latest/account.html) to see how to place orders.

- Use redirect and flash messages to display the messages when exception thrown while trying to buy coins.

- If order failed then display the error and redirect to index.html.

![](https://i.imgur.com/HtJ6pgZ.png)

- 200 response when order is successful.

![](https://i.imgur.com/nuEBLox.png)
