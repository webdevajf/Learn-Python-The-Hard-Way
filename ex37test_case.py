from sys import argv

(script, filename) = argv

with open(filename, 'r+') as txt:

    print(f"\nfirst, Here's your file {filename}:\n")
    print(txt.read())
    txt.seek(0)
    data = txt.read()
    w = ""
    if data == "a":
        w += "1"
    else:
        w += "a"

    txt.seek(0)
    txt.truncate()
    print(f"\nsecond, Here's your file {filename}:\n")
    print(txt.read())

    print(f"\nthird, Here's your file {filename}:\n")
    txt.write(w)
    txt.close()

with open(filename, 'r+') as txt:
    print(txt.read())
    txt.close()
