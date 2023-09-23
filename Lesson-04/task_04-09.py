height = int(input("Введите высоту пирамиды: "))
for i in range(height):
    print(" "*(height-i),"*"+"**"*i)