print("--Проверка паролей--")

answer = ""
while answer != "OK":
    password1 = input("Пароль: ")
    password2 = input("Подтвердите пароль: ")
    if len(password1) < 8:
        print("Короткий!")
    elif "123" in password1:
        print("Простой!")
    elif password1 != password2:
        print("Не совпадают")
    else:
        answer = "OK"
        print(answer)

