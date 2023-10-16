num = int(input("Num: "))
word = input("Phrase: ")
for i in range(len(word)):
    print(chr(ord(word[i])+num), end='')