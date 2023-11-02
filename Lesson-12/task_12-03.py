nums = input("Nums: ").split()
nums_range = input().split()
res = 0
for i in range(int(nums_range[0]), int(nums_range[1])+1):
    res += int(nums[i])
print(res)