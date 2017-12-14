numbers = []

i = 0
z = 6

x = 11
y = 19

def loop(itt, num, end):
    while itt < end:
        print(f"At the top itt is {itt}")
        num.append(itt)

        itt = itt + 1
        print("Numbers now: ", num)
        print(f"At the bottom itt is {itt}")

val_change = 2

def loop2(itt, num, v_c, end):
    while itt < end:
        print(f"At the top itt is {itt}")
        num.append(itt)

        itt = itt + v_c
        print("Numbers now: ", num)
        print(f"At the bottom itt is {itt}")

print('loop(i, numbers, z) is: ',loop(i, numbers, z))

print("The numbers: ")

for num in numbers:
    print(num)

print("and again: ")

print('loop2(i, numbers, val_change, z) is: ', loop2(x, numbers, val_change, y))

print("The numbers again: ")

for num in numbers:
    print(num)
