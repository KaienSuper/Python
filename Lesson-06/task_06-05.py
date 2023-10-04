count_en_student = int(input("Кол-во студентов, изучающих английский: "))
count_ge_student = int(input("Кол-во студентов, изучающих немецкий: "))
count_fr_student = int(input("Кол-во студентов, изучающих французский: "))
student_list = set()
new_student_list = set()
count_student = 0
for i in range(count_en_student+count_ge_student+count_fr_student):
    student = input()
    if student in student_list:
        if student in new_student_list:
            count_student -= 1
        else:
            new_student_list.add(student)
            count_student += 1
    student_list.add(student)
if count_student == 0:
    print("NO")
else:
    print(count_student)

