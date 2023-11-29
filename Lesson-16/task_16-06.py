gl_ru_dict = ["а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"]
def translate(text):
    text_arr = text.split()
    new_text_arr = []
    for i in range(len(text_arr)):
        b = [i2 for i2 in text_arr[i]]
        for i3 in range(len(b)):
            if b[i3].lower() in gl_ru_dict:
                b[i3] = ""
        b = "".join(b)
        new_text_arr.append(b)
    return " ".join(new_text_arr)

translated_text = translate("Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой тренировки - и вы сможете это делать")
print(translated_text)