num = int(input("Введите число: "))
res = 1
if num > 0:
    for i in range(1, num+1):
        res *=i
    else:
        print(res)
else:
    print("*ERROR")