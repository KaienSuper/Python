def average(array):
    if len(array) == 0:
        return 0
    else:
        return sum(array)/len(array)
print(average([1, 2, 3, 4, 5]))