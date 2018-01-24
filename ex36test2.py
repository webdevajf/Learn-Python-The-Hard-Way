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
crew = ["men"]
bridge_problem_chain_explained = 0
bridge_problem_gears_explained = 0
wood_problem_explained = 1
pully = ["rusty chain", "rotten gears"]
gt_activated = []

def courtyard():
    global drawbridge
    global inventory
    global crew
    global bridge_problem_chain_explained
    global bridge_problem_gears_explained
    global wood_problem_explained
    global pully

    while bridge_problem_chain_explained == 6:
        pully.insert(0,str("new chain"))
        bridge_problem_chain_explained += 1

    print("\nThe variables are:")
    print(f"------ drawbridge is: {drawbridge}. ------")
    print(f"------ inventory is: {inventory}. ------")
    print(f"------ crew is: {crew}. ------")
    print(f"------ bridge_problem_chain_explained is: {bridge_problem_chain_explained} ---------")
    print(f"------ bridge_problem_gears_explained is: {bridge_problem_gears_explained} ---------")
    print(f"------ wood_problem_explained is: {wood_problem_explained} ---------")
    print(f"------ pully is: {pully}. ------")
    print(f"------ gt_activated is: {gt_activated}.------")
    print("\nYou are in the castle courtyard. You can hear the zombies")
    print("moaning and screaming outside.\n")
    print("You can see:")
    print("the stables,")
    print("the barricks,")
    print("the blacksmith\'s workshop,")
    print("the carpenter\'s workshop,")
    print("the north east gaurd tower,")
    print("the south east gaurd tower,")
    print("the north west gaurd tower,")
    print("the south west gaurd tower,")
    print("and the Keep.")

    if drawbridge is False:
        print("At the castles' back wall you can see the drawbridge and its")
        print("gaurdtower.")
        print("It is currently raised.")
        print("You are trapped in the castle.\n")
    else:
        print("At the castles back wall you can see the drabridge and its")
        print("gaurdtower.")
        print("It is lowered!")
        print("Cross the chasam and escape the zombies!\n")

    print("You can stay here or enter one of those buildings.")
    print("Where would you like to go?")
    where_to = input("> ")

    if "drawbridge" in where_to:
        drawbridge_gaurdtower()
    elif "nw" in where_to or "north west" in where_to:
        nw_gaurd_tower()
    elif "sw" in where_to or "south west" in where_to:
        sw_gaurd_tower()
    elif "ne" in where_to or "north east" in where_to:
        ne_gaurd_tower()
    elif "blacksmith" in where_to:
        blacksmith()
    elif "se" in where_to or "south east" in where_to:
        se_gaurd_tower()
    elif "carpenter" in where_to:
        carpenter()
    elif "keep" in where_to:
        keep()
    elif "stables" in where_to:
        stables()
    elif "barricks" in where_to:
        barricks()
    else:
        courtyard()

# --------------------------------------------------------------------------------
#1 Create the 'carpenter' function. It will work the same way as the 'blacksmith'
## function in that "talking" to the carpenter will become accessable after
## the 'drawbridge_gaurdtower' is accessed for the first time and the nature of
## the gears and the carpenter's relationship to them is made clear. The carpenter
## will then explain that he needs wood to make the new gears and the "rotten
## gears" string will be removed from var 'pully'. It will be up to the player
## to explore the keep, barricks, and stables inorder to accertain where the
## wood is and how to get it to the blacksmith. Once the gears are made the player
## will need the strings 'men', 'horses', and 'wagon' to be in var 'crew' in order
## for the blacksmith to get the new gears to the drawbridge_gaurdtower.
def carpenter():
    global bridge_problem_gears_explained
    global wood_problem_explained

    print("\nYou are in the carpenter's workshop. You see him working in concentration")
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
                wood_problem_explained = 1
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
            print("\nYou can stay here, talk to the carpenter, or go back to the")
            print("courtyard. What would you like to do?")
            where_to = input("> ")

            if "courtyard" in where_to:
                courtyard()
            elif "talk" in where_to or "carpenter" in where_to:
                print("\nHe tells you that the wood from the keep's furnature was")
                print("perfect and he takes you to look at his new gears, which he's")
                print("obviously more than a little proud of. They're well made")
                print("and you thank him for his work. You both agree that they're")
                print("to big to be moved accross the courtyard by hand and that")
                print("you'll need to get the men to load them onto a horse drawn")
                print("wagon. You head back to the courtyard.")
                courtyard()
            else:
                carpenter()

    elif bridge_problem_gears_explained == 4:
            print("\nYou have brought the men, horses and wagon to the carpenter's")
            print("workshop so they can move the gears to the drawbridge gaurdtower.")
            print("You can stay here or talk to the carpenter. What would you like")
            print("to do?")
            where_to = input("> ")

            if "talk" in where_to or "carpenter" in where_to:
                print("\nHe oversees the men moving the gears outside and then he")
                print("directs them as they load the wooden contraptions into the")
                print("cart. The horses pull the cart away towards the drawbridge")
                print("gaurdtower. You watch them go as you stand in the courtyard.")
                print(f"pully is: {pully}")
                pully.insert(1, str("new gears"))
                print(f"now pully is: {pully}")
                bridge_problem_gears_explained = 5
                courtyard()
            else:
                carpenter()
    else:
        print("\nYou can stay here or go back to the courtyard. What would you")
        print("like to do?")
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        else:
            carpenter()

#2 Create the 'keep' function. This will be where the wood for the gears can be
## found in the form of furnature in the great hall. It will become clear that
## is what the furnature is for after talking to the carpenter. However, the
## player will need 'men' to be in var 'crew' inorder to get the furnature out
## of the keep and to the carpenter. The great hall of the keep will have a
## passage that leads down to function 'cript' where the story of the king
## and his family falling prey to disease, becoming zombies and eating eachother
## will be told.
def keep():
    global bridge_problem_gears_explained
    global wood_problem_explained
    global crew
    print("\nYou enter the great hall of the Keep. There's a fire burning in the")
    print("fireplace and the room's warmth is comforting after the cold of the")
    print("dreary day outside. There are tapestries on the wall that remind you")
    print("of happier days.")

    if wood_problem_explained == 0:
        print("You can see the beautiful wooden banquet tables that you used to")
        print("sit upon for the king's feasts. You miss those feasts.")
        print("\nYou can stay here, go down into the cript, or go back to the courtyard.")
        print("Where would you like to go?")
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "cript" in where_to:
            cript()
        else:
            keep()

    elif wood_problem_explained == 1 and "men" in crew:
        print("The men enter the great hall behind you. They open wide, the doors")
        print("to the hall, and set about removing the wooden feasting tables.")
        print("You quietly shed some tears thinking of all the good times you've")
        print("had while sitting at those tables. Then you take a deep breath and")
        print("resign yourself to the thought that they will soon be no more than")
        print("gears in a pully in a castle that you will be leaving behind.")
        print("\nYou dry your eyes and head back out into the courtyard.")
        bridge_problem_gears_explained = 3
        wood_problem_explained = 2
        courtyard()

    elif wood_problem_explained == 1:
        print("You can see the beautiful wooden banquet tables that you used to")
        print("sit upon for the king's feasts. These would be an adequate supply.")
        print("of wood for the carpenter to make the gears with. Unfortunatley,")
        print("these tables are too big for you to lift by yourself. You will")
        print("need some help to get them to the carpenter.")
        print("\nYou can stay here, go down into the cript, or go back to the courtyard.")
        print("Where would you like to go?")
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "cript" in where_to:
            cript()
        else:
            keep()

    elif wood_problem_explained == 2:
        print("You can see the empty space where the banquet tables used to be.")
        print("You feel a twinge of sadness.")
        print("\nYou can stay here, go down into the cript, or go back to the courtyard.")
        print("Where would you like to go?")
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "cript" in where_to:
            cript()
        else:
            keep()

def cript():
    print("\nYou enter the cript. It is dark and oppressive, lit by only a single torch.")
    print("Here you find the graves of the king, his family, and their ancestors.")
    print("You sigh with sorrow as you think upon the tragic death of your late")
    print("ruller and his family. It was you who found them. Late one night when")
    print("you rushed up to thier chambers to deliver a message that had been brought")
    print("by raven. You stood outside the door of thier family common room. The king")
    print("had been ill of late, so it was nothing surprising when you heard moans comming")
    print("from within the room, but then you heard a crunch and a scream! You rushed")
    print("headlong into the room to a sceen of utter horror! The royal prince and")
    print("princess lay upon the floor in pools of their own blood. The princess")
    print("was dead and the the prince was gurgling the last of his raggad, bloody")
    print("breaths. On the other side of the room the king, now a zombie, lay over")
    print("his wife's body chewing at her ruined throat. You cut off his head and")
    print("quickly decapitated the other boddies to stop an outbreak. To this day")
    print("none know how the king had gotten bitten nor why he didn't tell his")
    print("trusted advisors. Three days later the Zombie hoard appeard on the")
    print("horizon and it fell to you to oversee the castle's defenses.")

    print("You can stay here, or go back up to the great hall of the Keep.")
    print("Where would you like to go?")
    where_to = input("> ")

    if "eep" in where_to or "up" in where_to or "back" in where_to or "hall" in where_to:
        keep()
    else:
        cript()

courtyard()
