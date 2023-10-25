count_item = int(input("Enter a count of items: "))
full_price = int(input("Enter a fuul price: "))
prices_list = []
count_price_list = []
full_price_item_list = []
full_price_real = 0
false_price_list = []

for _ in range(count_item):
    price = int(input("Price: "))
    count_price = int(input("Count item: "))
    full_price_item = int(input("Full price: "))
    prices_list.append(price)
    count_price_list.append(count_price)
    full_price_item_list.append(full_price_item)
print(count_item, "    ", full_price, sep="")

for i in range(count_item):
    print(prices_list[i], "       *", count_price_list[i], "    =", full_price_item_list[i], sep="")

for i in range(count_item):
    full_price_real += prices_list[i]*count_price_list[i]

print(abs(full_price-full_price_real))

if full_price - full_price_real != 0:
    for i in range(count_item):
        if prices_list[i]*count_price_list[i] != full_price_item_list[i]:
            false_price_list.append(i+1)

for elem in false_price_list:
    print(elem, end=" ")