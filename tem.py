#!/usr/bin/python
# coding: utf-8

"""
HOW IT WORKS:
$ python array_generator.py
	Enter the array name:
	>  name
	Enter your string:
	>  array filled with the splitted string 
  Result:
	Array name
	name = ['array', 'filled', 'with', 'the', 'splitted', 'string']
"""

name = raw_input("\nEnter the name of your array.\n>")
items = raw_input("\nEnter your strings.\n>")
array = items.split()
print "\n\nArray name: ", name
print name, " = ", array
"""
WHAT I Have Learned

string.split = split(s, sep=None, maxsplit=-1)
    split(s [,sep [,maxsplit]]) -> list of strings
    
    Return a list of the words in the string s, using sep as the
    delimiter string.  If maxsplit is given, splits at no more than
    maxsplit places (resulting in at most maxsplit+1 words).  If sep
    is not specified or is None, any whitespace string is a separator.
    
    (split and splitfields are synonymous)
"""
"""
Based on WebMap: https://github.com/4rsh/python/blob/master/webmap.py
DNSMap - Developed by Arsh Leak.
$ wget https://github.com/4rsh/
"""

# Colours
D  = "\033[0m";  
W  = "\033[01;37m";  
O  = "\033[01;33m"; 
SUCESS = "\033[01;32m";
FAIL = "\033[01;31m";

import socket
import sys
import os
os.system("clear")
print O+ "+----------------------------------------------------------------------------+"
print "|                                      DNSMap                                |"
print "+----------------------------------------------------------------------------+"
print "|                            Development by Arsh Leak.                       |"
print "|                         $ Wget > http://github.com/4rsh                    |"
print "+----------------------------------------------------------------------------+"
print W+""
domain = raw_input("Set domain: ") # www.domain.com
 
try:
    ip = socket.gethostbyname( domain )
 
except socket.gaierror:			# NOT VERY UNDERSTAND
    print FAIL+'Invalid Domain.\n\n\n\n\n\n\n'
    sys.exit()
print SUCESS+"+-------------------------+"
print SUCESS+"| DNS   : " +ip+ "     |"
print SUCESS+"+-------------------------+"
"""
What I have learnd
socket.gethostbyname = gethostbyname(...)
    gethostbyname(host) -> address
    
    Return the IP address (a string of the form '255.255.255.255') for a host.
"""
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
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Know your PC — The machine settings.
Developed by Arsh Leak (https://github.com/4rsh/)
"""

import os
os.system("clear")
print " _____                                     _____ _____ "
print "|  |  |___ ___ _ _ _    _ _ ___ _ _ ___   |  _  |     |"
print "|    <    | . | | | |  | | | . | | |  _|  |   __|   --|"
print "|__|__|_|_|___|_____|  |_  |___|___|_|    |__|  |_____|"
print "                       |___| Developed by Arsh Leak     "
print "KNOW YOUR PC:\n"
print "[ the network node hostname: ]"
os.system("uname -n\n")
print "\n[ kernal name: ]"
os.system("uname -s")
print "\n[ kernel version: ]"
os.system("uname -v")
os.system("uname -r")
print "\n[ OS: ]"
os.system("uname -o")
print "\n[ machine hardware name: ]"
os.system("uname -m")
print "\n[ processador: ]"
os.system("uname -p")
print "\n[ hardware plataform: ]"

"""
WHAT I have Learned

os.system("uname -i")
os.system = system(...)
    system(command) -> exit_status
    
    Execute the command (a string) in a subshell.
"""
