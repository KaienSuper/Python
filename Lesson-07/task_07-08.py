num = int(input("Num: "))
while int(str(num)[0]) != 1:
    num *= int(str(num)[0])
print(num)