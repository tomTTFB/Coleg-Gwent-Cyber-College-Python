students = []
grades = {}
passed_students = set()

num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    name = input(f"Enter the name of student {i + 1}: ")
    score = int(input(f"Enter the score of {name} (0-100): "))

    students.append(name)
    grades[name] = score

    if score >= 50:
        passed_students.add(name)
        print(f"{name} has passed.")
    elif score >= 40:
        print(f"{name} is on probation.")
    else:
        print(f"{name} has failed.")

print(students)
print(grades)
print(passed_students)

while true:
    query = input("Enter a student's name to check if they passed (or 'exit' to quit): ")
    if query.lower() == 'exit':
        break
    elif query in passed_students:
        score = grades[query]
        print(f"{query}'s grade is {score}.")
        if score >= 50:
            print("Status: Passed.")
        elif score >= 40:
            print("Status: Probation.")
        else:
            print("Status: Fail")
    else:
        print(f"Student not found")

