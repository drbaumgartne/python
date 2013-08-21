# ex15.py

# Learn Python the Hard Way

# Reading from file

# imports
from sys import argv

# our two arguments that should come along when executing the program
script, filename = argv

# uses the built in open function, binds the data to a variable called file
txt = open(filename)

# print out some text along with the file using the function read()
print "Here's your file %r:" % filename
print txt.read()

# print some text, ask for user input and bind to the 'file_again' variabl
print "Type the filename again:"
file_again = raw_input("> ")

# open the filename given (no error checking here)
txt_again = open(file_again)

# print the text again
print txt_again.read()
