'''
Decorators – Advanced but Highly Relevant
A decorator allows us to add behavior to a function without modifying the original function's core logic.
A simple example:
def log_execution(func):

    def wrapper():
        print("Function started")

        func()

        print("Function completed")

    return wrapper

Use it:
@log_execution
def generate_report():

    print("Generating employee report")
Calling:
generate_report()
Output:
Function started
Generating employee report
Function completed


11. Why Decorators Matter in Backend Development
Decorators are heavily relevant to frameworks.
In FastAPI, trainees will see:
@app.get("/employees")
def get_employees():
    ...
The @app.get() syntax is decorator-based.
Other real-world uses include:
Logging
Authentication
Authorization
Performance measurement
Caching
Validation
Transaction handling
Permission checking

12. Production-Style Logging Decorator
import time
from functools import wraps


def log_execution(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        print(f"Started: {func.__name__}")

        result = func(*args, **kwargs)

        end = time.time()

        print(
            f"Completed: {func.__name__} "
            f"in {end - start:.4f} seconds"
        )

        return result

    return wrapper
Use:
@log_execution
def calculate_salary(basic, allowance):

    return basic + allowance
Then:
result = calculate_salary(50000, 10000)

print("Salary:", result)
This demonstrates a genuine backend use case: cross-cutting behavior without duplicating code in every function.
'''
