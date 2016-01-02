from os.path import exists

# the function creat_a_file can creat a file
# and input 2 lines into it
def creat_a_file(filename):
    print "you want to creat a file named %s" % filename
    print "Is %s already existed? %s" % (filename, exists(filename))
    print "Do you want to continue? If not, hit CTRL-C"
    raw_input()
    print "you can input two lines, press enter to submit"
    line1 = raw_input('line1-->')
    line2 = raw_input('line2-->')
    data = "%s\n%s\n" % (line1, line2)
    open(filename, 'w').write(data)
    print "Alright, the %s has been created\n" % filename

# first way
filename = "test1.txt"
creat_a_file(filename)
# second way
creat_a_file("test2.txt")
# third way
filename2 = raw_input("give the file which you want to creat a name\n-->")
creat_a_file(filename2)
# forth way
creat_a_file(raw_input("filename-->"))
