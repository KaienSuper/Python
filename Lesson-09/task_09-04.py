count_phrase = int(input("Enter a count of phrase: "))
phrase_list = []
num_phrase_list = []
for _ in range(count_phrase):
    phrase = input("Phrase: ")
    phrase_list.append(phrase)
count_phrase_in_text = int(input("Enter a count of phrase for text: "))
for _ in range(count_phrase_in_text):
    num_phrase = int(input("Enter a number of phrase for text: "))
    num_phrase_list.append(num_phrase)
for i in num_phrase_list:
    print(phrase_list[i-1])