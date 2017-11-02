# This line creates a function called 'cheese_and_crackers'
# and gives that function two variables: 'cheese_count'
# and 'boxes_of_crackers'
# The four indented lines, within the function, print strings.
# The first string holds a placeholder to embed whatever value
# is passed to var 'cheese_count' within the function.
# The second string holds a placeholder to emberd whatever value
# is passed to var 'boxes_of_crackers'. The third string is just
# a string and the fourth is a string with a \n command at the
# end of it (I don't know why that's there since there's nothing
# that comes after it to be placed on a new line...?)
# Key to remember: everything within this function will only be
# expressed in the terminal if the function is run (which is
# accomplished by naming the funciton within the script).
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# This line print's a string.
print("We can just give the function numbers directly:")
# This line expresses the function and passes the value 20
# to var 'cheese_count' and the value 30 to var 'box_of_crackers'
cheese_and_crackers(20,30)

# This line prints a string
print("OR, we can use variables from our script:")
# This line creates a var called 'amount_of_cheese' and assignes it
# an int value of 10.
amount_of_cheese = 10
# This line creates a var called 'amount_of_crackers' and assignes it
# an int value of 50
amount_of_crackers = 50

# This line takes the previously defigned var's 'amount_of_cheese'
# and 'amount_of_crackers' and, respectively, passes their values
# to the var's 'cheese_count' and 'boxes_of_crackers' withing the
# 'cheese_and_crackers' function. It then run's the
# 'cheese_and_crackers' function with those values embedded.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# This line prints a string.
print("We can even do math inside too:")
# This line runs the function 'cheese_and_crackers' with the int
# value of 10 + 20 & 5 + 6 being passed to the var's 'cheese_count'
# and 'boxes_of_crackers' respectively.
cheese_and_crackers(10 + 20, 5 + 6)

# This line prints a string.
print("And we can combine the two, variables and math:")
# This line #1 adds the int value of 100 to the value of var
# 'amount_of_cheese' and then passes that new value to var
# 'cheese_count' within function 'cheese_and_crackers' #2 it adds
# the int value of 1000 to the value of var 'amount_of_crackers'
# and then passes that new value to var 'boxes_of_crackers' within
# function 'cheese_and_crackers'. #3 it runs function
# 'cheese_and_crackers' with those values passed into their respective
# placeholders.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
