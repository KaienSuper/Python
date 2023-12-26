def partial_sums(lst):
    result = [0]
    for i in range(len(lst)):
        result.append(result[-1]+lst[i])
    return result
print(partial_sums([1, 2, 5, 6]))