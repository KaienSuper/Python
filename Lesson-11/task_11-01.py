text = input("Text: ")
text_list = text.split()
new_text_list = [text_list[i] for i in range(2, len(text_list), 3)]
print(" ".join(new_text_list))