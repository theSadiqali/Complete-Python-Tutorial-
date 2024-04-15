# Dictionary 
"""
In Python, a dictionary is a built-in data type that represents 
a collection of key-value pairs. It is also sometimes referred to 
as an associative array, map, or hash map in other programming 
languages.
1. Dictionaries are used to store data values in key value pairs.
2. A dictionaries is a collection which is ordered. changeble or 
mutable and do not allow dublicates.
3. Dictionaries items are ordered, changeble, and does not allow 
dublicates.
4. Dictionaries are changeble, meaning that we can change, add or 
remove items after the dictionary has been created.
5. Dictionaries cannot have two items with the same key.
6. A dictionary can nested and can contain another dictionary.
"""
# Just like keys and Values
#          'Name'   'Sadiq'
#          'Age'    '23'
#          'Job'    'Python Developer'

# Now lets take a simple example 
print('\nDictionary\n')
student = {
    'name': 'sadiq',
    'age': '23',
    'job': 'Python Developer'
}
# Lets Acess the values 
print('Name: ', student['name'])
print('Age: ', student['age'])
print('Job: ', student['job'])

# Lets modify the values
student['age'] = 80
print('Updated Version Age: ',student['age'])

# Now Lets add a new key value pairs 
student['gpa'] = 3.9
student['Nationality'] = 'Pakistani'
student['Courses'] = ['English', 'Python', 'C++', 'C#', 'Math', 'Statistics', 'Introduction to AI']
print('Gpa: ',student['gpa'])

# Iterating throught key value pairs 
print('\n\nAll Information ')
for key, value in student.items():
    print(f"{key}:  {value}")
    
# As you can see the whole dictionary is enclosed in the curly braces {}. each key is seperated from its value by a column ":" and commas are used to seperated the items in the dictionary.  
# Lets do some key,value function 
print("\n\nKey Function\n")
print(student.keys())
print("\n\nValue Function\n")
print(student.values())

# Lets use delete function 
print("\n\nDel Fucntion\n")
"""
del(student)  # It will show us Name Error
print("After deleting it: ", student)    
"""

# Verification using is or not in 
print("\n\nVerification using is or not in\n")
print("Courses" in student)
print("Python" in student['Courses'])
print("David" not in student)
print("sadiq" not in student['name']) # Upper case, lower case matter 

# Assignment: Practice copy function, pop function and pop items function 
# Assigment will be on my github 

# Get function 
print("\n\nGet Function \n")
print(student.get('Courses'))

# Iterating dictionary 
# A dictionary can be iterated using the for loop 
print("\n\nIteration\n")
for key in student:
    print(key)
    
# Thats it for today and i will upload the assignment and short project on my github
# THank you soo much for watching this video