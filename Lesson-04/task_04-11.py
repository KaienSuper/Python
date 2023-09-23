count_people = int(input("Введите кол-во тестируемых людей: "))
count_iq = 0
for i in range(count_people):
    iq = int(input("iq: "))
    count_iq += iq
    if i == 0:
        print("0")
    elif iq > count_iq/(i+1):
        print(">")
    elif iq < count_iq/(i+1):
        print("<")