# Write a program that keeps the information about students and their grades.
# On the first line, you will receive an integer number representing the next pair of rows. On the next lines, you will be receiving each student's name and their grade.
# Keep track of all grades for each student and keep only the students with an average grade higher than or equal to 4.50.
# Print the final dictionary with students and their average grade in the following format:
# "{name} -> {averageGrade}"
# Format the average grade to the 2nd decimal place.


n = int(input())
students = {}

for _ in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []
    students[student_name].append(grade)

filtered_students = {
    name: sum(grades) / len(grades)
    for name, grades in students.items()
    if sum(grades) / len(grades) >= 4.50
}

for student, average in filtered_students.items():
    print(f"{student} -> {average:.2f}")
