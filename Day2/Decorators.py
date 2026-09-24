Decorators in Python

A decorator is a function that adds or modifies the behavior of another function without changing its original code.

This is an important Day 2 topic because decorators are widely used in FastAPI, authentication, logging, authorization, caching, and validation.

1. Why do we need decorators?

Suppose we already have:

def greet():
    print("Hello, Arun")


greet()

Now we want to add:

Before executing greet()
    ↓
Print "Function started"
    ↓
Execute greet()
    ↓
Print "Function completed"

We could modify greet() directly, but decorators allow us to add this behavior without changing greet().

2. Basic Decorator
def decorator(function):

    def wrapper():
        print("Function started")

        function()

        print("Function completed")

    return wrapper


def greet():
    print("Hello, Arun")


greet = decorator(greet)

greet()

Output:

Function started
Hello, Arun
Function completed
What happened?

Initially:

greet → original greet function

Then:

greet = decorator(greet)

The decorator receives the original greet function.

It returns:

wrapper

So now:

greet → wrapper

When we call:

greet()

we are actually calling wrapper().

Inside wrapper():

function()

calls the original greet().

3. Using @ Syntax

Python provides a cleaner syntax.

Instead of:

greet = decorator(greet)

we can write:

@decorator
def greet():
    print("Hello, Arun")

Complete example:

def decorator(function):

    def wrapper():
        print("Function started")

        function()

        print("Function completed")

    return wrapper


@decorator
def greet():
    print("Hello, Arun")


greet()

Output:

Function started
Hello, Arun
Function completed

This:

@decorator
def greet():

is essentially equivalent to:

def greet():
    ...

greet = decorator(greet)
4. Understanding the Structure

A typical decorator has three parts:

def decorator(function):

    def wrapper():
        # Code before

        function()

        # Code after

    return wrapper

Think of it as:

             decorator
                 ↓
          ┌──────────────┐
          │    wrapper   │
          │              │
          │ Before       │
          │     ↓        │
          │  function()  │
          │     ↓        │
          │ After        │
          └──────────────┘
5. Decorator with Function Arguments

The previous example only works with functions that have no parameters.

What about:

def greet(name):
    print("Hello", name)

We need the wrapper to accept arguments.

def decorator(function):

    def wrapper(name):
        print("Function started")

        function(name)

        print("Function completed")

    return wrapper


@decorator
def greet(name):
    print("Hello", name)


greet("Arun")

Output:

Function started
Hello Arun
Function completed
6. Using *args and **kwargs

A good general-purpose decorator should be able to work with functions having different parameters.

def decorator(function):

    def wrapper(*args, **kwargs):

        print("Before function execution")

        result = function(*args, **kwargs)

        print("After function execution")

        return result

    return wrapper

Now it can work with different functions.

@decorator
def add(a, b):
    return a + b


@decorator
def greet(name):                                                                                             
    return f"Hello {name}"


print(add(10, 20))
print(greet("Arun"))

Output:

Before function execution
After function execution
30

Before function execution
After function execution
Hello Arun

This is a much more realistic decorator pattern.

7. Why return result is Important

Consider:

def decorator(function):

    def wrapper(*args, **kwargs):
        print("Before")
        function(*args, **kwargs)
        print("After")

    return wrapper

Suppose:

@decorator
def add(a, b):
    return a + b

Then:

result = add(10, 20)

print(result)

will produce:

Before
After
None

Why?

Because wrapper() didn't return the original result.

Correct:

def decorator(function):

    def wrapper(*args, **kwargs):
        print("Before")

        result = function(*args, **kwargs)

        print("After")

        return result

    return wrapper

Now:

30

is returned correctly.

8. Real-Life Example – Logging Decorator

This is a very useful example for backend trainees.

def log_function(function):

    def wrapper(*args, **kwargs):

        print("Calling:", function.__name__)

        result = function(*args, **kwargs)

        print("Completed:", function.__name__)

        return result

    return wrapper


@log_function
def calculate_salary(basic_salary):

    hra = basic_salary * 0.20
    da = basic_salary * 0.10

    return basic_salary + hra + da


salary = calculate_salary(30000)

print("Final Salary:", salary)

Output:

Calling: calculate_salary
Completed: calculate_salary
Final Salary: 39000.0

The original salary calculation hasn't been changed.

The decorator added logging behavior around it.

9. Real-Life Example – Execution Time

A decorator can measure how long a function takes.

import time


def measure_time(function):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = function(*args, **kwargs)

        end = time.time()

        print("Execution Time:",
              end - start,
              "seconds")

        return result

    return wrapper


@measure_time
def calculate_sum():

    total = 0

    for i in range(1, 1000000):
        total += i

    return total


result = calculate_sum()

print("Result:", result)

Here the decorator adds performance measurement without modifying calculate_sum().

10. Real-Life Example – Authentication

Decorators can also be used conceptually for authorization.

def check_admin(function):

    def wrapper(username, role):

        if role != "admin":
            print("Access denied")
            return

        return function(username, role)

    return wrapper


@check_admin
def delete_user(username, role):

    print(username, "deleted a user")


delete_user("Arun", "admin")
delete_user("Priya", "user")

Output:

Arun deleted a user
Access denied

The decorator checks authorization before allowing the function to execute.

This pattern is highly relevant when trainees later study authentication and authorization in backend development.

11. Multiple Decorators

You can apply more than one decorator.

def first(function):

    def wrapper():
        print("First decorator - Before")
        function()
        print("First decorator - After")

    return wrapper


def second(function):

    def wrapper():
        print("Second decorator - Before")
        function()
        print("Second decorator - After")

    return wrapper


@first
@second
def greet():
    print("Hello")
    

greet()

Execution order:

First decorator - Before
Second decorator - Before
Hello
Second decorator - After
First decorator - After

The decorators are applied from bottom to top:

@first
@second
def greet():

Conceptually:

greet = first(second(greet))
12. Decorator with Parameters

Sometimes we want to configure the decorator itself.

For example:

@repeat(3)
def greet():
    print("Hello")

This requires another level of function nesting.

def repeat(times):

    def decorator(function):

        def wrapper(*args, **kwargs):

            for i in range(times):
                function(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def greet():
    print("Hello")


greet()

Output:

Hello
Hello
Hello

There are now three levels:

repeat()
   ↓
decorator()
   ↓
wrapper()
   ↓
original function

This is an advanced but very useful decorator pattern.

13. functools.wraps

There is one important production-level issue.

Consider:

def decorator(function):

    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper

After decoration:

@decorator
def calculate_salary():
    """Calculate employee salary."""
    pass

The function's metadata can be replaced by the wrapper's metadata.

Python provides:

from functools import wraps

Use:

from functools import wraps


def decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper

Now Python preserves useful metadata such as:

function.__name__
function.__doc__
Recommended production pattern
from functools import wraps


def log_function(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print("Calling:", function.__name__)

        result = function(*args, **kwargs)

        print("Completed:", function.__name__)

        return result

    return wrapper
14. Decorator Flow

For trainees, this diagram is useful:

@decorator
def calculate():
    ...

Python effectively does:

calculate
   ↓
decorator(calculate)
   ↓
wrapper
   ↓
calculate now refers to wrapper

When we call:

calculate()

the flow is:

calculate()
    ↓
wrapper()
    ↓
Before
    ↓
original calculate()
    ↓
After
    ↓
return result
15. Nested Function → Closure → Decorator

This is why we studied the previous topics first.

A decorator combines several concepts you already learned:

Nested Function
       ↓
Functions as Objects
       ↓
Higher-Order Function
       ↓
Closure
       ↓
Decorator

A decorator:

receives a function
creates a nested wrapper function
wrapper remembers the original function
returns the wrapper
adds behavior before/after the original function
Simple definition for trainees

A decorator is a function that takes another function, extends or modifies its behavior, and returns a new function without changing the original function's code.

Recommended  decorator exercises
Create a decorator that prints Before/After function execution.
Create a decorator that logs the function name.
Create a decorator that measures execution time.
Create a decorator that checks whether a user is admin.
Create a decorator that validates a function's arguments.
Create a decorator that allows a function to execute only 3 times.
Create a parameterized decorator @repeat(3).
Create a decorator using *args, **kwargs, and @wraps.

These will give trainees a much stronger understanding than learning only the @decorator syntax.