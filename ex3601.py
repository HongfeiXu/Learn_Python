# -*- coding: utf-8 -*-
import random
import time                 # to sleep
import os
os.system("clear")          # clear the window

def round1():
    print "---------------------------------"
    print "*                               *"
    print "*                               *"
    print "*                               *"
    print "*           ROUND 1             *"       
    print "*                               *"
    print "*                               *"
    print "*                               *"
    print "---------------------------------"
    print "\nCheck Your Luck First!\n\n"
    weapons = ['scissors', 'stone', 'cloth']
    print "There are some cold weapons: "
    print weapons
    print "\nI bet you know the rules."
    print "You have three chances, You must win the computer at least once."
    score = 0;                                      # mark the Player's score, then judge he's win or fail.
    
    for i in range(1, 4):
        print "\nThe %dth chance! Come on!\n" % i

        cp = random.choice(weapons)                 # PC random choice a weapon
        player = raw_input("Choose Your Weapon\n> ")# Player choice a weapon by type
        print "Your weapon: %s" % player 
        print "PC's weapon is ..."
        time.sleep(2)
        print "                %s" % cp
        if (cp == 'scissors') and (player == 'stone'):
            score += 1
            print "NICE, You win this time."
        elif (cp == 'stone') and (player == 'cloth'):
            score += 1
            print "NICE, You win this time."
        elif (cp == 'cloth') and (player == 'scissors'):
            score += 1
            print "NICE, You win this time."
        else:
            print "You lose this time."
    if score ==  3:
        print "\nOMG, Congratulations! You win round 1 with %d score(s). Go on!"
        print "And, you have a big privilege which is you can jump to round 3, do you wanna this?"
        jump = raw_input("Yes(Y) or No(N)\n> ")
        if jump == 'Y':
            round3()
        elif jump == 'N':
            round2()
        else:
            print "Please follow the rules!"
            round1()
    elif score > 0:
        print "\nOMG, Congratulations! You win round 1 with %d score(s). Go on!"
        round2()
    else:
        print "Sorry, My friend, do you wanna another try?"
        ano_try = raw_input("Yes(Y) or Not(N)\n> ")
        if ano_try == 'Y':
            round1()
        elif ano_try == 'N':
            byebye("round1 player, see you around.")
        else:
            print "Please follow the rules!"
            byebye("round1 player, see you around.")

def byebye(what):
    print what
    print "\n\n\nWait, you still have a chance."
    print "Do you wanna wait another 5 minutes?"
    wait = raw_input("Yes(Y) or Not(N)\n> ")
    if wait == 'Y':
        time.sleep(100)
        round1()
    else:
        print "Best wishes to you. Good Bye."
        exit(0)

def round2():
    print "---------------------------------"
    print "*                               *"
    print "*                               *"
    print "*                               *"
    print "*           ROUND 2             *"       
    print "*                               *"
    print "*                               *"
    print "*                               *"
    print "---------------------------------"
    print "\nThat's gonna be a tough one.\n\n"


def round3():
    print "---------------------------------"
    print "*                               *"
    print "*                               *"
    print "*                               *"
    print "*           ROUND 3             *"       
    print "*                               *"
    print "*                               *"
    print "*                               *"
    print "---------------------------------"
    print "\n"

round1()





"""

WHAT I Have Learned
1:
    random.choice = choice(self, seq) method of random.Random instance
        Choose a random element from a non-empty sequence.
2:
    from random import choice
    或者from random import *
    下面调用函数直接这样:
    choice(---)

    import random
    下面调用函数这样:
    random.choice(---)

"""
