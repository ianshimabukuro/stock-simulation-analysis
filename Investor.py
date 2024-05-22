from numpy import random
import math



class Investor:
    def __init__(self,name,type):
        self.name, self.type = name,type
        self.sell_probability = 0.1
        self.buy_probability = 0.1
        self.hold_probability = 0.8
        self.eval = 0
        self.my_shares = []

    def update_prob(self,market):
        Ks = 7
        Kb = 3
        Xs = -3
        Xb = 10
        diff = self.eval - market.average_price

        if not self.my_shares:
            self.sell_probability = 0
            self.buy_probability = 1 / (1 + math.exp(-Kb*(diff - Xb)))
            self.hold_probability = 1- self.buy_probability - self.sell_probability
        else:
            self.sell_probability = 1 / (1 + math.exp(Ks*(diff - Xs)))
            self.buy_probability = 1 / (1 + math.exp(-Kb*(diff - Xb)))
            self.hold_probability = 1 - self.buy_probability - self.sell_probability



    def evaluate(self,market,iv):
        if type == "d":
            self.eval = random.normal(loc=market.average_price,scale=2)
        else:
            self.eval = random.normal(loc=iv,scale=2)


    def set_to_selling(self,market,price,my_shares):
        ids = []
        for mine in my_shares:
            ids.append(mine[0])

        if not self.my_shares:
            print("Investor doesnt own any stocks")
        else:
            for stock in market.stocks:
                if stock.id in ids:
                    stock.selling = True
                    stock.current_sell = price
                    print(self.name,"set a stock to selling with price",stock.current_sell)
                    break

    def set_to_hold(self,market,my_shares):
        ids = []
        for mine in my_shares:
            ids.append(mine[0])
        if not self.my_shares:
            print(self.name,"doesnt own any stocks")
        else:
            for stock in market.stocks:
                if stock.id in ids:
                    stock.selling = False

    def set_buying_price(self,market):
        return market.average_price

    def update_my_shares(self,market):
        list_stock= market.stocks
        for stock in list_stock:
            if stock.owner == self.name:
                self.my_shares.append([stock.id,stock.last_buy])








