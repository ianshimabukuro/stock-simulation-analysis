import random
from datetime import datetime
from Stock import Stock
from Market import Market
from Investor import Investor

n_shares = 5
investor_name = ["joe","max","mark","chris","ian"]
list=[]
for i in range(0,n_shares):
    list.append(Stock(owner=investor_name[i],last_buy= random.randint(5,10),selling =random.choice([True, False]),current_sell=random.randint(6,11),last_traded_at =datetime.now()))

for item in list:
    print(item.owner,item.last_buy,item.selling,item.current_sell,item.last_traded_at)
top = 0
market = Market(stocks=list,top = top )
print(market.average_price,market.latest_traded_price)

