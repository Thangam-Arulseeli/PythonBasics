### Getting the CSV Data
import csv

with open("EmployeeDetails.csv", "r") as file:

    reader = csv.DictReader(file)

    for employee in reader:
        print(employee["Name"] )
        print(employee["Department"])
        print(employee["Salary"])
        print("-------------------------")
# -------------------------------------------------
#### Process CSV Data
# CSV → Salary Analysis

total_salary = 0
employee_count = 0

with open("EmployeeDetails.csv", "r") as file:

    reader = csv.DictReader(file)

    for employee in reader:

        salary = float(employee["Salary"])

        total_salary += salary
        employee_count += 1

average_salary = total_salary / employee_count

print("Employees:", employee_count)
print("Average Salary:", average_salary)
# ---------------------------------------

### Creating new CSV file with the existing data
employees = [
    [101, "Arun", "Development", 85000],
    [102, "Priya", "Testing", 70000],
    [103, "Karthik", "Development", 95000]
]

with open("Employee_report.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(
        ["ID", "Name", "Department", "Salary"]
    )

    writer.writerows(employees)
# --------------------------------------------


