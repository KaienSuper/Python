count_str = int(input("Enter a count of items: "))
items_list = []
for _ in range(count_str):
    item = input("Item: ")
    items_list.append(item)
for elem in items_list:
    print(elem)