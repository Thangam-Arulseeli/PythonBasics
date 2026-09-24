#### ARITHMETIC OPERATOR
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

add = a + b
sub = a - b
mul = a * b
div = a / b   # Normal division # 10/3
floordiv =  a // b  # Floor Division [ Example: 10/3 = 3 and -10/3 = -4 ] 
mod =  a % b   # Remainder 
exp =  a ** b  # Exponents - Power 

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
print("Floor Division:",  floordiv)
print("Remainder:", mod)
print("Power:", exp)

print("Hello " * 3)  # Print string for 3 times

'''
Unary + and unary -
Arithmetic Assignment Operators (Shorthand Assignment Operator)
-----------------------------------------------------------------

Operator	Meaning	        Example
=	        Assignment	    x = 10
+=	        Add and assign	x += 5
-=	    Subtract and assign	x -= 5
*=	    Multiply and assign	x *= 5
/=	    Divide and assign	x /= 5
//=	    Floor divide and assign	x //= 5
%=	    Modulus and assign	x %= 5
**=	    Power and assign	x **= 2

'''
#--------------------------------------------------------------
# Relational Operators -- >, <, >=, <=, ==, !=
# Logical Operators -- and, or, not

age = 35
experience = 6

if age >= 30 and experience > 5:
    print("Eligible")
# ----------------------------------------------------

'''
Bitwise Operators in Python
Operator	Name	Example	Result
&	Bitwise AND	    5 & 3	1
`	`	Bitwise OR	`5
^	Bitwise XOR	    5 ^ 3	6
~	Bitwise NOT 	~5	-6
<<	Left Shift	    5 << 1	10
>>	Right Shift	    5 >> 1	2
'''

# Membership Operators -- This becomes very useful with collections. 
skills = ["Python", "SQL", "FastAPI"]

print("Python" in skills) # True
print("Java" in skills)  # False
print("Java" not in skills) # True

# ------------------------------------------------

# Comparison between == and is operators
# -------------------------------------------
    # == is called the equality operator -- "Do these two objects have the same value?"
    # is → compares object identity -- "Are these two variables referring to the exact same object in memory?"
    # None is a special singleton object in Python. There is only one None object, so checking:

a = [10, 20, 30]
b = [10, 20, 30]

print(a == b)  # True
print(a is b)  # False

# -------------------

a = [10, 20, 30]
b = a

print(a == b)   # True
print(a is b)   # True

#--------------------------------------

### Important Note --- No Conditional operators like C/C++, 
# Python uses a conditional expression, commonly called the ternary operator

'''
So a == b is value equality
   a is b is object identity
   == compares whether two objects have equal values, whereas is checks whether two references point to the same object.

   if value is None: --- This should be used in your Python code
Example
--------
student = None

if student is None:
    print("Student was not found")
'''

#Ex 1
age = 25
status = "Adult" if age >= 18 else "Minor"
print(status) # Adult

'''
Equivalent to ordinary if else statement
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
'''
# Ex 2
employee_name = "Arun"
performance_score = 82
performance = "Excellent" if performance_score >= 80 else "Needs Improvement"

print(employee_name)  # Arun
print(performance)  # Excellent

# Ex 3
def get_result(mark):
    return "Pass" if mark >= 40 else "Fail"

print(get_result(75))  # Pass
print(get_result(32))  # Fail



