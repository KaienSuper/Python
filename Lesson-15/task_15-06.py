def print_document(pages):
    point = True
    for elem in pages:
        if "Секретно" in elem:
            print("Дальнейшие материал засекречены")
            point = False
            break
        else:
            print(elem)
    if point == True:
        print("Напечатано без купюр")

print_document(["Обычная страница", "И еще страница", 
                "Секретно Вот этот вот текст не показывать", "Никому", 
                "Никогда"])
print_document(["Пустой трёп", "который", "никому не интересен"])