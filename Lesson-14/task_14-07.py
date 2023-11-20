def print_statisticks(array):
    med_num = 0
    if len(array) % 2 != 0:    
        med_num = array[int(len(array)/2) - 1]
    else:
        med_num = (array[int(len(array)/2)] + array[int(len(array)/2) - 1])/2
    print(len(array))
    print(sum(array)/len(array))
    print(min(array))
    print(max(array))
    print(med_num)
print_statisticks([3, 5, 8, 4])