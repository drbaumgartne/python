#ex4.yp
# Python the Hard Way

# variables; self evident naming and assignments

cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "cars not driven today."
print "We can transport", carpool_capacity, "number of people."
print "We have", passengers, "passengers wanting a ride."
print "To transport everyone we need to put", average_passengers_per_car, "passengers per car."
