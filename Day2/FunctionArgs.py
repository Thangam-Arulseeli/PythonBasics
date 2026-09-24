# Types of Function Arguments
# -----------------------------
# 1 Positional Arguments -- Arguments are passed in order. 
# NOTE: (Order matters)
def display(name, age):
    print(name, age)

display("Anu", 21) # Output: Anu 21
#-------------------------------

#2. Default Arguments -- A parameter has a default value, used when no argument is passed.
# NOTE Default arguments must come after positional arguments
def greet(name, msg="Good Morning"):
    msg = msg + " "    
    print(msg, name)

greet("Ravi")
greet("Ravi", "Welcome")
#Output
#Good Morning Ravi
#Welcome Ravi
#-----------------------------

# 3. Keyword Arguments -- Arguments are passed using parameter names.
# NOTE: Order does not matter
def student(name, age):
    print(name, age)


student(age=20, name="Meena") # Output: Meena 20
#------------------------------

   
# 4. Keyword-Only Arguments -- Arguments that must be passed using keywords 
# (Defined after *)
def register(name, *, course, fee):
    print(name, course, fee)


register("Arun", course="Python", fee=5000)
# NOTE:  ❌register("Arun", course="Python", 5000) → Error
# --------------------------------------------

# 5. Positional-Only Arguments (Python 3.8+)  -- Arguments that must be passed positionally
# NOTE: (Defined before /)  a and b are before /, so they must be positional only arguments
def calc(a, b, /, c, d):
    print(a + b + c + d)

calc(10, 20, c=30, d=40)
# NOTE: ❌ calc(a=10, b=20, c=30, d=40) → Error
#-----------------------------------------

# 6. Arbitrary Positional Arguments (*args)
# Accepts any number of positional arguments
def total(*nums):
    return sum(nums)

print(total(10, 20, 30))
# Output  -- 60
# ------------------------

# 7. Arbitrary Keyword Arguments (**kwargs)
# Accepts any number of keyword arguments
def profile(**data):
    print(data)

profile(name="Anu", age=21, course="Python")
print("End of Function arguments \n\n")

#Output
#{'name': 'Anu', 'age': 21, 'course': 'Python'}
# ===========================================


####  Function Returns
# Function with a return value
# Function returning multiple values

# A function can calculate something and send the result back to the place where the function was called using the return statement.

# Example
print ("Function Returns")
def add(a, b):
    result = a + b
    return result

answer = add(10, 20)
print("Result:", answer)

# Output:
# Result: 30

# Function Can Return Different Data Types
'''
A function can return:

def get_age():
    return 25

def get_name():
    return "Arun"

def get_numbers():
    return [10, 20, 30]  # List


def get_employee():   # Dictionary
    return {
        "name": "Arun",
        "salary": 50000
    }
'''
# ----------------------------------

##### Function Returning Multiple Values
# ------------------------------------------
# Python allows a function to return multiple values.
# Example:

def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b

    return addition, subtraction, multiplication, division

result = calculate(20, 10)

print(result)

# Output:
# (30, 10, 200, 2.0)

# Although we wrote:   return addition, subtraction, multiplication, division
    ### Python actually returns them as a tuple:   (30, 10, 200, 2.0)
# ===================================


#### Unpacking Multiple Return Values
# --------------------------------------
# Instead of storing everything in one variable:
'''
result = calculate(20, 10)

we can directly unpack the values:

addition, subtraction, multiplication, division = calculate(20, 10)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

'''
#==================================

#8. Returning Multiple Values Using a Tuple

#You can explicitly create a tuple:

def get_employee():
    name = "Arun"
    salary = 50000
    department = "Development"

    return (name, salary, department)


employee = get_employee()

print(employee)

# Output: ('Arun', 50000, 'Development')

# You can unpack it:
print("Unpacked values:")
name, salary, department = get_employee()
print(name)
print(salary)
print(department)
### ================================

# Important: Different Types Can Be Returned
# Python doesn't require all returned values to have the same type.

def employee_details():
    name = "Arun"
    age = 25
    skills = ["Python", "FastAPI", "SQL"]
    active = True

    return name, age, skills, active


name, age, skills, active = employee_details()

print(name)
print(age)
print(skills)
print(active)

# Output:
'''
Arun
25
['Python', 'FastAPI', 'SQL']
True

So a function can return a combination of:

String + Integer + List + Boolean



12. Very Important Difference
Concept	                       print() 	return
Displays result	               ✅	      ❌
Sends result to caller	       ❌	        ✅
Can store result in variable    ❌          ✅
Ends function               	❌	        ✅
Can return multiple values	    ❌	        ✅
'''

# Output {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
# ==========================================

# Order of Arguments (Important Interview Question)
# def func(pos1, pos2, /, default=10, *args, kw1, kw2=20, **kwargs):
#    pass


'''
Order Rule:
1.	Positional-only
2.	Positional / keyword
3.	Default
4.	*args
5.	Keyword-only
6.	**kwargs

  One-Line Interview Answers
•	Default argument: Uses default value if no argument passed
•	Keyword-only: Must be passed with name
•	Positional-only: Cannot use parameter name
•	*args: Variable positional arguments
•	**kwargs: Variable keyword arguments
•	Scope: Determines variable visibility
•	Annotation: Type hinting
•	Module: File containing reusable code

'''

