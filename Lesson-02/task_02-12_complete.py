words = input("Введите любую фразу: ")
kop = 40*len(words)
rub = kop // 100
print(f"Стоимость: {rub} р. {kop%100} коп.") 