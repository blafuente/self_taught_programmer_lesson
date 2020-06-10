# Write a program with an infinite loop and a list of numbers. Each time through the loop the program should 
# ask the user to guess a number (or type q to quit). If they type q, the program should end. Otherwise, it
# should tell them whether or not they successfully guessed a number in the list or not. 

import random
some_number = random.randint(1,10)
print(some_number)
# guess = input("From 1 to 10. Guess a number: ")
# print("Type q to quit.")

# print(type(guess))

while True:
    guess = input("From 1 to 10. Guess a number: ")
    print("Type q to quit.")
    if guess == 'q':
        break
    elif guess == str(some_number):
        print("You guess the number!!!")
        break
    else:
        print("Guess again.")