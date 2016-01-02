print "It's time to check if you are lucky."
luck = int(raw_input("\n>"))
if luck in range(1, 100):
    print "LUCKY!"
else:
    print "SORRY!"
