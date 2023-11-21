def take_large_banknotes(banknotes):
    money_list = [m for m in banknotes if m > 10]
    return money_list
print(take_large_banknotes([1, 5, 500, 0.5, 2, 0.1, 10, 100, 100, 1000, 50]))