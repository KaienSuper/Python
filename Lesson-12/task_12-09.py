char = input("Char: ").lower()
text = input("Text: ").lower()
text_list = text.split()
res = [i for i in text_list if char in i]
for i in res:
    print(i)