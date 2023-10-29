text = input("Num: ").split(" ")
print([int(i) ** 2 for i in text if int(i) % 2 == 1 and (int(i) ** 2) % 10 != 9])