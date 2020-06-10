# Loops

# There's two different kinds of loops
# - For loops
#     - used for iterating: one by one through an iterable like a list or a string

# example:
name = "Brian"
for character in name:
    print(character)

shows = ["GOT", "Narcos", "Vice"]
for show in shows:
    print(show)

coms = ("A. Developemnt", "Friends", "Always Sunny")
for show in coms:
    print(show)

people = {
    "G. Blurth II" : "A. Development",
    "Barney" : "HIMYM",
    "Dennis" : "Always Sunny"
}
for character in people:
    print(character)

tv = ["GOT", "Narcos", "Vice"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1
print(tv)

all_shows = []
for show in tv:
    all_shows.append(show.upper())
for show in coms:
    all_shows.append(show.upper())
print(all_shows)

# Print each item in the list ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"] and it's
# index. Makre sure to print its index first. Then, print the movie name.
shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for i in shows:
    print(str(shows.index(i)) + " " + i)
    # solution they wanted
    print(shows.index(i))
    print(i)


################################################################################################################

# While Loops
# Executes code as long as an expression evaluates to True. 

x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print("Happy New Year!")

# With an expression that always evalutes to True is called an Infinite Loop

qs = [
    "What is your name? ",
    "what is your fav. color? ",
    "What is your quest? "
]
n = 0
while True:
    print("Type q to quit.")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3

# Multiply all the numbers in the list [8, 19, 4] with all the numbers in the list [9, 1, 33], and
# append each result to a third list and print the third list. 
list1 = [8, 19, 4]
list2 = [9, 1, 33]
results = []
for i in list1:
    for j in list2:
        x = i * j
        results.append(x)

print(results)
