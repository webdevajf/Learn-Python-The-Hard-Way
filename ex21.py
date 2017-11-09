# This line creates the function 'add' and gives it
# the parameters 'a' and 'b' for passing 2 values
# into, respectively.
# Within the function: the first line prints a
# formated string with placeholders for the values
# that get passed into prams 'a' & 'b'.
# The second line within the function returns, to the
# script, the value of var 'a' and var 'b' being
# added to eachother.
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

# This line creates a function 'subtract' with
# the prams 'a' and 'b'.
# The first line of instruction prints a formated
# string with placeholders for the values passed
# into prams 'a' and 'b'.
# The second line of instruction returns the value,
# to the script, of subtracting the value of pram
# 'b' from the value of pram 'a'.
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

# This line creates the function 'multiply' with
# the prams 'a' and 'b'.
# The first line of instruction prints a formated
# string with placeholders for the values of prams
# 'a' and 'b'.
# The second line of instruction returns the value
# of pram 'a''s value and pram 'b''s value, multiplied
# by eachother, to the script.
def multiply (a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

# This line creates the function 'divide' with the
# prams 'a' and 'b'.
# The first line of instruction prints a formated
# string with placeholders for the values of prams
# 'a' and 'b'.
# The second line of instruction returns, to the
# script, the value of pram 'a' divided by the value
# of pram 'b'.
def divide (a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

# This line prints a string.
print("Lets's do some math with just functions!")

# This line creates a var 'age' and assigns it
# the value of the function 'add' with the values of
# int 30 and int 5 passed into it's prams 'a'
# and 'b', respectively.
age = add(30, 5)
# This line creates the var 'height' and assigns
# it the value of the function 'add' with the
# values of int 78 and int 4 passed into it's prams
# 'a' and 'b', respectively.
height = subtract(78, 4)
# This line creates the var 'weight' and assigns it
# the value of the function 'multiply' with the values
# of int 90 and int 2 passed into its prams 'a' and
# 'b', respectively.
weight = multiply(90, 2)
# This line creates the var 'iq' and assigns it the
# value of the function 'divide' with the values
# of int 100 and int 2 passed into its prams
# 'a' and 'b', respectively.
iq = divide(100, 2)

# This line prints a formated string with placeholders
# for the values of vars 'age', 'height', 'weight',
# and 'iq'.
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
# This line prints a string.
print("here is a puzzle.")

# This line creates the var 'what' and assignes it
# a value that I would have a hard time describing
# in english but essentially, if i've calculated
# correctly it's value will end up being -4391.
# I got it right but I forgot one thing: While
# var 'what' runs throught the various lines of
# code in all of these variables and functions,
# along with actually doing the math operations
# in the various functions return statements,
# it also will express their print statements
# within the terminal.
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# This line prints a string "That becomes: "
# concatinated with the value of var 'what' and
# concatinated with the string "Can you do it by
# hand?"
print("That becomes: ", what, "Can you do it by hand?")
