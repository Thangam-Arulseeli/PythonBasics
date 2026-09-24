# Variable Scope in Functions
# ---------------------------
# 1. Local Scope
def show():
    x = 10    # Local variable
    print(x)

# print (x) # NameError: name x is not defined

show()
# ✔️ x exists only inside function

# ---------------------------------

# 2. Global Scope
#--------------------
x = 20    # Global variable 

def show():
    print ("Global variable inside function = ", x)   ### Reading a global variable does not require 'global' keyword  
   #  Access golbal variable inside function

show()
print ("Global variable outside function = ", x)
#-------------------------------------------------

# 3. global Keyword, uses global scope
# -------------------
x = 10

def update(): ## 
    global x  # global keyword is used inside the function, Don't create a local x, which uses to update global variable
    x = 50  # value updated inside the function

update()
print(x) 

#Output -- 50
# --------------------

# 4. nonlocal Keyword
#--------------------
def outer():
    x = 10
    def inner():
        nonlocal x  # Referring x=10 
        x = 20      # Changing the value
        print ("x inside function = ", x)

    inner()

    print("x outside the function =  ", x)   # 20

outer()
# Output # 20

'''
What is the difference between global and nonlocal ?
-----------------------------------------------------
The main difference is which scope Python should look outside the current function for.

global → refers to a variable in the global/module scope
nonlocal → refers to a variable in an enclosing (outer) function's scope

The easiest way to understand nonlocal is with nested functions.
'''
# ================================

# Function Annotations    -- Used to describe parameter and return types
# -----------------------

def add(a: int, b: int) -> int:
    return a + b

print(add.__annotations__)
# Type annotations are not enforced automatically at runtime.
# They provide type information for developers, IDEs, type checkers, and frameworks.

### REcursion --- Example
## Factorial 

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print("Factorial:", factorial(5))

# -----------------------------------
