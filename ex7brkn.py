print("Mary had a little lamb.")
# Multiple things wrong here.
# The 'f' command at the begining of the print statement needs to be eliminated. That is only necessary for formating placeholder brackets when you are embeding the value of a variable.
# The '$' character within the string should be deleated. It's simply an extranious part of the string that will print when the string is expressed in the terminal.
# The 'snow' characters within the placeholder brackets should be deleated. That is not how placeholder brackets work.
# The command '.format('snow')' should be placed within the brackets of the print statement, following the string. Doing so will embed the string in the placeholder when it is printed in the terminal.
print(f"Its fleece was white as ${snow}.").format('snow')
print("And everywhere that Mary went.")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
