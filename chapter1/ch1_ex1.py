#########################################################################
# auhtor        : huanglilongwk@qq.com
# time          : 2016/4/21
# brief         : <Programming in Python3 > chapter1 exercise 1 (page:47)
##########################################################################

# How to solve the problem
# 1. get digits from command-line
# 2. get each items from digits
# 3. calculate a line using item(number) instead *
# 4. output seven lines

import sys      # using sys.argv -> input from command-line

Digits_Table =[ ["  ***  ",
                 " *   * ",
                 "*     *",
                 "*     *",
                 "*     *",
                 " *   * ",
                 "  ***  "],
                ["   *   ",
                 "  **   ",
                 "   *   ",
                 "   *   ",
                 "   *   ",
                 "   *   ",
                 "   *   "],
                ["  **** ",
                 " *    *",
                 " *   * ",
                 "    *  ",
                 "  *    ",
                 " *     ",
                 " ******"],
                ["  **** ",
                 " *    *",
                 "     * ",
                 "    *  ",
                 "     * ",
                 " *    *",
                 " ***** "],
                ["   *   ",
                 "  **   ",
                 " * *   ",
                 "*******",
                 "   *   ",
                 "   *   ",
                 "   *   "],
                ["*******",
                 "*      ",
                 "*      ",
                 "*******",
                 "      *",
                 "      *",
                 "*******"],
                ["*******",
                 "*      ",
                 "*      ",
                 "*******",
                 "*     *",
                 "*     *",
                 "*******"],
                ["*******",
                 "      *",
                 "      *",
                 "      *",
                 "      *",
                 "      *",
                 "      *"],
                ["*******",
                 "*     *",
                 "*     *",
                 "*******",
                 "*     *",
                 "*     *",
                 "*******"],
                ["*******",
                 "*     *",
                 "*     *",
                 "*******",
                 "      *",
                 "      *",
                 "*******"]
              ]
try:
    digits_in = sys.argv[1]         # 1. get digits
    row = 0
    while row < 7:
        column = 0
        line = ""
        while column < len(digits_in):
            item = int(digits_in[column])       # 2. get each item from digits_in
            for s in Digits_Table[item][row]:  # 3. using item instend "*"
                if s == "*":
                    line += str(item)
                else:
                    line += " "
            line += " "
            column += 1     # next item
        print(line)         # 4. output lines
        row += 1            # next row
except IndexError:
    print("Usage: bigdigit_ans.py number")
except ValueError as err:
    print(err, "in", digits_in)



