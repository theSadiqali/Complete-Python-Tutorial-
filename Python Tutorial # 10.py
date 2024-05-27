# Tutorial 10

"""
In Python, conditions are used to control the flow of a program based on certain criteria. The primary construct for expressing conditions is the if statement. 

A condition typically refers to an expression that evaluates to either True or False. Conditions are commonly used in control flow statements like if, elif (else if), and while loops to make decisions based on whether certain conditions are met.
"""

print("Condition in Python")
# Comparison operators in python are =, <, >, <=, >=, ==, !=

# For Example 
print("\n\nComparison Operator")
a = 1
b = 2
print(a>b)
print(a<b)
print(a!=b)
print(a==b)
# Now Lets do some if else statement 
print("\n\nIf else statement")
if a == b:
    print("a == b")
if a <= b:
    print("a is not equal to b")
else:
    print("Error!")
# In condition statement indentation matter
# Lets do grading example 
# A for 90 and above 
# B for 80 and above
# C for 50 and above
# D for 40 and above
# F for 39 and below
print("\n\nExample 1")
num = 94#int(input("Enter a Number: "))
print(f"The entered marks is: {num}")
if num >= 90:
    print("Grade is A")
elif num >= 80:
    print("Grade is B")
elif num >= 50:
    print("Grade is C")
elif num >= 40:
    print("Grade is D")
elif num <= 39:
    print("Grade is F")
else: 
    print("Invalid Number")
    
# Logical Operator 
# 1 and Return Ture if both statement are true 
# 2 or Return True if one statement are true
# 3 not Reverse the result, erturn flase if the result is true
# Example 2 
print("\n\nExample 2")

x = int(input( "Enter a number x: "))
y = int(input( "Enter a number y: "))
z = int(input( "Enter a number z: "))
print(f"The entered numbers for x, y, z are {x}, {y} and {z}")
if x > y and x != z: 
    print(f"First statement are true {x}, {y} and {z}")
elif x > y and x != z: 
    print(f"Second Statement are true {x}, {y} and {z}")
elif x >= y or x != z:
    print(f"Third statement are true {x}, {y} and {z}")

elif x == y and x <= z:
    print(f"Fourth statement are true {x}, {y} and {z}")

elif not x != y:
    print(f"Last statement are true {x}, {y} and {z}")

else:
    print("Invalid")
    
    
# I will upload a simple project with if else Soon


