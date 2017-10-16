days = "Mon Tue Wed Thu Fri Sat Sun"
# He's changed the last '\n' escape sequence to a '\t' so that it indent's instead of putting "Aug" onto a new line.
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\tAug"

print("Here are the days: ", days)
# He's brought the comma insde the string so that it becomes part of the string and no longer performs the function of providing proper syntax to the code.
print("Here are the months: ," months)

# On the string below he's added an extra '"' before 'or 5, or 6.'
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, "or 5, or 6."
""")
