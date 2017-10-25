# This line tells the computer to import arguments, that you write out in the terminal before you run the script, into the 'argv' var.
from sys import argv

# This line creates space for two values, named 'script' & 'filename' respectively, to be passed into the 'argv' var.
script, filename = argv

# This line creates the var 'txt', assigns it the value of the value of 'filename'(which is 'ex15_sample.txt') and uses the command 'open' to open the text file within the script.
txt = open(filename)

# This line embeds the value 'filename', as a string, within the string "Here's your file {}: " and then prints that string with the value 'filename' embeded in the string as a substring.
# Note: The value being held in 'filename' is the actual name of the file that you pass into the terminal: 'ex15_sample.txt'. It is NOT the text contained within 'ex15_sample.txt'.
print(f"Here's your file {filename}:")
# This line tells the computer to actually read the text file 'ex15_sample.txt' that you that you embeded, as a value, into 'argv' and opened within the script when you assigned the value to var 'txt'.
print(txt.read())

# This line prints the string "Type the filename again:".
print("Type the filename again:")
# This line creates the var 'file_again' and makes it's value an input from the user. It also prompts the user to give an input by printing the string "> ".
# Zed instructs us to put 'ex15_sample.txt' as the input.
file_again = input("> ")

# This line and the print statement below (line 26) accomplish the same thing as lines 8 and line 14 above. The difference is that in the lines above 'ex15_sample.txt' is imported to the script using an import command and assigning the value of the text file to an 'argv' whereas here the value of the text file has been imported into the script using an input command.
txt_again = open(file_again)

# See line 22.
print(txt_again.read())
