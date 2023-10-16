word = input("Word: ")
num = int(input("Num: "))
if num <= len(word) and num != 0:
    print(word[num-1])
else:
    print("ERROR")