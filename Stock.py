import uuid


class Stock:
    def __init__(self,owner,last_buy,selling,current_sell,last_traded_at):
        self.id = uuid.uuid1()
        self.owner = owner
        self.last_buy=last_buy
        self.last_traded_at = last_traded_at
        self.selling = selling
        self.current_sell = current_sell

    def trade(self,investor,time_stamp,tickers):
        self.owner = investor.name
        self.last_traded_at = time_stamp
        self.last_buy= self.current_sell
        tickers.append(self.last_buy)
        return tickers






