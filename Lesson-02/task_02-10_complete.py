print("Введите два дробных числа и строку")
num1 = float(input("Число 1: "))
num2 = float(input("Число 2: "))
op = input("Строка: ")

if op == "+":
    print(f"{num1} + {num2} =", num1+num2)
elif op == "-":
    print(f"{num1} - {num2} =", num1-num2)
elif op == "*":
    print(f"{num1} * {num2} =", num1*num2)
elif op == "/":
    if num2 == 0:
        print("888888")
        
    print(f"{num1} / {num2} =", num1/num2)
else:
    print("888888")