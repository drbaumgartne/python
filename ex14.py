# ex14.py

# Learn Python the Hard way

# Using argv and inputs to do things

from sys import argv

script, user_name = argv
prompt = 'Response: '
prompt_two = '> '

print "Hi {0}, I'm the {1} script".format(user_name, script)
print "I'd like to ask you a few questions."

# q1
print "Do you like me %s?" % user_name
q_one = raw_input(prompt)
print "Are you sure?"
q_one_check = raw_input(prompt_two)

# q2
print "Where do you live %s?" % user_name
q_two = raw_input(prompt)

# q3
print "What kind of computer do you have?"
q_thr = raw_input(prompt)

print """
Alright, so you said '{0}' about '{1}' liking me.
You live in {2}.  Which sounds like a crazy town.
And you have a {3} for a computer. Sounds badass.
""".format(q_one_check, q_one, q_two, q_thr)

