item_dict = {}
count = 0
def add_item(item, price):
    item_dict[item] = price

def print_receipt():
    end_value = 0
    global count
    count += 1
    print(f"Чек {count}. Всего предметов: {len(item_dict)}")
    item_dict_keys = item_dict.keys()
    for i in item_dict_keys:
        print(f"{i} - {item_dict[i]}")
        end_value += item_dict[i]
    print("Итого:", end_value)
    print("---")
    print()
    item_dict.clear()

def main():
    add_item('Блокнот', 100)
    print_receipt()

    add_item('Ручка', 70)
    print_receipt()
    print_receipt()

    add_item('Булочка', 15)
    add_item('Булочка', 15)
    add_item('Чай', 5)
    print_receipt()

main()