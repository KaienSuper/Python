count_phrase = int(input("Enter a count of phrases: "))
phrase_list = []
search_list = []
for _ in range(count_phrase):
    phrase = input("Phrase: ")
    phrase_list.append(phrase)
count_search = int(input("Enter a count of search: "))
for _ in range(count_search):
    search = input("Search: ")
    search_list.append(search)
for elem in phrase_list:
    for i in range(len(search_list)):
        if search_list[i] in elem:
            point = True
        else:
            point = False
            break
    if point == True:
        print(elem)