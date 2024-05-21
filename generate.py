from faker import Faker
from Investor import Investor
from Stock import Stock
import random
from datetime import datetime



def generate_inv_list(n_inv):
    list = []
    faker = Faker()
    names = [faker.unique.first_name() for _ in range(n_inv)]
    assert len(set(names)) == len(names)

    for i in range(0,n_inv):
        list.append(Investor(name=names[i],type = "s"))
    return list

def generate_stock_list(n_shares):
    list = []
    for i in range(0, n_shares):
        list.append(Stock(owner="IPO Company", last_buy=random.randint(5, 10), selling=True,
                          current_sell=random.randint(6, 11), last_traded_at=0))
    return list
