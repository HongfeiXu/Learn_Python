def break_words(stuff):         # stuff is string
    """This function will break up words for us."""
    words = stuff.split(' ')    # words is list of strings
    # string.split = split(s, sep=None, maxsplit=-1)
    #    split(s [,sep [,maxsplit]]) -> list of strings
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)        # return a sorted list
    # sorted(...)
    #    sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list

def print_first_word(words):    # words is a list
    """Prints the first word after popping it off."""
    word = words.pop(0)        
    #list.pop = pop(...)
    #   L.pop([index]) -> item -- remove and return item at index (default last).
    #   Raises IndexError if list is empty or index is out of range.
    print word

def print_last_word(words):     # words is a list
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):    # sentence is a string

    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)   # words is a list of the string
    return sort_words(words)        # return a sorted list

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words int the sentence then print the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
