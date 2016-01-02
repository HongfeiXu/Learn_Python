print "Let's practice everything."
print 'You\'d need to know \' bout escape with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates   # return 3 values


start_point = 10000
beans, jars, crates = secret_formula(start_point)   
# unpack 3 values, if you delete the 'crates', you will get an error
# ValueError: too many values to unpack
# apparently, if you give more than 3 values to unpack, you will get another error
# ValueError: need more than 3 values to unpack


print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." %  secret_formula(start_point)       
# unpack 3 values, if you delete a '%d', then you will get an error
# TypeError: not all arguments converted during string formatting
