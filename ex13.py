# ex13.py

# Learn Python the Hard way

# More variables and packing/unpacking

from sys import argv

script, first, second, third = argv

print "The script is called:", script
x = raw_input("What happens to a mid input? ")
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "This was what you tried to place in the middle:", x
