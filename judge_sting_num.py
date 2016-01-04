#coding=utf-8
# 函数judge_s_n 用于判断输入的字符串内容是否全为数字

def judge():
    a = raw_input("Enter a num:")
    try:
        a = int(a)
        print a
    except ValueError:
        print "Please enter a num, not a string or others."

