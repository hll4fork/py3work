#########################################################################
# auhtor        : huanglilongwk@qq.com
# time          : 2016/4/30
# brief         : <Programming in Python3 > chapter2 exercise 2 (page:104)
##########################################################################

# How to solve this problem
# 1. remove 0.0 factor
# 2. correct negative factor's output format(example: 1.0x^2 + 1.0x + -6.0 = 0 -> 1.0x^2 + 1.0x -6.0 = 0)

import cmath  # for complex numbers
import math   # for float
import sys

# get a non-zero float from user, if don't allow zero input
def get_float(msg, allow_zero):
    x= None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:  # check for zero input
                print("zero is not allowed")
                x = None
        except ValueError as err:
            print(err)
        return x

# get a, b, c from user
print("ax^2 + bx + c =0")
a = get_float("Enter a: ", False)
b = get_float("Enter b: ", True)
c = get_float("Enter c: ", True)

# calculate the root of ax^2 + bx + c =0
x1 = None
x2 = None
disc = (b**2) - (4 * a * c)
if disc == 0:
    x1 = -(b / (2 * a))
else:
    if disc > 0:
        root = math.sqrt(disc)
    else:
        root = cmath.sqrt(disc)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)

# 1. remove 0 factor output
equation = ("{0}x^2").format(a)
if abs(b) > sys.float_info.epsilon:
    if b > 0:                           # 2. correct negative factor output
        equation += ("+{0}x").format(b)
    elif b < 0:
        equation += ("{0}x").format(b)
if abs(c) > sys.float_info.epsilon:
    if c > 0:
        equation += ("+{0}").format(c)
    elif c < 0:
        equation += ("{0}").format(c)
equation +=(" = 0 -> x = {0}").format(x1)

if x2 is not None:
    equation += " or x = {0}".format(x2)
print(equation)

