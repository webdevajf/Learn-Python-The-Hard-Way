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

    print(string_start)
    courtyard()

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

    print("\nThe variables are:")
    print(f"------ drawbridge is: {drawbridge}. ------")
    print(f"------ inventory is: {inventory}. ------")
    print(f"------ crew is: {crew}. ------")
    print(f"------ bridge_problem_chain_explained is: {bridge_problem_chain_explained} ---------")
    print(f"------ bridge_problem_gears_explained is: {bridge_problem_gears_explained} ---------")
    print(f"------ wood_problem_explained is: {wood_problem_explained} ---------")
    print(f"------ pully is: {pully}. ------")
    print(f"------ gt_activated is: {gt_activated}.------")

    if drawbridge is True:

        string_drabridge_true = f"""
At the castles back wall you can see the drabridge and its gaurdtower.
It is lowered! You can now cross the chasam and escape the zombies!

What would you like to do?

Type 'cross' to cross the chasam and escape to safety
"""

        print(string_drabridge_true)
        what_to_do = input("\n> ")

        if "cross" in what_to_do:
            string_cross = f"""
You and your people have crossed the drawbridge and escaped
The besiged castle! GOOD JOB!!!
"""

            print(string_cross)
            exit()
        else:
            courtyard()
## current task on else statement below --> Trying to figure out how to 'dedent'
## a line in a string
    else:
        string_else = """
    You are in the castle courtyard:
        -type 'a' to enter the stables
        -type 'b' to enter the barricks
        -type 'c' to enter the blacksmith's workshop
        -type 'd' to enter the carpenter's workshop
        -type 'e' to enter the northeast gaurdtower
        -type 'f' to enter the southeast gaurdtower
        -type 'g' to enter the northwest gaurdtower
        -type 'h' to enter the southwest gaurdtower
        -type 'i' to enter the keep
        -type 'j' to enter the drawbridge gaurdtower

    At the castles' back wall you can see the drawbridge gaurdtower is currently raised.
    You are trapped in the castle.

    Where would you like to go?
    """
        print(string_else)
        where_to = input("> ")

        if "a" in where_to:
            stables()
        elif "b" in where_to:
            barricks()
        elif "c" in where_to :
            blacksmith()
        elif "d" in where_to:
            carpenter()
        elif "e" in where_to:
            ne_gaurd_tower()
        elif "f" in where_to:
            se_gaurd_tower()
        elif "g" in where_to:
            nw_gaurd_tower()
        elif "h" in where_to:
            sw_gaurd_tower()
        elif "i" in where_to:
            keep()
        elif "j" in where_to:
            drawbridge_gaurdtower()
        else:
            courtyard()

def drawbridge_gaurdtower():
    global pully
    global drawbridge

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

        string_if = """
    You are in the gaurdtower next to the drawbridge. You see that the
    pully apparatus, that raises and lowers the drabridge, is in
    disrepair. The chain is rusted and the wooden gears are rotten.
    You will need the blacksmith to remove the rusty chain and build
    a new one. Also, you will need the carpenter to remove the rotten
    gears and build new ones.

    Would you like to stay here or go back to the courtyard?
    """
        print(string_if)
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

    elif "new chain" in pully and "rotten gears" in pully:

        string_elif_1 = """
    You are in the gaurdtower next to the drawbridge. You see that the
    pully apparatus, that raises and lowers the drabridge, is in
    disrepair. The blacksmith has replaced the rusted chain
    with a shiny new one but the wooden gears are still rotten.
    You need the carpenter to remove the rotten gears and build
    new ones.

    Would you like to stay here or go back to the courtyard?
    """

        print(string_elif_1)
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

    elif "rusty chain" in pully and "new gears" in pully:

        string_elif_2 = """
    You are in the gaurdtower next to the drawbridge. You see that the
    pully apparatus, that raises and lowers the drabridge, is in
    disrepair. The carpenter has replaced the rotten gears
    with new ones but the chain is still rusty. You need the blacksmith
    to remove the rusty chain and build a new one.

    Would you like to stay here or go back to the courtyard?
    """

        print(string_elif_2)
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

    elif "new chain" in pully and "new gears" in pully and drawbridge == True:

        string_elif_3 = """
    You are in the gaurdtower next to the drawbridge. You see that the
    pully apparatus, that raises and lowers the drabridge, is repaired
    and you have lowered the drawbridge! You and your people are ready
    to make your escape!

    Would you like to stay here or go back to the courtyard?
    """

        print(string_elif_3)
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

    elif "new chain" in pully and "new gears" in pully:

        string_elif_4 = """
    You are in the gaurdtower next to the drawbridge. You see that the
    pully apparatus, that raises and lowers the drabridge, is repaired!
    The carpenter has replaced the rotten gears with new ones and the
    blacksmith has removed the rusty chain and replaced it with a new
    one.

    Would you like to stay here, lower the drawbridge, or go back to the
    courtyard?
    """
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        elif "lower" in where_to or "drawbridge" in where_to:
            drawbridge = True
            drawbridge_gaurdtower()
        else:
            drawbridge_gaurdtower()

    elif "rusty chain" in pully:

        string_elif_5 = """
    You are in the gaurdtower next to the drawbridge. You see that the
    pully apparatus, that raises and lowers the drabridge, is in
    disrepair. The rusty chain is still in place but the carpenter has
    removed the rotten wooden gears. You still need him to replace them
    with new ones. You will also need the blacksmith to remove the
    rusty chain and build a new one.

    Would you like to stay here or go back to the courtyard?
    """
        print(string_elif_5)
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

    elif "rotten gears" in pully:

        string_elif_6 = """
    You are in the gaurdtower next to the drawbridge. You see that the
    pully apparatus, that raises and lowers the drabridge, is in
    disrepair. The rotten gears are still in place but the blacksmith
    has removed the rusty chain. You still need her to replace it
    with a new one. You will also need the carpenter to remove the
    rotten gears and replace them with new ones.

    Would you like to stay here or go back to the courtyard?
    """

        print(string_elif_6)
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

    elif "new chain" in pully:

        string_elif_7 = """
    You are in the gaurdtower next to the drawbridge. You see that the
    pully apparatus, that raises and lowers the drabridge, is in
    disrepair. The blacksmith has replaced the rusted chain with a
    shiny new one. The carpenter has also removed the rotten gears but
    still needs to replace them with new ones.

    Would you like to stay here or go back to the courtyard?
    """

        print(string_elif_7)
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

    elif "new gears" in pully:

        string_elif_8 = """
    You are in the gaurdtower next to the drawbridge. You see that the
    pully apparatus, that raises and lowers the drabridge, is in
    disrepair. The carpenter has replaced the rotten gears with new
    ones. The blacksmith has also removed the rusty chain but still
    needs to replace it with a new one.

    Would you like to stay here or go back to the courtyard?
    """

        print(string_elif_8)
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

    else:

        string_else = """
    You are in the gaurdtower next to the drawbridge. You see that the
    pully apparatus, that raises and lowers the drabridge, is in
    disrepair. The blacksmith and carpenter have removed the rusted
    chain and the rotten wooden gears but have yet to replace them.

    Would you like to stay here or go back to the courtyard?
    """

        print(string_else)
        where_to = input("> ")

        if "courtyard" in where_to or "back" in where_to:
            courtyard()
        else:
            drawbridge_gaurdtower()

def blacksmith():
    global bridge_problem_chain_explained

    string_intro = """
    You are in the blacksmith's workshop. You look around and see her
    working diligengly at her forge.
    """

    print(string_intro)

    if bridge_problem_chain_explained == 0:

        string_if = """
    You can stay here or go back to the courtyard. What would you
    like to do?
    """

        print(string_if)
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        else:
            blacksmith()

    elif bridge_problem_chain_explained == 1:

        string_elif_1 = """
    You can stay here, talk to the blacksmith, or go back to the
    courtyard. What would you like to do?
    """
        print(string_elif_1)
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:

            string_elif_1_elif = """
    You tell her about the rusty chain and she says that
    she will take it down but that she will need 4 peices of
    metal to make a chain long enough for the drawbridge. You
    head back out into the courtyard.
    """

            print(string_elif_1_elif)
            bridge_problem_chain_explained = 2
            print(f"pully is: {pully}")
            pully.remove(str("rusty chain"))
            print(f"now pully is: {pully}")
            courtyard()
        else:
            blacksmith()

    elif bridge_problem_chain_explained == 2:

        string_elif_2 = """
    You can stay here, talk to the blacksmith, or go back to the
    courtyard. What would you like to do?
    """

        print(string_elif_2)
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:

            string_elif_2_elif_1 = """
    She tells you that she has removed the rusty chain but that
    she still needs 4 peices of metal to make a new one.
    """

            print(string_elif_2_elif_1)
            blacksmith()
        else:
            blacksmith()

    elif bridge_problem_chain_explained == 3:

        string_elif_3 = """
    You can stay here, talk to the blacksmith, or go back to the
    courtyard. What would you like to do?
    """

        print(string_elif_3)
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:

            string_elif_3_elif_1 = """
    She tells you that she has removed the rusty chain but that
    she still needs 3 peices of metal to make a new one.
    """

            print(string_elif_3_elif_1)
            blacksmith()
        else:
            blacksmith()

    elif bridge_problem_chain_explained == 4:

        string_elif_4 = """
    You can stay here, talk to the blacksmith, or go back to the
    courtyard. What would you like to do?
    """

        print(string_elif_4)
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:

            string_elif_4_elif_1 = """
    She tells you that she has removed the rusty chain but that
    she still needs 2 peices of metal to make a new one.
    """
            print(string_elif_4_elif_1)
            blacksmith()
        else:
            blacksmith()

    elif bridge_problem_chain_explained == 5:

        string_elif_5 = """
    You can stay here, talk to the blacksmith, or go back to the
    courtyard. What would you like to do?
    """

        print(string_elif_5)
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:
            string_elif_5_elif = """
    She tells you that she has removed the rusty chain but that
    she still needs 1 peice of metal to make a new one.
    """
            print(string_elif_5_elif)
            blacksmith()
        else:
            blacksmith()

    elif bridge_problem_chain_explained >= 6:

        string_elif_6 = """
    You can stay here, talk to the blacksmith, or go back to the
    courtyard. What would you like to do?
    """

        print(string_elif_6)
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:

            string_elif_6_elif = """
    She tells you that she has removed the rusty chain and made
    a new one which she installed in the drawbridge gaurdtower.
    """

            print(string_elif_6_elif)
            blacksmith()
        else:
            blacksmith()

def nw_gaurd_tower():
    global bridge_problem_chain_explained
    global gt_activated

    string_nw_gaurd_tower = """
    You are at the top of the north west gaurd tower. You find yourself
    next to a gaurd on duty. Looking over the tower's battlements you
    can see the sea of shambling zombies futilely trying to break into
    the castle.
    """

    print(string_nw_gaurd_tower)

    if bridge_problem_chain_explained <= 1:

        string_if = """
    You can either stay here and look aimlesly at the writhing hoard
    below you, shoot arrows at the zombies to relieve your boredom,
    or you can go back to the castle courtyard. What would you like
    to do?
    """

        print(string_if)
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:

            string_if_elif_1 = """
    You pick up a bow and a quiver of arrows. You pull out an
    arrow, knock it to the bow and pull the string back. You
    Sight along the arrow at the head of a particularly ugly and
    decomposed member of the walking dead and you let the arrow
    fly. There is a wet thud, which you can hear even over the,
    moaning of the undead, as the arrow slams through the zombies
    skull. It crumples to the ground and disapears under the sea
    of shambling, rotten boddies. You look up with a mischevious
    smile at the gaurd next to you expecting to see that you've
    impressed him with your marksmenship but are supprised to
    find him scowling at you. You realize then that even though
    he won't say it, because you outrank him, he's thinking that
    you've just waisted a precious arrow that can't be retrieved.
    You should quit showing off like a jackass and get back to
    work.
    """

            print(string_if_elif_1)
            nw_gaurd_tower()
        else:
            nw_gaurd_tower()

    elif bridge_problem_chain_explained > 1 and "nw" not in gt_activated:

        string_elif_1 = """
    You can either stay here and look aimlesly at the writhing hoard
    below you, shoot arrows at the zombies to relieve your boredom,
    go back to the castle courtyard, or talk to the gaurd. What
    would you like to do?
    """

        print(string_elif_1)
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:

            string_elif_1_elif_1 = """
    You pick up a bow and a quiver of arrows. You pull out an
    arrow, knock it to the bow and pull the string back. You
    Sight along the arrow at the head of a particularly ugly and
    decomposed member of the walking dead and you let the arrow
    fly. There is a wet thud, which you can hear even over the,
    moaning of the undead, as the arrow slams through the zombies
    skull. It crumples to the ground and disapears under the sea
    of shambling, rotten boddies. You look up with a mischevious
    smile at the gaurd next to you expecting to see that you've
    impressed him with your marksmenship but are supprised to
    find him scowling at you. You realize then that even though
    he won't say it, because you outrank him, he's thinking that
    you've just waisted a precious arrow that can't be retrieved.
    You should quit showing off like a jackass and get back to
    work.
    """

            print(string_elif_1_elif_1)
            nw_gaurd_tower()
        elif "talk" in what_to_do or "gaurd" in what_to_do:

            string_elif_1_elif_2 = """
    You walk over to the gaurd, explain the blacsmith's need for
    metal and politley ask him to go give her his sword. He heads
    off to go do that. You head back to the courtyard.
    """

            print(string_elif_1_elif_2)
            print(f"bridge_problem_chain_explained: {bridge_problem_chain_explained}.")
            bridge_problem_chain_explained += 1
            print(f"bridge_problem_chain_explained: {bridge_problem_chain_explained}.")
            print(f"gt_activated: {gt_activated}.")
            gt_activated.append("nw")
            print(f"gt_activated: {gt_activated}.")
            courtyard()
        else:
            nw_gaurd_tower()

    else:

        string_else = """
    You can either stay here and look aimlesly at the writhing hoard
    below you, shoot arrows at the zombies to relieve your boredom,
    or you can go back to the castle courtyard. What would you like
    to do?
    """

        print(string_else)
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:

            string_else_elif_1 = """
    You pick up a bow and a quiver of arrows. You pull out an
    arrow, knock it to the bow and pull the string back. You
    Sight along the arrow at the head of a particularly ugly and
    decomposed member of the walking dead and you let the arrow
    fly. There is a wet thud, which you can hear even over the,
    moaning of the undead, as the arrow slams through the zombies
    skull. It crumples to the ground and disapears under the sea
    of shambling, rotten boddies. You look up with a mischevious
    smile at the gaurd next to you expecting to see that you've
    impressed him with your marksmenship but are supprised to
    find him scowling at you. You realize then that even though
    he won't say it, because you outrank him, he's thinking that
    you've just waisted a precious arrow that can't be retrieved.
    You should quit showing off like a jackass and get back to
    work.
    """

            print(string_else_elif_1)
            nw_gaurd_tower()
        else:
            nw_gaurd_tower()

def sw_gaurd_tower():
    global bridge_problem_chain_explained
    global gt_activated

    if bridge_problem_chain_explained <= 1:

        string_if = """
    You are at the top of the south west gaurd tower. You find yourself
    next to a gaurd on duty. He looks very ill with a pallor to his skin,
    glassy eyes and sweat stained clothes. You decide to keep your eyes
    on him. The last thing you need is a plague breaking out in the middle
    of a seige. Looking over the tower's battlements you can see, to
    the west, the sea of shambling zombies futilely trying to break
    into the castle and, to the south, you see the chasam over which you
    plan to make your escape. From time to time a zombie gets pushed over
    the chasm's edge by the weight of the hoard. They fall listless and
    uncomprehending to the impact of their second death.

    You can either stay here and look aimlesly at the writhing hoard
    below you, shoot arrows at the zombies to relieve your boredom,
    or you can go back to the castle courtyard. What would you like
    to do?
    """

        print(string_if)
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:

            string_if_elif_1 = """
    You pick up a bow and a quiver of arrows. You pull out an
    arrow, knock it to the bow and pull the string back. You
    Sight along the arrow at the head of a particularly ugly and
    decomposed member of the walking dead and you let the arrow
    fly. There is a wet thud, which you can hear even over the,
    moaning of the undead, as the arrow slams through the zombies
    skull. It crumples to the ground and disapears under the sea
    of shambling, rotten boddies. You look up with a mischevious
    smile at the gaurd next to you expecting to see that you've
    impressed him with your marksmenship but are supprised to
    find him scowling at you. You realize then that even though
    he won't say it, because you outrank him, he's thinking that
    you've just waisted a precious arrow that can't be retrieved.
    You should quit showing off like a jackass and get back to
    work.
    """

            print(string_elif_1_elif_1)
            sw_gaurd_tower()
        else:
            sw_gaurd_tower()

    elif bridge_problem_chain_explained > 1 and "sw" not in gt_activated:

        string_elif_1 = """
    You assend the stairs to the top of the south west gaurdtower.
    As you open the door leading out to the gaurdtower's battlements
    you see the gaurd on duty. He's turned away from you, looking out
    at the chasam behind the castle. There's somethig off about his
    posture... you hear an animal groan comming from him as he turns
    around to face you... your eyes widen and adrenaline pumps into
    your veins as your blood runs cold. Before you have time to really
    process what you're seeing the zombie lunges at you! You raise
    your left arm to fend off it's onslaught and it bites into the chain
    mail armoring your forearm.
    """

        print(string_elif_1)
        zombie_battle()
    else:

        string_else = """
    You are at the top of the south west gaurd tower. The bloody body
    of the dead gaurd lies on the tower stones where you left it. Looking
    over the tower's battlements you can see, to the west, the sea of
    shambling zombies futilely trying to break into the castle and, to
    the south, you see the chasam over which you plan to make your
    escape. From time to time a zombie gets pushed over the chasm's
    edge by the weight of the hoard. They fall listless and uncomprehending
    to the impact of their second death.

    You can either stay here and look aimlesly at the writhing hoard
    below you, shoot arrows at the zombies to relieve your boredom,
    or you can go back to the castle courtyard. What would you like
    to do?
    """

        print(string_else)
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:

            string_else_elif_1 = """
    You pick up a bow and a quiver of arrows. You pull out an
    arrow, knock it to the bow and pull the string back. You
    Sight along the arrow at the head of a particularly ugly and
    decomposed member of the walking dead and you let the arrow
    fly. There is a wet thud, which you can hear even over the,
    moaning of the undead, as the arrow slams through the zombies
    skull. It crumples to the ground and disapears under the sea
    of shambling, rotten boddies. You look up with a mischevious
    smile at the gaurd next to you expecting to see that you've
    impressed him with your marksmenship but are supprised to
    find him scowling at you. You realize then that even though
    he won't say it, because you outrank him, he's thinking that
    you've just waisted a precious arrow that can't be retrieved.
    You should quit showing off like a jackass and get back to
    work.
    """

            print(string_else_elif_1)
            sw_gaurd_tower()
        else:
            sw_gaurd_tower()

face_smashes = 0

def zombie_battle():
    global bridge_problem_chain_explained
    global gt_activated
    global face_smashes

    string_zombie_battle_intro = """
    The zombie chews on your mailed arm and presses its weight into you.
    You can hear it's newly dead teath cracking and breaking against your
    armor.

    What will you do?

    Shove the zombie away and draw your sword? (type 'shove')
    Draw your knife? (type 'knife')
    Smash the zombie in the face with your armored fist? (type 'smash')
    """

    print(string_zombie_battle_intro)
    fight = input("> ")

    if fight == "shove":

        string_if = """
    You kick the zombie in the chest to gain space. In one fluid
    motion you draw your sword from the shieth on your belt and,
    using the momentum from that motion to sweep your sword in an upward
    arc and slice part of its head off. Unfortonatly, enough of its
    brain is sitll intact for it to keep functioning so you swing
    your blaid back around and slash its head off at the neck. The
    headless body crumples to the ground. You take the dead gaurds sword
    "out of its shieth and take it to the blacksmith for it's metal.
    """

        print(string_if)
        print(f"bridge_problem_chain_explained: {bridge_problem_chain_explained}.")
        bridge_problem_chain_explained += 1
        print(f"bridge_problem_chain_explained: {bridge_problem_chain_explained}.")
        print(f"gt_activated: {gt_activated}.")
        gt_activated.append("sw")
        print(f"gt_activated: {gt_activated}.")
        blacksmith()
    elif fight == "knife":

        string_elif_1 = """
    You draw your knife and plunge it into the zombies eye at an
    upward angle, destroying it's brain. The now lifeless body
    crumples to the ground. You take the dead gaurds sword out of
    its shieth and take it to the blacksmith for it's metal.
    """

        print(string_elif_1)
        print(f"bridge_problem_chain_explained: {bridge_problem_chain_explained}.")
        bridge_problem_chain_explained += 1
        print(f"bridge_problem_chain_explained: {bridge_problem_chain_explained}.")
        print(f"gt_activated: {gt_activated}.")
        gt_activated.append("sw")
        print(f"gt_activated: {gt_activated}.")
        blacksmith()
    elif fight == "smash" and face_smashes < 1:

        string_elif_2 = """
    As you hold the zombie off with your left arm, you work furiously
    to dislodge it's helmet with your right hand. Finally it comes
    off and clatters on the stones benieth you. You wind up your free
    hand and slam it into the zombies face as hard as you can.
    """

        print(string_elif_2)
        print(f"\'face_smashes\' is: {face_smashes}.")
        face_smashes = face_smashes + 1
        print(f"now \'face_smashes\' is: {face_smashes}.")
        zombie_battle()
    elif fight == "smash" and face_smashes >= 1 and face_smashes < 3:

        string_elif_3 = """
    Again you wind up your free hand and smash it into the zombies
    face with all your strenght.
    """

        print(string_elif_3)
        print(f"\'face_smashes\' is: {face_smashes}.")
        face_smashes = face_smashes + 1
        print(f"now \'face_smashes\' is: {face_smashes}.")
        zombie_battle()
    elif fight == "smash" and face_smashes >= 3 and face_smashes < 6:

        string_elif_4 = """
    Again you wind up your free hand and slam it into the zombies
    face as hard as you can. You feel the bones of its face break
    under your chain-mailed fist and when you pull your hand away
    blood and teath fall out of its face.
    """

        print(string_elif_4)
        print(f"\'face_smashes\' is: {face_smashes}.")
        face_smashes = face_smashes + 1
        print(f"now \'face_smashes\' is: {face_smashes}.")
        zombie_battle()
    elif fight == "smash" and face_smashes >= 6 and face_smashes < 9:

        string_elif_5 = """
    You're getting tired. You're gasping for breath and your punches
    are starting to loose their strength. None the less you hit the
    monster again and blood and gore spurt out from it\'s face.
    You feel its skull crack and it's face cave in a little.
    """

        print(string_elif_5)
        print(f"\'face_smashes\' is: {face_smashes}.")
        face_smashes = face_smashes + 1
        print(f"now \'face_smashes\' is: {face_smashes}.")
        zombie_battle()
    elif fight == "smash" and face_smashes == 9:

        string_elif_6 = """
    You hit the monster again and one of its eyes pop out of its
    socket and dangles over your left arm. You're nearing exaustion.
    If this doesn't end soon you're going to collapse and be eaten.
    You wonder to your self \'why!!!? why wont this asshole player try
    one of the other options? Why is this peice of shit who\'s typing
    on the keyboard so committed to typing \"smash\"!!!? What the
    hell wrong with this dumb shit mother fucker!!!? What?! You can't
    type \"shove\" or \"knife\" even ONCE just to see what fucking
    happens!!!? I hope you DIE!!! I HOPE YOU DIE AND YOU GO TO HELL!!!
    YOU WORTHLESS PEICE OF SHIT!!!\'
    """

        print(string_elif_6)
        print(f"\'face_smashes\' is: {face_smashes}.")
        face_smashes = face_smashes + 1
        print(f"now \'face_smashes\' is: {face_smashes}.")
        zombie_battle()
    elif fight == "smash" and face_smashes == 10:

        string_elif_7 = """
    You've exausted your strength. Obviously the player doesn\'t care
    about you and just thinks your suffering is funny. You realize
    you're going to die if you don't take matters into your own hands.
    With the last of your energy you push against the zombie with your
    whole body. When it tries to counter by pushing back you whip
    your body out of its way, grab it by its arm, stick your leg out
    and use its momentum to guid it over your outstreched leg. It
    trips over your leg, because it's an idiot, and its face bounces
    off the ground with a wet slap. You launch yourself on top of the
    fallen creature\'s back, grab it by the hair, and slam its head into
    the stones over and over and over untill nothing is left of its head
    but a sad leaky sack of skin with a soup of pulverized bone, brain
    and blood leaking out of it like and impotent untied garbage bag of
    fall leaves that's tipped over and is spilling its contents onto
    the ground. You roll over onto the ground next to it and spend
    forty five minutes catching your breath. That was seriously the
    worst thing you've ever experienced and you hope that the player
    gets ebola and anthrax at the same time. You pick yourself up
    off the ground. You take the dead gaurds sword out of its shieth
    and take it to the blacksmith for it's metal.
    """

        print(string_elif_7)
        print(f"bridge_problem_chain_explained: {bridge_problem_chain_explained}.")
        bridge_problem_chain_explained += 1
        print(f"bridge_problem_chain_explained: {bridge_problem_chain_explained}.")
        print(f"gt_activated: {gt_activated}.")
        gt_activated.append("sw")
        print(f"gt_activated: {gt_activated}.")
        blacksmith()
    else:
        print("You didn't do anything and the zombie ate you. Good Job!")
        exit(0)

def ne_gaurd_tower():
    global bridge_problem_chain_explained
    global gt_activated

    string_ne_gaurd_tower = """
    You are at the top of the north east gaurd tower. You find yourself
    next to a gaurd on duty. Looking over the tower's battlements you
    can see the sea of shambling zombies futilely trying to break into
    the castle.
    """

    print(string_ne_gaurd_tower)

    if bridge_problem_chain_explained <= 1:

        string_if = """
    You can either stay here and look aimlesly at the writhing hoard
    below you, shoot arrows at the zombies to relieve your boredom,
    or you can go back to the castle courtyard. What would you like
    to do?
    """

        print(string_if)
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:

            string_if_elif_1 = """
    You pick up a bow and a quiver of arrows. You pull out an
    arrow, knock it to the bow and pull the string back. You
    Sight along the arrow at the head of a particularly ugly and
    decomposed member of the walking dead and you let the arrow
    fly. There is a wet thud, which you can hear even over the,
    moaning of the undead, as the arrow slams through the zombies
    skull. It crumples to the ground and disapears under the sea
    of shambling, rotten boddies. You look up with a mischevious
    smile at the gaurd next to you expecting to see that you've
    impressed him with your marksmenship but are supprised to
    find him scowling at you. You realize then that even though
    he won't say it, because you outrank him, he's thinking that
    you've just waisted a precious arrow that can't be retrieved.
    You should quit showing off like a jackass and get back to
    work.
    """

            print(string_if_elif_1)
            ne_gaurd_tower()
        else:
            ne_gaurd_tower()

    elif bridge_problem_chain_explained > 1 and "ne" not in gt_activated:

        string_elif_1 = """
    You can either stay here and look aimlesly at the writhing hoard
    below you, shoot arrows at the zombies to relieve your boredom,
    go back to the castle courtyard, or talk to the gaurd. What
    would you like to do?
    """

        print(string_elif_1)
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:

            string_elif_1_elif_1 = """
    You pick up a bow and a quiver of arrows. You pull out an
    arrow, knock it to the bow and pull the string back. You
    Sight along the arrow at the head of a particularly ugly and
    decomposed member of the walking dead and you let the arrow
    fly. There is a wet thud, which you can hear even over the,
    moaning of the undead, as the arrow slams through the zombies
    skull. It crumples to the ground and disapears under the sea
    of shambling, rotten boddies. You look up with a mischevious
    smile at the gaurd next to you expecting to see that you've
    impressed him with your marksmenship but are supprised to
    find him scowling at you. You realize then that even though
    he won't say it, because you outrank him, he's thinking that
    you've just waisted a precious arrow that can't be retrieved.
    You should quit showing off like a jackass and get back to
    work.
    """

            print(string_elif_1_elif_1)
            ne_gaurd_tower()
        elif "talk" in what_to_do or "gaurd" in what_to_do:

            string_elif_1_elif_2 = """
    You walk over to the gaurd, explain the blacsmith's need for
    metal and politley ask him to go give her his sword. He heads
    off to go do that. You head back to the courtyard.
    """

            print(string_elif_1_elif_2)
            print(f"bridge_problem_chain_explained: {bridge_problem_chain_explained}.")
            bridge_problem_chain_explained += 1
            print(f"bridge_problem_chain_explained: {bridge_problem_chain_explained}.")
            print(f"gt_activated: {gt_activated}.")
            gt_activated.append("ne")
            print(f"gt_activated: {gt_activated}.")
            courtyard()
        else:
            ne_gaurd_tower()

    else:

        string_else = """
    You can either stay here and look aimlesly at the writhing hoard
    below you, shoot arrows at the zombies to relieve your boredom,
    or you can go back to the castle courtyard. What would you like
    to do?
    """

        print(string_else)
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:

            string_else_elif_1 = """
    You pick up a bow and a quiver of arrows. You pull out an
    arrow, knock it to the bow and pull the string back. You
    Sight along the arrow at the head of a particularly ugly and
    decomposed member of the walking dead and you let the arrow
    fly. There is a wet thud, which you can hear even over the,
    moaning of the undead, as the arrow slams through the zombies
    skull. It crumples to the ground and disapears under the sea
    of shambling, rotten boddies. You look up with a mischevious
    smile at the gaurd next to you expecting to see that you've
    impressed him with your marksmenship but are supprised to
    find him scowling at you. You realize then that even though
    he won't say it, because you outrank him, he's thinking that
    you've just waisted a precious arrow that can't be retrieved.
    You should quit showing off like a jackass and get back to
    work.
    """

            print(string_else_elif_1)
            ne_gaurd_tower()
        else:
            ne_gaurd_tower()

def se_gaurd_tower():
    global bridge_problem_chain_explained
    global gt_activated

    string_se_gaurd_tower = """
    You are at the top of the south east gaurd tower. You find yourself
    next to a gaurd on duty. Looking over the tower's battlements to the
    east you can see the sea of shambling zombies futilely trying to
    break into the castle. To the south you see the chasam over which you
    plan to make your escape. From time to time a zombie gets pushed over
    the chasm's edge by the weight of the hoard. They fall listless and
    uncomprehending to the impact of their second death.
    """

    print(string_se_gaurd_tower)

    if bridge_problem_chain_explained <= 1:

        string_if = """
    You can either stay here and look aimlesly at the writhing hoard
    below you, shoot arrows at the zombies to relieve your boredom,
    or you can go back to the castle courtyard. What would you like
    to do?
    """

        print(string_if)
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:
            string_if_elif_1 = """
    You pick up a bow and a quiver of arrows. You pull out an
    arrow, knock it to the bow and pull the string back. You
    Sight along the arrow at the head of a particularly ugly and
    decomposed member of the walking dead and you let the arrow
    fly. There is a wet thud, which you can hear even over the,
    moaning of the undead, as the arrow slams through the zombies
    skull. It crumples to the ground and disapears under the sea
    of shambling, rotten boddies. You look up with a mischevious
    smile at the gaurd next to you expecting to see that you've
    impressed him with your marksmenship but are supprised to
    find him scowling at you. You realize then that even though
    he won't say it, because you outrank him, he's thinking that
    you've just waisted a precious arrow that can't be retrieved.
    You should quit showing off like a jackass and get back to
    work.
    """
            se_gaurd_tower()
        else:
            se_gaurd_tower()

    elif bridge_problem_chain_explained > 1 and "se" not in gt_activated:

        string_elif = """
    You can either stay here and look aimlesly at the writhing hoard
    below you, shoot arrows at the zombies to relieve your boredom,
    go back to the castle courtyard, or talk to the gaurd. What
    would you like to do?
    """

        print(string_elif)
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:

            string_elif_1_elif_1 = """
    You pick up a bow and a quiver of arrows. You pull out an
    arrow, knock it to the bow and pull the string back. You
    Sight along the arrow at the head of a particularly ugly and
    decomposed member of the walking dead and you let the arrow
    fly. There is a wet thud, which you can hear even over the,
    moaning of the undead, as the arrow slams through the zombies
    skull. It crumples to the ground and disapears under the sea
    of shambling, rotten boddies. You look up with a mischevious
    smile at the gaurd next to you expecting to see that you've
    impressed him with your marksmenship but are supprised to
    find him scowling at you. You realize then that even though
    he won't say it, because you outrank him, he's thinking that
    you've just waisted a precious arrow that can't be retrieved.
    You should quit showing off like a jackass and get back to
    work.
    """

            print(string_elif_1_elif_1)
            se_gaurd_tower()
        elif "talk" in what_to_do or "gaurd" in what_to_do:

            string_elif_1_elif_2 = """
    You walk over to the gaurd, explain the blacsmith's need for
    metal and politley ask him to go give her his sword. He heads
    off to go do that. You head back to the courtyard.
    """

            print(string_elif_1_elif_2)
            print(f"bridge_problem_chain_explained: {bridge_problem_chain_explained}.")
            bridge_problem_chain_explained += 1
            print(f"bridge_problem_chain_explained: {bridge_problem_chain_explained}.")
            print(f"gt_activated: {gt_activated}.")
            gt_activated.append("se")
            print(f"gt_activated: {gt_activated}.")
            courtyard()
        else:
            se_gaurd_tower()

    else:

        string_else = """
    You can either stay here and look aimlesly at the writhing hoard
    below you, shoot arrows at the zombies to relieve your boredom,
    or you can go back to the castle courtyard. What would you like
    to do?
    """

        print(string_else)
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:

            string_else_elif_1 = """
    You pick up a bow and a quiver of arrows. You pull out an
    arrow, knock it to the bow and pull the string back. You
    Sight along the arrow at the head of a particularly ugly and
    decomposed member of the walking dead and you let the arrow
    fly. There is a wet thud, which you can hear even over the,
    moaning of the undead, as the arrow slams through the zombies
    skull. It crumples to the ground and disapears under the sea
    of shambling, rotten boddies. You look up with a mischevious
    smile at the gaurd next to you expecting to see that you've
    impressed him with your marksmenship but are supprised to
    find him scowling at you. You realize then that even though
    he won't say it, because you outrank him, he's thinking that
    you've just waisted a precious arrow that can't be retrieved.
    You should quit showing off like a jackass and get back to
    work.
    """

            print(string_else_elif_1)
            se_gaurd_tower()
        else:
            se_gaurd_tower()

def carpenter():
    global bridge_problem_gears_explained
    global wood_problem_explained

    string_intro = """
    You are in the carpenter's workshop. You see him working in concentration
    with his tools.
    """

    print(string_intro)

    if bridge_problem_gears_explained == 0:

        string_if = """
    You can stay here or go back to the courtyard. What would you
    like to do?
    """

        print(string_if)
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        else:
            carpenter()

    elif bridge_problem_gears_explained == 1:

        string_elif_1 = """
    You can stay here, talk to the carpenter, or go back to the
    courtyard. What would you like to do?
    """

        print(string_elif_1)
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "carpenter" in where_to:

            string_elif_1_elif_1 = """
    You tell him about the rotten gears and he says that
    he will remove them but that he will need a more
    extensive supply of wood to construct new ones. You
    head back out into the courtyard.
    """

            print(string_elif_1_elif_1)
            bridge_problem_gears_explained = 2
            wood_problem_explained = 1
            print(f"pully is: {pully}")
            pully.remove(str("rotten gears"))
            print(f"now pully is: {pully}")
            courtyard()
        else:
            carpenter()
    elif bridge_problem_gears_explained == 2:

        string_elif_2 = """
    You can stay here, talk to the carpenter, or go back to the
    courtyard. What would you like to do?"
    """

        print(string_elif_2)
        where_to = input("> ")
        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "carpenter" in where_to:

            string_elif_2_elif_1 = """
    He tells you that the rotten gears have been removed from
    the pully system in the drawbridge gaurdtower but that he
    still needs the wood to make the new gears. You head back
    to the courtyard.
    """

            print(string_elif_2_elif_1)
            courtyard()
        else:
            carpenter()

    elif bridge_problem_gears_explained == 3:
        string_elif_3 = """
    You can stay here, talk to the carpenter, or go back to the
    courtyard. What would you like to do?
    """

        print(string_elif_3)
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "carpenter" in where_to:

            string_elif_3_elif_1 = """
    He tells you that the wood from the keep's furnature was
    perfect and he takes you to look at his new gears, which he's
    obviously more than a little proud of. They're well made
    and you thank him for his work. You both agree that they're
    to big to be moved accross the courtyard by hand and that
    you'll need to get the men to load them onto a horse drawn
    wagon. You head back to the courtyard.
    """
            print(string_elif_3_elif_1)
            courtyard()
        else:
            carpenter()

    elif bridge_problem_gears_explained == 4 and "horses" in crew and "wagon" in crew:

        string_elif_4 = """
    You have brought the men, horses and wagon to the carpenter's
    workshop so they can move the gears to the drawbridge gaurdtower.
    You can stay here or talk to the carpenter. What would you like
    to do?
    """

        print(string_elif_4)
        where_to = input("> ")

        if "talk" in where_to or "carpenter" in where_to:

            string_elif_4_if = """
    He oversees the men moving the gears outside and then he
    directs them as they load the wooden contraptions into the
    cart. The horses pull the cart away towards the drawbridge
    gaurdtower. You watch them go as you stand in the courtyard.
    """

            print(string_elif_4_if)
            print(f"pully is: {pully}")
            pully.insert(1, str("new gears"))
            print(f"now pully is: {pully}")
            bridge_problem_gears_explained = 5
            courtyard()
        else:
            carpenter()
    else:

        string_else = """
    You can stay here or go back to the courtyard. What would you
    like to do?
    """

        print(string_else)
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        else:
            carpenter()

def keep():
    global bridge_problem_gears_explained
    global wood_problem_explained
    global crew

    string_intro = """
    You enter the great hall of the Keep. There's a fire burning in the
    fireplace and the room's warmth is comforting after the cold of the
    dreary day outside. There are tapestries on the wall that remind you
    of happier days.
    """

    print(string_intro)

    if wood_problem_explained == 0:

        string_if = """
    You can see the beautiful wooden banquet tables that you used to
    sit upon for the king's feasts. You miss those feasts.

    You can stay here, go down into the cript, or go back to the courtyard.
    Where would you like to go?
    """

        print(string_if)
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "cript" in where_to:
            cript()
        else:
            keep()

    elif wood_problem_explained == 1 and "men" in crew:

        string_elif_1 = """
    The soldiers enter the great hall behind you. They open wide, the
    doors to the hall, and set about removing the wooden feasting tables.
    You quietly shed some tears thinking of all the good times you've
    had while sitting at those tables. Then you take a deep breath and
    resign yourself to the thought that they will soon be no more than
    gears in a pully in a castle that you will be leaving behind.

    You dry your eyes and head back out into the courtyard.
    """

        print(string_elif_1)
        bridge_problem_gears_explained = 3
        wood_problem_explained = 2
        courtyard()

    elif wood_problem_explained == 1:

        string_elif_1 = """
    You can see the beautiful wooden banquet tables that you used to
    sit upon for the king's feasts. These would be an adequate supply.
    of wood for the carpenter to make the gears with. Unfortunatley,
    these tables are too big for you to lift by yourself. You will
    need some help to get them to the carpenter.

    You can stay here, go down into the cript, or go back to the courtyard.
    Where would you like to go?
    """

        print(string_elif_1)
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "cript" in where_to:
            cript()
        else:
            keep()

    elif wood_problem_explained == 2:

        string_elif_2 = """
    You can see the empty space where the banquet tables used to be.
    You feel a twinge of sadness.

    You can stay here, go down into the cript, or go back to the courtyard.
    Where would you like to go?
    """

        print(string_elif_2)
        where_to = input("> ")

        if "courtyard" in where_to:
            courtyard()
        elif "cript" in where_to:
            cript()
        else:
            keep()

def cript():

    string_intro = """
    You enter the cript. It is dark and oppressive, lit by only a single torch.
    Here you find the graves of the king, his family, and their ancestors.
    You sigh with sorrow as you think upon the tragic death of your late
    ruller and his family. It was you who found them. Late one night when
    you rushed up to thier chambers to deliver a message that had been brought
    by raven. You stood outside the door of thier family common room. The king
    had been ill of late, so it was nothing surprising when you heard moans comming
    from within the room, but then you heard a crunch and a scream! You rushed
    headlong into the room to a sceen of utter horror! The royal prince and
    princess lay upon the floor in pools of their own blood. The princess
    was dead and the the prince was gurgling the last of his raggad, bloody
    breaths. On the other side of the room the king, now a zombie, lay over
    his wife's body chewing at her ruined throat. You cut off his head and
    quickly decapitated the other boddies to stop an outbreak. To this day
    none know how the king had gotten bitten nor why he didn't tell his
    trusted advisors. Three days later the Zombie hoard appeard on the
    horizon and it fell to you to oversee the castle's defenses.

    You can stay here, or go back up to the great hall of the Keep.
    Where would you like to go?
    """

    print(string_intro)
    where_to = input("> ")

    if "eep" in where_to or "up" in where_to or "back" in where_to or "hall" in where_to:
        keep()
    else:
        cript()

def barricks():
    global wood_problem_explained
    global crew

    if wood_problem_explained == 1 and "men" in crew:

        string_if = """
    The barricks is so quiet when it's empty. It's good that the soldiers
    are occupied with work and not stuck in here ruminating on the doom
    outside the castle walls. You head back into the courtyard.
    """

        print(string_if)
        courtyard()
    elif wood_problem_explained == 1:

        string_elif_1 = """
    You call the soldiers to attention. They form up and you explain
    to them that the carpenter needs the wood from the banquet tables
    in the keep. They fall in line and you take them to the Keep.
    """

        print(string_elif_1)
        crew.append("men")
        keep()
    elif wood_problem_explained == 2:

        string_elif_2 = """
    The barricks is so quiet when it's empty. It's good that the soldiers
    are occupied with work and not stuck in here ruminating on the doom
    outside the castle walls. You head back into the courtyard.
    """

        print(string_elif_2)
        courtyard()
    else:

        string_else = """
    You walk into the barricks. The off duty soldiers are standing around
    chatting, sitting and playing cards, or laying in their bunks.
    It's good to see the men are healthy despite the troubles that
    surround them. You feel proud of them as you head back out to
    the courtyard.
    """

        print(string_else)
        courtyard()

def stables():
    global bridge_problem_gears_explained

    if bridge_problem_gears_explained < 3:

        string_if = """
    You walk into the stables. Outside you saw an open wagon that a
    pesant used to bring grain into the castle before the hoard arrived.
    It's a good thing that grain arrived in time or else the horses would
    have starved weeks ago. Inside the stables you see the creatures
    lounging in their stalls, peacfully unaware of the horrors outside.
    You head back out to the courtyard.
    """

        print(string_if)
        courtyard()
    elif bridge_problem_gears_explained == 3:

        string_elif_1 = """
    You enter the stables with the soldiers and they set about pulling
    the horses out of their pens. They bring the horses out of the
    stables and harness a team of them to the wagon. You are in the
    courtyard.
    """

        print(string_elif_1)
        crew.append("horses")
        crew.append("wagon")
        bridge_problem_gears_explained = 4
        courtyard()

    else:

        string_else = """
    You walk into the empty stables. The horses are out being used
    for work. There's nothing in here. You head back out to the
    courtyard.
    """

        print(string_else)
        courtyard()

start()
