text = input("Text: ").upper().split()
text2 = ""
for i in range(len(text)):
    char_list = [i2 for i2 in text[i]]
    text2 += "-".join(char_list) + " "
print(text2)