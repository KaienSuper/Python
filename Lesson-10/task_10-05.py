soldiers_list = []
soldiers_remove_list = []
for _ in range(int(input("Enter a count of soldiers: "))):
    soldiers_list.append(input("Soldiers name: "))
step = int(input("Enter the step: "))
count_step = int(input("Enter the number of repetitions: "))
for _ in range(count_step):
    for i in range(step-1, len(soldiers_list), step):
        soldiers_remove_list.append(soldiers_list[i])
    for i in soldiers_remove_list:
        soldiers_list.remove(i)
    soldiers_remove_list.clear()
for elem in soldiers_list:
    print(elem)