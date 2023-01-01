import csv
import os

db_location = "./database/"

db_name = {
    "batch": "batch.csv",
    "course": "course.csv",
    "student": "student.csv",
    "department": "department.csv",
}


# Create database if not exists
def create_db():
    if not os.path.exists(db_location):
        os.mkdir(db_location)
    for key in db_name:
        if not os.path.exists(db_location + db_name[key]):
            with open(db_location + db_name[key], "w") as db:
                # switch case 
                writer = csv.writer(db)
                if key == "student":
                    writer.writerow(
                        [
                            "student_id",
                            "student_name",
                            "student_roll",
                            "student_batch",
                        ]
                    )
                elif key == "batch":
                    writer.writerow(
                        [
                            "batch_id",
                            "batch_name",
                            "department_name",
                            "list_of_courses",
                            "list_of_students"
                        ]
                    )
                elif key == "course":
                    writer.writerow(
                        [
                            "course_id",
                            "course_name",
                            "marks_obtained", 
                        ]
                    )
                elif key == "department":
                    writer.writerow(
                        [
                            "department_id",
                            "department_name",
                            "list_of_batches",
                        ]
                    )


# Read database
def read_db(db):
    data = []
    with open(db_location + db_name[db], "r") as db:
        reader = csv.reader(db)
        for row in reader:
            data.append(row)
    return data