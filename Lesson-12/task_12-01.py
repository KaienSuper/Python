word_list = [input("Word: ") for _ in range(int(input("Count: ")))]
for i in range(len(word_list)):
    if "кот" in word_list[i]:
        word = [i2 for i2 in word_list[i]]
        print(i+1, word.index('к')+1)
    word.clear()
    
    