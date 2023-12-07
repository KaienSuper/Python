def transpose(matrix):
    if len(matrix) == 1:
        return matrix
    elif len(matrix) == 2:
        matrix0_1 = matrix[0][1]
        matrix[0][1] = matrix[1][0]
        matrix[1][0] = matrix0_1
        return matrix

matrix = [[1, 2], [3, 4]]
for i in matrix:
    print(i)
matrix = transpose(matrix)
for i in matrix:
    print(i)