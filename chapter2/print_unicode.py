#########################################################################
# auhtor        : huanglilongwk@qq.com
# time          : 2016/4/27
# brief         : <Programming in Python3 > chapter2 example 1 (page:88)
##########################################################################
import sys
import unicodedata

# function definition
def print_unicode_table(word):
    print("decimal    hex    chr   {0:^40}".format("name"))
    print("-------   -----  -----  {0:-<40}".format(""))

    code = ord(" ")
    end = 40
    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        if word is None or word in name.lower():
            print("{0:5}  {0:7X}   {0:2c}   {1:>20}".format(code, name.title()))
        code += 1

word = None
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("Usage: {0} [string]".format(sys.argv[0]))
        word = 0
    else:
        word = sys.argv[1].lower()
if word !=0:
    print_unicode_table(word)

