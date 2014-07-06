#!/usr/bin/python

# Setting variables via string formatting and basic variable assignment
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# Printing X and Y variables.
print x
print y

# Printing statements via format strings.
print "I said: %r." % x
print "I also said: '%s'." % y

# Joke variable assignment
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Print joke using string formatting
print joke_evaluation % hilarious

# Variable assignment
w = "This is the left side of..."
e = "a string with a right side."

# Print statement using string concatentation.
print w + e
