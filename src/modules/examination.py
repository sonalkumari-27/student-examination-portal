from modules.database import read_db, db_location, db_name
import csv

def set_marks(
    student_id,
    course_id,
    marks,
):
    data = read_db("course")
    with open(db_location + db_name["course"], "w") as db:
        writer = csv.writer(db)
        for row in data:
            if row[0] == course_id:
                if(row[2]==""):
                    writer.writerow([
                        row[0],
                        row[1],
                        student_id + ":" + marks,
                    ])
                else:
                    writer.writerow([
                        row[0],
                        row[1],
                        row[2] + "-" + student_id + ":" + marks,
                    ])
            else:
                writer.writerow(row)

def get_marks(student_id, course_id):
    data = read_db("course")
    for row in data:
        if row[0] == course_id:
            students = row[2].split("-")
            for student in students:
                student_data = student.split(":")
                if student_data[0] == student_id:
                    return student_data[1]
    return None

# View performance of all students in the examination

def view_examination_performance(course_id):
    data = read_db("course")
    for row in data:
        if row[0] == course_id:
            students = row[2].split("-")
            for student in students:
                student_data = student.split(":")
                student_id = student_data[0]
                marks = student_data[1]
                student = get_marks(student_id, course_id)
                print(student[2], student[0], student[1], marks)
