phrase_arr = []
def parrot(phrase):
    if phrase in phrase_arr:
        print(phrase)
    else:
        phrase_arr.append(phrase)

parrot("Привет!")
parrot("Привет!")
parrot("Как дела?")
