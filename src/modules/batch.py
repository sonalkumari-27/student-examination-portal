from modules.database import read_db, db_location, db_name
import csv
import pandas as pd
from matplotlib import pyplot as plt
from modules.student import get_particular_student

# Batch
def get_batch():
    return read_db("batch")

def create_batch(
    batch_id,
    batch_name,
    department_name,
    list_of_courses,
    list_of_students,
):
    with open(db_location + db_name["batch"], "a") as db:
        writer = csv.writer(db)
        writer.writerow([
            batch_id,
            batch_name,
            department_name,
            list_of_courses,
            list_of_students,
        ])
        # find the department in department db and add batch to the list_of_batches
        data = read_db("department")
        with open(db_location + db_name["department"], "w") as db:
            writer = csv.writer(db)
            for row in data:
                if row[0] == department_name:
                    if (row[2] == ""):
                        writer.writerow([
                            row[0],
                            row[1],
                            batch_id,
                        ])
                    else:
                        writer.writerow([
                            row[0],
                            row[1],
                            row[2] + ":" + batch_id,
                        ])
                else:
                    writer.writerow(row)

def update_batch(
    batch_id,
    batch_name,
    department_name,
    list_of_courses,
    list_of_students,
):
    data = read_db("batch")
    with open(db_location + db_name["batch"], "w") as db:
        writer = csv.writer(db)
        for row in data:
            if row[0] == batch_id:
                writer.writerow([
                    batch_id,
                    batch_name,
                    department_name,
                    list_of_courses,
                    list_of_students,
                ])
            else:
                writer.writerow(row)


def list_of_students_in_batch(batch_id):
    data = read_db("batch")
    for row in data:
        if row[0] == batch_id:
            return row[4].split(":")

def list_of_courses_in_batch(batch_id):
    data = read_db("batch")
    for row in data:
        if row[0] == batch_id:
            return row[3].split("-")

def view_batch_performance(batch_id):
    students = list_of_students_in_batch(batch_id)
    user_marks = []
    courses = read_db("course")
    for student in students:
        for course in courses:
            marks = course[2].split("-")
            for mark in marks:
                if mark.split(":")[0] == student:
                    user_marks.append({
                        "course_name": course[1],
                        "marks": mark.split(":")[1],
                    })
        total_marks = 0

        for user_mark in user_marks:
            total_marks += int(user_mark["marks"])
        percent = 0
        if user_marks.__len__() > 0:
            percent = total_marks/user_marks.__len__()
        student = get_particular_student(student)
        if student is not None:
            print(student[2], student[0], student[1], student[3], percent)

# Pie Chart of Percentage of all students in a batch
def get_percent_chart():
    data = read_db("batch")
    students = []
    student_percent_data = []
    for row in data:
        students.append(row[4].split(":"))

    students = students[1]
    user_marks = []
    courses = read_db("course")
    for student in students:
        for course in courses:
            marks = course[2].split("-")
            for mark in marks:
                if mark.split(":")[0] == student:
                    user_marks.append({
                        "course_name": course[1],
                        "marks": mark.split(":")[1],
                    })
        total_marks = 0

        for user_mark in user_marks:
            total_marks += int(user_mark["marks"])

        percent = total_marks/user_marks.__len__()
        student = get_particular_student(student)
        student_percent_data.append({
            "student_name": student[0],
            "student_percent": percent,
        })
        print(student[2], student[0], student[1], student[3], percent)

    student_percent_data = pd.DataFrame(student_percent_data)
    student_percent_data.plot(kind="pie", y="student_percent", labels=student_percent_data["student_name"])
    plt.show()


def view_batch_statistics(batch_id):
    students = list_of_students_in_batch(batch_id)
    user_marks = []
    average_percent = 0
    total_data = []
    courses = read_db("course")
    for student in students:
        for course in courses:
            marks = course[2].split("-")
            for mark in marks:
                if mark.split(":")[0] == student:
                    user_marks.append({
                        "course_name": course[1],
                        "marks": mark.split(":")[1],
                    })
        total_marks = 0

        for user_mark in user_marks:
            total_marks += int(user_mark["marks"])
        percent = 0
        if user_marks.__len__() > 0:
            percent = total_marks/user_marks.__len__()
        student = get_particular_student(student)
        if student is not None:
            total_data.append(percent)

    if total_data.__len__() > 0:
        average_percent = sum(total_data)/total_data.__len__()

    return {
        "average_percent": average_percent,
        "branch": batch_id,
    }