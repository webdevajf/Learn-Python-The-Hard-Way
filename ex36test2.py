## This is the 'test' document. This document exists
## to provide me a place to test and experiment with
## the game's code in a place that is isolated from
## then rest of the script.

bridge_problem_chain_explained = 0
bridge_problem_gears_explained = 0

print(f"chain: {bridge_problem_chain_explained}")
print(f"gears: {bridge_problem_gears_explained}")

def change():
    global bridge_problem_chain_explained
    global bridge_problem_gears_explained
    bridge_problem_chain_explained = 1
    bridge_problem_gears_explained = 1
    print(f"chain: {bridge_problem_chain_explained}")
    print(f"gears: {bridge_problem_gears_explained}")
    print("\n type a number from 3 to 5")
    number = input("> ")
    if "3" in number:
        bridge_problem_chain_explained = 3
        bridge_problem_gears_explained = 3
        print(f"you typed{number}.")
        print(f"chain becomes: {bridge_problem_chain_explained}")
        print(f"gears becomes: {bridge_problem_gears_explained}")
    elif "4" in number:
        bridge_problem_chain_explained = 4
        bridge_problem_gears_explained = 4
        print(f"you typed{number}.")
        print(f"chain becomes: {bridge_problem_chain_explained}")
        print(f"gears becomes: {bridge_problem_gears_explained}")
    elif "5" in number:
        bridge_problem_chain_explained = 5
        bridge_problem_gears_explained = 5
        print(f"you typed{number}.")
        print(f"chain becomes: {bridge_problem_chain_explained}")
        print(f"gears becomes: {bridge_problem_gears_explained}")
    else:
        print("follow directions dummy.")

change()
