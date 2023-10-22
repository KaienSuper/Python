phrase_count = int(input("Enter a count of phrase: "))
row = []
symb = []
for i in range(phrase_count):
    phrase = input("Phrase: ")
    for id in range(len(phrase)):
        if phrase[id] == "к":
            if len(phrase) > id+2:
                if phrase[id+1] == "о" and phrase[id+2] == "т":
                    row.append(i+1)
                    symb.append(id+1)
for i in range(len(row)):
    print(row[i], symb[i])