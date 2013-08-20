# ex5.py
# Learn Python the Hard Way

# define some static variables; notice no static type signatures (lame)
name = 'Dave Baumgartner'
age = 27
height = 70
weight = 145
eyes = 'blue'
teeth = 'white'
hair = 'brown'

# print some jazz
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "A reasonable weight."
print "He's got %s eye and %s hair." % (eyes, hair)
print "His teeth are usually %s when he brushes." % teeth

# something a literal more interesting
print "If I add %d, %d, and %d I get %d." %(age, height, weight, age + height + weight)

# Write some variables that convert inches and pouunds to centimeters and kilos
cents_to_inches = 2.54 # that is 2.54 cm per inc
inch_to_cent = (1/2.54)
inches = 100
cents = 100

# print something
print "%d inches is %d centimeters" % (inches, inches * inch_to_cent)
print "{0:10d} inches is {1:.1f} centimers".format(inches, inches * inch_to_cent)

lbs_to_kilos = 0.453592
kilos_to_lbs = 1/lbs_to_kilos

# print something
print "Dave weights %d pounds which is %d kilos." % (weight, weight * lbs_to_kilos)
print "If he weighed {0:10d} kilos, he'd be {1:.1f} pounds.".format(weight, weight * kilos_to_lbs)
