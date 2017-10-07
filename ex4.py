# The variable 'cars' means the "number of cars available" and it has been assigned the value of 100.
cars = 100
# The variable 'space_in_a_car' means "number of passengers per car" and it has been assigned a value of 4.
space_in_a_car = 4
# The variable 'drivers' means "number of drivers available to drive a car" and it has been assigned the value of 30.
drivers = 30
# The variable 'passengers' means "number of people that need tranport in the cars" and it has been assigned the value of 90.
passengers = 90
# The variable 'cars_not_driven' means "number of cars that do not have drivers" and it has been assigned the value of the difference between 'cars' and 'drivers'.
cars_not_driven = cars - drivers
# The variable 'cars_driven' means "number of cars that will be driven" and it has been assigned a value equal to the value of the variable 'drivers' which is 30.
cars_driven = drivers
# The variable 'carpool_capacity' means "number of passengers that can be accomodated in each car" and it has been assigned a value equal to the value of the variable 'cars_driven' multiplied by the value of the variable 'space_in_a_car'.
carpool_capacity = cars_driven * space_in_a_car
# The 'varable average_passengers_per_car' means "the number of passengers that will be in each car after the number of passengers has been evenly distributed amongst the cars being driven" and it has been assigend a value equal to the value of the variable 'passengers' divided by the value of the variable 'cars_driven'.
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
