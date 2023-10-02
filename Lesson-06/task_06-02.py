count_sity = int(input("Введите кол-во городов: "))
city_list = set()
for i in range(count_sity+1):
    city = input()
    city_list.add(city)
if len(city_list) != count_sity+1:
    print("TRY ANOTHER")
else:
    print("OK")