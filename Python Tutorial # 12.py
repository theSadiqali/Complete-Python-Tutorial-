# Loops are used to repeatedly execute a block of code. There are two main types of loops in Python: for loops and while loops.
"""
1. For Loop:
A for loop iterates over a sequence (like a list or string) and performs a set of actions for each element.
It’s useful when you know the number of iterations in advance.
Example: If you want to process each item in a shopping list, a for loop is handy.
2. While Loop:
A while loop keeps executing a block of code as long as a condition remains true.
It’s useful when you don’t know the exact number of iterations beforehand.
Example: Imagine waiting for a bus—you’ll keep checking until it arrives.
3. Nested Loops:
These are loops within loops.
Useful for complex scenarios, like processing a 2D grid or matrix.
Example: Creating a multiplication table involves nested loops.
 
"""

print("\nFor Loop:")
names = "sadiq", "ali", "sadiq ali", "thesadiqali", "TSA"
print("Without Loop: ",names)
for name in names: 
    print(f"Name with Loop: \033[1m{name}\033[0m")

fruits = "mango", "orange", "banana"
print("\nFruits without Loop: ",fruits)
for fruit in fruits:
    print(f"With loop Fruits: {fruit}")    

# Numbers 
print("\nNumbers: ")
for i in range(1,20):
    print(f"Numbers counting from 1 to 20: \033[1m {i}\033[0m")

# Example 1: 
# lets draw a traingle
    
print("\n\nTriangle Example: ")
height = 10 
# As you know range function. it is helpul to think of the range object in ordered list. Actually the range function return a sequence of numbers, starting from 1 to 10. 0---->10. OR by default, and the increment by 1 or by default and ends at aspecified number. 
for i in range (1, height + 1): 
    print("*"*i)

# Checking the range function 
# Lets take one more list 
for i in range (-8,5):
    print(f"Range function: \033[1m{i}\033[0m")

# While loop 
# Now lets start with while loop 
print("\n\nWhile Loop: ")
# A while loop is used to repeatedly excute a block of code as long as a condition is true. 

count = 1 
while count <= 10:
    print(f"Count: \033[1m{count}\033[0m")
    count +=1
    # Addition and also calculating
    # And you know sometimes we use true or false (bolean)
    # just like run until its get false
    
# Nested Loop 
print("\n\nNested Loop: ")
num = 10
print(f"The entered number is: {num}")
# Two ways you can do this 
i = 0
j = 0
# OR 
#i,j = 0,0
for i in range (0, num):
    print()
    for j in range (0, i+1): # Nested
        print("*", end='')
        
# Now lets do Else and For statement
print("\n\nFor - Else Statement: ")
for i in range (1,10):
    print("\n", i, end="")
else: 
    print("\nThese are numbers from 1 to 10. ")
    # Continue statement in for loop
print("\n\nContinue Statement") # Same as the above but at the end we use continue
num2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
for i in num2:
    if i == 11:
        continue # It will jump here 
    print(i) # Jumped on 11 
    
print("\n\nBreak Statement ") # Same as the above. But at the end we use continue 
for i in num2:
    if i == 11:
        break # It will break here 
    print(i)

# Now we will do the the while. WHile else statement
print("\nWhile Else Statement")
index = 0
while index <= 5:
    print(index, end = '') # same as above 
    index += 1
else: 
    print("\nIt give us the between 0 and 5")
    
print("\n\nBreak in while loop ")
i = 0
while i<=20:
    print(i)
    i+=1
    if i == 10:
        break
    
# Thank you soo much for watching this video. 
   
    
