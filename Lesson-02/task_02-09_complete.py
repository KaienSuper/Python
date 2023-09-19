print("Введите рост мальчиков")
height_Borya = input("Рост Бори: ")
height_Vova = input("Рост Вовы: ")
height_Dima = input("Рост Димы: ")

if height_Borya > height_Vova:
    if height_Borya > height_Dima:
        print("1. Боря", height_Borya)
        if height_Vova > height_Dima:
            print("2. Вова", height_Vova)
            print("3. Дима", height_Dima)
        else:
            print("2. Дима", height_Dima)
            print("3. Вова", height_Vova)
    else:
        print("1. Дима", height_Dima)
        print("2. Боря", height_Borya)
        print("3. Вова", height_Vova)
else:
    if height_Vova > height_Dima:
        print("1. Вова", height_Vova)
        if height_Dima > height_Borya:
            print("2. Дима", height_Dima)
            print("3. Боря", height_Borya)
        else:
            print('2. Боря', height_Borya)
            print("3. Дима", height_Dima)
    else:
        print("1. Дима", height_Dima)
        print("2. Вова", height_Vova)
        print("3. Боря", height_Borya)