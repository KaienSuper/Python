text_list = []
for _ in range(int(input("Count text: "))):
    text_list.append(input("Text: "))

for i in range(len(text_list)-1):
    for j in range(len(text_list)-1-i):
        if text_list[j] > text_list[j+1]:
            text_list[j], text_list[j+1] = text_list[j+1], text_list[j]
for elem in text_list:
    print(elem)