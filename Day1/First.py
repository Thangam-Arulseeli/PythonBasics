# This is my first program 
'''
This is the 
multi-line comment
'''
name = input ("Enter your name:")
age = int(input("Enter your age:"))
print ("My Name is " + name); print("\nType of name is ", type(name))
print ("My age is ", str(age)); print ("\nType of age is ", type(age))
height = 5.7; print ("My height is ", str(height)); print ("\nType of height is ", type(height))
if age >= 60:
    print (name, " is a senior citizon")
elif age >= 25:
    print (name, " is a working person")
elif age >= 17:
    print (name, " is a college student")
elif age >= 3:
    print (name, " is a school going student")
else:
    print (name, " is a infant")

# NOTE The variable can refer to objects of different types during execution.

'''
Type Conversion
----------------
bool(1) -> True
bool(0) -> False
int("100") -> 100
float (345.75) -> 345.75
str(56) -> "56"

'''
