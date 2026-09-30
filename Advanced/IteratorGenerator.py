'''
Iterables and Iterators in Python
--------------------------------
What is an Iterable?
An iterable is any object that can return its elements one at a time.

Examples:
•	list
•	tuple
•	string
•	set
•	dictionary
•	range

An object is iterable if:
•	It has __iter__() method

OR
•	It has __getitem__() method (index-based access)

Example
numbers = [10, 20, 30]

for n in numbers:
    print(n)

Here:
•	numbers → iterable
•	for loop internally calls iter() and next()

What is an Iterator?
An iterator is an object that:
1.	Has __iter__() method
2.	Has __next__() method

It remembers state (where it is currently).
Example
numbers = [10, 20, 30]

it = iter(numbers)   # Convert iterable to iterator

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
If you call next() again → StopIteration exception.

How for-loop Works Internally
------------------------------
numbers = [1, 2, 3]

it = iter(numbers)

while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break
'''

### Custom Iterator Example
# ----------------------------
class CountUp:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration

counter = CountUp(3)

print("Custom Iterator counter")
for num in counter:
    print(num)

'''
Output:
1
2
3
'''
print("--------------")
# -------------------------

### Generators --------------------------
# ------- Generators are a simplified way to create iterators.
# Instead of __next__(), we use yield.

# Generator Function
print("Generator with yield")
def count_up(max):
    n = 1
    while n <= max:
        yield n
        n += 1

gen = count_up(3)

print(next(gen))
print(next(gen))
print(next(gen))
print("--------------")
# -------------

'''
Why Generators?
•	Memory efficient
•	Lazy evaluation
•	Useful for large datasets


# Generator vs Normal Function
----------------------------------
Normal function:
def get_numbers():
    return [1, 2, 3]

Generator:
def get_numbers():
    yield 1
    yield 2
    yield 3

Normal → returns everything
Generator → returns one value at a time
'''

### Generator Expression
### ----------------------
# Like list comprehension but memory efficient.
print("Generator Expression - Like list comprehension but memory efficient ")
nums = (x*x for x in range(5))

for n in nums:
    print(n)


#Advanced Generator - yield from
#----------------------------------
print("Advanced Generator  -- Demonstrating how memory is efficiently handled")
def gen1():
    yield 1
    yield 2

def gen2():
    yield from gen1()
    yield 3

for i in gen2():
    print(i)
print("-----------------")
# -----------------------------------------
'''
Iterators & Generators
-----------------------
1. Concept Explanation
•	Iterators: Objects implementing the __iter__() and __next__() protocols to traverse elements sequentially.
•	Generators: Special functions defined with the yield keyword. 
        They lazy-evaluate and stream data one item at a time, 
        keeping state between yields rather than allocating memory for an entire dataset.

2. Real-Life Use Case
Processing massive log files (gigabytes to terabytes) without causing Out-Of-Memory (OOM) errors
    on high-throughput servers.


3. Executable Code
# Real-life scenario: Streaming a multi-gigabyte log file line by line
'''

def stream_server_logs(log_data):
    # Generator function that yields individual error logs dynamically.
    print("Generator that yield individual error log")
    for line in log_data:
        if "ERROR" in line:
            yield line.strip()
print("--------")

# Simulated log file stream (memory efficient)
raw_logs = [
    "2026-09-25 10:00:01 INFO User logged in",
    "2026-09-25 10:00:05 ERROR Database connection failed",
    "2026-09-25 10:00:10 WARNING Disk usage > 80%",
    "2026-09-25 10:00:12 ERROR Payment gateway timeout"
]


# Consuming generator via iterator interface
error_generator = stream_server_logs(raw_logs)

print("First Error:", next(error_generator))
print("Second Error:", next(error_generator))
# ------------------------------------------------
