# Imports argv's, that the user writes in the
# terminal into the script.
from sys import argv
# Don't know yet.
from os.path import exists

# Creates space and representations of three
# argv's
script, from_file, to_file = argv

# Prints a string that is formated with two argv's.
print(f"Copying from {from_file} to {to_file}")

# # we could do these two on one line, how?
# Creates a var 'in_file' which is assigned the
# value of the opened var 'from_file'.
in_file = open(from_file)
# Creates the var 'indata' which reads the value
# of var 'in_file'.
indata = in_file.read()

# Prints a string. not sure yet what the deal with the
# formatting is...? May just express litterally,
# as part of the string.
# It didn't express litterally. It actually expressed
# The numerical length of the 'indata' var.
print(f"The input file is {len(indata)} bytes long")

# The next two lines print strings. not yet sure what
# the deal with the formatting is on line 1...? May
# just express litterally, as part of the string.
# Also didn't express litterally. It actually asked the
# computer if the 'to_file' existed within the current
# directory and returned a 'True' boolian! pretty cool.
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
# Asks the user for an input.
input()

# Creates the var 'out_file' which is assigned the
# value of the opened 'to_file' var with the 'write'
# mode enabled.
out_file = open(to_file, 'w')
# writes the value of var 'indata' aka the value of
# the 'from_file' argv into the out_file.
out_file.write(indata)

# prints a string.
print("Alreight, all done.")

# Closes argv 'out_file'.
out_file.close()
# closes argv 'in_file'.
in_file.close()
