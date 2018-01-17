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
    print("bob")

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
            gt_activated.append("nw")
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
            gt_activated.append("nw")
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
