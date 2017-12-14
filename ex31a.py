print ("""You enter a dark room with three doors.
Do you go through door #1, door #2, or door #3.""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs of. Good Job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powdered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("""You see Darth Vader offering you a pint of gunness and beconing you to \'come here and join the dark side\'.""")
    print("1. Have a beer with Darth Vader and join the dark side.")
    print("2. Kick Darth Vader in his robot nuts, grab the pint and run away!")
    print("3. Draw your lightsaber.")

    fate_of_galaxy = input("> ")

    if fate_of_galaxy == "1" or fate_of_galaxy == "2":
        print("Darth Vader force chokes you to death.")

    else:
        print("Darth Vader draws his lightsaber.")
        print("1. You lunge at him with your lightsaber held high.")
        print("2. You wait in a defensive stance and becon him to \'come at me bro\'.")
        print("3. In terror, you shit into your hand and throw it at his face.")

        battleroyal = input ("> ")

        if battleroyal == "1" or battleroyal == "2":
            print("Darth Vader cuts you in half.")
            print("Valar Morgulis... bitches.")

        else:
            print("Your feces gets caught in Darth Vader\'s mouth vent thingy.")
            print("He suffocates on feces.")
            print("You saved the galexy! Hurrey!!!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
