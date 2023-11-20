def ask_password():
    point = False
    for _ in range(3):
        pw = input("Password: ")
        if pw != "password":
            point = False
        else:
            point = True
            break
    if point == True:
        print("Password is correct")
    else:
        print("Password is not correct")
ask_password()