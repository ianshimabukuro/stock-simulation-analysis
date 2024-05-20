import numpy as np
import random


class Investor:
    def __init__(self,name,sell_probability,buy_probability,hold_probability,pp,ip):
        self.name = name
        self.sell_probability = sell_probability
        self.buy_probability = buy_probability
        self.hold_probability = hold_probability
        self.pp = pp
        self.ip = ip
        self.my_shares = []

    def update_prob(self,market):
        return 0

    def set_to_selling(self,market,price,my_shares):
        ids = []
        for mine in my_shares:
            ids.append(mine.id)

        if not self.my_shares:
            print("Investor doesnt own any stocks")
        else:
            for stock in market.stocks:
                if stock.id in ids:
                    stock.selling = True
                    stock.current_sell = price

    def set_to_hold(self,market,my_shares):
        ids = []
        for mine in my_shares:
            ids.append(mine.id)
        if not self.my_shares:
            print("Investor doesnt own any stocks")
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
                self.my_shares.append(stock.id)








