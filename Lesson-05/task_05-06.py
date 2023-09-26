print("Введите числа: ")
num = int(input())
res = 0
count = 0
while num != 0:
    res += num
    if res <= 10:
        count +=1
    num = int(input())
print(count)