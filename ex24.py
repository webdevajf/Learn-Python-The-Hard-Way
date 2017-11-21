# This line prints a string.
print("Let's practice everything.")
# This line prints a string with several escape
# characters, including two escaped single quotes
# and an escaped backslash.
print('You\'d need to know \' bout escapes with \\ that do:')
# This line prints a string with a newline character
# and a tab character.
print('\n newlines and \t tabs.')

# lines 12 - 19 (5 - 12 in ex24br.py) create var
# 'poem' and give it the value of a string that
# has been formated with trippel double quotes.
# The string features a tab character in its
# first line, a newline character in its third
# line and a newline character followed by two
# tab characters in its final line.
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuiton
and requires an explanation
\n\t\twhere there is none.
"""

# This line prints a string.
print("--------------")
# This line prints var 'poem'.
print(poem)
# This line prints a string.
print("--------------")

# This line creates var 'five' and assigns it the
# value of 10 - 2 + 3 - 6 which will evaluate to
# int 5.
five = 10 - 2 + 3 - 6
# This line prints a formated string with the
# value of var 'five' appearing in the placeholder.
print(f"This should be five: {five}")

# This line creates the function 'secret_formula'
# and gives it space for one argument, tittled
# 'started' to be passed into it.
def secret_formula(started):
    # This line creates var 'jelly_beans',
    # within function 'secret_formula', and
    # assignes it the value of arg 'started'
    # multiplied by int 500.
    jelly_beans = started * 500
    # This line creates var 'jars',
    # within function 'secret_formula', and
    # assignes it the value of var
    # 'jelly_beans' divided by int 1000.
    jars = jelly_beans / 1000
    # This line creates var 'crates',
    # within function 'secret_formula', and
    # assignes it the value of var 'jars'
    # divided by int 100.
    crates = jars / 100
    # This line causes the values of the 3
    # vars within the function to return to
    # the computer and be stored, within it's
    # memory, for later use when the function
    # is called.
    return jelly_beans, jars, crates

# This line creates var 'start_point' and assignes
# it the value of int 10000.
start_point = 10000

# I'm a little confused by this line but I'll make
# a guess as to what it does: I think that this
# line creates three vars, 'beans', 'jars', & 'crates',
# within the script and assigns to them, respectively,
# the three returned values that come out of running
# the function 'secret_formula' with var 'start_point'
# passed into it as an argument.
beans, jars, crates = secret_formula(start_point)

# This prints a string with a placeholder and then
# attaches a format command with var 'start_point'
# passed into it so that the var's value appears
# in the placeholder.
# # remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# This line, below the note, prints a formated string
# with three placeholders that have been assigned the
# values of var's 'beans', 'jars', and 'crates',
# respectively.
# # it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# This line takes the var 'start_point' divides its
# value by 10 then takes the output of that opperation
# and assignes it to var 'start_point' as its new
# value.
# note: a more efficient way to write this is =
# 'start_point /= 10'
start_point = start_point / 10

# This line prints a string.
print("We can also do that this way:")
# This line creates a var 'formula' and assignes
# it the value of function 'secret_formula' with
# the value of var 'secret_formula' passed into the
# function.
formula = secret_formula(start_point)
# This line, below the note, prints a string with
# with three placeholders and then attaches a format
# command to the string with the formula var passed
# into it so that it's values will be placed into
# the placeholders. note: I do not know what the
# purpose of the '*' symbol next to var 'formula'
# is nor how it will affect the outcome of running
# this script.
# Well I ran it with '*' and without '*' and with
# the symbol everything went off without a hitch
# but without I got an error message that said:
# "IndexError: tuple index out of range".
# I don't know what this means yet or why it needs
# a '*' to run the formula but I will keep this
# question in mind.  
# # This is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
