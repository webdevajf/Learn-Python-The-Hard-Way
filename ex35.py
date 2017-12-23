#This line imports something but i'm not sure what...?
from sys import exit

# This line creates function 'gold_room'
def gold_room():
    # This line prints a string
    print("This room is full of gold. How much do you take?")

    # This line creates var 'chocie' within function
    # 'gold_room' and give it the value of an input
    # from the user
    choice = input("> ")
    # This line creates an if statement that begins
    # an "if-else" block of code. The parameter for
    # this 'if' statement to run its code is that
    # var choice be given a value by the user that
    # contains int '0' or int '1' in it.
    if "0" in choice or "1" in choice:
        # This line of code creates a var 'how_much'
        # and gives it a value the string value of
        # var 'choice' converted into an int.
        how_much = int(choice)
    # This line creates the else statement in this
    # 'if-else' block of code. Its parameter for
    # running its code is that the 'if' statement
    # not run its code.
    else:
        # This line calls the function 'dead'
        # and passes a string into it as an arg.
        dead("Man, learn to type a number.")

    # This line creates an 'if' statement within
    # another 'if-else' block of code within function
    # 'gold_room'. This if statement's parameter for
    # running its code is that var how much, in the
    # above 'if-else' block in this function be
    # assigned a value of less than int 50.
    if how_much < 50:
        # This line prints a string.
        print("Nice, you're not greedy, you win!")
        # Ok not totally sure about this but I think
        # this line runs the 'exit' function which I
        # think was loaded in the first line of code.
        # I don't understand why int '0' is being passed
        # into it as an arg though.
        exit(0)
    # This line creates the else statement in this
    # 'if-else' block of code. Its parameter to run is
    # that the if statement in this block not run its
    # code
    else:
        # This line calls function 'dead' and passes a
        # string into it as an arg.
        dead("You greedy bastard!")

# This line creates function 'bear_room'.
def bear_room():
    # This line prints a string.
    print("There is a bear here.")
    # This line prints a string.
    print("The bear has a bunch of honey.")
    # This line prints a string.
    print("The fat bear is in front of another door.")
    # This line prints a string.
    print("How are you going to move the bear?")
    # This line creates var 'bear_moved' and gives
    # it a value of boolean 'False'.
    bear_moved = False

    # This line simply creates an infinte loop using
    # boolean logic. Since the while statement
    # evaluates to 'True', without actually having
    # a parameter, it simply runs its code (below)
    # when the computer reads this line of code.
    while True:
        # This line creates var 'choice' and gives
        # it a value of an input from the user.
        choice = input("> ")

        # This line creates an 'if' statement and
        # begins an 'if-elif-else' block of code.
        # This if statements parameter for running
        # its code is that var 'choice' is equal to
        # the value of the string "take honey".
        if choice == "take honey":
            # This line calls function 'dead' and passes
            # a string into it as an arg.
            dead("The bear looks at you then slaps your face off.")
        # This line creates an 'elif' statement within
        # an 'if-elif-else' block of code. It has two
        # parameters for running its code. The first is
        # that the value of var 'choice' be equivilent
        # to the string 'taunt bear'. The second is
        # somewhat complicated to explain: var
        # 'bear_moved' is, at this point, equal to
        # 'False' meaning that if var 'bear_moved' is
        # used as a parameter that parameter won't be met
        # because 'bear_moved' would need to evaluate to
        # 'True' for that parameter to be met. In this
        # case the code states that the parameter is
        # "not bear_moved" what this means is that
        # "not(bear_moved)" == "not(False)" == "True"
        # meaning that the parameter evaluates to "True"
        # meaning that the parameter is met!
        elif choice == "taunt bear" and not bear_moved:
            # This line prints a string.
            print("The bear has moved from the door.")
            # This line prints a string.
            print("You can go through it now.")
            # This line changes the value of var 'bear_moved'
            # to 'True'.
            bear_moved = True
            
        elif choice == "taunt bear" and bear_moved:
            # This line calls function 'dead' and passes
            # a string into it as an arg.
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
