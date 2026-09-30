### Testing a normal function       # calculator.py
# pytest isn't only for classes. You can also test normal functions.

def add(a, b):
    print(f"Adding {a} and {b}") 
    return a + b

def subtract(a, b):
    print(f"Subtracting {b} from {a}")
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):

    if b == 0:
        raise ValueError("Cannot divide by zero")

    print(f"Dividing {a} by {b}")
    return a / b


