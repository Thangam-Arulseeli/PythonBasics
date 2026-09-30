### Lambda Functions
### A lambda is an anonymous function, generally used when a small function is required temporarily.
'''
Normal function:
------------------
def calculate_bonus(salary):
    return salary * 10 / 100

Lambda:
--------
calculate_bonus = lambda salary: salary * 10 / 100

print(calculate_bonus(50000))
'''

employees = [
    {"name": "Arun", "salary": 85000},
    {"name": "Priya", "salary": 70000},
    {"name": "Karthik", "salary": 95000}
]

### sorted()
# Sort employees based on salary:
sorted_employees = sorted(
    employees,
        key = lambda employee: employee["salary"]
)

print("Lamda - Sorted Employees based on salary :")
for employee in sorted_employees:
    print(employee)

'''
Important NOTE
--------------
Lambda should normally be used for small, simple operations.
Don't turn a complicated business rule into an unreadable lambda.
'''
# ------------------------------------------------

### map()   # map() applies a function to every element in a collection.

salaries = [40000, 50000, 60000]

annual_salaries = map(
    lambda salary: salary * 12,
    salaries
)
print("Apply Lamda - Map()")
print(list(annual_salaries))

# Output: [480000, 600000, 720000]
# ------------------------------------------

# ---------map() with Real Employee Data
employees = [
    {"name": "Arun", "salary": 50000},
    {"name": "Priya", "salary": 60000},
    {"name": "Karthik", "salary": 70000}
]

annual_salaries = list(
    map(
        lambda employee: employee["salary"] * 12,
        employees
    )
)
print("Apply Lamda - Map()")
print(annual_salaries)
# Output: [600000, 720000, 840000]
###-----------------------------------------------

### filter() -- selects elements satisfying a condition.
# Example:

salaries = [35000, 45000, 55000, 70000]

high_salaries = list(
    filter(
        lambda salary: salary >= 50000,
        salaries
    )
)
print("Apply Lamda - filter()")
print(high_salaries)
# Output: [55000, 70000]
# ---------------------------------------

### Real-Life Employee Filtering
employees = [
    {"name": "Arun", "salary": 85000},
    {"name": "Priya", "salary": 45000},
    {"name": "Karthik", "salary": 95000},
    {"name": "Divya", "salary": 40000}
]

high_salary_employees = list(
    filter(
        lambda employee: employee["salary"] >= 80000,
        employees
    )
)
print("Apply Lamda - filter() - Real life")
for employee in high_salary_employees:
    print(employee["name"])
'''
Output:
Arun
Karthik
'''

'''
map() vs filter() vs Comprehension
-----------------------------------
Concept	                 Purpose
map()	                Transform every item
filter()	            Select matching items
List comprehension	    Transform/filter in Pythonic syntax

For example:
salaries = [40000, 50000, 60000]

map()
result = list(
    map(lambda x: x * 12, salaries)
)

filter()
result = list(
    filter(lambda x: x >= 50000, salaries)
)

Comprehension
result = [x * 12 for x in salaries]

In modern Python code, comprehensions are often preferred when they make the logic clearer.
'''
#### ====================================



