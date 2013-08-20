# ex6.py

# Learn Python the Hard Way

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x # x with 2
print y # y with binary's value and do_not's value

print "I said: %r." % x  # concats x with something before it; note %r which is an interpretors represenation of x
print "And: '%s'." % y # concats y with something befre it; note %s which is a human-readable format, and hence why the additional single quotes were needed

hilarious = False
joke_eval = "Isn't that joke so funny?! %r"

print joke_eval % hilarious # print a str with something piped into it

w = "This is the left side of..."
e = "a string with a right side."

print w + e
