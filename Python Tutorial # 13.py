# Exception Handling in Python

# Exception:
"""
An Exception is an event, which occurs during the execution time of a program that disrupts the normal flow. Exception handling in Python allows you to manage and respond to errors that occur during program execution. It helps prevent the program from crashing abruptly by handling unexpected situations or errors gracefully. If you have suspicious code that may raise an exception, you can handle it using try-except blocks.
"""

# What are Exceptions?
"""
Errors in Python: When something goes wrong in Python during program execution, an error occurs. These errors are known as exceptions.
"""

# Basic Structure of Exception Handling:
"""
Try-Except Block: In Python, you can use a try block to test a block of code for exceptions. If an exception occurs within the try block, Python immediately jumps to the matching except block to handle the exception. The code within the except block is executed to manage the exception.
"""

# Common Exceptions:
# ZeroDivisionError
# NameError
# ValueError
# IOError
# EOFError
# IndentationError

# Example 1
print("\n\nExample 1:")

try: 
    1 / 0
except ZeroDivisionError:
    print("This code caused a zero devision error")
print("Continuing exceution after handling the exception ")

# This line below would cause an unhandled ZeroDivisionError 
# print(1 / 0) # Zero division error

# Syntax of Exception Handling 
"""
try:
    # Code that might raise an exception
    ...
except ExceptionType:
    # Code to handle the exception
    ...
else: 
    # Optional block executed if no exception occur in the try block
    ...
finally:
    # Optional block, always exceuted whether an exception occured or not.
    ...
"""    

# Types of Exceptions. 
"""
1. Built-in Exceptions: Python provides various built-in 
exceptions like TypeError, ValueError, ZeroDivisionError, etc.
2. Custom Exceptions: You can create custom exceptions to handle 
specific situations in your code by defining new exception 
classes.
"""

# Example 2
print("\n\nExample 2:")
try: 
    num = 1
    num2 = 3
    
    result = num / num2
    print("Result: ", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter a valid number.")
else:
    print("No exception occured.")
finally:
    print("Execution completed, regardless of exception. ")
    
# Benefit of of exception handling:
"""
Graceful Error Handling: Prevents aburpt program termination.
Controlled FLow: Allows you to control the program flow in case of errors. 
Cleanup Action: Provides a way to perform cleanup actions regardless of exceptions. 
Exception Handling is a powerful tool in python that helps you write more robust and reliable code by managing errors effectively.
"""

# Lets do some other example
# Zero Error already don 
# NameError

print("\n\nName Error: ")
try: 
    y = 1 # x + 5    Name Error
except NameError:
    print("This code give a NameError")
print(y)

print("\n\nIndex Error: ")
nlis = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729] # Chose Random Number

try: 
    nlis[10]
except IndexError:
    print("This code give the index error")
# print(nlis[10])  Index Error

# Lets do some Multiple except blocks
# Try except etc
print("\n\nMultiple Except Block: ")
num1 = 2
print("The entered value is ", num1)

try: 
    num2 = 5
    value = num1 / num2
    print("This process is running with value = ", value)
except ZeroDivisionError:
    print("This function gives a ZeroDivisionError since a number can not divide by 0. ")
except ValueError:
    print("You should provide a number ")
except:
    print("Something went wrong")

# Raising in Exception
# Using the raise keyword, the programmer can throw an exception when a certain condition is reached. 

print("\nRaising in Exception: ")
num = 1001
try: 
    if num > 1000 and num % 2 == 0 or num % 2 != 0:
        raise Exception("Do not allow to the even numbers higher than 1000")
except:
    print("Even or Odd numbers higher than 1000 are not allowed!")
    
else: 
    print("This process is running with value = ", num)
finally:
    print("The process is completed. ")
    
# Here is your Assignment
print("\n\nAssignment: \n") # Key Error. It just like Name Error and Multiple Except Error

# Thank  you soo much for watching this video. 
# thesadiqali  Youtube Facebook Instagram
# sadiq ali  linkdeln Whatsapp



    
    