# Write it to use for-loops and range. 
# Do you need the incrementor in the middle anymore? 
# What happens if you do not get rid of it?


def creat_numbers(numbers, end, step):
    for i in range(0, end, step):
        print "At the top i is %d" % i
        numbers.append(i)
      #  i = i + step  # Actually it doesn't work.
       
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

numbers = []
print numbers
creat_numbers(numbers, 10, 1)
print numbers
