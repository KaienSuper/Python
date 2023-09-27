count_command = int(input("Введите кол-во команд: "))
war = "Евразия"
world = "Остазия"
duo = True
for i in range(count_command):
    command = input()
    if command == "С кем война?":
        print(war)
    elif command == "С кем мир?":
        print(world)
    elif command == "Меняем":
        duo = not duo
        if duo == False:
            war = "Остазия"
            world = "Евразия"
        else:
            war = "Евразия"
            world = "Остазия"