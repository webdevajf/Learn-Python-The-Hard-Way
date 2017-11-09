# For #2 in study drills in ex21.py I want to play
# with the formula for the puzzle and see if I can
# find a cleaner way to express the same answer.

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply (a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide (a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Lets's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


#A puzzle for the extra credit, type it in anyway.
print("here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
print(" ")

#'---------A cleaner way to write this puzzle.--------'

def integrate (a, b, c, d, e):
    return (e + (d - (c * (b / a))))

better_formula = integrate(2, iq, weight, height, age)

print("better_formula = ", better_formula)
print(" ")

#'---------An even better way to write this puzzle.-------'

even_better_formula = (age + (height - (weight * (iq / 2))))

print("even_better_formula = ", even_better_formula)
