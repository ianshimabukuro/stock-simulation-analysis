from Investor import *
import matplotlib.pyplot as plt

intrinsic_value = 20
current_value = 20
t_period = 2000
n_investors = 500
list_of_investors = init_investor_list(n_investors)

stock_evolution = []
for t in range(0,t_period):
    for investor in list_of_investors:
        current_perception = investor.evaluate(intrinsic_value)
        buy_or_sell = investor.buy_or_sell(current_perception, intrinsic_value)
        last = investor.def_buysellprice(current_price=current_value, buy_sell=buy_or_sell)
        current_value = last[1]
    stock_evolution.append(current_value)
plt.plot(stock_evolution)
plt.show()
print(stock_evolution)
