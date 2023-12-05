a = [1, 2, 3]
def from_string_to_list(string, container):
    string = string.split(" ")
    res = container + string
    res_2 = ""
    for i in res:
        res_2 += str(i)
        res_2 += " "
    return res_2
print(from_string_to_list("1 3 99 52", a))