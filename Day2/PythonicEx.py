# Complete Pythonic Example
## Employee Performance Analyzer
employees = [
    {
        "name": "Arun",
        "department": "Development",
        "salary": 55000,
        "performance": 85
    },
    {
        "name": "Priya",
        "department": "QA",
        "salary": 48000,
        "performance": 92
    },
    {
        "name": "Kumar",
        "department": "Development",
        "salary": 65000,
        "performance": 78
    },
    {
        "name": "Divya",
        "department": "HR",
        "salary": 45000,
        "performance": 88
    }
]


def get_high_performers(
    employees: list[dict]
) -> list[dict]:

    return [
        employee
        for employee in employees
        if employee["performance"] >= 85
    ]


def get_departments(
    employees: list[dict]
) -> set[str]:

    return {
        employee["department"]
        for employee in employees
    }


def display_employees(
    employees: list[dict]
) -> None:

    for number, employee in enumerate(
        employees,
        start=1
    ):
        print(
            f"{number}. "
            f"{employee['name']} - "
            f"{employee['department']} - "
            f"{employee['salary']}"
        )


def get_salary_report(
    employees: list[dict]
) -> dict[str, int]:

    return {
        employee["name"]: employee["salary"]
        for employee in employees
    }


def sort_by_salary(
    employees: list[dict]
) -> list[dict]:

    return sorted(
        employees,
        key=lambda employee: employee["salary"],
        reverse=True
    )


def all_have_good_performance(
    employees: list[dict]
) -> bool:

    return all(
        employee["performance"] >= 70
        for employee in employees
    )


def has_high_performer(
    employees: list[dict]
) -> bool:

    return any(
        employee["performance"] >= 90
        for employee in employees
    )


print("EMPLOYEES")
display_employees(employees)

print("\nHIGH PERFORMERS")
high_performers = get_high_performers(employees)
display_employees(high_performers)

print("\nDEPARTMENTS")
print(get_departments(employees))

print("\nSALARY REPORT")
print(get_salary_report(employees))

print("\nSORTED BY SALARY")
sorted_employees = sort_by_salary(employees)
display_employees(sorted_employees)

print("\nPERFORMANCE CHECK")
print(
    "All employees have performance >= 70:",
    all_have_good_performance(employees)
)

print(
    "At least one employee has performance >= 90:",
    has_high_performer(employees)
)

'''
What this single program demonstrates
----------------------------------------
Requirement	                Where it is used
Type Hints              	Function parameters and return types
List Comprehension      	get_high_performers()
Set Comprehension       	get_departments()
Dictionary Comprehension	get_salary_report()
enumerate()	                display_employees()
sorted()	                 sort_by_salary()
any()	                    has_high_performer()
all()	                    all_have_good_performance()
Lambda	                    sorted(..., key=lambda...)
Clean Function Design	    Each function performs one clear responsibility

You can see how individual Pythonic features combine into a small piece of backend-style business logic rather than learning each function in isolation.
'''

