arr = ["a", "c", "d", "b"]
arr_2 = ["a", "c", "d", "b"]

arr.sort() #Метод sort сортирует сам список
arr_3 = sorted(arr_2) #Функция sorted создает новый список для отсортированных значений

print(arr_3)
print(arr_2)
print("---")
print(arr)