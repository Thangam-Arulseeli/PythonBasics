#List / Tuple / Set / Dictionary Output Questions
#List modification
numbers = [10, 20, 30]

numbers.append(40)
numbers.insert(1, 15)
numbers.remove(30)

print(numbers)
#Output:



#List indexing
employees = ["Arun", "Priya", "Kumar", "Divya"]

print(employees[1])
print(employees[-1])
#Output:



#Tuple
data = (10, 20, 30, 40)

print(data[1])
print(data[-2])
#Output:

#Can we execute data[1] = 50?



#Set
numbers = {10, 20, 10, 30, 20}

print(len(numbers))
#Output:




#Dictionary
employee = {
    "name": "Arun",
    "salary": 50000,
    "department": "IT"
}

employee["salary"] = 55000

print(employee["salary"])
#Output:



#Dictionary get()
employee = {
    "name": "Arun",
    "salary": 50000
}

print(employee[name])
print(employee.get("department"))
print(employee.get("department", "Not Available"))
print(employee[address])
#Output:



#Slicing Questions
#1
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])

#Output:


#2
numbers = [10, 20, 30, 40, 50]

print(numbers[:3])
print(numbers[2:])
print(numbers[:])
#Output:


#Q3. Negative indexing + slicing
numbers = [10, 20, 30, 40, 50]

print(numbers[-4:-1])
Output:



#Q4. Reverse
numbers = [10, 20, 30, 40, 50]

print(numbers[::-1])
#Output:


#Q5. Reverse with step
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[::-2])
# Output:



# Q6.
text = "PYTHON"

print(text[1:5])
print(text[::-1])
# Output:

### ----------------------------------

#. List Comprehension Questions
#Q1.
numbers = [1, 2, 3, 4, 5]

result = [x * 2 for x in numbers]

print(result)
#Output:


#Q2. With condition
numbers = [1, 2, 3, 4, 5, 6]

result = [x for x in numbers if x % 2 == 0]

print(result)
#Output:


#Q3. Convert strings
names = ["arun", "priya", "kumar"]

result = [name.upper() for name in names]

print(result)
#Output:



#Q4. Conditional expression inside comprehension
numbers = [10, 15, 20, 25]

result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print(result)
#Output:



#Q5. 
numbers = [1, 2, 3, 4, 5]

even = [x for x in numbers if x % 2 = 0]

print(even)



## Dictionary Comprehension
#Q6.
numbers = [1, 2, 3, 4]

result = {x: x * x for x in numbers}

print(result)



#Q7.
employees = {
    "Arun": 45000,
    "Priya": 60000,
    "Kumar": 55000
}

result = {
    name: salary
    for name, salary in employees.items()
    if salary >= 50000
}

print(result)
# ---------------------------------------------------

# Mixed Assessment Questions
# Q1. What is the output?
numbers = [1, 2, 3, 4, 5]

result = [x * x for x in numbers if x % 2 != 0]

print(result)
#Answer:


#Q2.
numbers = list(range(1, 11))

result = numbers[1:8:2]

print(result)
#Answer:



#Q3.
names = ["Arun", "Priya", "Kumar", "Divya", "Ravi"]

for name in names[1:4]:
    print(name)
Answer:


#Q4.
numbers = [10, 20, 30, 40, 50]

for i, value in enumerate(numbers):
    if value == 30:
        break
    print(i, value)
#Output:



#Q4. Predict carefully
numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    if number % 2 == 0:
        result.append(number * 10)

print(result)
#Output:


#Rewrite this using list comprehension:
result = [ x * 10  for x in numbers if x % 2 == 0 ]



# Q5
name=input("Name:")
salary=float(input("Salary:"))
if salary>=50000:
 print(name,"is senior")
else:
 print(name,"is junior")

 #Output