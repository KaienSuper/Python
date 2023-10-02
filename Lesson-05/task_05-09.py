count_str = int(input("Введите кол-во строк: "))
count_cat = 0
for i in range(count_str):
    phrase = input()
    if "Кот" in phrase or "кот" in phrase:
        count_cat += 1
    elif "пес" in phrase or "Пес" in phrase:
        if count_cat == 0:
            continue
        else:
            count_cat -= 1
if count_cat != 0:
    print("МЯУ")
else:
    print("НЕТ")