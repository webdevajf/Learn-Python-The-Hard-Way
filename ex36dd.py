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
inventory = []
support_people = []
bridge_problem_explained = 0

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

def drawbridge_gaurdtower():
    global  bridge_problem_explained
    #print(bridge_problem_explained)
    bridge_problem_explained += 1
    #print(bridge_problem_explained)
    pully = ["rusty chain", "rotten gears"]
    if "rusty chain" in pully and "rotten gears" in pully:
        print("You are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is in")
        print("disrepair. The chain is rusted and the wooden gears are rotten.")
        print("You will need the blacksmith to remove the rusty chain and build")
        print("a new one. Also, you will need the carpenter to remove the rotten")
        print("gears and build new ones.")
    elif "new chain" in pully and "rotten gears" in pully:
        print("You are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is in")
        print("disrepair. The blacksmith has replaced the rusted chain")
        print("with a shiny new one but the wooden gears are still rotten.")
        print("You need the carpenter to remove the rotten gears and build")
        print("new ones.")
    elif "rusty chain" in pully and "new gears" in pully:
        print("You are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is in")
        print("disrepair. The carpenter has replaced the rotten gears")
        print("with new ones but the chain is still rusty. You need the blacksmith")
        print("to remove the rusty chain and build a new one.")
    elif "new chain" in pully and "new gears" in pully:
        print("You are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is repaired!")
        print("The carpenter has replaced the rotten gears with new ones and the")
        print("blacksmith has removed the rusty chain and replaced it with a new")
        print("one.")
    elif "rusty chain" in pully:
        print("You are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is in")
        print("disrepair. The rusty chain is still in place but the carpenter has")
        print("removed the rotten wooden gears. You still need him to replace them")
        print("with new ones. You will also need the blacksmith to remove the")
        print("rusty chain and build a new one.")
    elif "rotten gears" in pully:
        print("You are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is in")
        print("disrepair. The rotten gears are still in place but the blacksmith")
        print("has removed the rusty chain. You still need him to replace it")
        print("with a new one. You will also need the carpenter to remove the")
        print("rotten gears and replace them with new ones.")
    elif "new chain" in pully:
        print("You are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is in")
        print("disrepair. The blacksmith has replaced the rusted chain with a")
        print("shiny new one. The carpenter has also removed the rotten gears but")
        print("still needs to replace them with new ones.")
    elif "new gears" in pully:
        print("You are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is in")
        print("disrepair. The carpenter has replaced the rotten gears with new")
        print("ones. The blacksmith has also removed the rusty chain but still")
        print("needs to replace it with a new one.")
    else:
        print("You are in the gaurdtower next to the drawbridge. You see that the")
        print("pully apparatus, that raises and lowers the drabridge, is in")
        print("disrepair. The blacksmith and carpenter have removed the rusted")
        print("chain and the rotten wooden gears but have yet to replace them with")

def nw_gaurd_tower():
    print("bob")

def stables():
    print("bob")

def sw_gaurd_tower():
    print("bob")

def barricks():
    print("bob")

def ne_gaurd_tower():
    print("bob")

def blacksmith():
    print("You are in the blacksmith's workshop. You look around and see him")
    print("working diligengly at his forge.")

def se_gaurd_tower():
    print("bob")

def carpenter():
    print("bob")

def keep():
    print("bob")

start()
