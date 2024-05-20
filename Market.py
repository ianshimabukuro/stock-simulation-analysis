from datetime import datetime
class Market:
    def __init__(self,stocks,top):
        self.stocks = stocks
        self.n_shares = len(stocks)
        cumulative = 0
        for  stock in stocks:
            cumulative+=stock.last_buy
        self.average_price = cumulative/self.n_shares
        self.latest_traded_price = top

    def update(self,stocks):
        self.stocks = stocks

    def match(self,price):
        for stock in self.stocks:
            if stock.selling == True:
                if price*0.9>stock.current_sell>price*1.1:
                    return stock.id
                    break
        return None


    def trade(self,id,investor):
        for stock in self.stocks:
            if stock.id == id:
                stock.owner = investor.name
                stock.last_traded_at= datetime.now()
                stock.last_buy = stock.current_sell
        print("A trade happened")
        return [stock.last_buy,stock.last_traded_at]



