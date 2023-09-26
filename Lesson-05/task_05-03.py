strs = input("Введите строки: ")
count = 0
while strs != "СТОП":
    if "кот" or "Кот" in strs:
        answer = True
        res = count
    count +=1
    strs = input()
if answer == True:
    print(res)
else:
    print("-1")
