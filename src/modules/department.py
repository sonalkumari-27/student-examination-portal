from modules.batch import view_batch_performance, view_batch_statistics
from modules.database import read_db, db_location, db_name
import csv
import pandas as pd
from matplotlib import pyplot as plt

def get_department():
    return read_db("department")

def create_department(
    department_id,
    department_name,
    list_of_batches,
):
    with open(db_location + db_name["department"], "a") as db:
        writer = csv.writer(db)
        writer.writerow([
            department_id,
            department_name,
            list_of_batches,
        ])

def list_of_batches_in_department(department_id):
    data = read_db("department")
    for row in data:
        if row[0] == department_id:
            return row[2].split(":")

# View average performance of all batches in the department
def view_department_performance(department_id):
    batches = list_of_batches_in_department(department_id)
    for batch in batches:
        view_batch_performance(batch)

# Show department statistics: Line plot – Average percentage of all students for each batch. X axis - Batch Name, Y axis – Average Percentage
def view_department_statistics(department_id):
    batches = list_of_batches_in_department(department_id)
    print(batches)
    all_branch_stat = []
    for batch in batches:
        branch_stat = view_batch_statistics(batch)
        all_branch_stat.append(branch_stat)

    print(all_branch_stat)
    df = pd.DataFrame(all_branch_stat)
    df.plot(kind="line", x="branch", y="average_percent")
    plt.show()




