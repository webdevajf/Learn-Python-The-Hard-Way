# This line imports argument var's
from sys import argv

# This line creates space for two argument var's (one
# of them being the script) and name's them
# 'script' and 'filename' within the script.
script, filename = argv

# The next three lines print strings. The first line
# formats the argv 'filename' within the string that
# that line prints.
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

# this line asks the user for an input by prompting
# them with a "?" string.
input("?")

# This line prints a string.
print("Opening the file...")
# This line creates the var 'target' and assigns
# it the value of the opened var 'filename' and
# the string 'w' which, to be honest, I don't yet
# understand. How does an 'open' command work on
# a string?
target = open(filename, 'w')

# This line prints a string.
print("Truncating the file. Goodbye!")
# This line performs the 'truncate' command on var
# 'target' which apparently, according to Shaw
# empties the contents of a file. I don't yet know
# for sure if I understand what that means... It
# deleats everything? What about that string 'w'?
target.truncate()

# This line prints a string.
print("Now I'm going to ask you for three lines.")

# The next three lines create three var's:
# 'line1', 'line2', and 'line3' respectively
# and then prompt the user for inputs to assign
# to those var's.
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# This line prints a string.
print("I'm going to write these to the file.")

# These lines, i'm guessing, write the values
# of var's 'line1', 'line2', and 'line3' to the
# text file assigned to var 'target' and format
# each of those variables as individual lines.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# this line writes a string.
print ("And finally, we close it.")
# this line closes the file and, effectively,
# saves it as is.
target.close()
