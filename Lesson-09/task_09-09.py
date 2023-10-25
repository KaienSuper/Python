count_num = int(input("Enter a count of nums: "))
nums_list = []
result = 0
for _ in range(count_num):
    num = int(input("Num: "))
    nums_list.append(num)
start_num = int(input("Enter the initial number: "))-1
end_num = int(input("Enter the final number: "))
nums_list_new = nums_list[start_num:end_num]
for i in nums_list_new:
    result += i
print(result)