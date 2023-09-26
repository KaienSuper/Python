count_str = int(input("Введите кол-во строк: "))
for i in range(count_str):
    str = input()
    if "кот" in str or "Кот" in str:
        print("МЯУ")
        break
    else:
        answer = False
if answer == False:
    print("НЕТ")