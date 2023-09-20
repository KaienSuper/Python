print("Введите 6 чисел")
res = 1
for i in range(6):
    num = int(input())
    if num !=0:
        res *=num
print(res)