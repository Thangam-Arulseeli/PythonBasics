# What is a Higher-Order Function?
'''
A higher-order function is a function that does at least one of these:
1.	Accepts another function as an argument 
2.	Returns another function 
This is possible because Python treats functions as first-class objects.

'''

# Function as an Argument

def greet():
    print("Hello Trainees")

def execute(function): # Higer order funnction  
    function()

execute(greet)

# Output:
# Hello Trainees

''' Here:
execute(greet) passes the function greet to execute.
Inside:
function() calls the received function.
Therefore, execute() is a higher-order function.
'''

# Real-Life Example – Employee Salary Processing
# Suppose we want to apply different salary calculations.
def calculate_bonus(salary):
    return salary * 0.10

def calculate_tax(salary):
    return salary * 0.05

def process_salary(salary, calculation):
    amount = calculation(salary)
    return amount

salary = 50000

bonus = process_salary(salary, calculate_bonus)
tax = process_salary(salary, calculate_tax)

print("Bonus:", bonus)
print("Tax:", tax)

'''
Output:
Bonus: 5000.0
Tax: 2500.0
Here:
process_salary(salary, calculate_bonus)
passes a function as an argument.
This makes the program flexible because process_salary() doesn't need to know exactly what calculation will be performed.
'''

# Function Returning Another Function
# A higher-order function can also return a function.
def create_greeting():

    def greet():
        print("Hello, welcome to Python training!")

    return greet

message = create_greeting()

message()

# Output:
# Hello, welcome to Python training!
'''
Notice:
return greet
not:
return greet()
We are returning the function itself, not executing it.
'''
# ---------------------------------

# Higher-Order Function with a Parameter
# This is a more meaningful example:
'''
def create_multiplier(number):

    def multiply(value):
        return value * number

    return multiply

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(10))
print(triple(10))
'''
# Output:
# 20
# 30
# What's happening?
# Step 1
#   double = create_multiplier(2)
#   The returned function remembers:
#   number = 2
# Step 2
#   triple = create_multiplier(3)
#   The returned function remembers:
#   number = 3
#   This leads to an important Python concept called a closure.
# -----------------------------------------------------

'''
Nested Function vs Higher-Order Function
--------------------------------------------
These concepts are related but not the same.
Feature	                             Nested Function	        Higher-Order Function
Function inside another function	✅	                        Not necessarily
Accepts function as argument	    Not required	            ✅
Returns a function	                Not required	            ✅
Main concept	                    Function nesting	        Functions treated as data
Example	                            inner() inside outer()	    map(), filter(), custom callback
Common use	                        Encapsulation, closures	    Callbacks, functional programming, decorators
'''

