## This is the 'test' document. This document exists
## to provide me a place to test and experiment with
## the game's code in a place that is isolated from
## then rest of the script.

drawbridge = False
inventory = []
crew = []
bridge_problem_chain_explained = 1
bridge_problem_gears_explained = 1

# This line creates function 'start' which
# explaines the game.
def start():
    print("You are in a castle that is under siege from a zombie hoard.")
    print("The castle walls and gate are holding the hoard off with no")
    print("difficulty but the castle is running out of food and you and your")
    print("people will soon starve if you stay here. At the back of the castle")
    print("is a drawbridge that can be used to cross a deep chasam which runs")
    print("behind the castle. This chasam cannot be crossed by the zombie")
    print("hoard and so it is by way of this drawbridge that you and your")
    print("people can make your escape. There is just one problem: the")
    print("drawbridge has not been used in decades. It is in disrepair and")
    print("cannot be lowerd. Its\' wooden gears have rotted and the chain has")
    print("rusted. You need to construct a new chain and gears and then")
    print("install them before you can make your escape.")
    courtyard()

# This line creates function 'courtyard' which
# brings the player to the games' start point
# and central hub from which you can access all
# of the other locations in the game. It describes
# all of these locations.
def courtyard():
    print("\nYou are in the castle courtyard. You can hear the zombies")
    print("moaning and screaming outside.\n")
    print("You can see several buldings within the walls of the castle:")
    print("In the north west corner of the castle are the stables and the")
    print("north west gaurd tower.")
    print("In the south west corner of the castle are the barricks and the")
    print("south west gaurd tower.")
    print("In the north east corner of the castle are the blacksmith\'s")
    print("workshop and the north east gaurd tower.")
    print("In the south east corner of the castle are the carpenter\'s workshop")
    print("and the south east gaurd tower.")
    print("In the center of the castle is the Keep where the king and his")
    print("family used to live.\n")

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

    print("Where would you like to go?")
    where_to = input("> ")

    if "drawbridge" in where_to:
        drawbridge_gaurdtower()
    elif "nw" in where_to:
        nw_gaurd_tower()
    elif "stables" in where_to:
        stables()
    elif "sw" in where_to:
        sw_gaurd_tower()
    elif "barricks" in where_to:
        barricks()
    elif "ne" in where_to:
        ne_gaurd_tower()
    elif "blacksmith" in where_to:
        blacksmith()
    elif "se" in where_to:
        se_gaurd_tower()
    elif "carpenter" in where_to:
        carpenter()
    elif "keep" in where_to:
        keep()
    else:
        courtyard()


def blacksmith():
    print("\nYou are in the blacksmith's workshop. You look around and see him")
    print("working diligengly at his forge.")
    if bridge_problem_chain_explained == 0:
        print("You can stay here or go back to the courtyard. What would you")
        print("like to do?")
        where_to = input("> ")
        if "courtyard" in where_to:
            courtyard()
        else:
            blacksmith()
    elif bridge_problem_chain_explained == 1:
        print("You can stay here, talk to the blacksmith, or go back to the")
        print("courtyard. What would you like to do?")
        where_to = input("> ")
        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:
            print("You tell her about the rusty chain and she says that")
            print("she will take it down but that she will need 4 peices of")
            print("metal to make a chain long enough for the drawbridge.")
            bridge_problem_chain_explained == 3
        else:
            blacksmith()


start()
