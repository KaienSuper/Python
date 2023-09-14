login = input("Введите логин: ")
email = input("Введите почту: ")

if "@" not in login:
    if "@" in email:
        print("OK")
    else:
        print("Некорректный адрес")
else:
    print("Некорректный логин")