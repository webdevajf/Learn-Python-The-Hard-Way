from sys import argv

script, filename = argv

string_text = open(filename)
print("ex16.txt reads: ")
print(string_text.read())
print(" ")

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" +  line3 + "\n")

print ("And finally, we close it.")
target.close()

print(" ")
string_text = open(filename)
print("Now ex16.txt says: ")
print(string_text.read())
