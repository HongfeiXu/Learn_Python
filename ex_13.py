#This is how you add features to your script from the Python feature set. 
#The argv is the "argument variable".
#and This variable holds the arguments you pass to your Python script when you run it.

from sys import argv # we call these "features" that we import modules, like the sys module


#This line "unpacks" argv so that,rather than holding all the arguments, 
#it gets assigned to four variable you can work with
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

name = raw_input('YOUR NAME-->')
#The difference has to do with where the user is required to give input. 
#If they give your script inputs on the command line, then you use argv. 
#If you want them to input using the keyboard while the script is running, then use raw_input().
