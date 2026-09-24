# Looping Structure
''' 
1. for Loop
2. while loop

Note: No do...while loop
#### Equivalent of do...while in Python
while True:
    # Execute the code first

    if condition_is_false:
        break
Example:
Menu Driven Program based on user input using  "while True"

'''
for i in range(5):
    print(i)

for i in range(1, 10): 
    print(i)  


for i in range(10, 0, -2): 
    print(i)



# Model 1 - For Loop in a range with break
print("# Model 1 - For Loop in a range with break")
for i in range(1, 10):
    if i == 5:
        break
    print(i)
print("\n\n")
# --------------------------------------

# Model 2 - For Loop in a range with continue
print("# Model 2 - For Loop in a range with continue")
for i in range(1, 10):  # 10 exclusive
    if i >= 3 and i<=7 :
        continue
    print(i)
print("\n\n")
# -------------------------------------

# Model 3 -- Pass statement - Used as a placeholder where a statement is syntactically   
print("# Model 3 - Pass statement - used as a placeholder where a statement is syntactically required  Loop in a range with break") 
for i in range(5): # pass does absolutely nothing. It is mainly used as a placeholder when Python requires a statement, but you don't want to perform any action yet
    if i == 3:
        pass # Used as a placeholder where a statement is syntatically required
    print(i) # So in my particular program, pass has no effect on the loop output. The numbers 0, 1, 2, 3, 4 are all printed.
print("\n\n")
# ----------------------------------------

# Model 4 - Nested for loop
print ("Model 4 -- Nested For Loop with print() end="" as second argumnet ")
for i in range(1, 5): # 5 exclusive 
    for j in range(1, 4):  # 4 exclusive
        print(j, end=" ") # 1 2 3  --- Stay on the same line by adding space  
    print()
print("\n\n")
# ---------------------------------------

# Model 5 - * Pattern
print("Model 5 -- Nested For loop with print() end="" as second argument ") 
for i in range(1, 5):
    for j in range(i):
        print("*", end="") # Stay on the same line without adding anything #### print (j, end="\n") -- Go to next line after printing j
    print()
print("\n\n")
# --------------------------------------

# Model 6 - Multiplication table
print("Mode 6 -- Multiplication table with formatted string output")
for i in range(1, 4):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}") # Formatted print statement
    print()
print("\n\n")
# -------------------------------------

# Model 7 - For Loop with collections
employees = ["Arun", "Priya", "Kumar", "Divya"]

for employee in employees:
    print("Employee:", employee)
#---------------------------------------

# Nested Loop -- 
# NOTE Useful for report-style processing: This is much more meaningful than simply printing numbers using nested loops.

departments = {
    "IT": ["Arun", "Kumar"],
    "HR": ["Priya", "Divya"],
    "Finance": ["Ravi", "Meena"]
}

for department, employees in departments.items():

    print("\nDepartment:", department)

    for employee in employees:
        print("  Employee:", employee)

# ----------------------------------------------

# While loop (Practical application - Login Attempt for 3 times )
# ------------
attempts = 0
max_attempts = 3

while attempts < max_attempts:

    password = input("Enter password: ")

    if password == "Admin@123":
        print("Login successful")
        break

    attempts += 1
    print("Invalid password")

if attempts == max_attempts:
    print("Account temporarily locked")
# ---------------------------------------

# Practical Application for break/contiue/pass
#---------------------------------------------

# break
employees = ["Arun", "Priya", "Kumar", "Admin"]

for employee in employees:

    if employee == "Admin":
        print("Admin account found")
        break

    print("Checking:", employee)
# ----------------------------------

# continue
employees = [
    {"name": "Arun", "active": True},
    {"name": "Priya", "active": False},
    {"name": "Kumar", "active": True},
    {"name": "Divya", "active": False}
]

for employee in employees:

    if not employee["active"]:
        continue

    print("Active employee:", employee["name"])
# ------------------------------------------

# pass -- pass is a placeholder
employees = []

if not employees:
    pass

# -------------
def generate_monthly_report():
    pass
    
# It allows us to create the structure first and implement it later.
# ---------------------------------



