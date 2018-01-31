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

from sys import exit

drawbridge = False
inventory = []
crew = []
bridge_problem_chain_explained = 0
bridge_problem_gears_explained = 0
wood_problem_explained = 0
pully = ["rusty chain", "rotten gears"]
gt_activated = []

def start():
    print("""\n
    \tYou are in a castle that is under siege from a zombie hoard.
    The castle walls and gate are holding the hoard off with no
    difficulty but the castle is running out of food and you and your
    people will soon starve if you stay here. At the back of the castle
    is a drawbridge that can be used to cross a deep chasam which runs
    behind the castle. This chasam cannot be crossed by the zombie
    hoard and so it is by way of this drawbridge that you and your
    people can make your escape. There is just one problem: the
    drawbridge has not been used in decades. It is in disrepair and
    cannot be lowerd. It must be fixed before you can escape.
    \n\tIf you stand in the courtyard, in front of the castle gates,
    you can see several buldings within the castle walls:
    In the north west corner of the castle are the stables and the
    north west gaurd tower. In the south west corner of the castle are
    the barricks and the south west gaurd tower. In the north east
    corner of the castle are the blacksmith\'s workshop and the north
    east gaurd tower. In the south east corner of the castle are the
    carpenter\'s workshop and the south east gaurd tower. In the center
    of the castle is the Keep where the king and his family used to live.""")
    courtyard()

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

    #print("\nThe variables are:")
    #print(f"------ drawbridge is: {drawbridge}. ------")
    #print(f"------ inventory is: {inventory}. ------")
    #print(f"------ crew is: {crew}. ------")
    #print(f"------ bridge_problem_chain_explained is: {bridge_problem_chain_explained} ---------")
    #print(f"------ bridge_problem_gears_explained is: {bridge_problem_gears_explained} ---------")
    #print(f"------ wood_problem_explained is: {wood_problem_explained} ---------")
    #print(f"------ pully is: {pully}. ------")
    #print(f"------ gt_activated is: {gt_activated}.------")
    print("""\n
    You are in the castle courtyard and you can see:")
    \t-the stables
    \t-the barricks
    \t-the blacksmith\'s workshop
    \t-the carpenter\'s workshop
    \t-the north east gaurd tower
    \t-the south east gaurd tower
    \t-the north west gaurd tower
    \t-the south west gaurd tower
    \t-The keep
    \t-the drawbridge gaurdtower""")

    if drawbridge is True:
        print("At the castles back wall you can see the drabridge and its")
        print("gaurdtower.")
        print("It is lowered!")
        print("You can now cross the chasam and escape the zombies!\n")
        print("What would you like to do?")
        what_to_do = input("\n> ")

        if "cross" in what_to_do or "chasam" in what_to_do or "escape" in what_to_do:
            print("\nYou and your people have crossed the drawbridge and escaped")
            print("The besiged castle! GOOD JOB!!!\n")
            exit()
        else:
            courtyard()
## current task on else statement below --> Trying to figure out how to 'dedent'
## a line in a string
    else:
        print("""\n
        \bAt the castles' back wall you can see the drawbridge gaurdtower
        \bis currently raised.You are trapped in the castle.")
        \nWhere would you like to go?""")
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

start()


#################################################################################
#def start():
#    print("""\nYou are in a castle that is under siege from a zombie hoard.
#    The castle walls and gate are holding the hoard off with no
#    difficulty but the castle is running out of food and you and your
#    people will soon starve if you stay here. At the back of the castle
#    is a drawbridge that can be used to cross a deep chasam which runs
#    behind the castle. This chasam cannot be crossed by the zombie
#    hoard and so it is by way of this drawbridge that you and your
#    people can make your escape. There is just one problem: the
#    drawbridge has not been used in decades. It is in disrepair and
#    cannot be lowerd. It must be fixed before you can escape.
#    \nIf you stand in the courtyard, in front of the castle gates,
#    you can see several buldings within the castle walls:
#    In the north west corner of the castle are the stables and the
#    north west gaurd tower. In the south west corner of the castle are
#    the barricks and the south west gaurd tower. In the north east
#    corner of the castle are the blacksmith\'s workshop and the north
#    east gaurd tower. In the south east corner of the castle are the
#    carpenter\'s workshop and the south east gaurd tower. In the center
#    of the castle is the Keep where the king and his family used to live.""")
#
#def start2():
#    print("""\n
#    \tYou are in a castle that is under siege from a zombie hoard.
#    The castle walls and gate are holding the hoard off with no
#    difficulty but the castle is running out of food and you and your
#    people will soon starve if you stay here. At the back of the castle
#    is a drawbridge that can be used to cross a deep chasam which runs
#    behind the castle. This chasam cannot be crossed by the zombie
#    hoard and so it is by way of this drawbridge that you and your
#    people can make your escape. There is just one problem: the
#    drawbridge has not been used in decades. It is in disrepair and
#    cannot be lowerd. It must be fixed before you can escape.
#    \n\tIf you stand in the courtyard, in front of the castle gates,
#    you can see several buldings within the castle walls:
#    In the north west corner of the castle are the stables and the
#    north west gaurd tower. In the south west corner of the castle are
#    the barricks and the south west gaurd tower. In the north east
#    corner of the castle are the blacksmith\'s workshop and the north
#    east gaurd tower. In the south east corner of the castle are the
#    carpenter\'s workshop and the south east gaurd tower. In the center
#    of the castle is the Keep where the king and his family used to live.""")

#def start3():
#    print("\nYou are in a castle that is under siege from a zombie hoard.")
#    print("The castle walls and gate are holding the hoard off with no")
#    print("difficulty but the castle is running out of food and you and your")
#    print("people will soon starve if you stay here. At the back of the castle")
#    print("is a drawbridge that can be used to cross a deep chasam which runs")
#    print("behind the castle. This chasam cannot be crossed by the zombie")
#    print("hoard and so it is by way of this drawbridge that you and your")
#    print("people can make your escape. There is just one problem: the")
#    print("drawbridge has not been used in decades. It is in disrepair and")
#    print("\nIf you stand in the courtyard, in front of the castle gates,")
#    print("you can see several buldings within the castle walls:")
#    print("In the north west corner of the castle are the stables and the")
#    print("north west gaurd tower. In the south west corner of the castle are")
#    print("the barricks and the south west gaurd tower. In the north east")
#    print("corner of the castle are the blacksmith\'s workshop and the north")
#    print("east gaurd tower. In the south east corner of the castle are the")
#    print("carpenter\'s workshop and the south east gaurd tower. In the center")
#    print("of the castle is the Keep where the king and his family used to live.")
#    courtyard()


#start()
#start2()
#start3()
