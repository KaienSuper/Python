print("Введите 2 числа")
num_a = int(input("a: "))
num_b = int(input("b: "))
for i in range(num_a, num_b+1):
    if i % 3 == 0:
        if i % 5 == 0:
            print("FizzBuzz")
            break
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

