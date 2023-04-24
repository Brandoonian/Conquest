import statistics as stat
buy_prices = []
sell_prices = []

buy_1 = 1.03
buy_2 = 1.19
buy_3 = 0.9877
buy_4 = 0.79

sell_1 = 0.95
sell_2 = 0.89
sell_3 = 0.45
sell_4 = 0.34

def add_to_buy_prices(buy, amount):
    while amount != 0:
        buy_prices.append(buy)
        amount -= 1

def add_to_sell_prices(sell, amount):
    while amount != 0:
        sell_prices.append(sell)
        amount -= 1

add_to_buy_prices(buy_1, 1000)
add_to_buy_prices(buy_2, 1500)
add_to_buy_prices(buy_3, 2096)
add_to_buy_prices(buy_4, 4000)

add_to_sell_prices(sell_1, 1000)
add_to_sell_prices(sell_2, 1500)
add_to_sell_prices(sell_3, 2096)
add_to_sell_prices(sell_4, 4000)

average_buy = stat.mean(buy_prices)
average_sell = stat.mean(sell_prices)
print(len(sell_prices))


print(f"Average cost basis is {average_buy}")
print(f"Average sell price is {average_sell}")