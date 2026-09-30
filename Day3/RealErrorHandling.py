### Real-Life File Processing
import json

try:

    with open("employee.json", "r") as file:
        employee = json.load(file)

    print("Employee:", employee["name"])

except FileNotFoundError:

    print("Employee file not found.")

except json.JSONDecodeError:

    print("Invalid JSON format.")

except KeyError:

    print("Required employee field is missing.")

# NOTE: This is much closer to production-style error handling.
#-----------------------------------------------------------

### Real Corporate Business Validation
class InvalidEmployeeError(Exception):
    pass


def validate_employee(employee):

    if not employee.get("name"):
        raise InvalidEmployeeError(
            "Employee name is required."
        )

    if employee.get("salary", 0) <= 0:
        raise InvalidEmployeeError(
            "Employee salary must be greater than zero."
        )

    return True


employee = {
    "name": "Arun",
    "salary": 85000
}

try:

    validate_employee(employee)

    print("Employee is valid.")

except InvalidEmployeeError as error:

    print("Validation Error:", error)


