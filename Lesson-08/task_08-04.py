num = int(input("Num: "))
words = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
count = num
for i in range(num):
    for i2 in range(num):
        print(words[i2], count, sep="", end=" ")
    count -= 1
    print()