# Match case is similar to switch case in other languages, but it is so powerful than switch case
# Match case using numeric input
print ("Match Case using numeric input \n")
choice = int(input("Enter your choice (1-3): "))
match choice:
    case 1:
        print("Add")
    case 2:
        print("Update")
    case 3:
        print("Delete")
    case _:
        print("Invalid choice")

print("\n")

# Match case using string input
print("Match case using string input \n")
day = input("Enter your day choice : ")
    
match day:
    case "Monday":
        print("Week day")
    case "Wednesday":
        print("Week day")
    case "Saturday":
        print("Weekend day")
    case _:
        print("Other day / Invalid day")
        

# Multiple Pattern --- | means an OR pattern.
day = int(input("Enter day number: "))

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Working Day")

    case 6 | 7:
        print("Weekend")

    case _:
        print("Invalid Day")


# Match with a guard -- This introduces the idea that match-case is more powerful than a simple switch statement.
age = int(input("Enter age: "))

match age:

    case age if age < 13:
        print("Child")

    case age if age < 20:
        print("Teenager")

    case age if age >= 20 and age < 40:
        print("Adult")
    
    case age if age >= 40 and age <= 60:
        print("Adult")

    case _:
        print("Senior Citizen")

