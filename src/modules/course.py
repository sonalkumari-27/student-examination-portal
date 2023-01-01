from modules.database import read_db, db_location, db_name
import csv
import pandas as pd
from matplotlib import pyplot as plt

from modules.student import get_particular_student

def get_course():
    return read_db("course")

def create_course(
    course_id,
    course_name,
    marks_obtained,
):
    with open(db_location + db_name["course"], "a") as db:
        writer = csv.writer(db)
        writer.writerow([
            course_id,
            course_name,
            marks_obtained,
        ])

def update_course(
    course_id,
    course_name,
    marks_obtained,
):
    data = read_db("course")
    with open(db_location + db_name["course"], "w") as db:
        writer = csv.writer(db)
        for row in data:
            if row[0] == course_id:
                writer.writerow([
                    course_id,
                    course_name,
                    marks_obtained,
                ])
            else:
                writer.writerow(row)

# View performance of all students in the course. Show class roll, student name and marks obtained for specific for all students
def view_course_performance(course_id):
    data = read_db("course")
    for row in data:
        if row[0] == course_id:
            students = row[2].split("-")
            for student in students:
                student_data = student.split(":")
                student_id = student_data[0]
                marks = student_data[1]
                student = get_particular_student(student_id)
                print(student[2], student[0], student[1], marks)


# Histogram showing number of students in each grade.X axis - Grades, Y axis- Number of students
def view_course_statistics(course_id):
    data = read_db("course")
    for row in data:
        if row[0] == course_id:
            students = row[2].split("-")
            marks = []
            for student in students:
                student_data = student.split(":")
                marks.append(int(student_data[1]))
            df = pd.DataFrame(marks, columns=["Marks"])
            df["Grade"] = pd.cut(df["Marks"], bins=[0, 40, 60, 80, 100], labels=["D", "C", "B", "A"])
            df["Grade"].value_counts().plot(kind="bar")
            plt.show()

