num = input("Введите выражние: ").split()
i = 0
while len(num) != 1:
    if num[i] == "-":
        num[i-2] = int(num[i-2]) - int(num[i-1])
        num.remove(num[i])
        num.remove(num[i-1])
        i = 0
    elif num[i] == "+":
        num[i-2] = int(num[i-2]) + int(num[i-1])
        num.remove(num[i])
        num.remove(num[i-1])
        i = 0
    elif num[i] == "*":
        num[i-2] = int(num[i-2]) * int(num[i-1])
        num.remove(num[i])
        num.remove(num[i-1])
        i = 0
    elif num[i] == "/":
        num[i-2] = int(num[i-2]) / int(num[i-1])
        num.remove(num[i])
        num.remove(num[i-1])
        i = 0
    i += 1
print(num[0])