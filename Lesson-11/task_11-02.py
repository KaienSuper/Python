count = input("Count: ")
count_list = [int(i) for i in count.split(" ")]
for i in count_list:
    print("*"*i)