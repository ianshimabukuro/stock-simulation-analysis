import numpy as np
import random
class Investor:
    def __init__(self, evaluation_points, age):
        self.evaluation_points = evaluation_points
        self.age = age

    def evaluate(self,intrinsic_value):
        evaluation = np.random.normal(intrinsic_value, self.evaluation_points, 1)
        return evaluation

    def buy_or_sell(self,evaluation,intrinsic_value):
        buy_sell = ''
        if evaluation>intrinsic_value:
            buy_sell = 'sell'
        else:
            buy_sell = 'buy'

        return buy_sell
    def def_buysellprice(self,current_price,buy_sell):
        std = 0.1
        if buy_sell == 'buy':
            current_price_dev = np.random.normal(0, std, 1)
            current_price_dev=-abs(current_price_dev)
        else:
            current_price_dev = np.random.normal(0, std, 1)
            current_price_dev = abs(current_price_dev)
        return buy_sell,float(current_price + current_price_dev)

def init_investor_list(n_investors):
    list = []
    for i in range(0,n_investors):
        list.append(Investor(random.uniform(0,1),20))
    return list


