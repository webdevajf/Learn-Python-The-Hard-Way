## 'dd' stands for design document. This is Where
## I will write out notes in english detailing what
## needs to be done and then write the code to
## perform that function.

# First I need to lay out the start location of the
# game. There needs to be an apt description of the
# situation that the player finds themselves in,
# namely in a castle courtyard, with the situation
# or the problem layed out clearly. There also needs
# to be a clear description of the avenues that the
# player can explore in order to find solutions
# to the problem.

# This line creates var 'drabridge' and sets it
# value equal to 'False'. Making it's value
# 'True' is the object of the game.
drawbridge = False

# This line creates function 'start' which
# explaines the game.
def start():
    print("You are in a castle that is under siege from a zombie hoard.")
    print("The castle walls and gate are holding the hoard off with no")
    print("difficulty but the castle is running out of food and you and your")
    print("people will soon starve if you stay here. At the back of the castle")
    print("is a drawbridge that can be used to cross a deep chasam that runs")
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
    print("moaning and screaming outside\n")
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
        print("At the castles' back wall you can see the drawbridgeand its")
        print("gaurdtower.")
        print("It is currently raised.")
        print("You are trapped in the castle.\n")
    else:
        print("At the castles back wall you can see the drabridge and its")
        print("gaurdtower.")
        print("It is lowered!")
        print("Cross the chasam and escape the zombies!\n")


start()
