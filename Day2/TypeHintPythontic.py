## Type Hints 
'''
Basic Type Hint
------------------
Without type hints:

name = "Arun"
age = 25
salary = 50000.50

With type hints:

name: str = "Arun"
age: int = 25
salary: float = 50000.50

The syntax of Type Hint is:
--------------
variable: data_type = value

Examples:
-----------
name: str = "Arun"
age: int = 25
is_active: bool = True
salary: float = 50000.50

'''


# 2. Type Hints in Functions --- This is where type hints become particularly useful.

def add(a: int, b: int) -> int:
    return a + b

c: int = add (100, 200)
print ("Result = ", c)
# Output: Result = 300
#------------------------------------

# Type Hints – Real-Life Employee Processing  -- Type hints make the expected input and output of a function clear.

# Example: Employee Salary Processing
def calculate_net_salary(
    basic_salary: float,
    bonus: float,
    tax: float
) -> float:

    gross_salary: float = basic_salary + bonus
    net_salary: float = gross_salary - tax

    return net_salary


salary: float = calculate_net_salary(
    40000.0,
    5000.0,
    4500.0
)

print("Net Salary:", salary)

# Output
# Net Salary: 40500.0

'''
Important point
----------------
Type hints do not automatically enforce the type at runtime.

They are useful for:

Readability
IDE support
Static type checking
Code maintenance
Useful for the Frameworks such as FastAPI
Practical Backend Example
def get_employee_status(
    experience: int,
    salary: float
) -> str:

# --------------------------------------
'''

# 2. Comprehensions – Real-Life Employee Filtering

# Comprehensions are a Pythonic way of creating collections from existing collections.
# Suppose:
employees = [
    {"name": "Arun", "salary": 45000},
    {"name": "Priya", "salary": 65000},
    {"name": "Kumar", "salary": 35000},
    {"name": "Divya", "salary": 75000}
]

# We want employees earning more than 50000.

# Traditional approach
high_salary_employees = []

for employee in employees:

    if employee["salary"] > 50000:
        high_salary_employees.append(employee)

print("Traditional Approach :", high_salary_employees)


# Pythonic approach
high_salary_employees = [
    employee
    for employee in employees
    if employee["salary"] > 50000
]

print("Pythontic approach : ",high_salary_employees)

# Output:
'''[
    {'name': 'Priya', 'salary': 65000},
    {'name': 'Divya', 'salary': 75000}
]
'''
### Structure  --- [result for item in collection if condition]
'''
Here:
    result       → employee
    item         → employee
    collection   → employees
    condition    → salary > 50000
'''


# 3. Dictionary Comprehension – Employee Salary Report
# Suppose management wants only:
# Employee Name → Salary
# We can create a dictionary directly.
employees = [
    {"name": "Arun", "salary": 45000},
    {"name": "Priya", "salary": 65000},
    {"name": "Kumar", "salary": 35000},
    {"name": "Divya", "salary": 75000}
]
salary_report = {
    employee["name"]: employee["salary"]
    for employee in employees
}

print(salary_report)

#Output:
'''{
    'Arun': 45000,
    'Priya': 65000,
    'Kumar': 35000,
    'Divya': 75000
}
'''

# With filtering
employees = [
    {"name": "Arun", "salary": 45000},
    {"name": "Priya", "salary": 65000},
    {"name": "Kumar", "salary": 35000},
    {"name": "Divya", "salary": 75000}
]
senior_salary_report = {
    employee["name"]: employee["salary"]
    for employee in employees
    if employee["salary"] >= 50000
}

print(senior_salary_report)

# Output:
'''{
    'Priya': 65000,
    'Divya': 75000
}
'''
# This is very useful when processing API/database results.

#4. Set Comprehension – Extract Unique Departments
employees = [
    {"name": "Arun", "department": "Development"},
    {"name": "Priya", "department": "QA"},
    {"name": "Kumar", "department": "Development"},
    {"name": "Divya", "department": "HR"}
]

departments = {
    employee["department"]
    for employee in employees
}

print(departments)

#Output:
# {'Development', 'QA', 'HR'}

#A set automatically removes duplicates.
#----------------------------------------------

# 5. enumerate() – Employee Numbering
# Suppose you need to display employees with serial numbers.
# Without enumerate():

employees = ["Arun", "Priya", "Kumar", "Divya"]

for i in range(len(employees)):
    print(i + 1, employees[i])

# Pythonic approach:
for number, employee in enumerate(employees, start=1):
    print(number, employee)

'''
Output:

1 Arun
2 Priya
3 Kumar
4 Divya
Why enumerate() is better

Instead of manually maintaining:

i = 0
i += 1

Python gives you both:

index/number
     +
value

through:
    for number, employee in enumerate(employees, start=1):
'''

# 6. Real-Life enumerate()  #  Ticket Processing
# Suppose a support team has tickets:
tickets = [
    "Login issue",
    "Password reset",
    "Database error",
    "Payment failure"
]

for ticket_no, ticket in enumerate(tickets, start=1001):
    print(f"Ticket #{ticket_no}: {ticket}")

'''
Output:
------------
Ticket #1001: Login issue
Ticket #1002: Password reset
Ticket #1003: Database error
Ticket #1004: Payment failure

This is more realistic than simply demonstrating enumerate() with numbers.
'''

