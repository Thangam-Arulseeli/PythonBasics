# This is a simple Python function that calculates the total price of an item based on its price and quantity.

def calculate_total(price, quantity):
    total = price * quantity

    print("price =", price)
    print("quantity =", quantity)
    print("total =", total)

    return total

result = calculate_total(100, 5)
print("Total:", result)

# --------------------------------

### Logging in Python
### However, large applications should not depend heavily on print() for diagnostics.
### That's where logging becomes important.

import pdb

def calculate_salary(basic, bonus):

    pdb.set_trace()   # Python Debugger (pdb) will pause execution here and allow you to inspect variables and step through the code.

    total = basic + bonus

    return total

print("Calculated Salary: ", calculate_salary(50000, 5000))

'''
Important pdb Commands
===========================
Command	    Meaning
------------------------    
n	        Next line
s	        Step into function
r	        Continue until current function returns
c	        Continue execution
p variable	Print variable
pp variable	Pretty-print variable
l	        Show source code
w	        Show stack
q	        Quit debugger

'''

### Using breakpoint()

# Modern Python provides: breakpoint()

# instead of explicitly writing:

## import pdb
## pdb.set_trace()

# -------------------------------------

'''
Now to use the debugger controls

At the top, you'll see controls similar to:

Continue   Step Over   Step Into   Step Out   Restart   Stop
   ▶          ↷           ↓           ↑

The important ones are:

Button	  Shortcut	            Meaning
▶ Continue	F5	            Continue execution
Step Over	F10	            Execute current line and move to next
Step Into	F11	            Enter a function
Step Out	Shift+F11       Exit current function
Restart	    Ctrl+Shift+F5	Restart debugging
Stop	    Shift+F5	    Stop debugging

'''






