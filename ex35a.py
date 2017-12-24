from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
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
    print("You're dead. In life, were you good or bad?")

    where_to = input("> ")

    if where_to == "good":
        print("We're going to send you to heven!")
        heven()
    elif where_to == "bad":
        print("You're going to hell!")
        hell()
    else:
        print("You never learned how to commit yourself.")
        print("We're sending you're boring ass to purgatory,")
        start()

def heven():
    print("OHHH SHIT your in heven!!!")
    print("Are you going to chill peacefully and do angel stuff or are you going to lead a rebellion and take over like a boss?")

    serve_or_reign = input("> ")

    if "chill" in serve_or_reign:
        print("Play that harp like a beast!")
        exit(0)
    elif "lead" in serve_or_reign or "rebellion" in serve_or_reign:
        print("That's badass but you don't have the stones to overthrow the almighty.")
        print("You get cast out and sent to hell.")
        hell()
    elif "take" in serve_or_reign or "boss" in serve_or_reign:
        print("That's badass but you don't have the stones")
        print("to overthrow the almighty.")
        print("You get cast out and sent to hell.")
        hell()
    else:
        print("They shoulda sent your indecisive ass to purgatory.")
        exit(0)

def hell():
    Torture = True
    print("OHHH SHIT your in hell!!!")
    print("The devil comes out to greet you.")
    print("He's so impressed with how bad you've been that he's not going to torture you! You're one of his homies!")
    print("He wants to give you a job!")
    print("You're going to intern with King Minos, learning how to assign different souls to different circles of hell.")
    print("Are you going to accept the job, refuse the job, or lead a rebellion in hell?")

    internship_or_no = input("> ")

    if "accept" in internship_or_no:
        print("NICE! You got job security for all eternity!")
        exit(0)
    elif "lead" in internship_or_no or "rebellion" in internship_or_no:
        while Torture == True:
            print("That's ballsy but you don't have the stones to overthrow the devel.")
            print("Deamons torture you forever!")
            print("Torture! Ouch!")
            print("Hit \'Ctrl C\' to end this infinite loop.")
    elif "refuse" in internship_or_no:
        while Torture == True:
            print("Deamons torture you forever!")
            print("Torture! Ouch!")
            print("Hit \'Ctrl C\' to end this infinite loop.")
    else:
        while Torture == True:
            print("Deamons torture you forever!")
            print("Torture! Ouch!")
            print("Hit \'Ctrl C\' to end this infinite loop.")

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
