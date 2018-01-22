## 'dd' stands for design document. This is Where
## I will write out notes in english detailing what
## needs to be done and then write the code to
## perform that function.

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

def start():
    print("\nYou are in a castle that is under siege from a zombie hoard.")
    print("The castle walls and gate are holding the hoard off with no")
    print("difficulty but the castle is running out of food and you and your")
    print("people will soon starve if you stay here. At the back of the castle")
    print("is a drawbridge that can be used to cross a deep chasam which runs")
    print("behind the castle. This chasam cannot be crossed by the zombie")
    print("hoard and so it is by way of this drawbridge that you and your")
    print("people can make your escape. There is just one problem: the")
    print("drawbridge has not been used in decades. It is in disrepair and")
    print("cannot be lowerd. It must be fixed before you can escape.")
    print("\nIf you stand in the courtyard, in front of the castle gates,")
    print("you can see several buldings within the castle walls:")
    print("In the north west corner of the castle are the stables and the")
    print("north west gaurd tower. In the south west corner of the castle are")
    print("the barricks and the south west gaurd tower. In the north east")
    print("corner of the castle are the blacksmith\'s workshop and the north")
    print("east gaurd tower. In the south east corner of the castle are the")
    print("carpenter\'s workshop and the south east gaurd tower. In the center")
    print("of the castle is the Keep where the king and his family used to live.")
    courtyard()

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

def nw_gaurd_tower():
    print("\nYou are at the top of the north west gaurd tower. You find yourself")
    print("next to a gaurd on duty. Looking over the tower's battlements you")
    print("can see the sea of shambling zombies futilely trying to break into")
    print("the castle.")

    global bridge_problem_chain_explained
    global gt_activated

    if bridge_problem_chain_explained <= 1:
        print("\nYou can either stay here and look aimlesly at the writhing hoard")
        print("below you, shoot arrows at the zombies to relieve your boredom,")
        print("or you can go back to the castle courtyard. What would you like")
        print("to do?")
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:
            print("\nYou pick up a bow and a quiver of arrows. You pull out an")
            print("arrow, knock it to the bow and pull the string back. You")
            print("Sight along the arrow at the head of a particularly ugly and")
            print("decomposed member of the walking dead and you let the arrow")
            print("fly. There is a wet thud, which you can hear even over the,")
            print("moaning of the undead, as the arrow slams through the zombies")
            print("skull. It crumples to the ground and disapears under the sea")
            print("of shambling, rotten boddies. You look up with a mischevious")
            print("smile at the gaurd next to you expecting to see that you've")
            print("impressed him with your marksmenship but are supprised to")
            print("find him scowling at you. You realize then that even though")
            print("he won't say it, because you outrank him, he's thinking that")
            print("you've just waisted a precious arrow that can't be retrieved.")
            print("You should quit showing off like a jackass and get back to")
            print("work.")
            nw_gaurd_tower()
        else:
            nw_gaurd_tower()

    elif bridge_problem_chain_explained > 1 and "nw" not in gt_activated:
        print("\nYou can either stay here and look aimlesly at the writhing hoard")
        print("below you, shoot arrows at the zombies to relieve your boredom,")
        print("go back to the castle courtyard, or talk to the gaurd. What")
        print("would you like to do?")
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:
            print("\nYou pick up a bow and a quiver of arrows. You pull out an")
            print("arrow, knock it to the bow and pull the string back. You")
            print("Sight along the arrow at the head of a particularly ugly and")
            print("decomposed member of the walking dead and you let the arrow")
            print("fly. There is a wet thud, which you can hear even over the,")
            print("moaning of the undead, as the arrow slams through the zombies")
            print("skull. It crumples to the ground and disapears under the sea")
            print("of shambling, rotten boddies. You look up with a mischevious")
            print("smile at the gaurd next to you expecting to see that you've")
            print("impressed him with your marksmenship but are supprised to")
            print("find him scowling at you. You realize then that even though")
            print("he won't say it, because you outrank him, he's thinking that")
            print("you've just waisted a precious arrow that can't be retrieved.")
            print("You should quit showing off like a jackass and get back to")
            print("work.")
            nw_gaurd_tower()

        elif "talk" in what_to_do or "gaurd" in what_to_do:
            print("\nYou walk over to the gaurd, explain the blacsmith's need for")
            print("metal and politley ask him to go give her his sword. He heads")
            print("off to go do that. You head back to the courtyard.")
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
        print("\nYou can either stay here and look aimlesly at the writhing hoard")
        print("below you, shoot arrows at the zombies to relieve your boredom,")
        print("or you can go back to the castle courtyard. What would you like")
        print("to do?")
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:
            print("\nYou pick up a bow and a quiver of arrows. You pull out an")
            print("arrow, knock it to the bow and pull the string back. You")
            print("Sight along the arrow at the head of a particularly ugly and")
            print("decomposed member of the walking dead and you let the arrow")
            print("fly. There is a wet thud, which you can hear even over the,")
            print("moaning of the undead, as the arrow slams through the zombies")
            print("skull. It crumples to the ground and disapears under the sea")
            print("of shambling, rotten boddies. You look up with a mischevious")
            print("smile at the gaurd next to you expecting to see that you've")
            print("impressed him with your marksmenship but are supprised to")
            print("find him scowling at you. You realize then that even though")
            print("he won't say it, because you outrank him, he's thinking that")
            print("you've just waisted a precious arrow that can't be retrieved.")
            print("You should quit showing off like a jackass and get back to")
            print("work.")
            nw_gaurd_tower()
        else:
            nw_gaurd_tower()

def sw_gaurd_tower():

    global bridge_problem_chain_explained
    global gt_activated

    if bridge_problem_chain_explained <= 1:
        print("\nYou are at the top of the south west gaurd tower. You find yourself")
        print("next to a gaurd on duty. He looks very ill with a pallor to his skin,")
        print("glassy eyes and sweat stained clothes. You decide to keep your eyes")
        print("on him. The last thing you need is a plague breaking out in the middle")
        print("of a seige. Looking over the tower's battlements you can see, to")
        print("the west, the sea of shambling zombies futilely trying to break")
        print("into the castle and, to the south, you see the chasam over which you")
        print("plan to make your escape. From time to time a zombie gets pushed over")
        print("the chasm's edge by the weight of the hoard. They fall listless and")
        print("uncomprehending to the impact of their second death.")
        print("\nYou can either stay here and look aimlesly at the writhing hoard")
        print("below you, shoot arrows at the zombies to relieve your boredom,")
        print("or you can go back to the castle courtyard. What would you like")
        print("to do?")
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:
            print("\nYou pick up a bow and a quiver of arrows. You pull out an")
            print("arrow, knock it to the bow and pull the string back. You")
            print("Sight along the arrow at the head of a particularly ugly and")
            print("decomposed member of the walking dead and you let the arrow")
            print("fly. There is a wet thud, which you can hear even over the,")
            print("moaning of the undead, as the arrow slams through the zombies")
            print("skull. It crumples to the ground and disapears under the sea")
            print("of shambling, rotten boddies. You look up with a mischevious")
            print("smile at the gaurd next to you expecting to see that you've")
            print("impressed him with your marksmenship but are supprised to")
            print("find him scowling at you. You realize then that even though")
            print("he won't say it, because you outrank him, he's thinking that")
            print("you've just waisted a precious arrow that can't be retrieved.")
            print("You should quit showing off like a jackass and get back to")
            print("work.")
            sw_gaurd_tower()
        else:
            sw_gaurd_tower()

    elif bridge_problem_chain_explained > 1 and "sw" not in gt_activated:
        print("You assend the stairs to the top of the south west gaurdtower.")
        print("As you open the door leading out to the gaurdtower's battlements")
        print("you see the gaurd on duty. He's turned away from you, looking out")
        print("at the chasam behind the castle. There's somethig off about his")
        print("posture... you hear an animal groan comming from him as he turns")
        print("around to face you... your eyes widen and adrenaline pumps into")
        print("your veins as your blood runs cold. Before you have time to really")
        print("process what you're seeing the zombie lunges at you! You raise")
        print("your left arm to fend off it's onslaught and it bites into the chain")
        print("mail armoring your forearm.")
        zombie_battle()
    else:
        print("\nYou are at the top of the south west gaurd tower. The bloody body")
        print("of the dead gaurd lies on the tower stones where you left it. Looking")
        print("over the tower's battlements you can see, to the west, the sea of")
        print("shambling zombies futilely trying to break into the castle and, to")
        print("the south, you see the chasam over which you plan to make your")
        print("escape. From time to time a zombie gets pushed over the chasm's")
        print("edge by the weight of the hoard. They fall listless and uncomprehending")
        print("to the impact of their second death.")
        print("\nYou can either stay here and look aimlesly at the writhing hoard")
        print("below you, shoot arrows at the zombies to relieve your boredom,")
        print("or you can go back to the castle courtyard. What would you like")
        print("to do?")
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:
            print("\nYou pick up a bow and a quiver of arrows. You pull out an")
            print("arrow, knock it to the bow and pull the string back. You")
            print("Sight along the arrow at the head of a particularly ugly and")
            print("decomposed member of the walking dead and you let the arrow")
            print("fly. There is a wet thud, which you can hear even over the,")
            print("moaning of the undead, as the arrow slams through the zombies")
            print("skull. It crumples to the ground and disapears under the sea")
            print("of shambling, rotten boddies. You look up with a mischevious")
            print("smile at the gaurd next to you expecting to see that you've")
            print("impressed him with your marksmenship but are supprised to")
            print("find him scowling at you. You realize then that even though")
            print("he won't say it, because you outrank him, he's thinking that")
            print("you've just waisted a precious arrow that can't be retrieved.")
            print("You should quit showing off like a jackass and get back to")
            print("work.")
            sw_gaurd_tower()
        else:
            sw_gaurd_tower()

face_smashes = 0

def zombie_battle():

    global bridge_problem_chain_explained
    global gt_activated
    global face_smashes

    print("\nThe zombie chews on your mailed arm and presses its weight into you.")
    print("You can hear it's newly dead teath cracking and breaking against your")
    print("armor.")
    print("What will you do?")
    print("Shove the zombie away and draw your sword? (type 'shove')")
    print("Draw your knife? (type 'knife')")
    print("Smash the zombie in the face with your armored fist? (type 'smash')")
    fight = input("> ")

    if fight == "shove":
        print("\nYou kick the zombie in the chest to gain space. In one fluid")
        print("motion you draw your sword from the shieth on your belt and,")
        print("using the momentum from that motion to sweep your sword in an upward")
        print("arc and slice part of its head off. Unfortonatly, enough of its")
        print("brain is sitll intact for it to keep functioning so you swing")
        print("your blaid back around and slash its head off at the neck. The")
        print("headless body crumples to the ground. You take the dead gaurds sword")
        print("out of its shieth and take it to the blacksmith for it's metal.")
        print(f"bridge_problem_chain_explained: {bridge_problem_chain_explained}.")
        bridge_problem_chain_explained += 1
        print(f"bridge_problem_chain_explained: {bridge_problem_chain_explained}.")
        print(f"gt_activated: {gt_activated}.")
        gt_activated.append("sw")
        print(f"gt_activated: {gt_activated}.")
        blacksmith()
    elif fight == "knife":
        print("\nYou draw your knife and plunge it into the zombies eye at an")
        print("upward angle, destroying it's brain. The now lifeless body")
        print("crumples to the ground. You take the dead gaurds sword out of")
        print("its shieth and take it to the blacksmith for it's metal.")
        print(f"bridge_problem_chain_explained: {bridge_problem_chain_explained}.")
        bridge_problem_chain_explained += 1
        print(f"bridge_problem_chain_explained: {bridge_problem_chain_explained}.")
        print(f"gt_activated: {gt_activated}.")
        gt_activated.append("sw")
        print(f"gt_activated: {gt_activated}.")
        blacksmith()
    elif fight == "smash" and face_smashes < 1:
        print("\nAs you hold the zombie off with your left arm, you work furiously")
        print("to dislodge it's helmet with your right hand. Finally it comes")
        print("off and clatters on the stones benieth you. You wind up your free")
        print("hand and slam it into the zombies face as hard as you can.")
        print(f"\'face_smashes\' is: {face_smashes}.")
        face_smashes = face_smashes + 1
        print(f"now \'face_smashes\' is: {face_smashes}.")
        zombie_battle()
    elif fight == "smash" and face_smashes >= 1 and face_smashes < 3:
        print("\nAgain you wind up your free hand and smash it into the zombies")
        print("face with all your strenght.")
        print(f"\'face_smashes\' is: {face_smashes}.")
        face_smashes = face_smashes + 1
        print(f"now \'face_smashes\' is: {face_smashes}.")
        zombie_battle()
    elif fight == "smash" and face_smashes >= 3 and face_smashes < 6:
        print("\nAgain you wind up your free hand and slam it into the zombies")
        print("face as hard as you can. You feel the bones of its face break")
        print("under your chain-mailed fist and when you pull your hand away")
        print("blood and teath fall out of its face.")
        print(f"\'face_smashes\' is: {face_smashes}.")
        face_smashes = face_smashes + 1
        print(f"now \'face_smashes\' is: {face_smashes}.")
        zombie_battle()
    elif fight == "smash" and face_smashes >= 6 and face_smashes < 9:
        print("\nYou're getting tired. You're gasping for breath and your punches")
        print("are starting to loose their strength. None the less you hit the")
        print("monster again and blood and gore spurt out from it\'s face.")
        print("You feel its skull crack and it's face cave in a little.")
        print(f"\'face_smashes\' is: {face_smashes}.")
        face_smashes = face_smashes + 1
        print(f"now \'face_smashes\' is: {face_smashes}.")
        zombie_battle()
    elif fight == "smash" and face_smashes == 9:
        print("\nYou hit the monster again and one of its eyes pop out of its")
        print("socket and dangles over your left arm. You're nearing exaustion.")
        print("If this doesn't end soon you're going to collapse and be eaten.")
        print("You wonder to your self \'why!!!? why wont this asshole player try")
        print("one of the other options? Why is this peice of shit who\'s typing")
        print("on the keyboard so committed to typing \"smash\"!!!? What the")
        print("hell wrong with this dumb shit mother fucker!!!? What?! You can't")
        print("type \"shove\" or \"knife\" even ONCE just to see what fucking")
        print("happens!!!? I hope you DIE!!! I HOPE YOU DIE AND YOU GO TO HELL!!!")
        print("YOU WORTHLESS PEICE OF SHIT!!!\'")
        print(f"\'face_smashes\' is: {face_smashes}.")
        face_smashes = face_smashes + 1
        print(f"now \'face_smashes\' is: {face_smashes}.")
        zombie_battle()
    elif fight == "smash" and face_smashes == 10:
        print("\nYou've exausted your strength. Obviously the player doesn\'t care")
        print("about you and just thinks your suffering is funny. You realize")
        print("you're going to die if you don't take matters into your own hands.")
        print("With the last of your energy you push against the zombie with your")
        print("whole body. When it tries to counter by pushing back you whip")
        print("your body out of its way, grab it by its arm, stick your leg out")
        print("and use its momentum to guid it over your outstreched leg. It")
        print("trips over your leg, because it's an idiot, and its face bounces")
        print("off the ground with a wet slap. You launch yourself on top of the")
        print("fallen creature\'s back, grab it by the hair, and slam its head into")
        print("the stones over and over and over untill nothing is left of its head")
        print("but a sad leaky sack of skin with a soup of pulverized bone, brain")
        print("and blood leaking out of it like and impotent untied garbage bag of")
        print("fall leaves that's tipped over and is spilling its contents onto")
        print("the ground. You roll over onto the ground next to it and spend")
        print("forty five minutes catching your breath. That was seriously the")
        print("worst thing you've ever experienced and you hope that the player")
        print("gets ebola and anthrax at the same time. You pick yourself up")
        print("off the ground. You take the dead gaurds sword out of its shieth")
        print("and take it to the blacksmith for it's metal.")
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
    print("\nYou are at the top of the north east gaurd tower. You find yourself")
    print("next to a gaurd on duty. Looking over the tower's battlements you")
    print("can see the sea of shambling zombies futilely trying to break into")
    print("the castle.")

    global bridge_problem_chain_explained
    global gt_activated

    if bridge_problem_chain_explained <= 1:
        print("\nYou can either stay here and look aimlesly at the writhing hoard")
        print("below you, shoot arrows at the zombies to relieve your boredom,")
        print("or you can go back to the castle courtyard. What would you like")
        print("to do?")
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:
            print("\nYou pick up a bow and a quiver of arrows. You pull out an")
            print("arrow, knock it to the bow and pull the string back. You")
            print("Sight along the arrow at the head of a particularly ugly and")
            print("decomposed member of the walking dead and you let the arrow")
            print("fly. There is a wet thud, which you can hear even over the,")
            print("moaning of the undead, as the arrow slams through the zombies")
            print("skull. It crumples to the ground and disapears under the sea")
            print("of shambling, rotten boddies. You look up with a mischevious")
            print("smile at the gaurd next to you expecting to see that you've")
            print("impressed him with your marksmenship but are supprised to")
            print("find him scowling at you. You realize then that even though")
            print("he won't say it, because you outrank him, he's thinking that")
            print("you've just waisted a precious arrow that can't be retrieved.")
            print("You should quit showing off like a jackass and get back to")
            print("work.")
            ne_gaurd_tower()
        else:
            ne_gaurd_tower()

    elif bridge_problem_chain_explained > 1 and "ne" not in gt_activated:
        print("\nYou can either stay here and look aimlesly at the writhing hoard")
        print("below you, shoot arrows at the zombies to relieve your boredom,")
        print("go back to the castle courtyard, or talk to the gaurd. What")
        print("would you like to do?")
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:
            print("\nYou pick up a bow and a quiver of arrows. You pull out an")
            print("arrow, knock it to the bow and pull the string back. You")
            print("Sight along the arrow at the head of a particularly ugly and")
            print("decomposed member of the walking dead and you let the arrow")
            print("fly. There is a wet thud, which you can hear even over the,")
            print("moaning of the undead, as the arrow slams through the zombies")
            print("skull. It crumples to the ground and disapears under the sea")
            print("of shambling, rotten boddies. You look up with a mischevious")
            print("smile at the gaurd next to you expecting to see that you've")
            print("impressed him with your marksmenship but are supprised to")
            print("find him scowling at you. You realize then that even though")
            print("he won't say it, because you outrank him, he's thinking that")
            print("you've just waisted a precious arrow that can't be retrieved.")
            print("You should quit showing off like a jackass and get back to")
            print("work.")
            ne_gaurd_tower()
        elif "talk" in what_to_do or "gaurd" in what_to_do:
            print("\nYou walk over to the gaurd, explain the blacsmith's need for")
            print("metal and politley ask him to go give her his sword. He heads")
            print("off to go do that. You head back to the courtyard.")
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
        print("\nYou can either stay here and look aimlesly at the writhing hoard")
        print("below you, shoot arrows at the zombies to relieve your boredom,")
        print("or you can go back to the castle courtyard. What would you like")
        print("to do?")
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:
            print("\nYou pick up a bow and a quiver of arrows. You pull out an")
            print("arrow, knock it to the bow and pull the string back. You")
            print("Sight along the arrow at the head of a particularly ugly and")
            print("decomposed member of the walking dead and you let the arrow")
            print("fly. There is a wet thud, which you can hear even over the,")
            print("moaning of the undead, as the arrow slams through the zombies")
            print("skull. It crumples to the ground and disapears under the sea")
            print("of shambling, rotten boddies. You look up with a mischevious")
            print("smile at the gaurd next to you expecting to see that you've")
            print("impressed him with your marksmenship but are supprised to")
            print("find him scowling at you. You realize then that even though")
            print("he won't say it, because you outrank him, he's thinking that")
            print("you've just waisted a precious arrow that can't be retrieved.")
            print("You should quit showing off like a jackass and get back to")
            print("work.")
            ne_gaurd_tower()
        else:
            ne_gaurd_tower()

def se_gaurd_tower():
    print("\nYou are at the top of the south east gaurd tower. You find yourself")
    print("next to a gaurd on duty. Looking over the tower's battlements to the")
    print("east you can see the sea of shambling zombies futilely trying to")
    print("break into the castle. To the south you see the chasam over which you")
    print("plan to make your escape. From time to time a zombie gets pushed over")
    print("the chasm's edge by the weight of the hoard. They fall listless and")
    print("uncomprehending to the impact of their second death.")

    global bridge_problem_chain_explained
    global gt_activated

    if bridge_problem_chain_explained <= 1:
        print("\nYou can either stay here and look aimlesly at the writhing hoard")
        print("below you, shoot arrows at the zombies to relieve your boredom,")
        print("or you can go back to the castle courtyard. What would you like")
        print("to do?")
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:
            print("\nYou pick up a bow and a quiver of arrows. You pull out an")
            print("arrow, knock it to the bow and pull the string back. You")
            print("Sight along the arrow at the head of a particularly ugly and")
            print("decomposed member of the walking dead and you let the arrow")
            print("fly. There is a wet thud, which you can hear even over the,")
            print("moaning of the undead, as the arrow slams through the zombies")
            print("skull. It crumples to the ground and disapears under the sea")
            print("of shambling, rotten boddies. You look up with a mischevious")
            print("smile at the gaurd next to you expecting to see that you've")
            print("impressed him with your marksmenship but are supprised to")
            print("find him scowling at you. You realize then that even though")
            print("he won't say it, because you outrank him, he's thinking that")
            print("you've just waisted a precious arrow that can't be retrieved.")
            print("You should quit showing off like a jackass and get back to")
            print("work.")
            se_gaurd_tower()
        else:
            se_gaurd_tower()

    elif bridge_problem_chain_explained > 1 and "se" not in gt_activated:
        print("\nYou can either stay here and look aimlesly at the writhing hoard")
        print("below you, shoot arrows at the zombies to relieve your boredom,")
        print("go back to the castle courtyard, or talk to the gaurd. What")
        print("would you like to do?")
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:
            print("\nYou pick up a bow and a quiver of arrows. You pull out an")
            print("arrow, knock it to the bow and pull the string back. You")
            print("Sight along the arrow at the head of a particularly ugly and")
            print("decomposed member of the walking dead and you let the arrow")
            print("fly. There is a wet thud, which you can hear even over the,")
            print("moaning of the undead, as the arrow slams through the zombies")
            print("skull. It crumples to the ground and disapears under the sea")
            print("of shambling, rotten boddies. You look up with a mischevious")
            print("smile at the gaurd next to you expecting to see that you've")
            print("impressed him with your marksmenship but are supprised to")
            print("find him scowling at you. You realize then that even though")
            print("he won't say it, because you outrank him, he's thinking that")
            print("you've just waisted a precious arrow that can't be retrieved.")
            print("You should quit showing off like a jackass and get back to")
            print("work.")
            se_gaurd_tower()
        elif "talk" in what_to_do or "gaurd" in what_to_do:
            print("\nYou walk over to the gaurd, explain the blacsmith's need for")
            print("metal and politley ask him to go give her his sword. He heads")
            print("off to go do that. You head back to the courtyard.")
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
        print("\nYou can either stay here and look aimlesly at the writhing hoard")
        print("below you, shoot arrows at the zombies to relieve your boredom,")
        print("or you can go back to the castle courtyard. What would you like")
        print("to do?")
        what_to_do = input("> ")

        if "courtyard" in what_to_do:
            courtyard()
        elif "shoot" in what_to_do or "arrows" in what_to_do or "relieve" in what_to_do or "boredom" in what_to_do:
            print("\nYou pick up a bow and a quiver of arrows. You pull out an")
            print("arrow, knock it to the bow and pull the string back. You")
            print("Sight along the arrow at the head of a particularly ugly and")
            print("decomposed member of the walking dead and you let the arrow")
            print("fly. There is a wet thud, which you can hear even over the,")
            print("moaning of the undead, as the arrow slams through the zombies")
            print("skull. It crumples to the ground and disapears under the sea")
            print("of shambling, rotten boddies. You look up with a mischevious")
            print("smile at the gaurd next to you expecting to see that you've")
            print("impressed him with your marksmenship but are supprised to")
            print("find him scowling at you. You realize then that even though")
            print("he won't say it, because you outrank him, he's thinking that")
            print("you've just waisted a precious arrow that can't be retrieved.")
            print("You should quit showing off like a jackass and get back to")
            print("work.")
            se_gaurd_tower()
        else:
            se_gaurd_tower()

def carpenter():
    print("bob")

def keep():
    print("bob")

def stables():
    print("bob")

def barricks():
    print("bob")

start()
