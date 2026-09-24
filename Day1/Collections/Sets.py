# ==========================================
# SET - IMPORTANT FUNCTIONS AND METHODS
# ==========================================
'''
 Set: A set is an unordered, mutable collection of unique elements in Python, 
        enclosed in curly braces { }.
'''
python_team = {"Arun", "Priya", "Kumar", "Priya", "Arun"}
fastapi_team = {"Kumar", "Divya", "Ravi"}

print (python_team) # Eliminates the duplicates
print(fastapi_team)
print("Common:", python_team & fastapi_team) # Intersection
print("All:", python_team | fastapi_team)  # Union
print("Only Python:", python_team - fastapi_team)  # Difference
print("symmetric difference:", python_team ^ fastapi_team)  # symmetric difference

#  union() - Combines elements from both sets
print("Union:", python_team.union(fastapi_team))

#  intersection() - Common elements
print("Intersection:", python_team.intersection(fastapi_team))

#  difference() - Elements only in set1
print("Difference:", python_team.difference(fastapi_team))

# symmetric_difference() - Elements not common
print("Symmetric Difference:",
      python_team.symmetric_difference(fastapi_team))

# --------------------------------
# Set Operations
#--------------------------------

# Creating a set
numbers = {10, 20, 30, 40, 50}
print("Original Set:", numbers)

# 1. len() - Returns the number of elements
print("Length:", len(numbers))

# 2. add() - Adds one element
numbers.add(60)
print("After add():", numbers)

# 3. update() - Adds multiple elements
numbers.update([70, 80, 90])
print("After update():", numbers)

# 4. remove() - Removes an element
numbers.remove(20)
print("After remove():", numbers)

# 5. discard() - Removes an element if it exists
numbers.discard(30)
print("After discard():", numbers)

# 6. pop() - Removes and returns a random element
removed = numbers.pop()
print("Popped element:", removed)
print("After pop():", numbers)

# 7. copy() - Creates a copy of the set
copy_set = numbers.copy()
print("Copied Set:", copy_set)
# ----------------------------------------

# ------------------------------------------
# SET RELATIONSHIP METHODS
# ------------------------------------------
set3 = {10, 20}
set4 = {10, 20, 30, 40}

# 12. issubset() - Checks whether one set is inside another
print("Is set3 a subset of set4?",
      set3.issubset(set4))

# 13. issuperset() - Checks whether a set contains another set
print("Is set4 a superset of set3?",
      set4.issuperset(set3))

# 14. isdisjoint() - Checks whether two sets have no common elements
set5 = {100, 200}

print("Are set3 and set5 disjoint?",
      set3.isdisjoint(set5))

# ------------------------------------------
# BUILT-IN FUNCTIONS
# ------------------------------------------

numbers2 = {10, 20, 30, 40, 50}

# 15. max() - Largest value
print("Maximum:", max(numbers2))

# 16. min() - Smallest value
print("Minimum:", min(numbers2))

# 17. sum() - Total of all values
print("Sum:", sum(numbers2))

# 18. sorted() - Returns a sorted list
print("Sorted:", sorted(numbers2))

# 19. Membership operator
print("Is 30 present?", 30 in numbers2)
print("Is 100 not present?", 100 not in numbers2)
# -------------------------------------------------

