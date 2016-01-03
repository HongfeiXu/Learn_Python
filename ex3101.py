print "Hello, Welcome to The real world.\nWhat's your name?"
name = raw_input (">")
print "OK, %s, I am gonna show you some skills in coding, Do you wanna check it?" % name
check = raw_input ("Y or N\n>")
if check == "Y":
    print "I can see the fire through your eyes."
    print "So, Which parts do you wanna to learn first? The plan parts, play parts?"
    part = raw_input ("PLAN or PLAY\n>")
    if  part == "PLAN":
        print "NICE ONE, let's do some homework first, then we walk out, then we play basketball, then we..."
    elif part == "PLAY":
        print "NICE ONE, why not write some python codes first, then we run it ,check the wrong and fix those bugs, it's fun, RIGHT?"
    else:
        print "yOU jUsT BrEaK tHe RulES!\n OR maybe you just make a small mistake..."
elif check == "N":
    print "Boring boy, just get out of my sight, and play with your codes.  Actually if you need help, I will be very kind to help you."
else:
    print "yOU jUsT BrEaK tHe RulES!\n OR maybe you just make a small mistake..."

        
