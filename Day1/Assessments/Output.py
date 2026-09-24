#Output-Based Questions – Loops
#Q1. range() with step
for i in range(2, 12, 3):
    print(i, end=" ")
#Expected output:



Q2. loop`
for i in range(10, 0, -2):
    print(i, end=" ")
Output:


#Q3. break
for i in range(1, 10):
    if i == 6:
        break
    print(i, end=" ")
#Output:


#Q4. continue
for i in range(1, 8):
    if i % 2 == 0:
        continue
    print(i, end=" ")
#Output:


#Q5. break + continue
for i in range(1, 11):

    if i % 2 == 0:
        continue

    if i > 7:
        break

    print(i, end=" ")
#Output:


#Q6. Nested loop
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
#Output:



#Q7. Nested loop with break
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(i, j)
#Output:

#Important discussion:
#Does break terminate both loops?


#Q8. while loop
count = 1
while count <= 5:
    print(count, end=" ")
    count += 2
#Output:



#Q9. Find the output
total = 0

for i in range(1, 6):
    total += i

print(total)

#Output:

#Q10. Find the output
for i in range(1, 6):
    print("*" * i)
Output:


#Debugging Questions – Loops
#Q11. Identify and fix the error
for i in range(1, 6)
    print(i)

#Q12 Identify and fix the error
count = 1

while count <= 5:
    print(count)


#Q13. Identify and fix the errorr
for i in range(1, 11):
    if i % 2 == 1:
        print("Even:", i)


#Q14. Requirement: Print numbers from 1 to 10.
for i in range(1, 10):
    print(i)

# What is missing?
# Correct:

