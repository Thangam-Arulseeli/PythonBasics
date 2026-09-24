# Nested Function 
    ###   A nested function is a function defined inside another function.


# Why use nested functions?
    ###     Nested functions are useful when a function is needed only inside another function.


def outer():
    print("This is outer function")

    def inner():
        print("This is inner function")

    inner()

outer()

# Output

# This is outer function
# This is inner function
# -----------------------------

def calculate_salary(basic_salary):
    
    def calculate_bonus():
        return basic_salary * 0.10

    bonus = calculate_bonus()
    return basic_salary + bonus


salary = calculate_salary(30000)

print("Final Salary:", salary)

# Output: Final Salary: 33000.0
# calculate_bonus() is only required by calculate_salary(), so keeping it inside makes the relationship clear.
# ----------------------------------

# Scope of a Nested Function
# -------------------------------
# An inner function can access variables from its outer function.
# Example
def employee_details():
    employee_name = "Arun"

    def display():
        print("Employee:", employee_name)

    display()

employee_details()

# Output:
# Employee: Arun
# The display() function can access: employee_name from its enclosing function.

'''
The inner function can access the value of the variables from its enclosing functions
This is related to the LEGB rule:
L → Local
E → Enclosing
G → Global
B → Built-in
Python searches for a variable in this order.

'''

# Modifying an Outer Variable with nonlocal
# If the inner function needs to modify a variable belonging to the outer function, use nonlocal.
def counter_app():

    count = 0

    def increment():
        nonlocal count
        count += 1
        print("Count:", count)

    increment()
    increment()
    increment()


counter_app()

'''
Output:
Count: 1
Count: 2
Count: 3
Without:
nonlocal count
Python would treat count as a local variable inside increment().
'''




