num = int(input("Введите число: "))
count=0
for i in range(1, 1000):
    if num%i == 0:
        print(i, end=" ")
        count += 1
if count == 2:
    print("\nПРОСТОЕ")
else:
    print("\nНЕТ")