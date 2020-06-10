# Exceptions
# Similar to syntax erros but slightly different


#Exception Handling
# - A way to deal with exceptions if they occur.
# - test for error conditions
# - "Catch" exceptions if they occur
# - Decide how to proceed.

a = input("type a number: ")
b = input("type another: ")
a = int(a)
b = int(b)

# print( a / b )

# Use "try" and "except" for exception handling

try:
    print(a/b)
except ZeroDivisionError:
    print("b cannot be zero")
