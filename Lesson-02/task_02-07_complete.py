num = float(input("Введите дробное число: "))
if abs(num) < 0.000001 or num == 0:
    print(1000000)
else:
    print(num**(-1))