nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
def who_are_you_and_hello():
    point = False
    name = input("Your name: ")
    while point == False:
        name = input("Your name: ")
        name_2 = name.split()
        if name[0] == name[0].upper():
            for n in nums:
                if n not in name:
                    if len(name_2) == 1:
                        if name[1:] == name[1:].lower():
                            point = True
    if point == True:
        print(f"Hello, {name}")
who_are_you_and_hello()