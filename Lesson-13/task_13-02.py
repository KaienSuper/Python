telephone_num_dict = {}
for _ in range(int(input("Count telephone number: "))):
    num = input("Number: ")
    name = input("Name: ")
    if name in telephone_num_dict:
        telephone_num_dict[name] = telephone_num_dict[name] + " "+ num
    else:
        telephone_num_dict[name] = num
names_list = [input("Name: ") for _ in range(int(input("Count name: ")))]
for i in names_list:
    if i in telephone_num_dict:
        print(telephone_num_dict[i])
    else:
        print("Нет в телефонной книге")