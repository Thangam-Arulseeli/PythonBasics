# Types of Errors in Python:
# 1. Syntax Errors: These occur when the code violates the rules of the Python language
# 2. Runtime Errors: These occur during the execution of the program and can be caused by various factors, such as invalid input or division by zero.
# 3. Logical Errors: These occur when the code runs without any syntax or runtime errors, but the output is not what was expected due to a mistake in the logic of the program.

#------------------------------


def add(a, b):
    print(f"Adding {a} and {b}") 
    return a + b


def divide(a, b):

    # if b == 0:
    #     raise ValueError("Cannot divide by zero")

    print(f"Dividing {a} by {b}")
    return a / b

a = 10
b = 20
c = add(a, b)
print(f"Result of addition: {c}")

d = divide(a, b)
print(f"Result of division: {d}")

#### Stack Trace through function calls --- in Python, when a function calls another function, 
# it creates a stack trace. The stack trace shows the sequence of function calls 
# that led to the current point in the program. 
#Each time a function is called, a new frame is added to the call stack.
# When a function returns, its frame is removed from the stack.

def func1():
    print("Function 1")
    func2()

def func2():
    print("Function 2")
    func3()

def func3():
    print("Function 3")
    func4()

def func4():
    try: 
        print("Function 4")
        print(10/0)  # This will raise a ZeroDivisionError
        # Uncomment the next line to raise an exception and see the stack trace
        # raise Exception("An error occurred in func4")
    except Exception as e:
        print(f"Exception caught in func4: {e}")
        # Print the stack trace
        import traceback
        traceback.print_exc()   
    print("Function 4")

# For demonstration, we can call func1() to see the stack trace in action.
func1()   
# -----------------------------
'''
# Printing the stack trace using the traceback module
import traceback
try:
    func1()
except Exception as e:
    traceback.print_exc()   
'''
