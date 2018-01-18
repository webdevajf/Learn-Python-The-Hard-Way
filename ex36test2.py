## This is the 'test' document. This document exists
## to provide me a place to test and experiment with
## the game's code in a place that is isolated from
## then rest of the script.


## Change this function from NW gaurd tower to SW gaurd tower with a zombie fight.

def sw_gaurd_tower():

    global bridge_problem_chain_explained
    global gt_activated

    if bridge_problem_chain_explained <= 1:
        print("\nYou are at the top of the south west gaurd tower. You find yourself")
        print("next to a gaurd on duty. He looks very ill with a pallor to his skin,")
        print("glassy eyes and sweat stained clothes. You decide to keep your eyes"
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
        print("you see the gaurd on duty. He's turned away from you looking out")
        print("at the chasam behind the castle. There's somethig off about his")
        print("posture... you hear an animal groan comming from him as he turns")
        print("around to face you... your eyes widen and adrenaline pumps into")
        print("your veins as your blood runs cold. Before you have time to really")
        print("process what you're seeing")
        zombie_battle()
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
            sw_gaurd_tower()
        else:
            sw_gaurd_tower()

def zombie_battle:
    print("the zombie lunges at you! You raise your arm to fend off it's onslaught")
    print("and it bights into the chain mail armoring your forearm. What will you")
    print("do?")
    print("Shove the zombie away and draw your sword? (type 'shove')")
    print("Smash the zombie in the face with your armored fist? (type 'smash')")
    print("Draw your knife? (type 'knife')")
    fight = input("> ")
    face_smashes = 0
    if fight == "shove":
        print("You kick the zombie in the chest to gain space. In one fluid")
        print("motion you draw your sword from the shieth on your belt and,"
        print("using the momentum from that motion")
