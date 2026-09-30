# Writing into the file

f = open("data.txt", "w")
f.write("Welcome to Python\n")
f.write("File Handling Concept")
f.close()
print("==================")
# -------------------------------
# "D:\CGVAK\Python\Practicals\PythonBasics\Day3"

# Reading the data from the file
file = open("employee.txt", "r")
data = file.read()
print(data)
file.close()
print("==================")
# ------------------------

#readline() - Reads one line
f = open("data.txt", "r")
print(f.readline())
f.close()
print("==================")
# --------------------------------

# readlines() - Reads all lines into a list
f = open("data.txt", "r")
lines = f.readlines()
print(lines)
f.close()
print("==================")
# -------------------------------

# Appending to a File (a)
f = open("data.txt", "a")
f.write("\nNew Line Added")
f.close()
print("==================")
# Existing content remains unchanged
# ----------------------------------

# Reading the data from the file
file = open("data.txt", "r")
data = file.read()
print(data)
file.close()
print("==================")
# ------------------------------------
'''

File Modes
----------------
Mode	Purpose
r	Read
w	Write / overwrite
a	Append
x	Create new file
r+	Read + write
rb	Read binary
wb	Write binary
'''
# -------------------------------------------
# But this is not the preferred corporate approach because the file may remain open if an exception occurs
# ===================================================


### Using with – Context Manager
# ----------------------------------
'''
The preferred approach:
with open("employees.txt", "r") as file:
    data = file.read()

print(data)

The file is automatically closed after the with block.

Why is this important?

Application
   ↓
Open File
   ↓
Read Data
   ↓
Exception occurs
   ↓
File may remain open

Using with:
Application
   ↓
Open File
   ↓
Read Data
   ↓
Exception occurs
   ↓
Resource automatically released


This same concept is extremely important later with:
•	database connections 
•	database sessions 
•	locks 
•	network resources 
•	transactions 

Real-Life Example - Employee Attendance File  -- Which is in our folder (attendane.txt)
attendance.txt
101,Arun,Present
102,Priya,Present
103,Karthik,Absent
104,Divya,Present
'''
# ----------------------------------

### Open and print the raw data
with open("attendance.txt", "r") as file:

    for line in file:
        print(line.strip())

### Process each employee -- Print in format
with open("attendance.txt", "r") as file:

    for line in file:

        employee_id, name, status = line.strip().split(",")

        print(f"ID: {employee_id}")
        print(f"Name: {name}")
        print(f"Status: {status}")
        print("-" * 30)
print("--------------------------------")
# -------------------------------------
'''
Corporate exercise
You are asked to prepare the following:
1.	Read attendance data. 
2.	Count total employees. 
3.	Count present employees. 
4.	Count absent employees. 
5.	Calculate attendance percentage. 
6.	Generate an attendance report. 
# -------------------------------------------
'''
# --------------------------------------------------
# Real-Life Report Generation
# ----------------------------
'''
employees = [
    ("101", "Arun", 85000),
    ("102", "Priya", 72000),
    ("103", "Karthik", 95000)
]

with open("salary_report.txt", "w") as file:

    file.write("EMPLOYEE SALARY REPORT\n")
    file.write("=" * 40 + "\n")

    for employee_id, name, salary in employees:
        file.write( f"{employee_id} | {name} | Rs.{salary}\n" )

print("Report generated successfully.")

'''
'''
Expected file
EMPLOYEE SALARY REPORT
========================================
101 | Arun | Rs.85000
102 | Priya | Rs.72000
103 | Karthik | Rs.95000
'''






