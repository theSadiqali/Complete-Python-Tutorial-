# Topic Sets
"""
Set: in Python are collection of unique and unordered elements enclosed in curly braces. They support common set operation, like union and interaction, and are mutable. Set can only contain immutable elements and are usefull for tasks like removing dublicates and membership testing. 
0. Creation: Sets are created using curly braces {} or the set() 
function.
1. Uniqueness: Sets contain unique elements, automatically 
removing duplicates.
2. No Order: Sets are unordered collections; they don't maintain 
element order.
3. Enclosed in Curly Braces: Defined using curly braces {}, with 
elements separated by commas.
4. Mutable: Sets are mutable; elements can be added or removed 
after creation.
5. Common Operations: Support operations like union, 
intersection, difference, and symmetric difference.
6. Membership Testing: Efficient for testing membership due to 
hashing mechanism.
7. Immutable Elements Only: Can only contain immutable elements 
like numbers, strings, and tuples.
8. Hashable Elements: Elements must be hashable with stable hash 
values.
9. Use Cases: Useful for removing duplicates, membership testing, 
and set operations.
#Actually set is one of built in data types in python used to 
store collection of data including list, tuples and dictionary.
"""
# Empty Set 
print("Empty Set: ")
set_1 = {}
print(f"Empty Set Value: {set_1}")
print(f"Type of Empty Set: {type(set_1)}") # As you can see the {} empty braces denotes the empty dic, not empty set
print()
set()
set_2 = set() # To take empty set without elements, use set() function without any items. 
print("Empty Set: ", set_2)
print("Type of Empty Set: ", type(set_2))
# Now lets convert list to Set
# Lets take List
print("\n\nConverting List To A Set\n")
lis = ["Python Programming Language",1,2,3,4,5,"Sadiq Ali", True, False, 2024,2025] # Its a simple list
lis
set_3 = set(lis)
print(f"Converting List: {set_3}")
print("Type of Set 3: ", type(set_3))

# Set Operation 
# Take A Set 
print("\n\nSet Operation\n")
print("Add Function")
set_3.add("Hi Python coders!")
print("After adding Hi Python Coders To Set 3: ",set_3)

# Update Function 
print("\n\nUpdate Function: ")
set_4 = {1,2,3,4,5,6}
print(set_4)
# To Add Multiple element into the sets 
set_4.update({7,8,9})
print(f"After Update Function: {set_4}")

# Remove Function 
print("\n\nRemove Function: \n")
# To Remove an element from the set .remove we use 
set_4.remove(1)     # TypeError: set.remove() takes exactly one argument 
print("After Removing: ",set_4)
# But if we give them more argument then it will give you error. #Type Error

print("\n\nDiscard Function\n")
# It leaves the set unchanged if the element to be deleted is not availble in the set. 
print(set_4.discard(3.11))
print(f"Show the result to prove: {2 in set_4}")

print("\n\nLogic Operation\n")
# Lets take two Sets
set1 = set(["Python",1,2,3,1.1,2.2,"Hello Sadiq", 11,22,33, 111,222,333])
set2 = set([7,8,9,77,88,99,True,False,2024,2025,111,222,333])
# We took Random sets
print(f"printing the sets: {set1,set2}")
# Lets do the intersection 
intersection = set1 & set2
print("Intersection: ",intersection)

# Lets the Difference 
print(f"Set 1: {set1} Set 2: {set2}")
print("Difference: ",set1-set2)
set3 = {5}
set4 = {5}
print(f"Set Comparison: ", set3 >= set4)

print("\n\nUnion Function\n")
# Union Function 
# It correspond to all the element in both sets
print("Union Set function: ", set1.union(set2))

# issubset and subset functions 
print("\n\nissubset and subset functions")
print(f"1,2,3 is Subset: {set([1.1,2.2]).issubset(set_1)}")

# Now coming to min, max and sum function 
a = [1,1,2,2,3,3,4,4,5,5,6,6]
b = {1,1,2,2,3,3,4,4,5,5,6,6}
print("\n\nmin, max and sum function\n")
print("Mini: a: ",min(a))
print("Sum: b: ", sum(b))
# Do the rest like this 

print("\n\npop function\n")
print("pop: a: ",a.pop())  
# do practice copy function like this 
# Thank You so much for watching this video 
# I will upload the Assignment 


