text = input("Text: ").lower()
text_list = [i for i in text]
text_list.sort()
count = 1
count_list = []
for i in range(len(text_list)-1):
    if text_list[i] == text_list[i+1]:
        count += 1
    else:
        count_list.append(count)
        count = 1
print(max(count_list))