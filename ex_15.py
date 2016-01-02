#The solution is to use argv or raw_input 
#to ask the user what file to open (In this case, I create two files, ex15_sample.txt and ex15_sample01.txt)
#instead of "hard coding" the file's name.

from sys import argv        # import module argv

script, filename = argv     
# unpack argv, argv gets assigned to 2 variables

txt = open(filename)       
# function open, return the file object and give it to txt. 
#You just open a file.

print "Here's your file %r:" % filename
print txt.read() 
# a function on txt named read. and print the file txt point to.
# give a file a command by using the dot, 
# the name of the command, and parameters.

txt.close() #It's important to close files when you are done with them

print "Type the filename again:"
file_again = raw_input("> ")    
# prompt with users, and ask which file he/she wants to open.

txt_again = open(file_again)
# func open, return file object and give it to txt_again

print txt_again.read()
# a function on txt named read. and print the file txt point to.

txt_again.close()
