#coding=utf-8
from sys import exit
from os import system

system("clear")

def gold_room():
    print "This room is full of gold. How much do you take?"

    how_much = raw_input("Enter a num\n> ")

    try:
        how_much = int(how_much)
        if how_much < 50:                 
            print "Nice, you're not greedy, you win!"
            exit(0)
        else: 
            dead("You greedy bastard!")
    except ValueError:
        print "Please enter a num, not sting or others!"
        gold_room()


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        elif choice == "open door" and not bear_moved:
            dead("You just go straight to the mouth of that bear.")
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:            # we can use 'in' that way NICE
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Keep Trying!"
    print "I give you another chance.Accept it or not?"
    accept = raw_input("Y or N > ")
    if accept == "Y":
        start()
    elif accept == "N":
        exit(0)
    else:
        dead("You'd better make a right choice.")

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
