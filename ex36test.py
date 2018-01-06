## This is the 'test' document. This document exists
## to provide me a place to test and experiment with
## the game's code in a place that is isolated from
## then rest of the script.

def drawbridge_gaurdtower():
    pully = []
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
        print("new ones.")

drawbridge_gaurdtower()
