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
