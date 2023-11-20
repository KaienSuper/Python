def print_average(array):
    if len(array) == 0:
        print("0")
    else:
        print(sum(array)/len(array))
print_average([])
print_average([79])
print_average([1, 2, 3])