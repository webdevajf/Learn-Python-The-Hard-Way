# No changes here
types_of_people = 10
# No changes here
x = f"There are {types_of_people} types of people."

# No changes here
binary = "binary"
# he changed "don't" to "I don't"
do_not = "I don't"

# No changes here
y = f"Those who know {binary} and those who {do_not}."

# He changed 'print(x)' to 'print(x + y)'
print(x + y)
# No changeds here
print(y)

# No canges here.
print(f"I said: {x}")
# He took out the f command preceding the string.
print('I also said: {y}')

# No changes here.
hilarious = False
# He took out the f command preceding the string.
joke_evaluation = "Isn't that joke so funny?! {}"

# he changed the command from one that prints var 'joke_evaluation' with var 'hillarious' embedded in the placeholder to one that prints var 'joke_evaluation' followed by a tupil of var 'do_not'.
print(joke_evaluation, tuple(do_not))

# no changes here.
w = "This is the right side of..."
# no changes here.
e = "a string with a left side."

# no changes here.
print(w + e)
