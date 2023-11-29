def find_mountain(heightsMap):
    if len(heightsMap) == 1:
        sad = heightsMap[0]
        return 0, sad.index(max(sad))
        
    if len(heightsMap[0]) == 1:
        return heightsMap.index(max(heightsMap)), 0
        
    el_max = heightsMap[0][0]
    for i, row in enumerate(heightsMap):
        for j, elem in enumerate(row):
            if el_max < elem:
                el_max = elem
                col = j
                ind = i
    
    return ind, col

a = [[1, 3, 1], [3, 2, 5], [2, 2, 2]]
print(find_mountain(a))
