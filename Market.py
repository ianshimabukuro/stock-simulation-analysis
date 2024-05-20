class Market:
    def __init__(self,stocks,top):
        self.stocks = stocks
        self.n_shares = len(stocks)
        cumulative = 0
        for  stock in stocks:
            cumulative+=stock.last_buy
        self.average_price = cumulative/self.n_shares
        self.latest_traded_price = top

