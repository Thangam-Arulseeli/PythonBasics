import json

with open("employee.json", "r") as file:

    employee = json.load(file)

print(employee["name"])
print(employee["department"])
print(employee["skills"])
print ("-----------------------------------")
#--------------------------------------

# Configuration settings
'''
with open("config.json", "r") as file:
    config = json.load(file)

print("Application:", config["application"]["name"])
print("Version:", config["application"]["version"])

print("Database Host:", config["database"]["host"])
print("Database Port:", config["database"]["port"])
print("----------------------------------------")
'''

