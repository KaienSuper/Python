text = input("Введите текст через пробелы: ").split()
len_text_list = [len(i) for i in text]
len_text_list.sort(reverse=True)
print(len_text_list[0])