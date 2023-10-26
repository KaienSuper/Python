nums = []
for _ in range(int(input("Count nums: "))):
    nums.append(int(input("Num: ")))
sum_nums = int(input("Summa: "))
for i in range(len(nums)):
    for i2 in range(len(nums)-1):
        if nums[i]*nums[i2+1] == sum_nums:
            print("ДА")
            break
        else:
            print("НЕТ")