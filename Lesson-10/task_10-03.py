texts_list = []
for _ in range(int(input("Count text: "))):
    texts_list.append(input("Text: "))

for i in range(len(texts_list)-1):
    if texts_list[i+1] > texts_list[i]:
        texts_list[i+1], texts_list[i] = texts_list[i], texts_list[i+1]
for elem in texts_list:
    print(elem)