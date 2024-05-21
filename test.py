
import random
from datetime import datetime
from Stock import Stock
from Market import Market
from Investor import Investor
import generate
import matplotlib.pyplot as plt
import time

n_shares = 20
n_investors = 20
inv_list = generate.generate_inv_list(n_investors)
stock_list = generate.generate_stock_list(n_shares)
t_max = 20000
tickers = []
market = Market(stocks=stock_list,top=tickers)
start = time.time()
for t in range(0, t_max):
    print(t)
    for investor in inv_list:
        investor.evaluate(market,20)
        print(investor.eval)
        investor.update_prob(market)
        print(investor.sell_probability,investor.buy_probability,investor.hold_probability)
        decision = random.choices(["Sell", "Buy", "Hold"], weights=[investor.sell_probability, investor.buy_probability, investor.hold_probability])
        if decision[0] == "Sell":
            investor.set_to_selling(market, market.average_price, investor.my_shares)
        elif decision[0] == "Buy":
            b_price = investor.set_buying_price(market)
            candidate_id = market.match(b_price)
            if candidate_id is not None:
                tick = market.trade(candidate_id, investor)
                tickers.append(tick)
        else:
            investor.set_to_hold(market, investor.my_shares)

        investor.update_my_shares(market)
end = time.time()

print("Time elapsed", end-start)
x_val = [x[0] for x in tickers]
y_val = [x[1] for x in tickers]
for stock in market.stocks:
    print(stock.owner,stock.last_buy)

plt.plot(y_val, x_val)

plt.show()





