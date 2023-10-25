count_phrase = int(input("Enter a count of phrase: "))
phrase_list = []
search_list = []
for _ in range(count_phrase):
    phrase = input("Phrase: ")
    phrase_list.append(phrase)
count_search = int(input("Enter a count of search: "))
for _ in range(count_search):
    search = input("Search: ")
    search_list.append(search)

for elem in search_list:
    for i in phrase_list:
        if elem in i:
            print(i)