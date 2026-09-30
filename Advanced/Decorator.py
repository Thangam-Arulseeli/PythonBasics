### Decorators -- Decorators modify behavior of a function without changing its code.
# A decorator allows us to add extra functionality to an existing function 
 # without modifying the original function's code.
'''
Used heavily in:
•	Frameworks
•	Logging
•	Authentication
•	Validation

Basic Decorator
-----------------
'''

def decorator_func(func): # decorator_func is a function that takes another function as an argument.
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator_func
def say_hello():
    print("Hello")

print("Simple decorator example")
say_hello()
print("-----------------------")

# Equivalent to:
# say_hello = decorator_func(say_hello)


# Decorator with Arguments
# ------------------------
def decorator_func(func):
    def wrapper(name, age):
        print("Before function")
        func(name, age)
        print("After function")
    return wrapper

@decorator_func
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

print("Simple decorator example")
greet("Arul", 23)
print("-----------------------")

'''
### Using *args and **kwargs (Best Practice)
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

print("Decorator with *args and **kwargs")
print("-----------------------")
'''

### Multiple Decorators
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def test():
    print("Original Function")

print("Multiple decorators")
test()
print("---------------------")

'''
Execution Order:
Decorator1
Decorator2
Original Function

Built-in Decorators
•	@staticmethod
•	@classmethod
•	@property
.   @abstractmethod
•	@dataclass  


Example:
class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks
'''

### Shallow Copy vs Deep Copy
# This is VERY IMPORTANT
# Assignment (Not Copy)
a = [1, 2, 3]
b = a
b.append(4)

print("Assignment")
print(a)  # [1, 2, 3, 4]
print( (a==b))  # True
print( (a is b))  # True
print("-----------------------------")
# Both refer to same object.



# Shallow Copy -- Creates new outer object -- But inner objects are shared
import copy

original = [ [1, 2], [3, 4] ]
shallow = copy.copy(original)

shallow[0][0] = 100

print ("Shallow Copy")
print("Original: ", original)
print("Shallow Copy: ", shallow)
print("-------------------------")
# Output: [[100, 2], [3, 4]]   -- Why? Inner list reference is shared.
####  ----------------------------


### Deep Copy   ## Creates completely independent copy --------- [Original remains unchanged.]
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 999

print("Deep Copy")
print("original :", original)
print("Deep copy:", deep)
print("---------------------")
###Now original remains unchanged.

'''
Visual Representation
----------------------
Original:
Outer List
  -> Inner List 1
  -> Inner List 2
Shallow Copy:
New Outer List
  -> Same Inner List 1
  -> Same Inner List 2
Deep Copy:
New Outer List
  -> New Inner List 1
  -> New Inner List 2


Interview  Questions
-------------------------
Q1: Is tuple immutable?
Yes.
But if tuple contains list → inner list can change.
t = (1, [2, 3])
t[1].append(4)
print(t)

Q2: Why are generators memory efficient?
Because they don't store entire data in memory.

Q3: Difference between iterator and generator?
Feature	                Iterator	        Generator
Implementation	        Class	            Function
Complexity	            More	            Simple
Memory	                Efficient	        More Efficient
State Handling      	Manual	            Automatic


Practical Enterprise Use Cases
--------------------------------
Iterators
•	Custom DB record traversal
•	File streaming
Generators
•	Reading large CSV files
•	Streaming API responses
Decorators
•	Logging
•	Authentication
•	Performance timing
•	Role validation
Deep Copy
•	Configuration cloning
•	Template duplication
•	Transaction rollback models


Final Concept Summary
•	Iterable → Can be looped
•	Iterator → Produces next element
•	Generator → Lazy iterator using yield
•	Decorator → Function modifier
•	Shallow Copy → Copy outer layer only
•	Deep Copy → Copy entire structure


Decorators in Depth
1.	OOP-related decorators
2.	Built-in function decorators
3.	Abstract Base Class decorators
4.	Dataclass decorators
5.	Typing-related decorators
6.	Function utility decorators
7.	Custom decorator patterns (advanced but important)
'''
### ====================================================


'''
### OOP-RELATED DECORATORS (Very Important)
# -------------------------------------------
# These are most asked in interviews.
1.1. @staticmethod
What it does:
•	Belongs to class
•	Does NOT receive self
•	Cannot access instance variables directly

->When to use:
Utility methods logically related to class.
'''

#### Example : @staticmethod
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print("Example : @staticmethod")
print(MathUtils.add(10, 20))
print("---------------------------")
'''

Key Point:
•	No access to instance (self)
•	No access to class (cls) unless passed manually
# --------------------------------------------------

1.2. @classmethod
 What it does:
•	Receives cls instead of self
•	Can modify class-level data
'''

####  Example : @classmethod
class Student:
    school_name = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

print("Example : @classmethod")
Student.change_school("XYZ School")
print(Student.school_name)
print("---------------------------")

'''
Key Difference:
----------------
Decorator	            First Parameter
instance method	        self
classmethod	            cls
staticmethod        	none
# ---------------------------------------------


1.3. @property
What it does:
Turns method into attribute-like access.
'''

#### Example : @property
class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary  ### getter

print("Example : @property")
emp = Employee(50000)
print(emp.salary)  # No parentheses
print("---------------------------")
# --------------------------------------------------


### 1.4. @property.setter
### Used to control setting value.
### Example : @property.setter
class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property          ### getter
    def salary(self):
        return self._salary     ### getter

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

print("Example : @property.setter")
emp = Employee(50000)
# emp.salary = -10000  # This will raise a ValueError 
print(emp.salary)  # No parentheses
print("---------------------------")



### 1.5. @property.deleter
### Used to delete the property.
### Example : @property.deleter
### @salary.deleter is called when you use del emp.salary.
### It is not called automatically when the object is destroyed.
class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.deleter
    def salary(self):
        print("Deleting salary")
        del self._salary

print("Example : @property.deleter")
emp = Employee(10000)
print(emp.salary)  # No parentheses
del emp.salary
# print(emp.salary)  #This will raise an AttributeError because the salary attribute has been deleted. 
del emp # This will delete the emp object itself, but it will not trigger the @salary.deleter method. The @salary.deleter method is only triggered when you explicitly delete the salary property using del emp.salary.   
print("---------------------------")


'''
NOTE: 
Here, salary is a property.

It has two operations:

Operation	        Decorator	        Trigger
---------------------------------------------------------
Get salary	        @property	        emp.salary
Set salary	        @salary.setter	    emp.salary = 60000
Delete salary	    @salary.deleter	    del emp.salary
'''
#----------------------------------------
#### Complete Example with Getter, Setter, and Deleter      
class Employee:

    def __init__(self, salary):
        self._salary = salary

    # Getter
    @property
    def salary(self):
        print("Getting salary")
        return self._salary

    # Deleter
    @salary.deleter
    def salary(self):
        print("Deleting salary")
        del self._salary


emp = Employee(10000)

print("Salary:", emp.salary)

print("---------------------------")

del emp.salary
del emp # This will delete the emp object itself,
# but it will not trigger the @salary.deleter method.
# The @salary.deleter method is only triggered 
# when you explicitly delete the salary property using del emp.salary.

print("---------------------------")

# This will cause AttributeError
#print("Salary:", emp.salary) # AttributeError: 'Employee' object has no attribute '_salary'
#-------------------------------------------

'''
2. ABSTRACT CLASS DECORATORS
From abc module.

2.1. @abstractmethod
Used inside abstract base classes.
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 10 * 10

IMPORTANT NOTE: If area() not implemented → error.


2.2. @abstractclassmethod
Rare but exists.
from abc import ABC, abstractclassmethod

class Base(ABC):

    @abstractclassmethod
    def create(cls):
        pass

2.3. @abstractstaticmethod
from abc import ABC, abstractstaticmethod

class Base(ABC):

    @abstractstaticmethod
    def utility():
        pass


3. DATACLASS DECORATORS
From dataclasses module.

3.1. @dataclass
Automatically generates:
•	__init__
•	__repr__
•	__eq__
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int

s = Student("Arul", 25)
print(s)


Important Parameters
@dataclass(frozen=True)
→ Makes object immutable
@dataclass(order=True)
→ Enables comparison operators




4. FUNCTION-RELATED IMPORTANT DECORATORS
4.1. @lru_cache
From functools
Used for memoization.
from functools import lru_cache

@lru_cache(maxsize=100)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(50))
Very important in performance optimization.


4.2. @wraps
Used when writing decorators.
Preserves original function metadata.
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
Without @wraps, function name changes to wrapper.


4.3. @total_ordering
From functools
If you define one comparison method, Python generates others.
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks
Now >, >=, <= auto-supported.


5. TYPE HINTING RELATED DECORATORS
5.1.  @overload
From typing
Used for type hinting (not runtime behavior).
from typing import overload

5.2. @overload
def add(x: int, y: int) -> int:
    ...

@overload
def add(x: str, y: str) -> str:
    ...

def add(x, y):
    return x + y
Used in advanced APIs.



6.  CUSTOM DECORATOR PATTERNS 
Parameterized Decorator
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello")



7. Class-Based Decorator
class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Logging...")
        return self.func(*args, **kwargs)


@Logger
def say_hi():
    print("Hi")


Most Important Interview Comparisons
-------------------------------------
Decorator	        Use Case
@staticmethod	    Utility function
@classmethod	    Factory methods
@property	        Encapsulation
@abstractmethod	    Enforcing contract
@dataclass	        Data models
@lru_cache	        Performance optimization
@wraps	            Writing decorators properly
@total_ordering	    Simplify comparisons


Enterprise Use Cases
----------------------------
•	@classmethod →      Factory constructors
•	@property →         Validation in business models
•	@dataclass →         DTO models
•	@lru_cache →         Expensive computation caching
•	@abstractmethod →    Clean architecture enforcement


Advanced Tip
Explain decorators like this:
A decorator is a function that takes another function (or class), extends/modifies its behavior, and returns it.

'''
### DECORATORS IN REAL LIFE
# 1. Definition
# A decorator is a higher-order function that takes another function as an argument, 
# extends or modifies its behavior without explicitly modifying its source code, and returns a new function. Decorators wrap execution logic before and after the target function call.
### 2. Real-Life Use Case
# API call timing, administrative authentication checks, and structured corporate logging across microservices.
### 3. Executable Code

# Example 1
import time
import functools

# Decorator to log function execution time and execution details

def audit_logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG]: Starting execution of '{func.__name__}'...")
        start_time = time.time()
        
        result = func(*args, **kwargs)  # Call original function
        
        elapsed_time = time.time() - start_time
        print(f"[LOG]: Finished '{func.__name__}' in {elapsed_time:.4f} seconds.")
        return result
    return wrapper

# Applying decorator
@audit_logger
def generate_payroll_report(department):
    print(f"Generating comprehensive payroll report for: {department}")
    time.sleep(0.5)  # Simulating heavy database processing
    return f"{department}_Payroll_2026.pdf"

# Execution
report = generate_payroll_report("Engineering")
print(f"Report generated: {report}") 

'''
Outout
----------
[LOG]: Starting execution of 'generate_payroll_report'...
Generating comprehensive payroll report for: Engineering
[LOG]: Finished 'generate_payroll_report' in 0.5008 seconds.
Report generated: Engineering_Payroll_2026.pdf
'''

# Example 2: Production-Style Logging Decorator
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


@log_execution
def calculate_salary(basic, allowance):
    return basic + allowance

result = calculate_salary(50000, 10000)
print("Salary:", result)

#This demonstrates a genuine backend use case: cross-cutting behavior
    # without duplicating code in every function.
  
  #--------------------------------------
  

### Using `*args` and `**kwargs` — Best Practice

def decorator_func(func):

    def wrapper(*args, **kwargs):

        print("Before")

        # Call the original function
        result = func(*args, **kwargs)

        print("After")

        return result

    return wrapper


# Function with positional arguments
@decorator_func
def add(a, b):

    result = a + b

    print("Result:", result)

    return result


# Function with keyword arguments
@decorator_func
def greet(name, message="Welcome"):

    result = f"{message}, {name}!"

    print(result)

    return result


print("Decorator with *args and **kwargs")
print("----------------------------------")


# Function call 1
print("\nCalling add()")
result = add(10, 20)

print("Returned value:", result)


# Function call 2
print("\nCalling greet()")
result = greet(name="Arun", message="Good Morning")

print("Returned value:", result)

# -------------------------------------------


