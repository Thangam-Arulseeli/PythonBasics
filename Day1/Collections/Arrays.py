'''
In Python, there are two common ways to work with arrays:

List – commonly used as a general-purpose dynamic array. [List  → Can store different data types []]
array module – provides a typed array where all elements must have the same data type. (Array → Normally stores elements of the same type())
Example for arrays:
    from array import array
    marks = array('i', [80, 90, 75, 88])
    prices = array('f', [10.5, 20.5, 30.5])
    print(marks)
    print(prices)

NOTE: It's useful to emphasize that Python lists are usually preferred for general-purpose collections,
 while the array module is useful when you specifically want a typed array
     with more compact storage for basic numeric types.

'''
from array import array

# Creating an integer array
numbers = array('i', [10, 20, 30, 40, 50])
print("Original Array:", numbers)

# 1. append() - Add an element at the end
numbers.append(60)
print("After append():", numbers)

# 2. insert() - Insert an element at a specific position
numbers.insert(2, 25)
print("After insert():", numbers)

# 3. extend() - Add multiple elements
numbers.extend([70, 80])
print("After extend():", numbers)

# 4. index() - Find the position of an element
print("Index of 30:", numbers.index(30))

# 5. count() - Count occurrences of an element
print("Count of 20:", numbers.count(20))

# 6. remove() - Remove a specific element
numbers.remove(25)
print("After remove():", numbers)

# 7. pop() - Remove and return an element
removed = numbers.pop()
print("Removed element:", removed)
print("After pop():", numbers)

# 8. reverse() - Reverse the array
numbers.reverse()
print("After reverse():", numbers)

# 9. tolist() - Convert array into a list
my_list = numbers.tolist()
print("Converted List:", my_list)

# 10. len() - Number of elements
print("Length:", len(numbers))

# 11. Accessing elements using index
print("First Element:", numbers[0])
print("Second Element:", numbers[1])

# 12. Slicing
print("First 3 Elements:", numbers[:3])

# ---------------------------------

'''
Expected output
----------------
Original Array: array('i', [10, 20, 30, 40, 50])
After append(): array('i', [10, 20, 30, 40, 50, 60])
After insert(): array('i', [10, 20, 25, 30, 40, 50, 60])
After extend(): array('i', [10, 20, 25, 30, 40, 50, 60, 70, 80])
Index of 30: 3
Count of 20: 1
After remove(): array('i', [10, 20, 30, 40, 50, 60, 70, 80])
Removed element: 80
After pop(): array('i', [10, 20, 30, 40, 50, 60, 70])
After reverse(): array('i', [70, 60, 50, 40, 30, 20, 10])
Converted List: [70, 60, 50, 40, 30, 20, 10]
Length: 7
First Element: 70
Second Element: 60
First 3 Elements: array('i', [70, 60, 50])

'''

'''
IMPORTANT ARRAY METHODS
-------------------------
| Method / Function | Purpose                                | Example                |
| ----------------- | -------------------------------------- | ---------------------- |
| `append()`        | Adds an element at the end             | `arr.append(60)`       |
| `insert()`        | Adds an element at a specific position | `arr.insert(2, 25)`    |
| `extend()`        | Adds multiple elements                 | `arr.extend([70, 80])` |
| `remove()`        | Removes a specified element            | `arr.remove(20)`       |
| `pop()`           | Removes and returns an element         | `arr.pop()`            |
| `index()`         | Finds the index of an element          | `arr.index(30)`        |
| `count()`         | Counts occurrences                     | `arr.count(20)`        |
| `reverse()`       | Reverses the array                     | `arr.reverse()`        |
| `tolist()`        | Converts array to list                 | `arr.tolist()`         |
| `len()`           | Returns number of elements             | `len(arr)`             |


| Type Code | Data Type           |
| --------- | ------------------- |
| `'i'`     | Integer             |
| `'f'`     | Float               |
| `'d'`     | Double/Float        |
| `'b'`     | Signed integer/byte |
| `'u'`     | unicode/string      |  

'''


