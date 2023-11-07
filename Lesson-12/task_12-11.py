nums_list = [input("Num: ") for _ in range(int(input("Count round: ")))]
new_list = []
point = True
for i in nums_list:
    num = i.split()
    b = len(num) - 1 
    if len(num) == 1:
        point = True
        print(num[0], end='')
    for i2 in range(len(num)//2):  
        if num[i2] >= num[b]:
            new_list.append(num[i2])
            new_list.append(num[b])
        else:
            point = False
            break
        b -= 1
    if point == True:
        for i in new_list:
            print(i, end=" ")
        print()
    else:
        print("НЕТ")
    new_list.clear()