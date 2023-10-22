texts_arr = []
for _ in range(int(input("Enter a count of text: "))):
    text = input("Text: ")
    if text[0] == "%" and text[1] == "%":
        texts_arr.append(text[2:1])
    elif "####" in text:
        continue
    else:
        texts_arr.append(text)
for elem in texts_arr:
    print(elem)