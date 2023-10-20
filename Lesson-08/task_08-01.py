word = input("Word: ")
word_max = [word]
word_min = [word]
while word != "стоп":
    word = input("Word: ")
    if word == "стоп":
        break
    if len(word) > len(word_max[0]):
        word_max[0] = word
    elif len(word) < len(word_min[0]):
        word_min[0] = word

for elem in word_min[0]:
    if elem in word_max[0]:
        point = True
    else:
        point = False
        break

if point == True:
    print("ДА")
else:
    print("НЕТ")
