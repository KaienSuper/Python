chars = {"А":"A", "Б":"B","В":"V","Г":"G","Д":"D","Е":"E","Ё":"E","Ж":"ZH",
         "З":"Z","И":"I","Й":"I", "К":"K", "Л":"L", "М":"M", "Н":"N", "О":"O",
         "П":"P","Р":"R","С":"S","Т":"T","У":'U',"Ф":"F","Х":"KH","Ц":"TC",
         "Ч":"CH","Ш":"SH","Щ":"SHCH", "Ы":"Y","Э":"E","Ю":"IU","Я":"IA"}
text = input("Text: ").upper().split()
new_text = []
for word in text:
    for char in word:
        if char in chars:
            word = word.replace(char, chars[char])
        else:
            continue
    new_text.append(word)
new_text = " ".join(new_text)
print(new_text)