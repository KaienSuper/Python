mans_1 = set()
mans_2 = set()
count_mans = 0
for _ in range(int(input("Enter a count of mans: "))):
    man_surname = input("Surname: ")
    if man_surname not in mans_1:
        mans_1.add(man_surname)
        mans_2.add(man_surname)
    elif man_surname in mans_2:
        count_mans += 2
        mans_2.remove(man_surname)
    else:
        count_mans += 1
print(count_mans)

