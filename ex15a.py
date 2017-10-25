#from sys import argv

#script, filename = argv

#txt = open(filename)

#print(f"Here's your file {filename}:")
#print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

# I don't really find either method to be superior to
# the other but I do personally preffer the latter
# method to the former. It seems like an easier way
# to stay organized and avoid mistakes if you can
# have a prompt reminding you what needs to be written
# rather than needing to remember everything all at
# once when you're typing in the command line.
