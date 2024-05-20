import random
from datetime import datetime
from Stock import Stock
from Market import Market
from Investor import Investor
import generate

n_shares = 5
n_investors = 40
inv_list = generate.generate_inv_list(n_investors)
stock_list  = generate.generate_stock_list(n_shares)
t_max = 500
tickers = []
market = Market(stocks=stock_list,top = tickers )

for t in range(0,t_max):
    for investor in inv_list:
        decision = random.choices(["Sell","Buy","Hold"],weights = [investor.sell_probability,investor.buy_probability,investor.hold_probability])
        print(decision)
        if decision[0] == "Sell":
            investor.set_to_selling(market,10,investor.my_shares)
        elif decision[0] == "Buy":
            b_price=investor.set_buying_price(market)
            candidate_id = market.match(b_price)
            tick=market.trade(candidate_id,investor)
            tickers.append(tick)
        elif decision[0] == "Hold":
            investor.set_to_hold(market,investor.my_shares)
        else:
            print("Error")




print(tickers)



