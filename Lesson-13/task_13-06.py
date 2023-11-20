text = input("Text: ").split()
words_dict = {}
count = ""
for i in text:
    if i not in words_dict:
        words_dict[i] = 1
        count += str(words_dict[i])
        count += " "
    else:
        words_dict[i] += 1
        count += str(words_dict[i])
        count += " "
print(count)