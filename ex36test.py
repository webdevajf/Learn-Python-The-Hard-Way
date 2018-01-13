## This is the 'test' document. This document exists
## to provide me a place to test and experiment with
## the game's code in a place that is isolated from
## then rest of the script.


def blacksmith():
    global bridge_problem_chain_explained
    print("\nYou are in the blacksmith's workshop. You look around and see her")
    print("working diligengly at her forge.")
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
            bridge_problem_chain_explained = 2
            print(pully)
            pully.remove(str("rusty chain"))
            print(pully)
            blacksmith()
        else:
            blacksmith()
    elif bridge_problem_chain_explained == 2:
        print("You can stay here, talk to the blacksmith, or go back to the")
        print("courtyard. What would you like to do?")
        where_to = input("> ")
        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:
            print("She tells you that she has removed the rusty chain but that")
            print("she still needs 4 peices of metal to make a new one.")
            blacksmith()
        else:
            blacksmith()
    elif bridge_problem_chain_explained == 3:
        print("You can stay here, talk to the blacksmith, or go back to the")
        print("courtyard. What would you like to do?")
        where_to = input("> ")
        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:
            print("She tells you that she has removed the rusty chain but that")
            print("she still needs 3 peices of metal to make a new one.")
            blacksmith()
        else:
            blacksmith()
    elif bridge_problem_chain_explained == 4:
        print("You can stay here, talk to the blacksmith, or go back to the")
        print("courtyard. What would you like to do?")
        where_to = input("> ")
        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:
            print("She tells you that she has removed the rusty chain but that")
            print("she still needs 2 peices of metal to make a new one.")
            blacksmith()
        else:
            blacksmith()
    elif bridge_problem_chain_explained == 5:
        print("You can stay here, talk to the blacksmith, or go back to the")
        print("courtyard. What would you like to do?")
        where_to = input("> ")
        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:
            print("She tells you that she has removed the rusty chain but that")
            print("she still needs 1 peice of metal to make a new one.")
            blacksmith()
        else:
            blacksmith()
    elif bridge_problem_chain_explained == 6:
        print("You can stay here, talk to the blacksmith, or go back to the")
        print("courtyard. What would you like to do?")
        where_to = input("> ")
        if "courtyard" in where_to:
            courtyard()
        elif "talk" in where_to or "blacksmith" in where_to:
            print("She tells you that she has removed the rusty chain and made")
            print("a new one which she installed in the drawbridge gaurdtower.")
            print(pully)
            pully.insert(0,str("new chain"))
            #pully.append(str("new chain")) # if the above line can't be made to work.
            print(pully)
            blacksmith()
        else:
            blacksmith()
