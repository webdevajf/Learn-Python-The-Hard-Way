# This line creates a variable 'types_of_people' and sets it's value to 10.
types_of_people = 10
# this line does several things. First it creates the var 'x'. Then it sets the value of x to the string "There are {} types of people." and embeds the value of 'types_of_people' within that string.
x = f"There are {types_of_people} types of people."

# This line creates the var 'binary' and sets its value equal to "binary".
binary = "binary"
# This line creates the var 'do_not' and sets its value equal to "don't".
do_not = "don't"
# This line creats the var 'y' and sets is value equal to the string "Those who know {} and those who {}." and then embeds the values of the vars 'binary' and 'do_not' within the string, respectively.
y = f"Those who know {binary} and those who {do_not}." # These are the first and second places, in this exercise, where strings are embeded inside of strings.

# This line prints the value of var 'x'.
print(x)
# This line prints the value of var 'y'.
print(y)

# This line prints the string "I said: {}" and then embeds the value of var 'x' within the string.
print(f"I said: {x}") # This is the third place, in this exercise, where a string is embeded inside of a string.
# This line prints the string "I also said: '{}'" and then embeds the value of var 'y' within the strint.
print(f"I also said: '{y}'") # This is the fourth place, in this exercise, where a string is embeded inside of a string.

# This line creates the var 'hilarious' and sets its value to the boolian 'False'.
hilarious = False
# This line creates the var 'joke_evaluation' and sets its value to the string "Isn't that joke so funny?! {}".
joke_evaluation = "Isn't that joke so funny?! {}"
# This line prints the var 'joke_evaluation' and embeds the value of var 'hilarious' into the string within var 'joke_evaluation'.
print(joke_evaluation.format(hilarious))

# This line creates the var 'w' and sets its value to the strint "This is the left side of...".
w = "This is the left side of..."
# This line creats the var 'e' and sets its value to the string 'a string with a right side.'.
e = "a string with a right side."

# This line combines and prints the values of var 'w' and var 'e', respectively.
print (w + e) # This line combines the strings 'w' and 'e' making a longer string. Combining strings make a longer string because when the final result is printed you have one long string.
