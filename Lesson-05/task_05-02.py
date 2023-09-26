count = int(input("Введите кол-во строк: "))
for i in range(count):
    str = input()
    if "кот" or "Кот" in str:
        answer = True
if answer == True:
    print("МЯУ")
else:
    print("НЕТ")
