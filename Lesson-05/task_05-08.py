print("Введите слова: ")
phrase = input()
count_str = 0
count_cat = 0
first_cat = 0
while phrase != "СТОП":
    count_str += 1
    if "кот" in phrase or "Кот" in phrase:
        count_cat += 1
        if count_cat == 1:
            first_cat = count_str
    phrase = input()
print(count_cat, first_cat)