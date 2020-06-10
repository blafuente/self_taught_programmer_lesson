#Functions
# compound statements
# A function can have no parameters: f()
# One parameter: f(x)
# Multiple paramters: f(x,y,z)

# keyword "def" defines the function and the name of it afterwards. 
# the function name shouldn't be capitalized
# example:
def f(x):
    return x * 2

result = f(3)
print(result)

# should save a function's output in a variable incase its used later in the program
def f(x):
    return x + 1

z = f(4)

if z == 5:
    print("z is 5.")
else:
    print("z is not 5.")

# define a function without a parameter
def f():
    return 1 + 1

result = f()
print(result)

# when you define a function with multiple parameters, you must seperate with commas (,)
def f(x, y, z):
    return x + y + z

result = f(1, 2, 3)
print(result)

# Functions can accept two types of parameters:
# - Optional Parameters
# - Required Parameters

# Function exercise 1
# Write a function named square that takes a number n, as a parameter 
# and returns that number squared
def square(n):
    return n ** 2

result = square(25)
print(result)

# Function exercise 2
# Create a function called print_string that accepts a string as a parameter and prints it
def print_string(s):
    print(s)

print_string("Hello")

# Optional Parameters
def f(x=2):
    return x ** x
print(f(4))
print(f())

# Function Exercise 3
# Write a function called opt that takes three required parameters and two optional parameters
def opt(a=1, b=2, c=3):
    return a+b+c

print(opt())

#solution
def opt(a,b,c,d=1,e=3):
    return
print(opt(1,2,3))

