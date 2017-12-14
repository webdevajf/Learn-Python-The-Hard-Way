i = 0
z = 6

x = 0
y = 21

def loop(itt, end):
    numbers = []
    while itt < end:
        print(f"At the top itt is {itt}")
        numbers.append(itt)

        itt = itt + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom itt is {itt}")

    print("The numbers: ")
    for num in numbers:
        print(num)

val_change = 2

def loop2(itt, v_c, end):
    numbers = []
    while itt < end:
        print(f"At the top itt is {itt}")
        numbers.append(itt)

        itt = itt + v_c
        print("Numbers now: ", numbers)
        print(f"At the bottom itt is {itt}")

    print("The numbers again: ")
    for num in numbers:
        print(num)

print('def loop(i, z) is: ',loop(i, z))

print("""
and again:
""")

print('def loop2(i, val_change, z) is: ', loop2(x, val_change, y))
