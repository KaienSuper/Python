students_birth_dict = {"янв":'','фев':'',"мар":'','апр':'',"май":'','июн':'',
                       "июл":'','авг':'',"сен":'','окт':'',"ноя":'','дек':''}
for _ in range(int(input("Count student: "))):
    name = input("Name: ")
    birthday = input("Birthday: ").split()
    students_birth_dict[birthday[1]] = name
for _ in range(int(input("Count month: "))):
    month = input().lower()
    print(students_birth_dict[month]) 