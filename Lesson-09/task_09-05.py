count_num = int(input("Enter a count of nums: "))
nums_list = []
for _ in range(count_num):
    num = int(input("Num: "))
    nums_list.append(num)
for i in range(len(nums_list)):
    if nums_list[i] != nums_list[-1]:
        print(nums_list[i]+nums_list[i+1])