count_str = int(input("Enter a count of texts: "))
texts_list = []
for _ in range(count_str):
    text = input("Text: ")
    texts_list.append(text)
num_char = int(input("Enter a number of char: "))-1
for i in texts_list:
    print(i[num_char], end="")