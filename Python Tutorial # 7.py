# Tuples
""" 
1 - Tuples are similar to list but immutable, meaning their contents can not be changed after creation. 
2 - They are written using parentheses () instead of square brackets [].
3 - Tuples are used to store collections of items, just like lists.
4 - They are handy for grouping data that shouldn't change, such as coordinates or program settings.
5 - Items in a tuple can be accessed using indexing, similar to lists.

"""
# Lets take a simple tuple
print("Tuples\n")
tuple_1 = ('Hello World!', 'Python Programming Language', 'sadiq ali',1,2,3,True,False,[4,5,6],{7,8,9},{'A':3,'B':8},(0,1))
tuple_1
print(tuple_1)
# Lets check the type 
print(f"Type: {type(tuple_1)}")
# Length 
print(f"Length: {len(tuple_1)}")
# Lets print each value in a tuple using positive and negative indexing 
print("\nPrinting each values\n")
# Lets take same tuple 
tuple_1
print(tuple_1[0])
print(tuple_1[1])
print(tuple_1[-1])
print(tuple_1[2])
print(tuple_1[-2])
print(tuple_1[3])
print(tuple_1[-3])
# Now lets find the type of these tuple 
print("type")
print(type(tuple_1[0]))
print(type(tuple_1[1]))
print(type(tuple_1[-1]))
print(type(tuple_1[2]))
print(type(tuple_1[-2]))
print(type(tuple_1[3]))
print(type(tuple_1[-3]))

# Concatenation of tuples 
print("\nConcatenation of tuples \n") # To Concatenation of tuples  + sign is used.
# Lets take the same tuples 
tuple_1
tuple_2 = tuple_1 + ("Concatenation of tuples ", 2024, 2025, 2026)
print(f"Concatenation of tuples: {tuple_2}")

# Repition of tuples 
print("\nRepition of tuples\n")
rep_tuple = (1,2,3)
repition = rep_tuple * 4
print("Before Repition of tuples: ",rep_tuple)
print("After Repition of tuples: ",repition)

# Membership tuple
# lets take the first tuple 
print("\nMembership tuple\n")
tuple_1
print(tuple_1)
print(f"1 in tuple 1: {1 in tuple_1}")
print(f"1 in tuple 1: {'sadiq ali' not in tuple_1}")

# Iteration 
for i in tuple_1:
    print(i)
# For loop iterates over elements in a sequence or iterable, executing a block of code for each item.

# And do not worry about for loop. I will teach you that later.

# cmp() function 
"""
Actually it is to compare two tuples and returns true or false.

"""

print("\ncmp() Function\n")
# Its a simple function and don`t worry about that. I will teach you that later. 
def cmp(t1,t2):  
    return bool(t1>t2) - bool(t1<t2)
def cmp(t3,t4):  
    return bool(t3>t4) - bool(t3<t4)
def cmp(t5,t6):  
    return bool(t5>t6) - bool(t5<t6)
t1 = (1,3,5) # t1 is lower than t2. Output is -1
t2 = (2,4,6)

t3 = (5,)   # t3 is higher than t4. Output is 1
t4 = (4,)

t5 = (3.14,) # t5 is equal to t6. Since output is 0
t6 = (3.14,)
# Lets print the value 
print("t1 and t2: ", t1,t2)
print("Cmp function: ", cmp(t1,t2))

print("t3 and t4: ", t3,t4)
print("Cmp function: ", cmp(t3,t4))

print("t5 and t6: ", t5,t6)
print("Cmp function: ", cmp(t5,t6))

# print function 
# As you all know about print function 
# Minimum function  
print("\nMinimum Function\n")
# Lets take the same tuple 
t1
minimum = min(t1)
print("t1 value: ", t1)
print("Minimum: ",minimum)
# Similar the max function 
# Lets talk about tuple sequence function 
print("\nSequence function")
seq = "Python"
sequence = tuple(seq)
print(sequence)

# Slicing function 
print("\nSlicing function ")
# We took tuple_1
print("Before Slicing: ",tuple_1)
slicing = tuple_1[1:3]
print("After Slicing: ",slicing)

# Sorting Tuple
# Tuple can be sorted and save as new tuple. 
print("Sorting Tuple ")
# Lets take the new tuple and lets sort them
sort_tuple = (1,2,3,9,5,6,8,7,4)
sort_the_tuple = sorted(sort_tuple)
print(sort_the_tuple)
"""
# Lets take the first tuple 
tuple_1
print(tuple_1)
sort_tuple_1 = sorted(tuple_1)
print("Sort the tuple 1: ", sort_tuple_1) # TypeError: '<' not supported between instances of 'int' and 'str'
"""
# Nested Tuple 
print("\nNested Tuple")
"""
Nested tuple in python refer to tuples that are elements of another tuple. Tuples are immutable, ordered collections, and they can contain other tuples as their elements.
"""
nested_tuple = ((1,2,3),('a','b','c'),(4.5,5.5,6.5))
#                  0          1             2
# Accessing the element in the nested tuples
print(nested_tuple)
print(f"Nested tuple zero: {nested_tuple[0]}")
print(f"Nested tuple 0 and 1: {nested_tuple[0][1]}")
print(f"Nested tuple 2 and 2: {nested_tuple[2][2]}")
print(f"Nested tuple 1 and 2: {nested_tuple[1][2]}")

# Tuples are Immutable 
print("\nTuples are Immutable")
"""
immu_tuple = (1,2,3,4,5,6,7,8)
immu_tuple[1] = 9
print(immu_tuple) # TypeError: 'tuple' object does not support item assignment

"""

# Delete a tuple 
print("\nDelete a tuple ")
# You can not diretly delete a indivitual element from a tuple. tuple are immutable.
del_tuple = (1,2,3,4,5,6,67,7,7,9)
print(del_tuple) # Before deleting the tuple
"""
del del_tuple
print(del_tuple) # NameError: name 'del_tuple' is not defined.
"""

# Count Method, Index method are your Assignement 
print("\n\nCount Method")
count = del_tuple.count(4)
print(f"Count method: {count}")

#actually it return the index of the first occurence of the specified value in a tuple

print("\nIndex Method")
print("Index Method 4: ",del_tuple.index(4))
#because it start from zero

# One Element tuple
"""
Creating a one element tuple requires a trailing comma after the single element. This is necessary to distinguish it from parenthesis () used for grouping expression.
"""
print("\nOne Element tuple")
one_element_tuple = (0)
print("One element tuple: ",one_element_tuple)
print("Type of One element tuple: ",type(one_element_tuple))
# I think thats it for today. Next tutorial all about sets in Python 


