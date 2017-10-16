formatter = "{} {} {} {}"

print(formatter.format (1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
# He's made the first letters of all the boolians lowercase so that they don't work.
print(formatter.format(true, false, false, true))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"Try your",
"Own text here",
"Maybe a poem",
"Or a song about fear"
))
