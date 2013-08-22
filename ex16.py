# ex16.py
# Learn Python the Hard Way

# imports
from sys import argv

# our script arguments
script, filename = argv

# print out the script name first
print "Running script: '%s'" % script

# print out the next things e are going to do
print "We're going to erase '%s'." % filename   # erasing the file given (careful!!!)
print "If you don't want to do that, cancel the program now with CTRL-C (^C)."
print "If you do wan that, hit RETURN."

# get input from the user, which acts as a pausing mechanism
raw_input("?")

# open the file and wipe it with the tuncate command
print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Zow!"
target.truncate()

# ask for some input to now write to the file
print "Now I'm going to ask for three lines of input."

line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")

# now write them to the file
print "Now writing the three lines provided to the file."

target.write(line1)
target.write("\n") # new line
target.write(line2)
target.write("\n") # new line
target.write(line3)
target.write("\n") # new line

# close the file
print "Closing the file."
target.close()
