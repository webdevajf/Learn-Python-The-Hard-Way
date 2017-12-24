## The original way of doing function 'gold_room' takes
## The takes the user's answer to a question (which gets
## converted into a string) and assigns it to var
## 'choice' and then assigns the string value to var
## 'how_much' which converts it to an int value and then
## runs that int value through the functions parameters.


#def gold_room():
#    print("This room is full of gold. How much do you take?")
#
#    choice = input("> ")
#    if "0" in choice or "1" in choice:
#        how_much = int(choice)
#    else:
#        dead("Man, learn to type a number.")
#
#    if how_much < 50:
#        print("Nice, you're not greedy, you win!")
#        exit(0)
#    else:
#        dead("You greedy bastard!")

## This way of doing var 'gold_room' is much supperior
## to the previous  iteration of the function. Instead
## of running the users input through two var's that
## convert it into a usable form we only have var
## 'how_much' which converts the string input into a
## usable form immediatly. Furthermore we have
## eleminated, entirely, the parameter that the answer
## have a '0' or '1' in it which is unneccesarily
## restrictive an causes the program to break for any
## number of totally vallad answers that the user could
## be inclined to give. 
def gold_room():
    print("This room is full of gold. How much do you take?")

    how_much = int(input("> "))

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def dead(why):
    print(why, "Good job!")
    exit(0)

gold_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

gold_room()
