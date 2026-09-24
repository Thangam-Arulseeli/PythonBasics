#Dictionary get()
print("Hi")
employee = {
    "name": "Arun",
    "salary": 50000
}

# print(employee[name]) # NameError comes
print (employee["name"])
print(employee.get("department"))
print(employee.get("department", "Not Available"))
# print(employee[address]) # NameError Comes
print(employee["address"]) # KeyError comes 


