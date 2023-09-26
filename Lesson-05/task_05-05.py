print("Введите строки: ")
str = input()
count = 1
while str != "СТОП":
    if "кот" in str or "Кот" in str:
        print(count)
        break
    else: 
        answer = False
    str = input()
    count += 1
if answer == False:
    print("-1")