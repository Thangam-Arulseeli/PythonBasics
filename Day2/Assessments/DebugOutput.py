# 1. Positional Arguments
def add(a, b):
    print(a + b)

add(10, 20)
# Output :
#-----------------------------

# 2.
def display(name, age):
    print(name, age)

display(21, "Anu") → Wrong meaning



🔹 2. Default Arguments
Definition
A parameter that has a predefined value.
Used when the caller does not pass that argument.

Rule : ✔️ Default arguments must come after positional arguments

Example 1 – Basic Default Argument
def greet(name, msg="Good Morning"):
    print(msg, name)

greet("Ravi")
greet("Ravi", "Welcome")
Output
Good Morning Ravi
Welcome Ravi



Example 2 – Multiple Default Arguments
def salary(basic, hra=2000, da=1500):
    return basic + hra + da

print(salary(20000))
print(salary(20000, 3000))
Output
23500
24500


❌ Invalid Example
def test(a=10, b):
    pass
❌ Syntax Error
(Default argument before non-default)

Note: Default arguments reduce repetitive code and improve readability.


🔹 3. Keyword Arguments
Definition
Arguments passed using parameter names.
Advantage
✔️ Order does not matter
✔️ Improves readability
Example 1 – Basic Keyword Argument
def student(name, age):
    print(name, age)

student(age=20, name="Meena")
Output
Meena 20


Example 2 – Mix of Positional + Keyword
def course(name, duration, fee):
    print(name, duration, fee)

course("Python", fee=5000, duration="2 Months")
✔️ Valid
❌ course(name="Python", "2 Months", 5000) → Error

Rule : ✔️ Positional arguments must come before keyword arguments


🔹 4. Combined Example (Very Important)
def employee(name, dept="IT", salary=30000):
    print(name, dept, salary)

employee("Ravi")
employee("Ravi", salary=40000)
employee(name="Ravi", dept="HR")
Output
Ravi IT 30000
Ravi IT 40000
Ravi HR 30000

🔹 5. Comparison Table (Exam-Ready)
Feature	Positional	Default	Keyword
Order matters	✅ Yes	❌ No	❌ No
Has predefined value	❌ No	✅ Yes	❌ No
Improves readability	❌ No	⚠️ Moderate	✅ High
Can skip arguments	❌ No	✅ Yes	✅ Yes
Common use	Simple calls	Optional values	Clear calls

🔹 6. Real-Time Use Case Example
def book_ticket(name, source, destination="Chennai"):
    print(name, source, destination)

book_ticket("Arun", "Coimbatore")
book_ticket("Arun", source="Madurai", destination="Bangalore")

🔹 7. One-Line Interview Answers
•	Positional argument: Passed based on position
•	Default argument: Uses predefined value if not passed
•	Keyword argument: Passed using parameter name
•	Rule: Positional → Default → Keyword
 
🔹 1. Positional-Only Arguments
✅ Definition
Positional-only arguments are parameters that must be passed by position and cannot be passed using parameter names.
They are defined using / in the function definition
(Python 3.8+).

🔹 Syntax
def function_name(pos1, pos2, /):
    statements
/ means:
👉 All parameters before this must be positional-only

🔹 Example 1 – Basic Positional-Only
def add(a, b, /):
    return a + b

print(add(10, 20))
Output
30

❌ Invalid Usage
add(a=10, b=20)
❌ TypeError
add() got some positional-only arguments passed as keyword arguments


🔹 Example 2 – Mixing Positional-Only & Normal Arguments
def calculate(a, b, /, c):
    print(a, b, c)

calculate(10, 20, 30)
calculate(10, 20, c=40)
✔️ Valid

🔹 Real-Time Use Case
Built-in functions use positional-only arguments:
len(obj)
❌ len(obj=mylist) → Not allowed

🔹 Note : Positional-only arguments prevent misuse of internal parameter names and improve API safety.

🔹 2. Keyword-Only Arguments
✅ Definition
Keyword-only arguments are parameters that must be passed using their names.
They are defined after * in function definition.

🔹 Syntax
def function_name(positional, *, keyword1, keyword2):
    statements
* means:
👉 All parameters after this must be keyword-only

🔹 Example 1 – Basic Keyword-Only
def register(name, *, course, fee):
    print(name, course, fee)

register("Anu", course="Python", fee=5000)


❌ Invalid Usage
register("Anu", "Python", 5000)
❌ TypeError

🔹 Example 2 – Keyword-Only with Default Values
def book_ticket(name, *, source="Chennai", destination):
    print(name, source, destination)

book_ticket("Ravi", destination="Bangalore")
✔️ Valid

🔹 Real-Time Use Case
def send_email(to, *, cc=None, bcc=None):
    print("To:", to)
    print("CC:", cc)
    print("BCC:", bcc)

send_email("abc@gmail.com", cc="hr@gmail.com")
✔️ Clear and safe API design

🔹 Note: Keyword-only arguments improve readability and avoid confusion in function calls.

🔹 3. Combining Positional-Only & Keyword-Only
def order(product, qty, /, *, discount=0):
    total = qty * 100 - discount
    print(product, total)

order("Pen", 10, discount=50)
✔️ Positional-only → product, qty
✔️ Keyword-only → discount

❌ Invalid Calls
order(product="Pen", qty=10, discount=50)
order("Pen", 10, 50)

🔹 4. Full Argument Order (Very Important 🔥)
def func(pos1, pos2, /, normal, default=10, *args, kw1, kw2=20, **kwargs):
    pass
Order Rule:
1️. Positional-only
2️. Positional / keyword
3️. Default
4️. *args
5️. Keyword-only
6️. **kwargs

🔹 5. Comparison Table (Exam-Ready)
Feature	Positional-Only	Keyword-Only
Defined using	/	*
Passed by position	✅ Yes	❌ No
Passed by name	❌ No	✅ Yes
Improves API safety	✅ Yes	⚠️ Moderate
Improves readability	❌ No	✅ Yes
Used in built-ins	✅ Yes	⚠️ Limited

🔹 6. One-Line Interview Answers
•	Positional-only arguments: Must be passed without parameter names
•	Keyword-only arguments: Must be passed using parameter names
•	/ → positional-only separator
•	* → keyword-only separator

🔹 7. Common Interview Trap Question
def test(a, b, /, c, *, d):
    print(a, b, c, d)
✔️ Valid call:
test(1, 2, 3, d=4)
❌ Invalid calls:
test(a=1, b=2, c=3, d=4)
test(1, 2, 3, 4)


🔹 1. What is *args?
✅ Definition
*args allows a function to accept any number of positional arguments.
•	Internally, arguments are stored as a tuple
•	The name args is a convention (you can use any name)

🔹 Syntax
def function_name(*args):
    statements



🔹 Example 1 – Basic *args
def add(*numbers):
    print(numbers)
    print(sum(numbers))

add(10, 20, 30)
Output
(10, 20, 30)
60

🔹 Example 2 – Looping through *args
def display(*values):
    for v in values:
        print(v)

display("Python", 10, 5.5, True)


🔹 Example 3 – Fixed + Variable Arguments
def bill(customer, *prices):
    print("Customer:", customer)
    print("Total:", sum(prices))

bill("Ravi", 200, 350, 450)

🔹 Note: Use *args when the number of inputs is unknown.

🔹 2. What is **kwargs?
✅ Definition
**kwargs allows a function to accept any number of keyword arguments.
•	Stored internally as a dictionary
•	Name kwargs is a convention

🔹 Syntax
def function_name(**kwargs):
    statements

🔹 Example 1 – Basic **kwargs
def profile(**data):
    print(data)

profile(name="Anu", age=21, course="Python")
Output
{'name': 'Anu', 'age': 21, 'course': 'Python'}


🔹 Example 2 – Iterating **kwargs
def employee(**info):
    for key, value in info.items():
        print(key, ":", value)

employee(name="Ravi", dept="IT", salary=35000)


🔹 Example 3 – Conditional Access
def settings(**options):
    if "theme" in options:
        print("Theme:", options["theme"])
    else:
        print("Default Theme")

settings(theme="Dark")
settings()


🔹 Note :Use **kwargs when named parameters may vary.


🔹 3. Using *args and `**kwargs Together
def order(customer, *items, **details):
    print("Customer:", customer)
    print("Items:", items)
    print("Details:", details)

order("Arun", "Pen", "Book", payment="Card", discount=50)


🔹 4. Argument Order Rule (Very Important 🔥)
def func(positional, default=10, *args, kw1, kw2=20, **kwargs):
    pass

Correct Order:
1️. Positional arguments
2️. Default arguments
3️. *args
4️. Keyword-only arguments
5️. **kwargs

🔹 5. Packing vs Unpacking
📦 Packing
def demo(*args):
    print(args)

demo(1, 2, 3)
➡Packs values into a tuple

📤 Unpacking List/Tuple
nums = [10, 20, 30]
print(*nums)


📤 Unpacking Dictionary
data = {"a": 10, "b": 20}

def add(a, b):
    print(a + b)

add(**data)


🔹 6. Common Errors (Interview Traps)
❌ Wrong Order
def test(*args, a):
    pass
✔️ Correct:
def test(*args, a):
    pass  # a becomes keyword-only


❌ Passing Positional After Keyword
add(a=10, 20)
❌ SyntaxError



🔹 7. Real-Time Use Case Examples
🔸 Logging Function
def log(message, **meta):
    print("Message:", message)
    for k, v in meta.items():
        print(k, ":", v)

log("Login Success", user="admin", time="10:30 AM")


🔸 Flexible API Function
def send_email(to, *attachments, **options):
    print("To:", to)
    print("Attachments:", attachments)
    print("Options:", options)

send_email("abc@gmail.com", "file1.pdf", cc="hr@gmail.com")


🔹 8. Comparison Table (Exam-Ready)
Feature	*args	**kwargs
Accepts	Positional arguments	Keyword arguments
Stored as	Tuple	Dictionary
Order matters	✅ Yes	❌ No
Name matters	❌ No	❌ No
Use case	Variable inputs	Flexible named options


🔹 9. One-Line Interview Answers
•	*args → Variable number of positional arguments
•	**kwargs → Variable number of keyword arguments
•	Tuple → *args
•	Dictionary → **kwargs
•	Used for flexible function APIs



FUNCTION-BASED LAB PROGRAMS (COMPLEX)
1.	Student Result Management System
def calculate_total(*marks):
    return sum(marks)

def calculate_grade(total):
    if total >= 450:
        return "A"
    elif total >= 350:
        return "B"
    else:
        return "C"

def student_result(name, roll_no, *marks):
    total = calculate_total(*marks)
    grade = calculate_grade(total)
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Total:", total)
    print("Grade:", grade)

student_result("Anu", 101, 90, 85, 88, 92, 95)
Output
Name: Anu
Roll No: 101
Total: 450
Grade: A


2️. Banking System (Deposit / Withdraw / Balance)
balance = 5000

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
    else:
        print("Insufficient Balance")

def show_balance():
    print("Balance:", balance)

deposit(2000)
withdraw(1500)
show_balance()
Output
Balance: 5500


3️. Login Authentication System
def authenticate(username, password, *, admin=False):
    if admin and username == "admin" and password == "1234":
        return "Admin Login Success"
    elif not admin and password == "user123":
        return "User Login Success"
    return "Login Failed"

print(authenticate("admin", "1234", admin=True))
Output
Admin Login Success


4️. Payroll System (Default + Keyword Arguments)
def salary_calc(basic, hra=2000, da=1500, bonus=0):
    return basic + hra + da + bonus

print("Net Salary:", salary_calc(20000, bonus=3000))
Output
Net Salary: 26500



5️. Shopping Cart System (*args + **kwargs)
def cart_total(*prices, **discount):
    total = sum(prices)
    if "offer" in discount:
        total -= discount["offer"]
    return total

print("Total Amount:", cart_total(500, 1200, 800, offer=300))
Output
Total Amount: 2200


6️. Password Strength Validator
def validate_password(password):
    if len(password) < 6:
        return "Weak"
    if not any(ch.isdigit() for ch in password):
        return "Weak"
    if not any(ch.isupper() for ch in password):
        return "Weak"
    return "Strong"

print(validate_password("Pass123"))
Output
Strong


7️. Date Difference Calculator
import datetime

def date_difference(d1, d2):
    return abs((d2 - d1).days)

date1 = datetime.date(2024, 1, 1)
date2 = datetime.date.today()

print("Days Difference:", date_difference(date1, date2))


8️. Loan EMI Calculator (Math + Functions)
import math

def calculate_emi(p, r, n):
    r = r / 12 / 100
    return p * r * math.pow(1+r, n) / (math.pow(1+r, n) - 1)

print("EMI:", round(calculate_emi(500000, 10, 60), 2))


9️. Attendance Percentage Calculator
def attendance_percentage(total_days, present_days):
    return (present_days / total_days) * 100

def attendance_status(percent):
    return "Eligible" if percent >= 75 else "Not Eligible"

percent = attendance_percentage(100, 82)
print("Percentage:", percent)
print("Status:", attendance_status(percent))


10. Email Validator & Username Generator
def email_process(email):
    if "@" in email and email.endswith(".com"):
        return email.split("@")[0]
    return "Invalid Email"

print("Username:", email_process("student99@gmail.com"))

11. Recursive Factorial Calculator
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print("Factorial:", factorial(5))


12. Prime Number Checker
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(29))


13. Employee Data Formatter (**kwargs)
def employee_details(**data):
    for k, v in data.items():
        print(k, ":", v)

employee_details(name="Ravi", dept="IT", salary=35000)


14. Temperature Converter (Multiple Functions)
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print(celsius_to_fahrenheit(30))
print(fahrenheit_to_celsius(86))

15. System Utility Menu (Function Calls)
def add(a, b): return a+b
def sub(a, b): return a-b
def mul(a, b): return a*b

print(add(10, 20))
print(sub(30, 10))
print(mul(5, 6))



