name = input("Enter a login: ")
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for i in name:
    if ord(i) >= 97 and ord(i) <= 122:
        point = True
    elif ord(i) >= 1072 and ord(i) <= 1103:
        point = True
    elif i == "_":
        point = True
    elif i in nums:
        point = True
    else:
        point = False
        print("Неверный символ:", i)
        break
if point == True:
    print("OK")