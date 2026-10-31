def calculate_total(marks):
    return sum(marks.values())


def calculate_average(marks):
    return round(calculate_total(marks) / len(marks), 2)

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75 and average < 90:
        return "B"
    elif average >= 60 and average < 75:
            return "C"
    elif average >= 40 and average < 60:
            return "D"
    else:
         return "F"

def check_result(marks, pass_mark=40):
    for mark in marks.values():
        if mark < pass_mark:
            return "Fail"

    return "Pass"

def student_summary(student):
    student_info = {
        "name" : student["name"],
        "total" : calculate_total(student["marks"]),
        "average" : round(calculate_average(student["marks"]), 2),
        "grade" : get_grade(calculate_average(student["marks"])),
        "result" : check_result(student["marks"])
         
    }
    return student_info

def add_student(data, student_id, name, **marks):
     if student_id in data:
          return False
     else:
          data.update({
          student_id : {"name":name, "marks":marks}
          })
          return True

def update_marks(data, student_id, **changes):
     if student_id not in data:
          return False
     else:
          for key, value in changes.items():
               data[student_id]["marks"][key] = value
          return True

def print_report(data):

    print(f"{'ID':<6}{'Name':<8}{'Total':>6}{'Avg':>8}{'Grade':>7}  Result")
    print("-" * 42)

    result_list = []

    for std_id, values in data.items():

        summary = student_summary(values)
        average = summary["average"]

        result_list.append((average, std_id))

    result_list.sort(reverse=True)

    for average, std_id in result_list:

        summary = student_summary(data[std_id])

        print(
            f"{std_id:<6}"
            f"{summary['name']:<8}"
            f"{summary['total']:>6}"
            f"{summary['average']:>8.2f}"
            f"{summary['grade']:>7}  "
            f"{summary['result']}"
        )

def remove_student(data, student_id):
    if student_id not in data:
        return False

    data.pop(student_id)
    return True

def class_statistics(data, *subjects):

    topper = ""
    highest_average = 0

    pass_count = 0
    subject_totals = {}

    if not subjects:
        subjects = list(next(iter(data.values()))["marks"].keys())

    for student_id, student in data.items():

        summary = student_summary(student)

        if summary["average"] > highest_average:
            highest_average = summary["average"]
            topper = summary["name"]

        if summary["result"] == "Pass":
            pass_count += 1

        for subject in subjects:
            subject_totals.setdefault(subject, 0)
            subject_totals[subject] += student["marks"][subject]

    pass_percentage = round((pass_count / len(data)) * 100, 1)

    subject_averages = {}

    for subject, total in subject_totals.items():
        subject_averages[subject] = round(total / len(data), 1)

    return {
        "topper": topper,
        "pass_percentage": pass_percentage,
        "subject_averages": subject_averages
    }



    

    

    