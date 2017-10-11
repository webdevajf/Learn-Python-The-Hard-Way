# This line creates the var 'formatter' and gives it the value of four placeholders.
formatter = "{} {} {} {}"

# This line assignes the integers 1, 2, 3, & 4, respectively, to the four placeholders in the value of var 'formatter' and then prints '1, 2, 3, 4'.
print(formatter.format (1, 2, 3, 4))
# This line assigns the strings "one", "two", "three", and "four", respectively to the four placeholders in the value of var 'formatter' and then prints 'one, two, three, four'.
print(formatter.format("one", "two", "three", "four"))
# This line assigns the booleans 'True', 'False', 'False', and 'True', respectively to the four placeholders in the value of var 'formatter' and then prints 'True, False, False, True'.
print(formatter.format(True, False, False, True))
# I'm not yet clear what this line will do but my guess is that it takes var 'formatter' and places four coppies of its own value into its placeholders. In other words it inserts 16 empty placeholders into 4 placeholders and my guess is that it will print a blank line.
# I was wrong! It printed sixteen individual placeholders like this: "{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}".
print(formatter.format(formatter, formatter, formatter, formatter))
# Lines 13 through 18 assigns the strings "Try your", "Own text here", "Maybe a poem", "Or a song about fear" to each of the four placeholders, respectively, and then prints the string "Try your Own text here Maybe a poem Or a song about fear".
# An interesting thing to note is that because the four smaller strings were connected using a comma instead of a "+" the computer has placed a space between them whereas, if a "+" had been used the space would have needed to have been placed manually into the end of the first three strings or into the beginning of the last three strings, otherwise it would have printed "Try yourOwn text hereMaybe a poemOr a song about fear".
# Another thing of note is that even though the four individual strings were each given their own line, within the code, they were all printed in one line together. I think this means that, should I want to print the four strings onto four respective lines, I need to put each string into its own "print(formater.format("some string"))" argument on each line.
# Interesting thing: I think the # line right above this one is wrong! If I attempted to do that I think all four lines would read as errors because each "formatter.format("some string")" argument would leave three placeholders empty making it impossible for the arument to express and then print! I think that what has to happen, if I wanted the argument to print, is that I need to reorganize the value of the var so that, within the quotes, each placeholder has it's own line. I will try it in "ex8a.py" and then print below wheather it worked or not.
# It did NOT work. I think if I want to do something like that the only way I can see to doing it right now is to make a var that has one placeholder and then express it four times, with each respective string, on four different lines.
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))
