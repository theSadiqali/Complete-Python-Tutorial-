# String, DataTypes, Expression, Variable
"""
String: Text data enclosed in single (' ') or double qoutes (" ")

Data Types: Different kinds of data Python can handle, like integer,floats, string, and booleans.

Expression: A combination of values, variables, and operators, that evalutes to a sing value.

Variable: A symbolic name that store data/values and can be referenced and manipulated ina program.

"""

# Lets start from very begining 

print("Hello World!")

# Single line Comment with #
"""
Multi  
line  
Comment  
With Double Qoutes or Single Qoutes
"""
# Now lets Check Python Version 
import sys 

print("Python "+ sys.version)
print(sys.winver)
print(sys.gettrace)
print(sys.argv)
print("\n\n\n")

#help(sys)  # Python Help FUnction, Which display the Python Documentation

# String
print("\nString\n")
print("The Sadiq Ali YouTube Channel.")
print("Python is my favorite Programming Language.")
 #print("Hello World") # Indetation Matter in Python 
 # IndentationError: unexpected indent
# And You Can not write print like frint 
#frint("Hello") # NameError: name 'frint' is not defined. Did you mean: 'print'?

# DataTypes
print("\n\nDataTypes")
print("Basic Data Types And Strings\n")
# Integer 
print("Integer")
print(f"123456: {type(123456)}")
print(f"1: {type(1)}")
print("Float")
print(f"1.2: {type(1.2)}")
print(f"2.2: {type(2.2)}")
print("Booleans")
print(f"True: {type(True)}")
print(f"False: {type(False)}")
print(f"(bool(1): {type(bool(1))}")
print(f"bool(0): {type(bool(0))}")

# You can Add Space Between two Output. Like This:
print("Sadiq")
print()
print("Ali\n")
print("Python")
print()
print("Programming")

# Lets Convert Integer number to a string and floats 
print("\n\n\nConvert Integer number To A String And Floats.\n")
n = 1 # Variable 
print("Before Converting To String")
print(n)
print(type(n))
print("After Converting To String")
print(str(n))
print(type(str(n)))
print("After Converting To Floats")
print(n)
print(type(float(n)))
# First lets Do the Boolean Conversion
print("\n\nBoolean Conversion\n")
bool_1 = True
bool_2 = False 
print("Before Conversion", bool_1, type(bool_1))
print("After Conversion: ",int(bool_1), type(int(bool_1)))
print("Before Conversion", bool_2, type(bool_2))
print("After Conversion: ",float(bool_2), type(float(bool_2)))


# Ctrl + ZOOM IN and Ctrl - Zoom Out

# Now Lets Find The Datatypes  of 1/2
print("\n\nDatatypes  of 1/2\n")
print(1/2)
print(type(1/2))
print(2/1)
print(type(2/1))
print(1/1)
print(type(1/1))

# Variable 
print("\n\nVariable And Expression \n")
print("SUM")
x = 2
y = 3
z = 4
# Addition 
Z = x+y+z
print(x)
print(y)
print(z)
print(Z)
sum = 1+2+3
print("Total sum = ", sum)
print("x+y+z = ",x,y,z," = " , Z)
print("x,y,z = ",x,y,z)
print(f"x,y,z = {x,y,z}")
print(type(Z))
"""
A = 1,2,3
A = a,b,c 
NameError: name 'a' is not defined. Did you mean: 'A'?
"""
# Subtraction
print("\nSUB")
Z = x-y-z
print(x)
print(y)
print(z)
print(Z)
sub = 1-2-3
print("Total sub = ", sub)
print("x-y-z = ",x,y,z," = " , Z)
print("x,y,z = ",x,y,z)
print(f"x,y,z = {x,y,z}")
print(type(Z))

# Multiplication is Your Assignment 
print("\nMUL")
Z = x-y-z
print(x)
print(y)
print(z)
print(Z)
mul = 1*2*3
print("Total mul = ", mul)
print("x*y*z = ",x,y,z," = " , Z)
print("x,y,z = ",x,y,z)
print(f"x,y,z = {x,y,z}")
print(type(Z))

# Assingment Division 
print("\nDIV")
Z = x/y/z
print(x)
print(y)
print(z)
print(Z)
div = 1/2
print("Total sub = ", div)
print("x-y-z = ",x,y,z," = " , Z)
print("x,y,z = ",x,y,z)
print(f"x,y,z = {x,y,z}")
print(type(Z))

# Floor Division 
print("\nFloor Divsion")
floor1 = 45 
floor2 = 123
FloorDivision = floor1 // floor2
print(f"Floor: {FloorDivision}")
print(type(FloorDivision))

# Modulus 
print("\nModulus")
mod1 = 100
mod2 = 200 
modulus = mod1 % mod2 
print("Modulus: ", modulus," Type: ", type(modulus))

# Exponential 
print("\nExponential ")
exponential = 2**3
print("Exponential: ", exponential, "Type: ",type(exponential))

# Lets Do Some Example 
print("\nExamples: ")
# Example 1
# Calculate How Many Hours Are There Are in 20 Hours?
print("\nCalculate How Many Hours Are There Are in 20 Hours?")
one_hours = 60 # 60 Min
hour = 20
min = one_hours * hour 
print(f"Ans: There Are {min} Minutes And Type is {type(min)}")
# Example 2
# Lets Calculate How Many Hours Are There Are in 348 Minutes?
print("\nCalculate How Many Hours Are There Are in 348 Minutes?")
minutes = 348
one_hours = 60
#hours = 348/60
# Lets Use the Variable 
hours = minutes/one_hours
print(f"Ans: There Are {hours} Hours And Type is {type(hours)} ")

# Mathematics Expression 
print("\n\nMathematics Expression \n")
var_1 = 1*2+3-1
print("1*2+3-1 = ",var_1)
var_2 = 1*(2+3)
print("1*(2+3) = ",var_2)
# The Rest For You is Assignment 
print(f"var_1 + var_2 = {var_1 + var_2}")
print(f"var_1 - var_2 = {var_1 - var_2}")
print(f"var_1 * var_2 = {var_1 * var_2}")
print(f"var_1 / var_2 = {var_1 / var_2}")
print(f"var_1 // var_2 = {var_1 // var_2}")
print(f"var_1 ** var_2 = {var_1 ** var_2}")
print(f"var_1 % var_2 = {var_1 % var_2}")

# Variable 
print("\n\nVariable \n")
# Variable store the value 
variable = 1.0
print(f"variable: {variable} And Type is {type(variable)}")
# Lets Write the multiple varibale in one line 
v1, v2, v3, v4 = "1","2","3","4"

print(f"v1, v2, v3, v4 = {v1, v2, v3, v4} And Type is {type(v1)}")
print("1 2 3 4      5 6 7 8 9 ") # Spaces . 
print("!@#$%^&*()_+~`") # Special Character 
v5 = "the sadiq ali"
#     0123456789... Indexing 
print(f"print the message: {v5} And Length {len(v5)} And Type {type(v5)} And print only 2nd String {v5[2]} And Striding {v5[::3]} And Slicing {v5[0:9]} And Change the String To Upper {v5.upper()}")
# Lets do Striding And Slicing And Change the String To Upper 

# I think For TOday Thats it. 