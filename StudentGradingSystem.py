def calculate_grade(marks):
    if marks >= 90 :
        return 'A+'
    elif marks >= 80:
        return 'A'
    elif marks >=70:
        return 'B'
    elif marks >=60:
        return 'C'
    else:
        return 'F'
print('Welcome to student grading system.')

students = []

total_students =  int(input('Enter number of students : '))

for i in range(total_students):
    print(f'\nEnter data for student {i+1}')
    name = input('Name : ')
    marks = int(input('Marks: '))
    Student={
    'Name': name,
    'Marks' : marks,
    'Grade' : calculate_grade(marks)
    }

    students.append(Student)

print('\n ---- Students Results ----')

index=0
while index < len(students):
    Student = students[index]
    print(f"Name : {Student['Name']}, Marks : {Student['Marks']}, Grade : {Student['Grade']}")
    index+=1

unique_grade= {}
unique_grade = set(unique_grade)

for s in students:
    unique_grade.add(s['Grade'])

print('\nUnique Grades in class : ', unique_grade)