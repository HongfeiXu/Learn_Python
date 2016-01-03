list1 = range (1, 6)
for i in list1:
    print "item = %d" % i
list1.append (10)
print "\n"
for i in list1:
    print "item = %d" % i
list2 = range (3, 7)
print "\n"
for i in list2:
    print "item = %d" % i
list1.extend(list2)
print "\n"
for i in list1:
    print "item = %d" % i

