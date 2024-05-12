from Investor import Investor
intrinsic_value = 20
inv1 = Investor(0.1,20)

current_perception=inv1.evaluate(intrinsic_value)
buy_or_sell=inv1.buy_or_sell(current_perception,intrinsic_value)
last = inv1.def_buysellprice(24,buy_or_sell)
print(current_perception,buy_or_sell,last)