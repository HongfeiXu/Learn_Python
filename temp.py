import random
choice = raw_input("> ")
if 'e' not in choice:
    print "What are you doing is good!"
array = choice.split()
print array
print random.choice(array)
