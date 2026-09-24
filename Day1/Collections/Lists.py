# Collections -- List
# --------------------
''' 
 List: A list is an ordered, mutable collection of elements in Python 
        that can store multiple values (duplicate values) of different data types.  [ ]
''' 
employees = [
    "Arun",
    "Priya",
    "Kumar",
    "Divya",
    "Priya"
]

print("Employees:", employees)
print("First Employee:", employees[0])
print("Last Employee:", employees[-1])

employees.append("Ravi")

employees.insert(1, "Meena")

employees.insert(1, "Meena")

removed_employee = employees.pop()

print("Removed:", removed_employee)

removed_employee = employees.pop()

print("Removed:", removed_employee)

# Search data in the List
if "Kumar" in employees:
    print("Employee exists")

employees.sort()
print(employees)


# List Slicing -- Important because slicing will later appear in string processing and other Python operations.
employees = [
    "Arun",
    "Priya",
    "Kumar",
    "Divya",
    "Ravi"
]
print("List Slicing")
print(employees[0:3])
print(employees[:3])
print(employees[2:])
print(employees[::-2]) # list[start : stop : step] 
# Start from the end of the list and move backwards by 2 positions at a time.
# Output ['Ravi', 'Kumar', 'Arun']

# employees[1:5:2] means Start at index 1, stop before index 5, move forward by 2.

# List Comprehension
# --------------------

'''
List comprehension is a shorter, cleaner way to create a new list out of an existing list (or any collection),
 in just a single line of code. Think of it as a shorthand way of writing a for loop.
'''
print("List Comprehension")
numbers = [10, 20, 30, 40, 50]
squares = [number ** 2 for number in numbers]
doubled = [num * 2 for num in numbers]
print(doubled)
print(squares)
#----------------------------------

# Adding a Filter (if condition)
#--------------------------------
# You can also filter items so that only certain elements make it into your new list.
# You simply drop an if statement at the very end 

# Example: Grab only the even numbers from a list.

# Read it as: keep "number" for every "number" in "numbers" ONLY IF "number" is even
even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers) # Output: [20, 40]
# ----------------------------------------------

# Built-in functions used with Lists
numbers = [10, 50, 20, 40, 30]

print ("Original List: ", numbers)
print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))
print("Reversed:", list(reversed(numbers)))

# --------------------------------------

numbers = [10, 50, 20, 40, 30]
print ("------ List Functions -----------------")
print("Original List:", numbers)

# append()
numbers.append(60)
print("After append:", numbers)

# extend()
numbers.extend([70, 80])
print("After extend:", numbers)

# insert()
numbers.insert(2, 25)
print("After insert:", numbers)

# remove()
numbers.remove(25)
print("After remove:", numbers)

# pop()
numbers.pop()
print("After pop:", numbers)

# index()
print("Index of 30:", numbers.index(30))

# count()
numbers.append(30)
print("Count of 30:", numbers.count(30))

# sort()
numbers.sort()
print("After sort:", numbers)

# reverse()
numbers.reverse()
print("After reverse:", numbers)

# copy()
new_numbers = numbers.copy()
print("Copied List:", new_numbers)

# clear()
new_numbers.clear()
print("After clear:", new_numbers)
# ------------------------------------------------


