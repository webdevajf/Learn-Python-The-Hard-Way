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

# TO DD ITEM:

from sys import exit

drawbridge = False
inventory = []
crew = []
bridge_problem_chain_explained = 0
bridge_problem_gears_explained = 0
pully = ["rusty chain", "rotten gears"]
gt_activated = []

def courtyard():
    global drawbridge
    global inventory
    global crew
    global bridge_problem_chain_explained
    global bridge_problem_gears_explained
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

def drawbridge_gaurdtower():
    global pully

    if "rusty chain" in pully and "rotten gears" in pully:
        global bridge_problem_chain_explained
        global bridge_problem_gears_explained
        print(f"------ pully is {pully} ---------")
        print(f"------ bridge_problem_chain_explained is {bridge_problem_chain_explained} ---------")
        print(f"------ bridge_problem_gears_explained is {bridge_problem_gears_explained} ---------")
        bridge_problem_chain_explained = 1
        bridge_problem_gears_explained = 1
        print(f"------ bridge_problem_chain_explained is {bridge_problem_chain_explained} ---------")
        print(f"------ bridge_problem_gears_explained is {bridge_problem_gears_explained} ---------")
        print("\nYou are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is in")
        print("disrepair. The chain is rusted and the wooden gears are rotten.")
        print("You will need the blacksmith to remove the rusty chain and build")
        print("a new one. Also, you will need the carpenter to remove the rotten")
        print("gears and build new ones.")
        print("\nWould you like to stay here or go back to the courtyard?")
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

    elif "new chain" in pully and "rotten gears" in pully:
        print("\nYou are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is in")
        print("disrepair. The blacksmith has replaced the rusted chain")
        print("with a shiny new one but the wooden gears are still rotten.")
        print("You need the carpenter to remove the rotten gears and build")
        print("new ones.")
        print("\nWould you like to stay here or go back to the courtyard?")
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

    elif "rusty chain" in pully and "new gears" in pully:
        print("\nYou are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is in")
        print("disrepair. The carpenter has replaced the rotten gears")
        print("with new ones but the chain is still rusty. You need the blacksmith")
        print("to remove the rusty chain and build a new one.")
        print("\nWould you like to stay here or go back to the courtyard?")
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

    elif "new chain" in pully and "new gears" in pully:
        print("\nYou are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is repaired!")
        print("The carpenter has replaced the rotten gears with new ones and the")
        print("blacksmith has removed the rusty chain and replaced it with a new")
        print("one.")
        print("\nWould you like to stay here or go back to the courtyard?")
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

    elif "rusty chain" in pully:
        print("\nYou are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is in")
        print("disrepair. The rusty chain is still in place but the carpenter has")
        print("removed the rotten wooden gears. You still need him to replace them")
        print("with new ones. You will also need the blacksmith to remove the")
        print("rusty chain and build a new one.")
        print("\nWould you like to stay here or go back to the courtyard?")
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

    elif "rotten gears" in pully:
        print("\nYou are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is in")
        print("disrepair. The rotten gears are still in place but the blacksmith")
        print("has removed the rusty chain. You still need her to replace it")
        print("with a new one. You will also need the carpenter to remove the")
        print("rotten gears and replace them with new ones.")
        print("\nWould you like to stay here or go back to the courtyard?")
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

    elif "new chain" in pully:
        print("\nYou are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is in")
        print("disrepair. The blacksmith has replaced the rusted chain with a")
        print("shiny new one. The carpenter has also removed the rotten gears but")
        print("still needs to replace them with new ones.")
        print("\nWould you like to stay here or go back to the courtyard?")
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

    elif "new gears" in pully:
        print("\nYou are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is in")
        print("disrepair. The carpenter has replaced the rotten gears with new")
        print("ones. The blacksmith has also removed the rusty chain but still")
        print("needs to replace it with a new one.")
        print("\nWould you like to stay here or go back to the courtyard?")
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

    else:
        print("\nYou are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is in")
        print("disrepair. The blacksmith and carpenter have removed the rusted")
        print("chain and the rotten wooden gears but have yet to replace them.")
        print("\nWould you like to stay here or go back to the courtyard?")
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

def carpenter():
    print("bob")

def keep():
    print("bob")

def stables():
    print("bob")

def barricks():
    print("bob")

courtyard()
