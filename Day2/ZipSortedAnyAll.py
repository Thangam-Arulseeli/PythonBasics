# 1. zip() – Combining Related Data
# Suppose employee names and salaries are stored separately:

names = ["Arun", "Priya", "Kumar", "Divya"]
salaries = [45000, 65000, 35000, 75000]

# We can combine them using zip():

for name, salary in zip(names, salaries):
    print(name, salary)

'''
Output:
-------
Arun 45000
Priya 65000
Kumar 35000
Divya 75000

zip() pairs corresponding elements:
Arun   → 45000
Priya  → 65000
Kumar  → 35000
Divya  → 75000
'''
# ----------------------------------

# 2. zip() – Creating a Dictionary
# This is a very useful real-world example.

names = ["Arun", "Priya", "Kumar", "Divya"]
salaries = [45000, 65000, 35000, 75000]

employee_salary = dict(zip(names, salaries))

print(employee_salary)
# ----------------------------------

'''
Output:
{
    'Arun': 45000,
    'Priya': 65000,
    'Kumar': 35000,
    'Divya': 75000
}
This is a very common Pythonic pattern.
'''
# -------------------------------------

# 3. Important zip() Edge Case
# If the lists have different lengths:

names = ["Arun", "Priya", "Kumar"]
salaries = [45000, 65000]
for name, salary in zip(names, salaries):
    print(name, salary)

'''
Output:
--------
Arun 45000
Priya 65000

Important Note: The unmatched "Kumar" is ignored by normal zip().
'''
#------------------------------------------

# 4. sorted() – Employee Salary Sorting

employees = [
    {"name": "Arun", "salary": 45000},
    {"name": "Priya", "salary": 65000},
    {"name": "Kumar", "salary": 35000},
    {"name": "Divya", "salary": 75000}
]

# Sort employees based on salary:

sorted_employees = sorted(
    employees,
    key=lambda employee: employee["salary"] #,
   # reverse=True
)

for employee in sorted_employees:
    print(employee)

'''
Output:
-------
{'name': 'Kumar', 'salary': 35000}
{'name': 'Arun', 'salary': 45000}
{'name': 'Priya', 'salary': 65000}
{'name': 'Divya', 'salary': 75000}
'''
### Descending order
'''
sorted_employees = sorted(
    employees,
    key=lambda employee: employee["salary"],
    reverse=True
)
Now highest salary comes first.
'''
#------------------------------------


# 5. sorted() by Multiple Criteria  --- This is useful in real applications.

# Suppose employees have:

employees = [
    {"name": "Arun", "department": "Development", "salary": 50000},
    {"name": "Priya", "department": "QA", "salary": 50000},
    {"name": "Kumar", "department": "Development", "salary": 70000}
]

# Sort by salary and then name:

sorted_employees = sorted(
    employees,
    key=lambda employee: (
        employee["salary"],
        employee["name"]
    )
)

# NOTE: Python compares the first key first, then uses the second key when necessary.
#--------------------------------------------------

# 6. any() – At Least One Condition
# any() returns True if at least one item is truthy.

# Example:
# --------
marks = [45, 67, 82, 91, 38]
has_failed = any(mark < 50 for mark in marks)
print(has_failed)

# Output: True
# Because at least one mark is below 50.
#----------------------------------

# Real-life use
employees = [
    {"name": "Arun", "active": True},
    {"name": "Priya", "active": True},
    {"name": "Kumar", "active": False}
]

has_inactive_employee = any(
    not employee["active"]
    for employee in employees
)

print(has_inactive_employee)

# Output: True
# ----------------------------


# 7. all() – Every Condition
# all() returns True only if all items are truthy.

# Example:

marks = [75, 82, 91, 68, 88]
all_passed = all(mark >= 50 for mark in marks)
print(all_passed)

# Output:  True

# Now:
marks = [75, 82, 45, 68, 88]
all_passed = all(mark >= 50 for mark in marks)
print(all_passed)

# Output: False
# Because one student has a mark below 50.
#  --------------------------------


# 8. any() and all() – Real Backend Validation
# Suppose we receive employee records from an API:

employees = [
    {"name": "Arun", "email": "arun@example.com"},
    {"name": "Priya", "email": "priya@example.com"},
    {"name": "Kumar", "email": ""}
]

# Check whether any employee has a missing email:
has_missing_email = any(
    not employee["email"]
    for employee in employees
)

print(has_missing_email)

# Output: True

# Check whether all employees have an email:

all_have_email = all(
    employee["email"]
    for employee in employees
)
print(all_have_email)

Output: False

# NOTE: This is much closer to the type of validation developers will encounter in backend development.


