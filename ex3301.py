# Convert this while-loop to a function that you can call, 
# and replace 6 in the test (i < 6) with a variable.
# Use this function to rewrite the script to try different numbers.
# Add another variable to the function arguments 
# that you can pass in that lets you change the + 1 
# so you can change how much it increments by.
def creat_numbers(numbers, end, step):
    i = 0
    while i < end:
        print "At the top i is %d" % i
        numbers.append(i)
    
        i = i + step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

numbers = []
print numbers
creat_numbers(numbers, 10, 2)
print numbers
