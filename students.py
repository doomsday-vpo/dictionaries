# finish the task using dictionaries:
# You will be receiving names of students, their ID, and a course of programming they have taken in the format "{name}:{ID}:{course}".
# On the last line, you will receive the name of a course in snake case lowercase letters.
# You should print only the information of the students who have taken the corresponding course in the format: "{name} - {ID}" on separate lines.
# Note: each student's ID will always be unique


students_data = {}

while True:
    data = input()
    if ":" not in data:
        course_to_search = data.replace("_", " ")
        break

    name, ID, course = data.split(":")
    if course not in students_data:
        students_data[course] = []
    students_data[course].append({"name": name, "ID": ID})

if course_to_search in students_data:
    for student in students_data[course_to_search]:
        print(f"{student['name']} - {student['ID']}")
