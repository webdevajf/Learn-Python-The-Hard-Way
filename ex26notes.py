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

# These 3 lines are intended to print strings.
# PROBLEMS W/ THESE LINES:
#1 the comma within the string, on the first line,
# is being read by python as a single quote which is
# causing python to cut the string of prematurely.
# The comma needs to be preceded by a backslash so
# that it can be escaped.
#2 The third line shouldn't be indented.
#3 All three of these lines should be in only
# one print statement, formated with tripple quotes
# (''' ''') or tripple double quotes (""" """).
print('Let's practice everything.')
print('You\'d need to know \'bout escapes
      with \\ that do \n newlines and \t tabs.')

# This line is intended to create a var 'poem' with
# the value of a a string that will be formated into
# multiple lines, newlines, and tabbed, the way that
# the programmer desires, due to the use of tripple
# double quotes.
# PROBLEMS W/ THIS LINE: none.
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# This line is intended to print a string.
# PROBLEMS W/ THIS LINE: the programmer forgot
# to close the string within the parentheses.
print("--------------)
# This line is intended to print the value of
# var poem.
# PROBLEMS W/ THIS LINE: none.
print(poem)
# This line is intended to print a string.
# PROBLEMS W/ THIS LINE: the programmer forgot to
# enclose the intended string in a double quote
# symbol and thus created a var name
# '(--------------' with no value that will return
# an error message when the script is run in the
# terminal.
print(--------------")

# This line is intended to create the var 'five'
# and assigns it the int value 5.
# PROBLEMS W/ THIS LINE: The math doesn't add up
# to the int value 5. There should be an int 6
# following the '-' sign.
five = 10 - 2 + 3 -
# This line is intended to print a formated string
# that incorporates the value of var 'five  into
# a placeholder.
# PROBLEMS W/ THIS LINE: The parentheses on the
# print statement was left open on the end.
print(f"This should be five: {five}"

# This line is intended to create a function
# 'secret_formula' with one designated arg named
# 'started'.
# PROBLEMS W/ THIS LINE: there is no ':' following
# the first line of the function.
def secret_formula(started)
    # This line is intended to create a var named
    # 'jelly_beans' within the function, with a
    # value of 500 multiplied by the value of arg
    # 'started'.
    # PROBLEMS W/ THIS LINE: none.
    jelly_beans = started * 500
    # This line is intended to create a var named
    # 'jars' within the function, with a value of
    # var 'jelly_beans'\'s value divided by 1000.
    # PROBLEMS W/ THIS LINE: none.
    jars = jelly_beans / 1000
    # This line is intended to create a var named
    # 'crates' within the function, with a
    # value of var 'jars'\'s value divided by 100.
    # PROBLEMS W/ THIS LINE: There is no '/' symbol
    # between var 'jars' and int 100.
    crates = jars  100
    # This line is intended to return the value of
    # var's jelly_beans, jars, crates to the computer.
    # PROBLEMS W/ THIS LINE: none.
    return jelly_beans, jars, crates

# This line is intended to create a var 'start_point'
# with an int value of 10000.
# PROBLEMS W/ THIS LINE: none.
start_point = 10000
# This line is intended to create the var's 'beans'
# 'jars' and crates with the respecteve values of
# the 3 returned values of function 'secret_formula'
# with var 'start_point' passed into it as an arg.
# PROBLEMS W/ THIS LINE: 'crates' is not specified
# on the left side of the '=' symbol as a var name.
beans, jars = secret_formula(start_point)

# This line, aftar the note, is intended to print
# a formated string using the ''.format()' command
# with var 'start_point' passed into the command
# so that its value will appear in the placeholder
# brackets within the string.
# PROBLEMS W/ THIS LINE: none.
## remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# This line, aftar the note, is intended to print
# a formated string with the values of var's 'beans',
# 'jars' and 'crates' passed into the three placeholder
# brackets withing the string, respectively.
# PROBLEMS W/ THIS LINE: none.
## remember that this is another way to format a string
## it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# This line is intended to divide the value of var
# 'start_point' by the int 10 and then reasign the
# output of that opperation to var start_point as
# its new value.
# PROBLEMS W/ THIS LINE: none but it would be better
# written like this: start_point /= 10
start_point = start_point / 10

# This line is intended to print a string.
# PROBLEMS W/ THIS LINE: none
print("We can also do that this way:")
# This line is intended to create a var 'formula'
# with the value of function 'secret_formula'\'s value
# with var 'start_point' passed into it as an arg.
# PROBLEMS W/ THIS LINE: var 'start_point' has between
# misspelled as 'startpoint'.
formula = secret_formula(startpoint)
# This line, below the note, is intended to print
# a formated, using the '.format()' command with
# var 'formula' passed into the command so that it's
# returned values appear in the placeholders within
# the string.
# PROBLEMS W/ THIS LINE: None but there is still the
# question of why the '.format()' command requires
# var 'formula' to be preceded by a '*' symbol inorder
# to work. When that character is removed the computer
# returns this error message: "IndexError: tuple index
# out of range". I still don't know what a tuple index
# is...?
## this is an easy way to apply a list to a format string
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
