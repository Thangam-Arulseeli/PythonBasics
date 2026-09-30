from salary import calculate_annual_salary
from salary import calculate_bonus

monthly_salary = 50000

annual_salary = calculate_annual_salary(
    monthly_salary
)

bonus = calculate_bonus(
    annual_salary,
    10
)

print("Annual Salary:", annual_salary)
print("Bonus:", bonus)

