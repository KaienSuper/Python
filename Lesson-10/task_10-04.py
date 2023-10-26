text_list = []
for _ in range(int(input("Enter a count of text: "))):
    text_list.append(input("Text: "))

for i in range(len(text_list)-1):
    for j in range(len(text_list)-1-i):
        if len(text_list[j]) > len(text_list[j+1]):
            text_list[j], text_list[j+1] = text_list[j+1], text_list[j]
        elif len(text_list[j]) == len(text_list[j+1]):
            if text_list[j] > text_list[j+1]:
                text_list[j], text_list[j+1] = text_list[j+1], text_list[j]

for elem in text_list:
    print(elem)