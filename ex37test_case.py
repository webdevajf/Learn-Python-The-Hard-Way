from sys import argv

script, filename = argv

txt = open(filename, 'r+')

print(f"\nfirst, Here's your file {filename}:\n")
print(txt.read())

w = "a, b, c"

txt.truncate(0)
print(f"\nsecond, Here's your file {filename}:\n")
print(txt.read())

print(f"\nthird, Here's your file {filename}:\n")
print(txt.write(w))
print(txt.read())

txt.close()
