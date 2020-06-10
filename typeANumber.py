# Assignment: Type A Number

# Write a program that asks the user to type a number, convert it to an integer,
# and print it. If you can't convert their input to an integer, print a message
# that says "Please type an integer."

num = input("Type a number: ")

try:
    print(int(num))
except:
    print("Please type an integer.")