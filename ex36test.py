## This is the 'test' document. This document exists
## to provide me a place to test and experiment with
## the game's code in a place that is isolated from
## then rest of the script.


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
        print("of a seige. Looking over the tower's battlements you can see the sea")
        print("of shambling zombies futilely trying to break into the castle.")
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
        print("over the tower's battlements you can see the sea of shambling zombies")
        print("futilely trying to break into the castle.")
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
        print("using the momentum from that motion sweep your sword in an upward")
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

## change the view from the top of the SE gaurd tower to reflect the chasam to
## the south and the zombie hoard to the west.

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
