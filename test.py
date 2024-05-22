import functions
import random
from datetime import datetime
from Stock import Stock
from Market import Market
from Investor import Investor
import generate
import matplotlib.pyplot as plt
import time

n_shares = 10
n_investors = 30
inv_list = generate.generate_inv_list(n_investors)
stock_list = generate.generate_stock_list(n_shares)
t_max = 3000
tickers = []
market = Market(stocks=stock_list,top=tickers)
start = time.time()


for t in range(0, t_max):
    for investor in inv_list:
        #For each t_step and investor, update their evaluation of the market
        investor.evaluate(market,15)
        investor.update_prob(market)
        #Decide what to do
        decision = random.choices(["Sell", "Buy", "Hold"], weights=[investor.sell_probability, investor.buy_probability, investor.hold_probability])
        print(investor.sell_probability,investor.buy_probability,investor.hold_probability)
        #Take action based on the decision
        if decision[0] == "Sell":
            """Investors will most likely sell for the average stock price, 
            as the further from it the chance of selling is low"""
            ap_price = functions.draw_gaussian(market.average_price,2)
            investor.set_to_selling(market, ap_price, investor.my_shares)
        elif decision[0] == "Buy":
            #Investor will define a price he would buy
            b_price = investor.set_buying_price(market)
            candidate_id = market.match(b_price)
            if candidate_id is not None:
                tick = market.trade(candidate_id, investor)
                tickers.append(tick)
        else:
            investor.set_to_hold(market, investor.my_shares)

        investor.update_my_shares(market)



end = time.time()
print(len(tickers))
print("Time elapsed", end-start)

x_val = [x[0] for x in tickers]
y_val = [x[1] for x in tickers]
plt.plot(y_val, x_val)

plt.show()





