#!/usr/bin/python

""" Learn Python the hard way - Exercise 4

    Author: Adrian Arumugam

"""

# Setting variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers

# Working out carpool capacity by multiplication
carpool_capacity = cars_driven * space_in_a_car

# Working out avg passengers per car via division
average_passengers_per_car = passengers / cars_driven

# Printing statements with given variables
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
