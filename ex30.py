# This line creates var 'people' and assigns it a value
# of int 30
people = 30
# This line creates var 'cars' and assigns it a value
# of int 40
cars = 40
# This line creates var 'trucks' and assigns it a value
# of int 15
trucks = 15

# This line creates an 'if' statement with a condition
# that the value of var 'cars' be greater than the
# value of var 'people' inorder for its code to run.
# It also begins a block of branching code.
if cars > people:
    # This line prints a string.
    print("We should take the cars.")
# This line continues the block of branching code with
# an 'elif' statement which holds the condition that
# the value of var 'cars' must be less than the value of
# var 'people' for it's code to run.
elif cars < people:
    # This line prints a string.
    print("We should not take the cars.")
# This line continues the block of branching code
# with an 'else' statement. This statement's code
# will run if the conditions of the above 'if' and
# 'elif' statement are not satisfied.
else:
    # This line prints a string.
    print("We can't decide.")

# This line creates an 'if' statement with the
# condition that the value of var 'trucks' be
# greater than the value of var 'cars' in order
# for its code to run. It also begins a block of
# branching code.
if trucks > cars:
    # This line prints a string.
    print("That's too many trucks.")
# This line continues the block of branching code
# with an 'elif' statement which holds the condition
# that the the value of var 'trucks' must be greater
# than the value of var 'cars' for its code to run.
elif trucks < cars:
    # This line prints a string.
    print("Maybe we could take the trucks.")
# This line continues the block of branching code with
# an 'else' statement. This statemens code will run
# if the conditions of the 'if' and 'elif' statements
# are not satisfied.
else:
    # This line of code will print a string.
    print("We still can't decide.")

# This line of code creates an 'if' statement with the
# condition that the value of var 'people' must be
# greater than the value of var 'trucks'inorder for it
# to run its code. This also initiates a block of
# branching code.
if people > trucks:
    # This line prints a string.
    print("Alright, let's just take the trucks.")
# This line of code continues the block of branching
# code with an 'else' statement, which will run its
# code if the conditions for the 'if' statement are
# not satisfied.
else:
    # This line prints a string.
    print("Fine, let's stay home then.")

# Study Drills

#1
# Q: Try to guess what 'elif' and 'else' are doing.
# A: They're clearly creating differnet branches in
# code each of which will activate if certain
# conditions are met. An interesting question to ask
# here is why would we not accomplish the same thing
# by simply using multiple 'if' statements? The
# answer is that by utalizing 'if', 'elif', and 'else'
# we create a 'block' of code wherein all the different
# lines of code work in tandem with eachother. The
# computer reads the block of code line by line untill
# it reaches a condition that it can satisfy and then
# runs the code contained in that 'if', 'elif', or
# 'else' statement. The other key thing is that, once
# the conditions are met within this 'if', 'elif',
# 'else' statement, the computer skips over the rest
# of the block. This means that even if both the 'if'
# statemet and the 'elif' statement evaluate to true
# the 'elif' statement will not be read beacause, once
# the computer has picked the 'if' statement's code
# to run, it will skip over the rest of the block.
