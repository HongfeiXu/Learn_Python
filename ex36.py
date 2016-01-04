from os import system
system("clear")

def job():
    print "Which company do you prefer, Alibaba(A), Xunfei(X), Guochuang(G)?"
    job = raw_input("> ")
    if job == 'A':
        print "May you can do this!"
    elif job == 'X':
        salary()
    elif job == "G":
        print "Keep trying. You can do way better!"
    else:
        print "Please follow the hint."
        job()

def salary():
    print "Let's talk about your salary."
    print "How much do you want per month?"
    salary = raw_input("> ")
    try:
        salary = int(salary)
        if salary < 10000:
            print "Poor guy, you need to be aggerssive!"
        else:
            print "Poor guy, you must be thirsty!"
    except ValueError:
        print "Please enter an number, not a string or others."
        salary()
def home():
    print "Alright, now, you are at home, so Play(P) or Study(S)?"
    do = raw_input("> ")
    if do == 'P':
        print "Go back, and recosider it!"
        home()
    elif do == 'S':
        print "That is my nice guy, take care of your health as well."
    else:
        print "Please follow the hint."
        home()

def hefei():
    print "You are now in Hefei. You have two choice"
    print "Job(J) or Home(H)?"
    choice = raw_input("> ")
    if choice == 'J':
        job()
    elif choice == 'H':
        home()
    else:
        print "Please follow the hint."
        hefei
        
hefei()
