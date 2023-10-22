text = input("Enter a text: ")
count_o = 0
count_o_arr = [count_o]
for i in range(len(text)):
    if text[i] == "о":
        count_o += 1
        if count_o > count_o_arr[0]:
            count_o_arr[0] = count_o
    else:
        count_o = 0
print(count_o_arr[0])