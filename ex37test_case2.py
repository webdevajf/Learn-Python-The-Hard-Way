from sys import argv
script, filename = argv

with open(filename, 'r+') as txt:
    w = "1,2,3\n"
    print("\nfile.txt says: ")
    print(txt.read(), "\n")
    txt.seek(0)
    print("We are truncating that and writing something new.")
    txt.truncate()
    txt.write(w)
    txt.seek(0)
    print("now file.txt says: ")
    print(txt.read())
    txt.close

with open(filename, 'r+') as txt:
    w = "a,b,c\n"
    print("\nLets change file.txt bak to 'a,b,c' from '1,2,3'.")
    print("\nCurrently file.txt says: ")
    print(txt.read())
    txt.seek(0)
    print("We are truncating that and writing something new.")
    txt.truncate()
    txt.write(w)
    txt.seek(0)
    print("file.txt once again says: ")
    print(txt.read())
    txt.close
