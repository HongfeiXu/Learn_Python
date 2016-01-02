# coding: utf-8

"""
HOW IT WORKS:
$ python array_generator.py
	Enter the array name:
	>  name
	Enter your string:
	>  array filled with the splitted string 
  Result:
	Array name
	name = ['array', 'filled', 'with', 'the', 'splitted', 'string']
"""

name = raw_input("\nEnter the name of your array.\n>")
items = raw_input("\nEnter your strings.\n>")
array = items.split()
print "\n\nArray name: ", name
print name, " = ", array
"""
WHAT I Have Learned

string.split = split(s, sep=None, maxsplit=-1)
    split(s [,sep [,maxsplit]]) -> list of strings
    
    Return a list of the words in the string s, using sep as the
    delimiter string.  If maxsplit is given, splits at no more than
    maxsplit places (resulting in at most maxsplit+1 words).  If sep
    is not specified or is None, any whitespace string is a separator.
    
    (split and splitfields are synonymous)
"""
