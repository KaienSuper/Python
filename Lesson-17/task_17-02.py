daily_food = [0, 150, 150]
def count_food(days):
    res = 0
    for i in days:
        res += daily_food[i-1]
    return res

print(count_food([1]))
print(count_food([2, 3]))