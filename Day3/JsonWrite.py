import json

employee = {
    "id": 1001,
    "name": "Arun Kumar",
    "department": "Development",
    "salary": 85000,
    "skills": ["Python", "FastAPI", "SQL", "SqlAlChemy"]
}

with open("employee.json", "w") as file:

    json.dump(employee, file, indent=4)
