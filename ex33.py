# This line creates var 'i' and give it a value of
# int 0.
i = 0
# This line creates var 'numbers' and gives it a value
# of an empty braket "[]"
numbers = []

# This line creates a while loop and give it the
# condition that it's code will run as long as the
# value of var 'i' is less than int 6.
while i < 6:
    # This line prints a formated string with a
    # placeholder that takes the value of var
    # 'i'
    print(f"At the top i is {i}")
    # This line appends the value of var 'i' to
    # the list object which is the value of var
    # 'numbers'.
    numbers.append(i)

    # This line adds the value of int 1 to the value
    # of var i. Another way to write this is "i += 1".
    i = i + 1
    # This line prints a string and then prints the
    # value of var 'numbers'
    print("Numbers now: ", numbers)
    # This line prints a formated string with a
    # placeholder that takes the value of var 'i'.
    # Note: the key here is that the value of var 'i'
    # has changed as it passed throught the function
    # and it will now be different then it was at the
    # top of the function (in the while loops first
    # print statement).
    print(f"At the bottom i is {i}")
    # Because it is in a while loop the computer will,
    # at this point, return to the top of the while loop
    # and evaluate it's condition. If the condition
    # evaluates to true the while loop will run again.
    # If the condition evaluates to false it will move
    # on to the first line in the script that
    # follows the while loops code. The loop will run
    # 6 times.



# This line prints a string.
print("The numbers: ")

# This line creates a for loop that reads var 'numbers'
# and passes it's value into the loop's arg 'num'.
# Since the value of var 'numbers' is a list object it
# will pass the elements from the list into the arg of
# the loop, one at a time, reading the for loop and
# running its code each time. It will run 6 times.
for num in numbers:
    # This line prints the value that has been passed
    # into arg 'num' with each particular running of
    # the for loop.
    print(num)
