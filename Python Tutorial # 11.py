# Function 
# In Python a function is a group of related statements that performs a specific task. 
"""
A function is a block of reusable code that performs a specific task.
It takes inputs, processes them, and produces outputs. 
Just like give input....  ( input  ---> Process ---> Output ) 
Parts of a function:

Function name: It's a unique identifier for the function.
Parameters (arguments): These are the inputs the function receives to perform its task.
Body: It contains the code that defines what the function does.
Return statement: It specifies the output of the function.
Creating a function:

Use the def keyword followed by the function name and parentheses ( ).
Define parameters inside the parentheses if the function needs input.

# 1. Use the 'def' keyword to define a function.
# 2. Optionally, provide parameters inside the parentheses.
# 3. Add a docstring to describe the function's purpose (optional but recommended).
# 4. Write the body of the function.
# 5. Use the 'return' statement to return a value from the function (if needed).
# 6. Call the function by its name, passing arguments if required.
"""
# For example 
print("\nExample")
# Lets take sadiq as a function 
def sadiq(x): # Indentation 
    y1 = x-8
    y2 = x+8
    y3 = x*8
    y4 = x/8
    y5 = x%8
    y6 = x//8
    print(f"If you make the above operations with {x}, the results will be {y1}, {y2},{y3},{y5},{y6}")
    return y1,y2,y3,y4,y5,y6
# So here we have to run the function or process it. 
sadiq(5) # x = 5
 
# No lets do another simple function example 
print("\n\nAnother example: ")
def add():
    a = 1 
    b = 2
    c = a + b
    print(f"sum equal to {c}")
add()
# Help function 
# You can use help function. 
# help(sadiq) 
print('\n\nCall the function again and again or with another number: ')
sadiq(1)

# Function with multiple parameters 
# Define a function with multiple elements 

print("Multiple Parameter: ")
def mult(x,y):
    z = 2*x + 5*y + 45
    return z 
output = mult(3.14,1.618) # Actually you can yield the output by assigning to a variable 
print(output)
print(mult(3.14,1.618)) # You can obtain the result directly 
mult(3.14,1.618) # This is also another version

print("\n\nSimple example of Multiple Parameter: ")
def add_number(a,b):
    result = a + b
    return result
# Calling the function and passing arguments 
sum_result = add_number(1,9)
print(sum_result) # 10

# Variable 
# Input for a function is called a formal parameter
# A variable that is declared inside a function is called a loocal variable 
# Parameter only exists within the function (i.e the point where the function start and stops ) 
# A function that is declared outside a function is known as global variable
# Its value is accessible and modifiable throughout the program 

print("\nVariable")
global_var = 10 
def my_variable():
    # Local variable
    local_variable = 20
    print("Inside the function: ")
    print("Local Variable: ", local_variable)
    print("Global Varibale: ", global_var)
print("Accessing the gloabl variable outside the function: ", global_var)
my_variable()

# You can not access the local variable outside the function it will give you the error 
#print("OUtside the function local variable ", local_variable) # NameError: name 'local_variable' is not defined

 
# Define a function with and without return statement 
print("\n\nWithout return statement, the function returns None.")

def msg1():
    print("Hello World!")
def msg2():
    print("Hello! Sadiq!")
    return None
msg1()
msg2()

# Now printiting a function after a call indicates a None is the default return statement. 
# Lets see printing the function what function returns are 
print(msg1())
print(msg2())

# Concatetantion of two strings 
# Define a function 
print("\n\nConcatetantion of two strings")
def strings(x,y):
    print(x,y)
    return x + y
# Testing the function string x,y
strings ("Hello", "Sadiq")

# Simplicity of function 
# Here is the following code

print("\n\nSimplicity of function: ")
x = 2.7
y = 0.5 
eqaution = x*y + x+y - 37
if eqaution > 0:
    eqaution = 6
else: eqaution = 37

eqaution
print(eqaution)

# Lets write them as a function 
def function(x,y):
    print("\n\nSimplicity of function: inside the code ")
    x = 2.7
    y= 0.5
    
    eqaution = x*y + x+y - 37
    if eqaution > 0:
        eqaution = 6
    else: eqaution = 37

    eqaution
    print(eqaution)

function(x,y)

# Predefined function 
print("\n\nPredefined function like print(), sum(), len(), min(), max(), etc")
num = [1,2,3,4,5]
print(sum(num))
print(min(num))
print(max(num))

# Do the remining like this 

# Condition and Loops in functions
# Define a fnunction including condition if/else

print("\n\nUsing condition and loops \n")
# Simple example
def fermentation (microorganism, substrate, product, activity):
    print(microorganism, substrate, product, activity)
    if activity < 1000:
        return f"The fermentation process was unsucessfull with the {product} activity of {activity} u/ml from {substrate}"
    else: 
        return f"The fermentation process was successful with the {product} activity of {activity} u/ml from {substrate}"
result1 = fermentation("Aspergillus niger", "molasses", "insulinase", 1800)
print(result1)
print("")
result2 = fermentation("Aspergillus niger", "molasses", "Insulinase", 785)
print(result2)

# Thats a simple Bio Problem

# Now lets do the loop 

print("\n\nLoop: ")
def fermentation(context):
    for parameters in context:
        print(parameters)
context = ["Stirred-tank bioreactor", "30 C temperature", "200 rpm agitation speed ", "1vvm aeration", "1% (v/v) inoculr"]
fermentation(context)

# Another Example 
print("\n\nExample: ")
def simple(example1):
    for parameters in example1:
        print(parameters)
example1 = [1,2,3,4,5,6]

simple(example1)

# Now lets do recursive function 
print("\n\nRecursive function: ")
# Calculating the factorial of a certain number
def factorial(num):
    if num == 0:
        return 1 
    else: 
        return num * factorial (num -1)
print("the value is: ", factorial (0))

# Nested function 
print("\n\nNested function: ")
def added_num(num1):
    def incremented_num(num1):
        num1 = num1 + 1
        return num1
    num2 = incremented_num(num1)
    print(num1, "----->>", num2)
added_num(10)
    
# Non local function 
# Define a function regarding nonlocal function 
print("\n\nNonLocal Function: \n")
def print_year():
    year = 2001
    def print_current_year():
        nonlocal year
        year += 23
        
        print("Current year is", year)
    print_current_year()
print_year()

# Thank you soo much for watching this video and dont worry i will upload the code on my github. and soon i will upload a small project on function. 


