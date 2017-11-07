# This line creates an import for arguments
# typed into the command line.
from sys import argv

# This line defines 'argv' as two inputs from
# the command line: 'script' and 'input_file'.
script, input_file = argv

# The first line of this function creates a function
# called 'print_all' and gives it a variable 'f'
# so that values can be passed into it.
# The next line within the function tells the
# computer to read the 'f' var within the script
# and then print the value of 'f'.
def print_all(f):
    print(f.read())

# The first line of this function creates the function
# 'rewind' and give's it a var 'f' so that value's can
# be passed into it. The next line of the function
# instructs the computer to seek the first character
# in the 'f' var's value (the one that is in the
# "zeroith" position.)
def rewind(f):
    f.seek(0)

# The first line of this function creates the function
# 'print_a_line' and give it two vars 'line_count' &
# 'f' so that two values can be passed into it.
# The next line in the function instructs the computer
# to express whatever value is passed into the
# function's 'line_count' value, to read the first line
# in whatever value is passed into the 'f' value (and
# to keep track of which line, in that value, the
# .readline command is currently on) and then it prints
# whatever text has come out of expressing 'line_count'
# and reading 'f'.
def print_a_line(line_count, f):
    print(line_count, f.readline())

# This line creates a var 'curren_file' and gives it the
# value of performing an 'open' command on the argv,
# that has been passed into the 'input_file' value of
# argv, within the script.
current_file = open(input_file)

# This line prints a string
print("First let's print the whole file:\n")

# This line passes the 'current_file' var into the
# 'print_all' function and then prints the outcome
# in the terminal.
print_all(current_file)

# This line prints a string.
print("Now let's rewind, kind of like a tape.")

# This line passes the 'current_file' var into the
# 'rewind' function and then prints the outcome in
# the terminal.
rewind(current_file)

# This line prints a string.
print("Let's print three lines:")

# This line creates a var 'current_line' and
# assigns it the value of the int '1'.
current_line = 1
# This line passes the current value of the
# 'current_line' var into the 'line_count' value
# within the function 'print_a_line' and it also
# passes the value of var 'current_file' into the
# 'f' value of the 'print_a_line' function. It then
# prints the outcome, of those two variables being
# processed within the function, to the terminal.
# Note on the 'current_file' var: within the
# 'print_a_line function' the 'current_file' var is
# being placed within the 'f' value which has the
# '.readline()' command attached to it. This causes
# the 'print_a_line' functon to read a specific line
# within the text file that the 'current_line' var
# has opened and then keeps track of what line within
# the text file has just been read. Should the script
# engage the '.readline()' command yet again, it will
# read the next line down from the one that it last read
# and will then stop, once again, at the end of that
# line and keep track of its current positon. In this
# case the function has caused the computer to read
# the first line.
print_a_line(current_line, current_file)

# This line reassigns the var 'current line' the
# value of it's own previous value plus the value
# of the int '1'.
current_line = current_line + 1
# This line passes the current value of the
# 'current_line' var into the 'line_count' value
# within the function 'print_a_line' and it also
# passes the value of var 'current_file' into the
# 'f' value of the 'print_a_line' function. It then
# prints the outcome, of those two variables being
# processed within the function, to the terminal.
# Note on the 'current_file' var: within the
# 'print_a_line function' the 'current_file' var is
# being placed within the 'f' value which has the
# '.readline()' command attached to it. This causes
# the 'print_a_line' functon to read a specific line
# within the text file that the 'current_line' var
# has opened and then keeps track of what line within
# the text file has just been read. Should the script
# engage the '.readline()' command yet again, it will
# read the next line down from the one that it last read
# and will then stop, once again, at the end of that
# line and keep track of its current positon. In this
# case the function has caused the computer to read
# the second line.
print_a_line(current_line, current_file)

# This line reassigns the var 'current line' the
# value of it's own previous value plus the value
# of the int '1'.
current_line = current_line + 1
# This line passes the current value of the
# 'current_line' var into the 'line_count' value
# within the function 'print_a_line' and it also
# passes the value of var 'current_file' into the
# 'f' value of the 'print_a_line' function. It then
# prints the outcome, of those two variables being
# processed within the function, to the terminal.
# Note on the 'current_file' var: within the
# 'print_a_line function' the 'current_file' var is
# being placed within the 'f' value which has the
# '.readline()' command attached to it. This causes
# the 'print_a_line' functon to read a specific line
# within the text file that the 'current_line' var
# has opened and then keeps track of what line within
# the text file has just been read. Should the script
# engage the '.readline()' command yet again, it will
# read the next line down from the one that it last read
# and will then stop, once again, at the end of that
# line and keep track of its current positon. In this
# case the function has caused the computer to read
# the third line.
print_a_line(current_line, current_file)
