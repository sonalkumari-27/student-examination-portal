from modules.database import read_db, db_location, db_name
import csv
import os

def get_student():
    return read_db("student")

def get_particular_student(student_id):
    data = read_db("student")
    for row in data:
        if row[0] == student_id:
            return row

def create_student(
    student_id,
    student_name,
    student_roll,
    student_batch,
):
    with open(db_location + db_name["student"], "a") as db:
        writer = csv.writer(db)
        writer.writerow([
            student_id,
            student_name,
            student_roll,
            student_batch,
        ])
        # find the batch in batch db and add student to the list_of_students
        data = read_db("batch")
        with open(db_location + db_name["batch"], "w") as db:
            writer = csv.writer(db)
            for row in data:
                if row[0] == student_batch:
                    # check if row[4] is empty then dont add : at start
                    if (row[4] == ""):
                        writer.writerow([
                            row[0],
                            row[1],
                            row[2],
                            row[3],
                            student_id ,
                        ])
                    else:
                        writer.writerow([
                            row[0],
                            row[1],
                            row[2],
                            row[3],
                            row[4] + ":" + student_id ,
                        ])
                else:
                    writer.writerow(row)

def update_student(
    student_id,
    student_name,
    student_roll,
    student_batch,
):
    data = read_db("student")
    with open(db_location + db_name["student"], "w") as db:
        writer = csv.writer(db)
        for row in data:
            if row[0] == student_id:
                writer.writerow([
                    student_id,
                    student_name,
                    student_roll,
                    student_batch,
                ])
            else:
                writer.writerow(row)

def remove_student(student_id):
    data = read_db("student")
    with open(db_location + db_name["student"], "w") as db:
        writer = csv.writer(db)
        for row in data:
            if row[0] != student_id:
                writer.writerow(row)

def generate_report_card(student_id):
    courses = read_db("course")
    user_marks = []

    for course in courses:
        marks = course[2].split("-")
        for mark in marks:
            if mark.split(":")[0] == student_id:
                grade = "F"
                m = mark.split(":")[1]
                if (int(m)) >= 90:
                    grade = "A"
                elif (int(m)) >= 80:
                    grade = "B"
                elif (int(m)) >= 70:
                    grade = "C"
                elif (int(m)) >= 60:
                    grade = "D"
                elif (int(m)) >= 40:
                    grade = "E"
                elif (int(m)) <= 40:
                    grade = "F"

                user_marks.append({
                    "course_name": course[1],
                    "marks": mark.split(":")[1],
                    "grade": grade
                })
    
    # calculate percentage
    total_marks = 0

    for user_mark in user_marks:
        total_marks += int(user_mark["marks"])

    percent = total_marks/user_marks.__len__()

    isPass = percent >= 40 

    if(not os.path.exists("results")):
        os.mkdir("results")

    if(os.path.exists("results/" + student_id + ".txt")):
        os.remove("results/" + student_id + ".txt")

    # Write data to the file.
    with open("results/" + student_id + ".txt", "w") as report:
        report.write("Student ID: " + student_id)
        report.write("\n\nCourse Name\tMarks\tGrade")
        for user_mark in user_marks:
            report.write("\n" + user_mark["course_name"] + " = " + "\t" + user_mark["marks"] + "\t" + user_mark["grade"])

        report.write("\n\n" + "Percentage: " + str(percent))
        report.write("\n" + "Status: " + "Pass" if isPass else "\n" + "Status: " + "Fail")


