print("Введите числа с первого листка: ")
first_list = set()
second_list = set()
for i in range(3):
    num = int(input())
    first_list.add(num)
print("")
print("Введите числа со второго листка: ")
for i in range(4):
    num2 = int(input())
    second_list.add(num2)
intersection_list = first_list.intersection(second_list)
print()
if len(intersection_list) == 0:
    print("EMPTY")
else:
    for i in intersection_list:
        print(i)