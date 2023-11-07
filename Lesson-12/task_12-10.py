text = input("Text: ").lower().split()
count = 0
for i in text:
    for i2 in i:
        count += 1
print(count)