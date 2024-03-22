# List 
# In A Python list is a collection of items that can be changed and accessed easily, useful for storing and organizing data in python programs.
"""
1. A mutable and ordered collection of items.
2. Capable of storing heterogeneous elements.
3. Able to dynamically grow or shrink in size.
4. Accessed using zero-based indexing.
5. Modified using methods like append(), insert(), remove(), and pop().
"""
# Indexing 
print("List")
print("\nIndexing \n")
# Take a list 
nlis = ['sadiq', 'Python', 1,2,3,4]
#          1        2      3 4 5 6
print("Simple List: ",nlis)
print("Length of a list: ", len(nlis),"\n")
print("Positive And Negative Indexing")
print(nlis[1])
print(nlis[-1])
# List Content 
# 1. String
# 2. Floats
# 3. Integer
# 4. Booleans
# 5. Nested List
# 6. Nested Tuples
# 7. Other Data Structure

# For Example 
print("Examples")
# Lets Take A New List 
nlist = ['sadiq ali', 'Python Programming Language', 1,2,3,4,5,6, 'thesadiqali', 2024,2025]
#             1                  2                   3 4 5 6 7 8       9          10   11
# List Operation 
print("\nList Operation")
print(f"nlist: {nlist}")
print(f"List Length {len(nlist)}")
# Slicing 
print(f"Slicing: {nlist[0:10]}")
# Extend the list 
# Lets Make A New List 
nlist2 = [0,100] # You Know we extend the function to add new element to the list with this function, we add more than one element to the list 
nlist2.extend([1,2,3,4,5,6,777,7,8]) # We did not use the parenthesis 
nlist2
print("\nExtending the list: ",nlist2)

# Append the list 
nlist3 = [1,2,3,4,5,6]
nlist3.append(['Hello World', 'Sadiq Ali', 1,2,3,4])
nlist3
print("\n\nAppend the List",nlist3)
# Its different from the extending the list. With append method we only add only one element.

# Lets Do Some Examples
print("\n\nExamples\n")
nlist5 = [1,2]
print(nlist5)
print(f"Length of a list: {len(nlist5)}")
nlist5.append(100)
print(f"list 5: {nlist5}")
print(f"List 5: {nlist5.count(2)}")
print(f"List 5: Index 2:  {nlist5.index(1)}")
nlist5.insert(1, 0)
nlist5
print(f"List5 Insert 4 -> 5: {nlist5}") # 4 is a index
print(f"Maximum of list 5: {max(nlist5)}")
print(f"Minimum of a list 5: {min(nlist5)}")
print(f"Sum of a list 5: {sum(nlist5)}")
# And You can also change the element 
# And ALso you delete the element with del()
# del(nlist5)   NameError: name 'nlist5' is not defined. Did you mean: 'nlist'?
# print(f"List 5:{nlist5}")
# Because its deleted 
# Spliting the list 
print("\nSpliting\n")
spliting = 'sadiq ali is making a python tutorial'
print(f"Spliting: {spliting.split()}")

# Basic Operationg 
print("\nBasic Operation")
operation1 = ['a','b','Python Programming']
operation2 = [1,2,3,4,5,6,7,8,9]
print(f"Operation: {operation1}")
print(f"Operation: {operation2}")
print(f"Operation Length: {len(operation1)}")
print(f"Operation Length: {len(operation2)}")

print(f"Operation 1 + Operation 2: {operation1 + operation2}")
# Input Function 
print("\n\nInput Function")
nlist6 = "Sadiq Ali" # input("Enter A List Or String: ")
# It is a a Little bit different from the list 
print(f"Sadiq: {nlist6}")

# Evalute Function 
# The function serves the aim of converting a string into int or float 
print("\n\nExpression\n")
expression = '1+2'
total = eval(expression)
print("Sum of the expression: ",expression)
print("Sum of the expression after evalute: ",total)

# Format Function 
# This function helps to format the output printed on the screen. It give them a Good and Attractive Look
# Example 
print("\n\nFormat Function\n")
a = 3.17# float(input('Enter the Pi number: '))
b = 2.63# float(input('Enter the Golden ratio: ')) 
total = a+b
print("Sum of {} and {} is {}." .format(a,b,total))

# Copmarisom Operator And Logical Operator 
print("\nComparison Operator")
var = 1
var2 = 2
var3 = 3
print("var: ",var)
print("var: ",var2)
print("var: ",var3)
print("var < var 2: ",var<var2)
print("var < var 3: ",var<var3)
print("var3 < var 2: ",var3<var2)
print("var3 > var 2: ",var3>var2)

print("\nLogical Operator")
print(f"Logical Operator of var < var2 and var3 > var: {var<var2 and var3>var}")

# Assignment Operator 
print("Assignment Operator")
# ==, +=, -=, /=, %=, |=, //=, &=, >>=, <<= etc 
# Employed to evalute a value to a variable.
x = 3.14
x+= 5
print("X value: ",x)

# Identity Operator 
# The operator is or not are employed to control if the operands or object to the left and right of these operators are referncing to a value stored in the same memory location and return true or false. 

# Example 
print("\n\nIdentity Operators")
a1 = 3.14
b1 = 1.618
print(a1 is b1)   # False
print(a1 is not b1) # True

msg = "Hello World!"
msg2 = "Python Programming"
msg3 = "Sadiq Ali"
print(msg is msg2) # False
print(msg3 is not msg) # True 

# Membership Operators 
# These operators inclusion in and not in are empolyed to check. if certain value is availble in the sequence of value and return true or false.
print("\nMembership Operator")
# Lets take a new list 
nlist7 = ['thesadiqali', 'sadiq ali', 1,2,3,4,5,6]
print(1 in nlist7)
print(0 in nlist7)
print(2 in nlist7)
# I think thats it for today. We will cover tuples in next tutorial. 
# I will upload the code on github. 
