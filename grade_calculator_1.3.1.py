student_name = input("Write your name: ")
grades = []

for i in range(1, 6):
    while True:
        grade = float(input(f"Write grade {i}: "))
        if 0 >= grade <= 5:
            break
        
        print("Invalid Grade")

    grades.append(grade)

grade_average = sum(grades) / len(grades)
max_grade = max(grades)
min_grade = min(grades)

print(f"\n{student_name}, your grade average is: {round(grade_average, 2)}")

if grade_average < 3.5:
    print("Status: Failed")
else:
    print("Status: Passed")

print(f"Your highest grade was: {max_grade}")
print(f"Your lowest grade was: {min_grade}")
