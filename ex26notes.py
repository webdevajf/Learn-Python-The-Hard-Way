# This line is intended to print a string that
# querreys the user for an input.
# PROBLEMS W/ THIS LINE: None. However, if I
# were to write this I'd have combined the var
# and the print statement by making the string
# into the querry within the print statement.
print("How old are you?", end=' ')
# This line is intended to create the var 'age'
# and ask the user for an input to defign the
# var.
# PROBLEMS W/ THIS LINE: There's could be a prompt
#('>' for example) to inform the user that an input
# is needed. However, the question in the print
# statement probably does this adequatley.
age = input()
# This line is intended to print a string that
# querreys the user for an input.
# PROBLEMS W/ THIS LINE: There's no variable,
# with an 'input()' assigned to it's value, following
# this printed querry. Furthermore, if I
# were to write this I'd have made the string in
# this print statement the querry for an input
# in a var 'Height'.
print("How tall are you?", end=' ')
# This line is intended to querry the user for
# an input() to defign a var in the next line.
# PROBLEMS W/ THIS LINE: There's no end braket
# (')') to close the print statemnt.
print("How much do you weigh?", end=' '
# This line is intended to create a var 'weight'
# and querry the user for an input to defign the
# value of the var.
# PROBLEMS W/ THIS LINE: none.
weight = input()

# This line is intended to print a formated string
# with the values of the var's 'age', 'height', and
# 'weight' inserted, respectively, into the
# placeholder brackets within.
# PROBLEMS W/ THIS LINE: I would have followed the
# placeholder {age} with the string "years old,"
# instead of just "old," because when typing the
# answer to the input querry "How old are you?"
# I think the typical english speaker is more likely
# to simply type the number of their age rather than
# the number of their age + the word 'years'.
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# This line is intended to import a text file into
# the script.
# PROBLEMS W/ THIS LINE: There isn't an import
# statement preceding this line.
script, filename = argv

# This line is intended to open the imported text
# file and assigne the value of the oppened file
# object to var 'txt'.
# PROBLEMS W/ THIS LINE: the argument name that the
# file object has been assigned to is spelled wrong.
txt = open(filenme)

# This line is intended to print a formated string
# with the name of the imported file object inserted
# into the placeholder.
# PROBLEMS W/ THIS LINE: There is not a 'f' symbol
# preceding the formated string.
print("Here's your file {filename}:")
# This line is intended to read and then print the
# value of the file object attached to var 'txt'.
# PROBLEMS W/ THIS LINE: The name of the var is
# misspelled.
print(tx.read())

# This line is intended to print a string that will
# serve as an explanation to the user of the input
# querry, for which they are being prompted by the
# next line.
# PROBLEMS W/ THIS LINE: None. Personally, if I were
# to write this line and the next one, I would have
# combined them into one line, using the string in
# the print statement as the querry for the input.
print("Type the filename again:")
# This line is intended to create the var 'file_again'
# and assign it an input provided by the user.
# PROBLEMS W/ THIS LINE: none but also see above
# "PROBLEMS W/ THIS LINE:" section.
file_again = input("> ")

# This line is intended to open the file object,
# importd by the user via the input statement,
# and assigne its value to var 'txt_again'.
# PROBLEMS W/ THIS LINE: none.
txt_again = open(file_again)

# This line is inteded to read the value of the
# opened file object attached to var 'txt_again',
# thus returning that value to the script, and then
# print that returned value.
# PROBLEMS W/ THIS LINE: the 'read' command needs
# to attache to the target object's name with a
# '.' character. The progammer in this example has
# accidentally used a '_' character instead which
# creates an undefinged var name 'txt_again_read'
# and will return an error message to the terminal
# when this program is run.
print(txt_again_read())


print('Let's practice everything.')
print('You\'d need to know \'bout escapes
      with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------)
print(poem)
print(--------------")


five = 10 - 2 + 3 -
print(f"This should be five: {five}"

def secret_formula(started)
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars  100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(startpoint)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cates = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs
    print("People are less than or equal to dogs.)


if people = dogs:
    print("People are dogs.")



# This line is intended to
# PROBLEMS W/ THIS LINE:
