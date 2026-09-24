1. Basic Type Hint

Without type hints:

name = "Arun"
age = 25
salary = 50000.50

With type hints:

name: str = "Arun"
age: int = 25
salary: float = 50000.50

The syntax is:

variable: data_type = value

Examples:

name: str = "Arun"
age: int = 25
is_active: bool = True
salary: float = 50000.50
2. Type Hints in Functions

This is where type hints become particularly useful.

def add(a: int, b: int) -> int:
    return a + b

Here:

a: int

means a is expected to be an integer.

b: int

means b is expected to be an integer.

-> int

means the function is expected to return an integer.

Usage:

result = add(10, 20)

print(result)

Output:

30
3. Type Hint Does NOT Automatically Validate

Consider:

def add(a: int, b: int) -> int:
    return a + b


print(add("Hello", "Python"))

Python may execute this and produce:

HelloPython

The type hint:

a: int

does not automatically force a to be an integer.

This is an important point for trainees:

Type hints describe the intended types; they are not, by themselves, runtime validation.

Tools such as mypy or Pyright can analyze code and report type inconsistencies.

4. Type Hint for Multiple Parameters
def calculate_salary(
    basic_salary: float,
    bonus: float,
    tax: float
) -> float:

    return basic_salary + bonus - tax

Usage:

salary = calculate_salary(30000.0, 5000.0, 2000.0)

print("Final Salary:", salary)

Output:

Final Salary: 33000.0

This makes the function much easier to understand.

5. Type Hints for Collections

Modern Python allows us to specify the element types inside collections.

List
numbers: list[int] = [10, 20, 30, 40]

This means:

numbers is a list containing integers.

List of strings
employees: list[str] = [
    "Arun",
    "Priya",
    "Kumar"
]
Dictionary
employees: dict[str, int] = {
    "Arun": 50000,
    "Priya": 60000
}

Meaning:

key   → str
value → int
Tuple
employee: tuple[str, int] = ("Arun", 50000)
6. Function Returning a List
def get_even_numbers(numbers: list[int]) -> list[int]:

    result = []

    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    return result


numbers = [10, 15, 20, 25, 30]

even_numbers = get_even_numbers(numbers)

print(even_numbers)

Output:

[10, 20, 30]

The function clearly communicates:

numbers: list[int]

and:

-> list[int]
7. None Return Type

If a function doesn't return a meaningful value:

def display_message(message: str) -> None:
    print(message)

Here:

-> None

means:

This function is not expected to return a value.

Example:

display_message("Welcome to Python")
8. Optional Values

Sometimes a parameter may contain a value or None.

Modern Python:

def find_employee(employee_id: int) -> str | None:

    if employee_id == 101:
        return "Arun"

    return None

The return type:

str | None

means:

Either a string
OR
None

For example:

employee = find_employee(101)

print(employee)

Output:

Arun

For a missing employee:

employee = find_employee(999)

print(employee)

Output:

None
9. Union Types

A value can sometimes be one of several types.

Modern Python:

def display_id(employee_id: int | str) -> None:
    print(employee_id)

Both are acceptable:

display_id(101)
display_id("EMP101")

The | means either type.

10. Type Hints with Dictionaries

Suppose we have employee information:

employee: dict[str, str | int] = {
    "name": "Arun",
    "age": 25,
    "department": "Development"
}

Here:

Key   → str
Value → str OR int

This is useful when dictionary values have different types.

11. Type Alias

If a type becomes complicated, we can give it a meaningful name.

Employee = dict[str, str | int]

Then:

employee: Employee = {
    "name": "Arun",
    "age": 25,
    "department": "Development"
}

This improves readability.

12. Type Hints with Functions as Parameters

This connects directly with the higher-order functions you just learned.

Suppose a function accepts another function:

def execute_operation(
    operation: callable,
    a: int,
    b: int
):
    return operation(a, b)

For more precise typing, Python's Callable can be used:

from collections.abc import Callable


def execute_operation(
    operation: Callable[[int, int], int],
    a: int,
    b: int
) -> int:

    return operation(a, b)

Now we are saying:

operation:
    accepts two integers
    returns an integer

Example:

def add(a: int, b: int) -> int:
    return a + b


result = execute_operation(add, 10, 20)

print(result)

Output:

30

This is a good example connecting:

Higher-Order Functions
        +
Type Hints
13. Type Hints with Classes
class Employee:

    def __init__(
        self,
        name: str,
        salary: float
    ):
        self.name = name
        self.salary = salary

    def display(self) -> None:
        print(self.name, self.salary)

Usage:

employee = Employee("Arun", 50000.0)

employee.display()

The constructor clearly tells us what types are expected.

14. Why Type Hints Are Important for Backend Development

For your trainees, this is especially important because they will move into FastAPI + Pydantic + SQLAlchemy.

For example:

def get_employee(employee_id: int) -> dict:
    ...

Immediately we know:

employee_id → integer
return       → dictionary

FastAPI also makes extensive use of Python type annotations for things such as:

Request parameters
Path parameters
Query parameters
Request models
Response models
Dependency declarations

So the trainees should understand type hints before moving deeply into FastAPI.

15. Type Hints + FastAPI

A simple FastAPI example:

from fastapi import FastAPI

app = FastAPI()


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int) -> dict:

    return {
        "id": employee_id,
        "name": "Arun"
    }

Here:

employee_id: int

tells FastAPI that the path parameter is expected to be an integer.

This is one reason Python type hints are particularly important in your Python backend training.

16. Common Type Hints
Python Type	Type Hint
Text	str
Integer	int
Decimal number	float
True/False	bool
List	list
List of integers	list[int]
Tuple	tuple
Dictionary	dict
Set	set
No return value	None
Either type	str | int
Optional value	str | None
Function	Callable
Important trainee takeaway

Without type hints:

def calculate(a, b):
    return a + b

With type hints:

def calculate(a: int, b: int) -> int:
    return a + b

The second version communicates the contract of the function much more clearly:

Input:
    a → int
    b → int

Output:
    int
One-line definition

Type hints are annotations that specify the expected types of variables, function parameters, and return values, improving code readability, tooling, and maintainability without inherently enforcing types at runtime.
