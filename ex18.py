# this one is like your scripts with argv
def print_two (*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2:{arg2}")

# ok, that* args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2:{arg2}")

# ths just takes one argument
def print_one(arg1):
    print (f"arg1: {arg1}")

# this one takes no aguments
def print_none():
    print("I got nothin'.")

print_two("Alex", "Friedman")
print_two_again("Alex", "Friedman")
print_one("First!")
print_none()
