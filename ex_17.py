from sys import argv
from os.path import exists  
# exists returns True if a file exists, 
# based on its name in a string as an argument.
# It returns False if not.

script, from_file, to_file = argv

print "Copying from %s to %s " % (from_file, to_file)

# we could do these two on one line, how?
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read() # You don't need to do in_file.close()
#  It should already be closed by Python once that one line runs.

print "The input file is %d bytes long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# we could do these two on one line, how?
#out_file = open(to_file, 'w')
#out_file.write(indata)
open(to_file, 'w').write(indata)

print "Alright, all done."

#out_file.close()
#in_file.close()
