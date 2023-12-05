arr = [1, 2, 3, 4, 5]
def mirror(arr):
    arr_2 = [i for i in arr]
    for i in range(1, len(arr)+1):
        arr_2.append(arr[-i])
    return arr_2
print(mirror(arr))
