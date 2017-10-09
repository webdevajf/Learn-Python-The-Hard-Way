name = 'Alex J. Friedman'
age = 29 # not a lie
height = 66 # inches
height_in_cm = round(height * 2.54)
weight = 178 # lbs
weight_in_kg = round(weight * 0.543592)
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("That's a little too heavy but he's working on it and making progress (yay for the gym!)")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
print(f"If I convert his height to centimeters he's {height_in_cm} centimeters tall. That's not so tall.")
print(f"If I convert his weight to kilograms he's {weight_in_kg} kilograms. That's still not so flattering.")
