print("Python Tutorial 3") # Ctrl + S ----> To Save
# Python 
# - Python is a widely used programming language for telling computers what to do.
# - It's well-known for being easy to understand and write, making it popular among programmers.
# - People use Python for various tasks such as creating websites, analyzing data, developing games, and teaching computers to do smart tasks like understanding speech or recognizing images.
# - Python is like a toolbox with many tools inside, helping programmers work quickly and easily.
# - Many companies seek people who know Python because it's versatile and applicable in various job roles.

# Let start Coding 
print("Sadiq Ali") # print your own name or Hello World! OR Print Different Things 

# Comment 
print("\n") # For A New Line
print("Comment: #") 
# Single line Comment 
print("Multiline Comment: Double qoutes or single qoutes ")
"""
Multi
line 
Comment 
"""
'''
Multi
line 
Comment 
'''

# Variable 
# In Python variable are container to storing data values 
# Just like this 
print("\n\nVariable \n")
x = 1    # Variable 1
y = 2    # Variable 2
z = x+y  # Variable 3 ---> Here we are adding them 
print(f"x values: {x}")
print(f"y values: {y}") 
print("z values:", z)# Print the z

# You know Variable are case sensitive 
# print(X) # NameError
X = 100
Y = 200 
Z = X + Y
print(f"Capital X value: {X}")
print(f"Capital Y value: {Y}")
print(f"Capital Z value: {Z}")

# Variable can also store string and characters 
a = "Sadiq Ali"
print(a)
# Double qoutes and single qoutes are quite same 
b = 'thesadiqali'
print(b)
# We have legal and Illegal Variable 
print("\n\nLegal Variable")
myvar = "sadiq"
my_var = "sadiq"
_my_var = "sadiq"
MYVAR = "sadiq"
myvar = "sadiq"
print("\n\nIllegal Variable")
"""
1myvar = "sadiq"
my-var = "sadiq"
my var = 'sadiq'
#SyntaxError:
"""
# Many Values to Multiple Variable 
# Actually allow you to assign values to multiple variables in one line 
print("\n\nMany Value To Multiple Variable\n")
name = "sadiq", "ali", "sadiq ali"
a,b,c = name
print(a)
print(b)
print(c)

# Now lets Look into Globale Variable 
print("\n\nGlobal Variable\n")
# You know Global variable can be used by everyone, both inside and outside of a function 
def glbl(): # Its a function, I will teach you that later 
    global xyz
    xyz = "XYZ"
glbl()
print(f"Globale Variable insisde a function and outside a function:  {xyz}")
# For today its enough. I will teach you about function later