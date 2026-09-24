# ==========================================
# DICTIONARY - IMPORTANT FUNCTIONS & METHODS
# ==========================================
'''
Dictionary: A dictionary is a mutable collection of key-value pairs in Python,
                 where each key is unique and used to access its corresponding value.
'''
employee = {
    "id": 1001,
    "name": "Arun",
    "department": "IT",
    "salary": 65000,
    "skills": ["Python", "SQL", "FastAPI"]
}
print("Original Dictionary:", employee)

# Add / Update Dictionary Values
employee["email"] = "arun@example.com"
employee["salary"] = 70000

# -----------------------
# Access data from dictionary
print(employee["name"])
print(employee["salary"])

# Safe Dictionary Access
# ----------------------------
#print(employee["phone"]) # This can cause KeyError

### Instead we can use
print(employee.get("phone"))  # OR  --- To access safe access
print(employee.get("phone", "Phone number not available")) # More safely with error message
# ---------------------------------

# Dictionary Iteration
for key, value in employee.items():
    print(key, ":", value)

# Keys
for key in employee.keys():
    print(key)

# Values
for value in employee.values():
    print(value)

#-----------------------------
### Nested Dictionary -- This is particularly important because API/JSON data frequently looks like this.
employees = {
    1001: {
        "name": "Arun",
        "department": "IT",
        "skills": ["Python", "FastAPI"]
    },

    1002: {
        "name": "Priya",
        "department": "HR",
        "skills": ["Recruitment", "Excel"]
    }
}
# Access
print("Nested Dictionary")
print(employees[1001]["name"])
print(employees[1001]["skills"][0])
#---------------------------

### List of Dictionaries — VERY IMPORTANT --- This structure is extremely common in backend development.
employees = [
    {
        "id": 1001,
        "name": "Arun",
        "department": "IT",
        "salary": 65000
    },

    {
        "id": 1002,
        "name": "Priya",
        "department": "HR",
        "salary": 55000
    },

    {
        "id": 1003,
        "name": "Kumar",
        "department": "IT",
        "salary": 75000
    }
]
# Process data
for employee in employees:

    print(
        employee["id"],
        employee["name"],
        employee["department"],
        employee["salary"]
    )
# NOTE: This structure will later resemble API response data.

# ------------------------------------------

'''
Collection comparison
-----------------------
Feature	        List	Tuple	Set	                        Dictionary
Ordered	         Yes	Yes	    No traditional index order	Yes
Mutable	         Yes	No	    Yes	                        Yes
Duplicates	    Yes	    Yes	    No	                        Keys: No
Indexing	    Yes	    Yes	    No	                        By key
Data structure	Values	Values	Unique values	            Key + Value
Common use	Dynamic data	Fixed data	Unique data	        Structured data

'''




