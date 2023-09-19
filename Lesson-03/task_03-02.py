print("Придумайте пароль")
password = input("Пароль: ")
password2 = input("Подтвердите пароль: ")
if len(password) < 8:
    print("Короткий!")
elif password != password2:
    print("Различаются")
else:
    print("OK")
print("*--END--*")