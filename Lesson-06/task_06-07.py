student_list = []
for _ in range(int(input("Enter a count of page: "))):
    student_surname_list = set(input("Surname: ") for _ in range(int(input("Enter a count of lesson: "))))
    student_list.append(student_surname_list)
 
students_list_2 = student_list.pop(0)
for student in student_list:
    students_list_2 = students_list_2 & student
print(*students_list_2, sep ='\n')