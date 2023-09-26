print("Введите числа больше 0")
num = input()
res = 0
sign = 1
while num != "stop":
    res += int(num)*sign
    sign *=(-1)
    num = input()
print(res)