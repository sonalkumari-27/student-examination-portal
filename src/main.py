from modules.database import create_db
from modules.batch import create_batch, get_percent_chart, view_batch_performance
from modules.course import create_course, view_course_performance, view_course_statistics
from modules.department import create_department, view_department_performance, view_department_statistics
from modules.examination import set_marks
from modules.student import create_student, remove_student, update_student, generate_report_card
import os
import shutil

# A class with all the functions
class StudentExaminationPortal:
    def __init__(self):
        if(os.path.exists("database")):
            shutil.rmtree("database")
        if(os.path.exists("results")):
            shutil.rmtree("results")
        create_db()

    def create_course(self, course_id, course_name, course_description):
        create_course(course_id, course_name, course_description)

    def create_department(self, department_id, department_name, department_description):
        create_department(department_id, department_name, department_description)

    def create_batch(self, batch_id, batch_name, department_id, course_ids, batch_description):
        create_batch(batch_id, batch_name, department_id, course_ids, batch_description)

    def create_student(self, student_id, student_name, student_roll_no, batch_id):
        create_student(student_id, student_name, student_roll_no, batch_id)

    def update_student(self, student_id, student_name, student_roll_no, batch_id):
        update_student(student_id, student_name, student_roll_no, batch_id)

    def remove_student(self, student_id):
        remove_student(student_id)

    def set_marks(self, student_id, course_id, marks):
        set_marks(student_id, course_id, marks)

    def generate_report_card(self, student_id):
        generate_report_card(student_id)

    def view_course_performance(self, course_id):
        view_course_performance(course_id)

    def view_course_statistics(self, course_id):
        view_course_statistics(course_id)

    def view_batch_performance(self, batch_id):
        view_batch_performance(batch_id)

    def get_percent_chart(self):
        get_percent_chart()

    def view_department_performance(self, department_id):
        view_department_performance(department_id)

    def view_department_statistics(self, department_id):
        view_department_statistics(department_id)

# create a object of the class
obj = StudentExaminationPortal()

# call the functions
obj.create_course("C001", "Python", "")
obj.create_course("C002", "Java" ,"")
obj.create_course("C003", "C++" ,"")
obj.create_course("E001", "AEC" ,"")
obj.create_course("E002", "PDC" ,"")
obj.create_course("E003", "DEC" ,"")

obj.create_department("CSE", "Computer Science Engineering", "")
obj.create_department("EE", "Electrical Engineering", "")
obj.create_department("ECE", "Electronics and Communication Engineering", "")

obj.create_batch("CSE22", "CSE 2022-2026", "CSE", "C001:C002:C003", "")
obj.create_batch("CSE21", "CSE 2021-2025", "CSE", "C001:C002", "")
obj.create_batch("CSE20", "CSE 2020-2024", "CSE", "C001:C002:C003", "")
obj.create_batch("ECE22", "ECE 2022-2026", "ECE", "E001:E002", "")
obj.create_batch("EE22", "EE 2022-2026", "EE", "E002:E003", "")

obj.create_student("CSE2205", "Test 1", "01", "CSE22")
obj.create_student("CSE2206", "Test 2", "01", "CSE22")
obj.create_student("CSE2207", "Test 3", "01", "CSE20")
obj.create_student("CSE2208", "Test 4", "01", "CSE20")
obj.create_student("CSE2209", "Test 5", "01", "CSE20")
obj.create_student("CSE2210", "Test 6", "01", "CSE20")

obj.create_student("CSE2201", "Sonal", "01", "CSE22")
obj.create_student("CSE2202", "Prajakta", "02", "CSE21")
obj.create_student("CSE2203", "Rohan", "03", "CSE21")
obj.create_student("ECE2201", "Anjali Kumari", "04", "ECE22")
obj.create_student("EE2202", "Ankit Kumar", "05", "EE22")
obj.create_student("EE2203", "Rahul Kumar", "06", "EE22")

obj.update_student("CSE2201", "Sonal Kumari", "01", "CSE22")
obj.remove_student("EE2203")

obj.set_marks("CSE2201", "C001", "90")
obj.set_marks("CSE2201", "C002", "80")
obj.set_marks("CSE2201", "C003", "100")

obj.set_marks("CSE2202", "C001", "90")
obj.set_marks("CSE2202", "C002", "70")
obj.set_marks("CSE2202", "C003", "80")

obj.set_marks("CSE2203", "C001", "70")
obj.set_marks("CSE2203", "C002", "80")
obj.set_marks("CSE2203", "C003", "95")

obj.set_marks("CSE2207", "C001", "70")
obj.set_marks("CSE2207", "C002", "83")
obj.set_marks("CSE2207", "C003", "83")
obj.set_marks("CSE2208", "C001", "83")
obj.set_marks("CSE2208", "C002", "86")
obj.set_marks("CSE2208", "C003", "96")
obj.set_marks("CSE2209", "C001", "76")
obj.set_marks("CSE2209", "C002", "80")
obj.set_marks("CSE2209", "C003", "99")
obj.set_marks("CSE2210", "C001", "99")
obj.set_marks("CSE2210", "C002", "99")
obj.set_marks("CSE2210", "C003", "95")

obj.set_marks("CSE2205", "C001", "60")
obj.set_marks("CSE2205", "C002", "90")

obj.set_marks("CSE2206", "C001", "98")
obj.set_marks("CSE2206", "C002", "90")

obj.set_marks("EE2202", "E001", "60")
obj.set_marks("EE2202", "E002", "30")
obj.set_marks("EE2202", "E003", "100")

obj.set_marks("ECE2201", "E001", "20")
obj.set_marks("ECE2201", "E002", "30")


obj.generate_report_card("CSE2201")
obj.generate_report_card("CSE2202")
obj.generate_report_card("CSE2203")
obj.generate_report_card("EE2202")
obj.generate_report_card("ECE2201")

obj.view_course_performance("C001")

obj.view_course_statistics("C001")

obj.view_batch_performance("ECE22")

obj.get_percent_chart()

obj.view_department_performance("CSE")

obj.view_department_statistics("CSE")