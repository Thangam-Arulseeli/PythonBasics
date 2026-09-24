employee_name = "Arun"
employee_age = 25
employee_salary = 45000

if employee_age >= 18:
    print("Employee:", employee_name)
    print("Eligible employee")
    
    if employee_salary >= 40000:
        print("Salary category: Standard")
    else:
        print("Salary category: Entry Level")
else:
    print("Not Eligible employee age")