students = []
student_info = []
for _ in range(int(input("Enter a count of students: "))):
    name = input("Last Name: ")
    grade = int(input("Grade: "))
    student = (name, grade)
    students.append(student)
    if grade >= 4:
        student_info.append(student)
print()
for i in range(len(students)):
    for b in students[i]:
        print(b, end=" ")
    print()
print()
for i in range(len(student_info)):
    for b in student_info[i]:
        print(b, end=" ")
    print()