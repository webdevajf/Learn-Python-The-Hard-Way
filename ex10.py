# This line creates var 'tabby_cat' and it assigns it the value: string "I'm tabbed in." the '\t' command, within the string, causes everything after it to be tabbed in.
tabby_cat = "\tI'm tabbed in."
# This line creates var 'persian_cat' and assigns it the value "I'm split on a line." and the '\n' command causes everything after itself to be moved down to the next line.
persian_cat = "I'm split\non a line."
# This line creates var 'backslash_cat' and assigns it the value "I'm \ a \ cat." The two '\' commands preceding '\ a' and '\ cat', respectively, ensure that the two '\' symbols, within the string, get printed as part of the string.
backslash_cat = "I'm \\ a \\ cat."

# This line creates the var 'fat_cat' and gives it the value of the string "I'll do a list: * Cat food * Fishies * Catnip * Grass". Enclosing the string in tripple quotes ensures that it will be formatted as seen below, instead of as a simple one line string. The one '\n' command causes the '* Grass' part of the string to be moved to the next line and the '\t' commands cause the parts of the string following them to be tabbed on the line that they appear on.
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# The next four lines print the values of the variables listed within their parenthasees.
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
