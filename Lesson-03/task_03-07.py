try_ = 0
answer = ""
range = 1000
while answer != "=" or try_ < 10:
    num = range/2
    print(num)
    answer = input()
    if answer == ">":
        num = (range + num)/2
        print(num)
        answer = input()
    elif answer == "<":
        num = (1+num)/2
        print(num)
        answer = input()
    try_ += 1
        