dict = {}
mothers_words = []
for _ in range(int(input("Count words: "))):
    word = input("Word: ")
    description = input("Description: ")
    dict[word] = description
for _ in range(int(input("Count mothers words: "))):
    word_m = input("Word: ")
    mothers_words.append(word_m)
for i in mothers_words:
    if i in dict:
        print(dict[i])
    else:
        print("Not in the dict")