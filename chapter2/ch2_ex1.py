#########################################################################
# auhtor        : huanglilongwk@qq.com
# time          : 2016/4/29
# brief         : <Programming in Python3 > chapter2 exercise 1 (page:104)
##########################################################################

# How to solve the problem
# 1. get user's input from command-line
# 2. use in operator to get every characters

import sys
import unicodedata

# function definition

def print_unicode_table(word):
    print("decimal    hex    chr   {0:^40}".format("name"))
    print("-------   -----  -----  {0:-<40}".format(""))

    for item in word:   # 2. use in operator to get every characters
        code = ord(item)
        name = unicodedata.name(item, "*** unknown ***")
        print("{0:5}  {0:7X}   {0:2c}   {1:>20}".format(code, name.title()))

word = ""
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("Usage: {0} [string]".format(sys.argv[0]))
        word = 0
    else:
        icount = 1
        while icount < len(sys.argv):   # 1. get user's input from command-line
            word += sys.argv[icount].lower()
            icount += 1
if word != 0:
    print_unicode_table(word)
