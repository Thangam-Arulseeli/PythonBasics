### Clean Function Design
### ----------------------
# This is the most important part of the Pythonic Programming module.
# --------------------------------------------------------------------

'''
A clean function should generally have:

One clear responsibility
Meaningful names
Clear parameters
Appropriate return values
Type hints
Minimal side effects
Avoid unnecessary global variables
Avoid deeply nested logic
Be easy to test and reuse
'''''

# Bad Design -- Example 

total = 0

def process():
    global total

    name = input("Enter name: ")
    salary = float(input("Enter salary: "))

    if salary > 50000:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05

    total = salary + bonus

    print(name)
    print(total)
process()
'''
Problems:

Uses global state
Takes input inside business logic
Prints inside calculation logic
Function does several things
Difficult to unit test
Difficult to reuse
'''

### Clean Function Design -- Separate responsibilities:

def calculate_bonus(salary: float) -> float:

    if salary > 50000:
        return salary * 0.10

    return salary * 0.05


def calculate_total_salary(
    salary: float,
    bonus: float
) -> float:

    return salary + bonus


def create_employee_summary(
    name: str,
    salary: float
) -> dict:

    bonus = calculate_bonus(salary)
    total_salary = calculate_total_salary(
        salary,
        bonus
    )

    return {
        "name": name,
        "salary": salary,
        "bonus": bonus,
        "total_salary": total_salary
    }


employee = create_employee_summary(
    "Arun",
    60000
)

print(employee)

'''
Output:
--------
{
    'name': 'Arun',
    'salary': 60000,
    'bonus': 6000.0,
    'total_salary': 66000.0
}

Now each function has a clear responsibility:

calculate_bonus()
        ↓
Calculate bonus

calculate_total_salary()
        ↓
Calculate total salary

create_employee_summary()
        ↓
Combine employee information
'''
