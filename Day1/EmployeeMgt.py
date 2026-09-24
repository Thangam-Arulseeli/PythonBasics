employees = []

while True:

    print("\n========== EMPLOYEE MANAGEMENT ==========")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. View Department Employees")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Please enter a valid numeric choice.")
        continue

    match choice:

        case 1:

            print("\n--- Add Employee ---")

            employee_id = int(input("Enter Employee ID: "))
            name = input("Enter Employee Name: ")
            department = input("Enter Department: ")
            salary = float(input("Enter Salary: "))

            employee = {
                "id": employee_id,
                "name": name,
                "department": department,
                "salary": salary
            }

            employees.append(employee)

            print("Employee added successfully.")

        case 2:

            print("\n--- Employee List ---")

            if not employees:
                print("No employees available.")

            else:

                for employee in employees:

                    print(
                        f"ID: {employee['id']} | "
                        f"Name: {employee['name']} | "
                        f"Department: {employee['department']} | "
                        f"Salary: {employee['salary']}"
                    )

        case 3:

            print("\n--- Search Employee ---")

            employee_id = int(input("Enter Employee ID: "))

            found = False

            for employee in employees:

                if employee["id"] == employee_id:

                    print("Employee Found")
                    print("Name:", employee["name"])
                    print("Department:", employee["department"])
                    print("Salary:", employee["salary"])

                    found = True
                    break

            if not found:
                print("Employee not found.")

        case 4:

            print("\n--- Update Salary ---")

            employee_id = int(input("Enter Employee ID: "))

            found = False

            for employee in employees:

                if employee["id"] == employee_id:

                    new_salary = float(
                        input("Enter New Salary: ")
                    )

                    employee["salary"] = new_salary

                    print("Salary updated successfully.")

                    found = True
                    break

            if not found:
                print("Employee not found.")

        case 5:

            print("\n--- Delete Employee ---")

            employee_id = int(input("Enter Employee ID: "))

            found = False

            for index, employee in enumerate(employees):

                if employee["id"] == employee_id:

                    employees.pop(index)

                    print("Employee deleted successfully.")

                    found = True
                    break

            if not found:
                print("Employee not found.")

        case 6:

            department = input(
                "Enter department to search: "
            )

            department_employees = [
                employee
                for employee in employees
                if employee["department"].lower()
                == department.lower()
            ]

            if department_employees:

                print(
                    f"\nEmployees in {department}:"
                )

                for employee in department_employees:

                    print(
                        employee["id"],
                        employee["name"],
                        employee["salary"]
                    )

            else:

                print(
                    "No employees found in this department."
                )

        case 7:

            print("Thank you. Application closed.")
            break

        case _:

            print("Invalid choice.")
