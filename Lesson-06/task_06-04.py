count_en_student = int(input("Кол-во учеников, изучающих английский: "))
student_list = set()
count_ge_student = int(input("Кол-во учеников, изучающих немецкий: "))
count_student = 0
for i in range(count_en_student+count_ge_student):
    student = input()
    if student in student_list:
        count_student += 1
    student_list.add(student)
if len(student_list)-count_student == 0:
    print("NO")
else:
    print(len(student_list)-count_student)