'''
Error Handling 
	Syntax error → Program does not run
	Logical error → Program runs but gives wrong output
	Runtime error → Program crashes

Where is Exception Handling Used?
Exception handling is used in situations where errors may occur at runtime, such as:
Common Use Cases
•	User input validation
•	File handling
•	Database operations
•	Network communication
•	Mathematical calculations
•	API calls
•	Large applications where program crash must be avoided

Real-World Example
•	ATM transactions
•	Online forms
•	Banking software
•	Web applications
•	Data processing systems

Why Exception Handling is Important?
Without exception handling:
•	Program crashes
•	User sees error messages
•	Data may be lost

With exception handling:
✔ Program continues
✔ Graceful error handling
✔ User-friendly messages
✔ Prevents program termination
✔ Improves program reliability
✔ Handles unexpected user input
✔ Helps debugging
✔ Ensures resource cleanup

Complete Syntax 
---------------
try:
    # risky code
except ExceptionType1:
    # handling block
except ExceptionType2:
    # handling block
else:
    # executes if no exception occurs
finally:
    # executes always
'''

### Simple Example
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    print(a / b)
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Please enter valid integers")
# ----------------

### Multiple Exception Handling
try:
    x = int("abc")
except (ValueError, TypeError):
    print("Conversion error occurred")
### -----------------------------------------

### Generic Exception Handling
try:
    print(a)
except Exception as e:
    print("Error occurred:", e)
# Used when exception type is unknown, it must be placed at the last after the known exceptions


### else Block
### Executes only if no exception occurs.
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", num)


### finally Block
### Executes regardless of exception occurrence.
try:
    file = open("sample.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("File operation completed")
# Used for cleanup activities (closing files, DB connections, release memory)


### Raising an Exception (raise)
# Used to explicitly raise exceptions.
age = int(input("Enter age: "))
if age < 18:
    raise ValueError("Age must be 18 or above")
'''

Common Built-in Exceptions
---------------------------------
Exception	            Reason
ZeroDivisionError	Divide by zero
ValueError	        Invalid value
TypeError	        Wrong data type
IndexError       	Index out of range
KeyError	        Missing dictionary key
FileNotFoundError	File missing
# ---------------------------------------
'''

### Custom Exception (Advanced)
'''
Sometimes Python's built-in exceptions don't clearly represent our business rule.
Example:
Employee salary cannot be negative.

### EXample - 1:

class InvalidAgeError(Exception):
    pass

age = int(input("Enter age: "))
if age < 18:
    raise InvalidAgeError("Invalid age entered")

### EXample -  2:
class NegativeNumberError(Exception):
    pass

num = int(input("Enter number: "))
if num < 0:
    raise NegativeNumberError("Negative number not allowed")

### Example - 3
class InvalidSalaryError(Exception):
    pass

def validate_salary(salary):

    if salary < 0:
        raise InvalidSalaryError(
            "Salary cannot be negative."
        )

    return True
# -----------------------------------
'''
