from pathlib import Path
'''
What is Path?
Path comes from Python's built-in pathlib module and is used to work with files and folders.

For example:

from pathlib import Path
'''

file_path = Path("salary_report.txt")

print(file_path)
print(file_path.exists())
print(file_path.name)
print(file_path.suffix)

'''
Output:

salary_report.txt
False
salary_report.txt
.txt
Common mistake

❌ Without importing:

file_path = Path("salary_report.txt")

Python gives:
NameError: name 'Path' is not defined

✅ Correct:

from pathlib import Path

file_path = Path("salary_report.txt")

For the File Handling concept, pathlib.Path is worth specifying along with open(), 
because it provides a cleaner way to handle file paths, folders, file existence, 
creation, deletion, and directory traversal.
'''
#------------------------------

report_folder = Path("reports")

report_folder.mkdir(exist_ok=True)

report_file = report_folder / "employee_report.txt"

with report_file.open("w") as file:
    file.write("Employee Report\n")
    file.write("Total Employees: 25\n")

print("Report created:", report_file)
# ---------------------------------

# Useful pathlib operations
path = Path("report/employee.txt")

print("Full Path:", path.resolve()) # Full Path
print("Current directory:", Path.cwd()) # Current working dir
print("Exists:", path.exists())  # exactly where Python is looking for the file.
print("File:", path.is_file())
print("Parent:", path.parent)
print("Name:", path.name)
print("Suffix:", path.suffix)



