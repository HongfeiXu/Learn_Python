from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CRTL-C(^C)."
print "If you do want, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

# The file  will be truncated when opened for writing.
# SO you don't really need the target.truntcate().
#print "Truncating the file.  Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# There's too much repetition in this file. 
# Use strings, formats, and escapes to print out line1, line2, and line3 
# with just one target.write() command instead of six.
line = "%s\n%s\n%s\n" % (line1, line2, line3)
target.write(line)
# what if I trunctae the target
target.truncate()

print "And finally, we close it."
target.close()
