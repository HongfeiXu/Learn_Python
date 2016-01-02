print "You enter a dark room with three doors. Do you go through door #1, door #2 or door #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off.  Good job!"
    elif bear == "2":
        print "The bear eats your legs off.  Good job!"
    else:
        print "Well, doing %s is probably better. Bears runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at  Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yello jacket clothespins."
    print "3. Understanting revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

elif door == "3":
    print "It's your time to show solve this dangerous challenge."
    print "Choose a weapon first:"
    print "1. Gun."
    print "2. Sword."

    weapon = raw_input("> ")
    
    if weapon == "1":
        print "You can use this gun to kill Obama. Would you?"
        print "1. YES, OF COURSE!"
        print "2. Sorry, I'm a polite person."
        kill = raw_input("> ")
        if kill == "1":
            print "You will be the king of the seven kindoms! HAHA"
        elif kill == "2":
            print "Smart man, We all know it is difficult to kill Obama, Genleman."
        else:
            "What the hell are you doing? Why not follow the rules?"
    elif weapon == "2":
        print "oh, my old sport, actually I prefer sword, too."
        print "So ,practice it , may be I will need you do something for me in the future."
    else:
        print "What's this? I do not play with a person who does not follow the rules."

else:
    print "You stumble around and fall on a knife and die.  Good job!"
