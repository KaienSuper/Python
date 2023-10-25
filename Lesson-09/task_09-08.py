count_people = int(input("Enter a count of people: "))
money_list = []
for _ in range(count_people):
    money = int(input("Money: "))
    money_list.append(money)
for i in money_list:
    print(i)
print()
for i in money_list:
    print(i*3)