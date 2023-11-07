text = input("Text: ").lower()
print(max(sorted(list(text.replace(" ", ""))), key=text.count))