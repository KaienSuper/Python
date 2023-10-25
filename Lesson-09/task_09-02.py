count_phrase = int(input("Enter a count of phrase: "))
phrase_list = []
for _ in range(count_phrase):
    phrase = input("Phrase: ")
    phrase_list.append(phrase)
search = input("Search: ")
for elem in phrase_list:
    if search in elem:
        print(elem)