# ==========================================
# TUPLE - IMPORTANT FUNCTIONS AND METHODS
# ==========================================
'''
TUPLE: Tuple: A tuple is an ordered and immutable collection of elements in Python,
         enclosed in parentheses (), and it allows duplicates.
'''
# Employee coordinates example
employee_location = (11.0168, 76.9558)

latitude = employee_location[0]
longitude = employee_location[1]

print("Latitude:", latitude)
print("Longitude:", longitude)
# ------------------------------------


# Tuple unpacking
employee = (1001, "Arun", "IT")

employee_id, name, department = employee

print(employee_id)
print(name)
print(department)

# Exceptional Case -- (because tuples are immutable.)
# employee[0] = 2000 # Raises TypeError
 
# --------------------------------

# Creating a tuple
numbers = (10, 20, 30, 20, 40, 50)

print("Original Tuple:", numbers)

# 1. len() - Returns the number of elements
print("Length:", len(numbers))

# 2. count() - Counts how many times a value occurs
print("Count of 20:", numbers.count(20))

# 3. index() - Returns the index of the first occurrence
print("Index of 30:", numbers.index(30))

# 4. max() - Returns the largest value
print("Maximum:", max(numbers))

# 5. min() - Returns the smallest value
print("Minimum:", min(numbers))

# 6. sum() - Returns the total of all values
print("Sum:", sum(numbers))

# 7. sorted() - Returns a sorted LIST
print("Sorted:", sorted(numbers))
# 8. reversed() - Returns elements in reverse order
print("Reversed:", tuple(reversed(numbers)))

# 9. Membership operator - 'in'
print("Is 30 present?", 30 in numbers)

# 10. Membership operator - 'not in'
print("Is 100 not present?", 100 not in numbers)

# 11. Concatenation - Joining two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print("Concatenated Tuple:", result)

# 12. Repetition - Repeating a tuple
repeated = (1, 2) * 3

print("Repeated Tuple:", repeated)

# 13. Slicing - Getting a part of the tuple
print("First 3 elements:", numbers[:3])
print("Last 3 elements:", numbers[-3:])
print("Reversed using slicing:", numbers[::-1])

'''

Expected Output
-----------------
Original Tuple: (10, 20, 30, 20, 40, 50)
Length: 6
Count of 20: 2
Index of 30: 2
Maximum: 50
Minimum: 10
Sum: 170
Sorted: [10, 20, 20, 30, 40, 50]
Reversed: (50, 40, 20, 30, 20, 10)
Is 30 present? True
Is 100 not present? True
Concatenated Tuple: (1, 2, 3, 4, 5, 6)
Repeated Tuple: (1, 2, 1, 2, 1, 2)
First 3 elements: (10, 20, 30)
Last 3 elements: (20, 40, 50)
Reversed using slicing: (50, 40, 20, 30, 20, 10)
# ----------------------------------------------------
'''


