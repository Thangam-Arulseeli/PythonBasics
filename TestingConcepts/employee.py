# Employee class to represent an employee with a name and salary
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.10

    def is_high_earner(self):
        return self.salary >= 50000
