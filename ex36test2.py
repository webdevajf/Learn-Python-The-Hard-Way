## This is the 'test' document. This document exists
## to provide me a place to test and experiment with
## the game's code in a place that is isolated from
## then rest of the script.

## THE Z. SHAW CODING PROCESS:
#1 Write a to do list.
#2 Pick the easiest thing from your list.
#3 Describe the thing in your source code in English comments.
#4 Write code under the comments.
#5 run the code to see if it works.
#5 stay in the cycle of writing code, running it to test it, and fixing it untill
## it works.
#6 cross the task off your list, go to the next task, repeat.

# TO DO ITEM: function 'carpenter'


drawbridge = False
inventory = []
crew = []
bridge_problem_chain_explained = 0
bridge_problem_gears_explained = 1
pully = ["rusty chain", "rotten gears"]
gt_activated = []

def blacksmith():
    global bridge_problem_chain_explained
    print("\nYou are in the blacksmith's workshop. You look around and see her")
    print("working diligengly at her forge.")

    if bridge_problem_chain_explained == 0:
        print("\nYou can stay here or go back to the courtyard. What would you")
        print("like to do?")
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        else:
            blacksmith()

    elif bridge_problem_chain_explained == 1:
        print("\nYou can stay here, talk to the blacksmith, or go back to the")
        print("courtyard. What would you like to do?")
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:
            print("\nYou tell her about the rusty chain and she says that")
            print("she will take it down but that she will need 4 peices of")
            print("metal to make a chain long enough for the drawbridge. You")
            print("head back out into the courtyard.")
            bridge_problem_chain_explained = 2
            print(f"pully is: {pully}")
            pully.remove(str("rusty chain"))
            print(f"now pully is: {pully}")
            courtyard()
        else:
            blacksmith()

    elif bridge_problem_chain_explained == 2:
        print("\nYou can stay here, talk to the blacksmith, or go back to the")
        print("courtyard. What would you like to do?")
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:
            print("\nShe tells you that she has removed the rusty chain but that")
            print("she still needs 4 peices of metal to make a new one.")
            blacksmith()
        else:
            blacksmith()

    elif bridge_problem_chain_explained == 3:
        print("\nYou can stay here, talk to the blacksmith, or go back to the")
        print("courtyard. What would you like to do?")
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:
            print("\nShe tells you that she has removed the rusty chain but that")
            print("she still needs 3 peices of metal to make a new one.")
            blacksmith()
        else:
            blacksmith()

    elif bridge_problem_chain_explained == 4:
        print("\nYou can stay here, talk to the blacksmith, or go back to the")
        print("courtyard. What would you like to do?")
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:
            print("\nShe tells you that she has removed the rusty chain but that")
            print("she still needs 2 peices of metal to make a new one.")
            blacksmith()
        else:
            blacksmith()

    elif bridge_problem_chain_explained == 5:
        print("\nYou can stay here, talk to the blacksmith, or go back to the")
        print("courtyard. What would you like to do?")
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:
            print("\nShe tells you that she has removed the rusty chain but that")
            print("she still needs 1 peice of metal to make a new one.")
            blacksmith()
        else:
            blacksmith()

    elif bridge_problem_chain_explained >= 6:
        print("\nYou can stay here, talk to the blacksmith, or go back to the")
        print("courtyard. What would you like to do?")
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:
            print("\nShe tells you that she has removed the rusty chain and made")
            print("a new one which she installed in the drawbridge gaurdtower.")
            blacksmith()
        else:
            blacksmith()


# --------------------------------------------------------------------------------
#1 Create the 'carpenter' function. It will work the same way as the 'blacksmith'
## function in that "talking" to the carpenter will become accessable after
## the 'drawbridge_gaurdtower' is accessed for the first time and the nature of
## the gears and the carpenter's relationship to them is made clear. The carpenter
## will then explain that he needs wood to make the new gears and the "rotten
## gears" string will be removed from var 'pully'. It will be up to the player
## to explore the keep, barricks, and stables inorder to accertain where the
## wood is and how to get it to the blacksmith. Once the gears are made the player
## will need the strings 'men', 'horses', and 'wagon' to be in var 'crew' inorder
## for the blacksmith to get the new gears to the drawbridge_gaurdtower.
def carpenter():
    global bridge_problem_gears_explained

    print("You are in the carpenter's workshop. You see him working in concentration")
    print("with his tools.")

    if bridge_problem_gears_explained == 0:
        print("\nYou can stay here or go back to the courtyard. What would you")
        print("like to do?")
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        else:
            carpenter()

    elif bridge_problem_gears_explained == 1:
            print("\nYou can stay here, talk to the carpenter, or go back to the")
            print("courtyard. What would you like to do?")
            where_to = input("> ")
            if "courtyard" in where_to:
                courtyard()
            elif "talk" in where_to or "carpenter" in where_to:
                print("\nYou tell him about the rotten gears and he says that")
                print("he will remove them but that he will need a more")
                print("extensive supply of wood to construct new ones. You")
                print("head back out into the courtyard.")
                bridge_problem_gears_explained = 2
                print(f"pully is: {pully}")
                pully.remove(str("rotten gears"))
                print(f"now pully is: {pully}")
                courtyard()
            else:
                carpenter()
    elif bridge_problem_gears_explained == 2:
            print("\nYou can stay here, talk to the carpenter, or go back to the")
            print("courtyard. What would you like to do?")
            where_to = input("> ")
            if "courtyard" in where_to:
                courtyard()
            elif "talk" in where_to or "carpenter" in where_to:
                print("\nHe tells you that the rotten gears have been removed from")
                print("the pully system in the drawbridge gaurdtower but that he")
                print("still needs the wood to make the new gears. You head back")
                print("to the courtyard.")
                courtyard()
            else:
                carpenter()

    # This will be the section where the wood has been brought to the carpenter
    # and he has built the gears but still needs horses, and a wagon to transport
    # them to the drawbridge gaurdtower and men to load them onto the wagon.
    elif bridge_problem_gears_explained == 3:

carpenter()
