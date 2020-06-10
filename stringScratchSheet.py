# Print every character in the string "Camus".
my_string = "Camus"

for i in my_string:
    print(i)


# Use a method to make the string "aldous was born in 1894." grammatically correct by
# capitalizing the first letter in the sentence. Then, print your new string. 
string2 = "aldous was born in 1894"
print(string2.capitalize())


# Take the string "Where now? Who now? When now?" and call a method that returns a list that looks 
# like: ["Where now". "Who now", "when now"]. Print the list
string3 = "Where now? Who now? When now?"
new_list = list(string3.split("?"))
print(new_list)


# Take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and turn it into the string
# "The fox jumped over the fence." (Don't forget, you learned a methoed that urns a list of strings into
# a single line string.) Note, There should be a blank splace between the final "e" and the period
# at the end. Make sure to pring your new string
words = ["The", "fox", "jumped", "over", "the", "fence", "."]
one_string = " ".join(words)
print(one_string)

# Create the string "threethreethree" using concatenation and pring it. And then print it again using multiplication.
word = "three"
print(word+word+word)
print(word * 3)

#Slice the string "It was a bright cold day in April, and the clocks were striking thirteen." to only inlcude the 
# characters before the comma and print it.
sen = "It was a bright cold day in April, and the clocks were striking thriteen."
print(sen[:sen.index(",")])

# Find dialogue in your favorite book (containing quotes) and turn it into a string and print it. 
# Make sure your stinrg contains double-quotes.
d = " and then she said, \"I didn't think you'd make it out tonight.\" "
print(d)

# Replace every instance of "s" in "A screaming comes across the sky." with a dollar sign and print the result.
saying = "A screaming comes across the sky."
print(saying.replace('s','$'))

# Use a method to find the first index of the character "m" in the string "Hemingaway" and print it.
word = "Hemingway"
print(word.index("m"))