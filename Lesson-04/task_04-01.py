print("Введите температуру")
temp = float(input())
day = 0
while temp < 22.0:
    day +=1
    temp = float(input())
else:
    print(day//7)