colors = ['blue', 'black', 'red']
numbers = [1, 2, 3, 4]
list_of_numbers = []

for color in colors:
    print(f"This is a color: {color}.")

for number in numbers:
    print(f"This is a number: {number}.")

for i in range(0,11):
    print(f"Add # {i} to the list.")
    list_of_numbers.append(i)

for number in list_of_numbers:
    print(f"This is also a number {number}.")
