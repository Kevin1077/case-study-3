import result_system as result

students = {
    "S101": {"name": "Anu", "marks": {"Python": 88, "Maths": 76, "Stats": 92}},
    "S102": {"name": "Binu", "marks": {"Python": 45, "Maths": 38, "Stats": 52}},
    "S103": {"name": "Cathy", "marks": {"Python": 95, "Maths": 91, "Stats": 89}},
    "S104": {"name": "Dev", "marks": {"Python": 60, "Maths": 72, "Stats": 55}},
    "S105": {"name": "Esha", "marks": {"Python": 72, "Maths": 65, "Stats": 80}},
}


# TASK 1
print("Task 1: One student")

print(result.student_summary(students["S101"]))

print(result.check_result(students["S102"]["marks"]))
print(result.check_result(students["S102"]["marks"], pass_mark=35))
print(result.check_result(students["S102"]["marks"], 35))


# TASK 2
print("\nTask 2: Report")

result.print_report(students)


# TASK 3
print("\nTask 3: Update marks")

print(result.update_marks(students, "S102", Maths=55))

print(result.update_marks(students, "S999", Maths=55))

corrections = {"Python": 50, "Stats": 58}

print(result.update_marks(students, "S102", **corrections))

print(result.student_summary(students["S102"]))


# TASK 4
print("\nTask 4: Add student")

print(result.add_student(students,"S106","Farhan",Python=70,Maths=35,Stats=74))

print(result.add_student(students,"S101","Zara", Python=80, Maths=90, Stats=85))

print(students["S106"])


# TASK 5
print("\nTask 5: Remove student")

print(result.remove_student(students, "S104"))

print(result.remove_student(students, "S104"))

print(len(students))


# TASK 6
print("\nTask 6: Final report and statistics")

result.print_report(students)

stats = result.class_statistics(students)

print("Topper:", stats["topper"])

print("Pass percentage:", stats["pass_percentage"])

print("Subject averages:", stats["subject_averages"])

stats = result.class_statistics(students, "Python", "Stats")

print("Python and Stats only:", stats["subject_averages"])