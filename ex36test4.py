from sys import exit

drawbridge = False
inventory = []
crew = []
bridge_problem_chain_explained = 0
bridge_problem_gears_explained = 0
wood_problem_explained = 0
pully = ["rusty chain", "rotten gears"]
gt_activated = []

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

stables()
