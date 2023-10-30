text = input("Text: ").split(" ")
print("[", end="")
for i in range(len(text)):
    if text[i] == text[-1]:
        print(f'"{text[i]}"', end="")
    else:
        print(f'"{text[i]}"', end=", ")
print("]")