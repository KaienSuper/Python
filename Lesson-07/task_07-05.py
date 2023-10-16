word = input("City: ")
citys = [word]
point = True
while point == True:
    citys.append(input("City: "))
    if (citys[-2])[-1] == (citys[-1])[0]:
        continue
    else:
        point = False
        print(citys[-1])