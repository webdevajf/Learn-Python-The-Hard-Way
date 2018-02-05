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

drawbridge = True
inventory = []
crew = []
bridge_problem_chain_explained = 0
bridge_problem_gears_explained = 0
wood_problem_explained = 0
pully = ["rusty chain", "rotten gears"]
gt_activated = []

def start():

    string_start = f"""

You are in a castle that is under siege from a zombie hoard.
The castle walls and gate are holding the hoard off with no
difficulty but the castle is running out of food and you and your
people will soon starve if you stay here. At the back of the castle
is a drawbridge that can be used to cross a deep chasam which runs
behind the castle. This chasam cannot be crossed by the zombie
hoard and so it is by way of this drawbridge that you and your
people can make your escape. There is just one problem: the
drawbridge has not been used in decades. It is in disrepair and
cannot be lowerd. It must be fixed before you can escape.

"""

    #return string_start
    print(string_start)
    courtyard()

drawbridge_open: f"""
At the castles back wall you can see the drabridge and its gaurdtower. It is lowered!
You can now cross the chasam and escape the zombies!

What would you like to do?

Type \'cross\' to cross the chasam and escape to safety"""

def courtyard():
    global drawbridge
    global inventory
    global crew
    global bridge_problem_chain_explained
    global bridge_problem_gears_explained
    global wood_problem_explained
    global pully
    global drawbridge_open

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

    if drawbridge is True:
        print(drawbridge_open)
        what_to_do = input("\n> ")

        if "cross" in what_to_do:
            print("""
You and your people have crossed the drawbridge and escaped
The besiged castle! GOOD JOB!!!\n""")
            exit()
        else:
            courtyard()
## current task on else statement below --> Trying to figure out how to 'dedent'
## a line in a string
    else:
        print("""\n
        You are in the castle courtyard:
        \t-type \'a\' to enter the stables
        \t-type \'b\' to enter the barricks
        \t-type \'c\' to enter the blacksmith\'s workshop
        \t-type \'d\' to enter the carpenter\'s workshop
        \t-type \'e\' to enter the north east gaurdtower
        \t-type \'f\' to enter the south east gaurdtower
        \t-type \'g\' to enter the north west gaurdtower
        \t-type \'h\' to enter the south west gaurdtower
        \t-type \'i\' to enter the keep
        \t-type \'j\' to enter the drawbridge gaurdtower

    At the castles' back wall you can see the drawbridge gaurdtower is currently raised.
    You are trapped in the castle.

    Where would you like to go?""")
        where_to = input("\n> ")

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

print(start())


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
