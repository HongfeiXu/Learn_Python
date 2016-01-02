#!/usr/bin/python
# coding: utf-8

"""
Good Luck or Not. — Developed by Arsh Leak.
$ wget https://github.com/4rsh/
"""
import random
import time
import os
os.system("clear")  # clear the terminal screen

sorte	=	["yes", "nope"]

print "Good luck... or not.\n\n"
time.sleep(5.5)
if (random.choice(sorte)) == sorte[0]:
	print "You're in luck!"
else:
	print "You're outta luck."

# Enjoy, Arsh Leak.

"""
WHAT I have Learned
random.choice = choice(self, seq) method of random.Random instance
    Choose a random element from a non-empty sequence.

time.sleep = sleep(...)
    sleep(seconds)

    Delay execution for a given number of seconds. The argument may be
    a floating point number for subsecond precision.
"""
