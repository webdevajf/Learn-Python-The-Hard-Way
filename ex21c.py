# Finally I just want to reduce this down to
# the cleanest and most efficient way to do
# the opperations in ex21.py because that
# exercise is great for practicing using
# functions and variables in tandem but it is
# a supper inefficient way to do these math
# opperations.

#def add(a, b):
#    print(f"ADDING {a} + {b}")
#    return a + b

#def subtract(a, b):
#    print(f"SUBTRACTING {a} - {b}")
#    return a - b

#def multiply (a, b):
#    print(f"MULTIPLYING {a} * {b}")
#    return a * b

#def divide (a, b):
#    print(f"DIVIDING {a} / {b}")
#    return a / b

#print("Lets's do some math with just functions!")

#age = add(30, 5)
#height = subtract(78, 4)
#weight = multiply(90, 2)
#iq = divide(100, 2)

#print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


#A puzzle for the extra credit, type it in anyway.
#print("here is a puzzle.")

#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#print("That becomes: ", what, "Can you do it by hand?")
#print(" ")

#'---------A cleaner way to write this puzzle.--------'

#def integrate (a, b, c, d, e):
#    return (e + (d - (c * (b / a))))

#better_formula = integrate(2, iq, weight, height, age)

#print("better_formula = ", better_formula)
#print(" ")

#'---------An even better way to write this puzzle.-------'

#even_better_formula = (age + (height - (weight * (iq / 2))))

#print("even_better_formula = ", even_better_formula)


#--------------------- The above can be reduced to this:

age = 30 + 5
height = 78 - 4
weight = 90 * 2
iq = 100 / 2
efficient_what = (age + (height - (weight * (iq / 2))))

print("\n-var 'age' adds 5 to 30")
print("-var 'height' subtracts 4 from 78")
print("-var 'weight' multiplies 90 by 2")
print("-var 'iq' divides 100 by 2")
print("""-var 'efficient_what':
#1 divdes the value of var 'iq' by 2,
#2 multiplies that by the value of var 'weight',
#3 subtracts that from the value of var 'height'
#4 adds that to the value of var 'age'
giving the user the value of: """, efficient_what)
