code_list = [input() for _ in range(int(input("#")))]
for i in range(len(code_list)):
    if "#" in code_list[i]:
        code_list[i] = code_list[i].split("#")[:1]
for i in code_list:
    print(i)