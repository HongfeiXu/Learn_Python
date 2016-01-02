from sys import argv

script, user_name, user_words = argv
prompt = "->"

print "Hi %s, I'm %s, welcome to my world." % (user_name, script)
print "And I heard you say '%s', Isn't it?" % user_words
answer1 = raw_input(prompt)
print "So you say %r" % answer1
print "%s, I am tired now, may I just have a break?" % user_name
answer2 = raw_input(prompt)
print """
Acturally, I don't care your opinion, 
cause I'm not that smart, 
my master don't know too much to improve my brain, 
so %s, GOOD BYE!
""" % user_name
