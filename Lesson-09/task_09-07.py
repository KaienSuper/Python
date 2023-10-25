count_day = int(input("Enter a count of days: "))
soup_list = ["щи", "борщ", "щавелевый суп", "овсяной суп", "суп по-чабански"]
for i in range(count_day):
    if i >= len(soup_list):
        i = i -len(soup_list)
        print(soup_list[i])
    else:
        print(soup_list[i])