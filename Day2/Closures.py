# Closures in Python
'''
A closure is a function that remembers variables from its enclosing (outer) function even after the outer function has finished executing.
This sounds complicated at first, so let's build it step by step.
'''

# 1. First understand the problem

# Consider this nested function:
def outer():
    message = "Hello"

    def inner():
        print(message)

    inner()

outer()

# Output:  Hello

 # Here, inner() can access message because message belongs to the enclosing outer() function.
# But this is not necessarily a closure in the useful sense yet, because inner() is executed before outer() finishes.


# 2. The important part: Returning the inner function
def outer():
    message = "Hello"

    def inner():
        print(message)

    return inner

function = outer()

function()

# Output: Hello

# When we execute: 

# function = outer()  -- outer() has already finished.
# Normally, you might think message should disappear because it was a local variable of outer().
# But:  function()  still prints: 
    ### Hello Why?  Because inner() remembers the variable message from its enclosing scope.
            ###     That is a closure.

#### 3. Simple definition
'''
A closure is an inner function that remembers and retains access to variables 
from its enclosing function even after the enclosing function has finished execution.

The three important conditions are:

1. There is an outer function
          ↓
2. There is an inner function
          ↓
3. Inner function uses a variable from outer function
          ↓
4. Inner function is returned/referenced outside
          ↓
       CLOSURE
'''

# 4. Very simple example
# ------------------------
def create_greeting(name):

    def greet():
        print("Hello", name)

    return greet

greeting = create_greeting("Arun")

greeting()

# Output: Hello Arun
'''
Here:
name = "Arun"
belongs to create_greeting().

But after:
greeting = create_greeting("Arun")
the outer function has finished.

Still:
greeting() can access "Arun".
That remembered value is the important part of the closure.
'''
# ----------------------------------------------

# 5. Different closures can remember different values
# This is where closures become really useful.

def create_greeting(name):

    def greet():
        print("Hello", name)

    return greet

greeting1 = create_greeting("Arun")
greeting2 = create_greeting("Priya")

greeting1()
greeting2()

# Output:
# Hello Arun
# Hello Priya

'''
 We have created two different closures.

Conceptually:

greeting1
   ↓
remembers name = "Arun"

greeting2
   ↓
remembers name = "Priya"
'''

# 6. Practical Example – Multiplier
# -------------------------------------
# This is one of the best examples for closures.

def create_multiplier(number):

    def multiply(value):
        return value * number

    return multiply

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(10))
print(triple(10))

# Output:
# 20
# 30
# What happened?
'''
When we execute:
double = create_multiplier(2)
the closure remembers:
number = 2
So:
double(10)
means:
10 × 2 = 20
Similarly:
triple = create_multiplier(3)
remembers:
number = 3
Therefore:
triple(10)
gives:
30
'''
# ------------------------------


# 7. Closure with nonlocal
# ----------------------------
# Closures become even more useful when combined with nonlocal.

# Counter example
def create_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter = create_counter()

print(counter())
print(counter())
print(counter())
print(counter())

Output:

1
2
3
4
How?

Initially:

count = 0

Then:

counter()

changes it to:

count = 1

Next call:

count = 2

and so on.

# The closure remembers the state.
# ----------------------------


# 8. Why nonlocal is needed
# Consider
3 :

def create_counter():

    count = 0

    def counter():
        count += 1
        return count

    return counter

This produces an error because:

count += 1

means:

count = count + 1

Python therefore considers count local to counter().

But we actually want to modify the count belonging to create_counter().

So:

nonlocal count

is required.

Correct:

def create_counter():

    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter
9. Closure vs Nested Function

These are often confused.

Nested function

A function defined inside another function:

def outer():

    def inner():
        print("Hello")

    inner()

This is a nested function.

Closure

An inner function that retains access to an enclosing function's variable after the outer function has returned:

def outer():

    message = "Hello"

    def inner():
        print(message)

    return inner

So:

Every closure involves a nested function, but not every nested function is necessarily being used as a closure.

10. Closure vs global

This is useful to connect with your previous question.

Global
count = 0

def increment():
    global count
    count += 1

The variable belongs to the global scope.

Closure
def create_counter():

    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

The variable belongs to the enclosing function.

global
   ↓
global count
   ↓
increment()


closure
   ↓
outer count
   ↓
inner function
11. Why are closures useful?

Closures are useful when you want a function to remember state or configuration without using global variables or a class.

Common uses include:

Creating configurable functions
Maintaining state
Callbacks
Function factories
Decorators
Data hiding/encapsulation
Event handlers
Creating reusable customized functions
12. Practical Example – Discount Calculator

This is a good real-life example for trainees.

def create_discount_calculator(discount_percentage):

    def calculate(price):
        discount = price * discount_percentage / 100
        final_price = price - discount
        return final_price

    return calculate


student_discount = create_discount_calculator(10)
premium_discount = create_discount_calculator(20)

print("Student Price:", student_discount(1000))
print("Premium Price:", premium_discount(1000))

Output:

Student Price: 900.0
Premium Price: 800.0

The functions remember their respective discount:

student_discount
       ↓
discount_percentage = 10


premium_discount
       ↓
discount_percentage = 20
13. Another practical example – Tax Calculator
def create_tax_calculator(tax_rate):

    def calculate_tax(amount):
        return amount * tax_rate / 100

    return calculate_tax


gst = create_tax_calculator(18)
service_tax = create_tax_calculator(5)

print("GST:", gst(10000))
print("Service Tax:", service_tax(10000))

Output:

GST: 1800.0
Service Tax: 500.0

This demonstrates how we can create specialized functions from a common function factory.

14. How Python stores the remembered value

You can actually inspect the closure:

def create_multiplier(number):

    def multiply(value):
        return value * number

    return multiply


double = create_multiplier(2)

print(double.__closure__)

Python stores the captured variable in the function's closure.

You can inspect the actual value:

print(double.__closure__[0].cell_contents)

Output:

2

This is useful for understanding what Python is doing internally, although trainees don't need to memorize __closure__.

