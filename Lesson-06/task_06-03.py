count_en_student = int(input("Кол-во учеников, изучающих английский: "))
en_student_list = set()
count_ge_student = int(input("Кол-во учеников, изучающих немецкий: "))
ge_student_list = set()
for i in range(count_en_student):
    student = input()
    en_student_list.add(student)
print()
for i in range(count_ge_student):
    student = input()
    ge_student_list.add(student)
symm_diff = len(en_student_list ^ ge_student_list)
if symm_diff == 0:
    print("NO")
else:
    print(symm_diff)