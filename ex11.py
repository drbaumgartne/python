# ex11.py

# LEarn Python the Hard way
# First taste of input

# Question and raw_input states
# Again, I like Haskell's way of having to do dirty IO and binding to variables rather than Pythons dirty everywhere implementation

print "How old are you?",
age = raw_input()
print "How tall are you",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

# the new way of doing string formats
print "Are you really {0} years old, {1} tall, and {2} heavy.".format(age, height, weight)
# old way with string reps
print "Are you really %s years old, %s tall, and %s heavy." % (age, height, weight)
# old way with debug reps
print "Are you really %r years old, %r tall, and %r heavy." % (age, height, weight)
